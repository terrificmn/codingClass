CMakeLists.txt 파일을 만들어준다  

참고 restc-cpp 관련 패키지 만들 때 사용한 CMakeLists.txt 파일   
```c
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

add_executable(${PROJECT_NAME} jsontest.cpp)
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

## 기초 빌드

같은 디렉토리에서 build 디렉토리를 만들어 주고  
mkdir build  
cd build  
cmake ..

그리고  실제 컴파일 및 link 시키기  
```
cmake --build .
```

그러면 build 디렉토리 안에 실행파일이 생김   
