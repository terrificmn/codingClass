## 의존성 openssl
dnf  
sudo dnf install openssl-devel

apt  
sudo apt-get install libssl-dev


## 의존성 boost 설치   
dnf
sudo dnf install boost-devel

apt
apt install libboost-all-dev


## restc-cpp 설치하기
Clone the repository
```
git clone https://github.com/jgaa/restc-cpp.git
```
Initialize the submodules
```
cd restc-cpp
git submodule init
git submodule update
```
Compile the library and tests
```
mkdir dbuild   
cd dbuild
cmake ..
sudo make install
cd ..
```

> 원래 메뉴얼에는 make까지만 되어 있는데 make install 해주면  
/usr/local/include/restc-cpp 를 설치해준다   
그래서 header파일을 inlcude할 때 잘 인식해준다 



## cpp 코드 빌드하기
그냥 g++ 등을 이용해서 하면 에러 발생   
CMakelists.txt 파일을 이용해서 빌드해야함 - restc-cpp 사용할 경우   
```
cmake_minimum_required(VERSION 3.0)
project (restapi_test)

find_package(restc-cpp REQUIRED)
find_package(ZLIB REQUIRED)
find_package(OpenSSL REQUIRED)
find_package(Boost REQUIRED COMPONENTS
    system
    program_options
    filesystem
    date_time
    context
    coroutine
    chrono
    log
    )

add_executable(${PROJECT_NAME} rest.cpp)
set_property(TARGET ${PROJECT_NAME} PROPERTY CXX_STANDARD 14)
target_link_libraries(${PROJECT_NAME}
    ${RESTC_CPP_LIBRARIES}
    ${Boost_LIBRARIES}
    ${ZLIB_LIBRARIES}
    ${OPENSSL_LIBRARIES}
    )

add_definitions(
    -DBOOST_COROUTINE_NO_DEPRECATION_WARNING=1
    -DBOOST_ALL_DYN_LINK=1
    )

target_include_directories(${PROJECT_NAME} PUBLIC
    $<BUILD_INTERFACE:${ZLIB_INCLUDE_DIR}>
    $<BUILD_INTERFACE:${ZLIB_INCLUDE_DIR}/build>
    $<BUILD_INTERFACE:${OPENSSL_INCLUDE_DIR}>
    )
```

단, boost libraries 이용해서 빌드하기 (boost 사용할 때만 적용)
```
g++ ./http_test.cpp -o http_test -L /usr/lib/ -lboost_system -lboost_thread -lpthread
```

-o 옵션으로 (linker flags) 만들때에 파일명이 먼저 나오고 그 다음에 -o 옵션이 와야 한다 


