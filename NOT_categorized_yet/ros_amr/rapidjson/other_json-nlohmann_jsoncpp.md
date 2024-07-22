# other json 라이브러리
다양한 json 관련 라이브리러 빌드 방법   
몇개를 테스트 해봤는데, 모두 각각의 깃 허브 저장소를 들어가면 예제도 있고 사용은 가능하겠지만  
rapidjson 많이 사용해서 그런지 아무래도 뭔가 쓰기에 부족? 느낌이 든다.  

### jsoncpp
먼저 클론 후 빌드

```
git clone https://github.com/open-source-parsers/jsoncpp.git
cd jsoncpp
mkdir build; cd build
cmake -DCMAKE_BUILD_TYPE=release -DBUILD_STATIC_LIBS=OFF -DBUILD_SHARED_LIBS=ON -DARCHIVE_INSTALL_DIR=. -G "Unix Makefiles" ..
make 
sudo make install
```


헤더파일로 
```
#include "json/json.h"
```
넣어주면 되고   

CMakeLists.txt 에서는  
```
add_executable(${PROJECT_SOURCE_DIR} src/main.cpp)
target_include_directories(${PROJECT_SOURCE_DIR} PUBLIC ${CMAKE_SOURCE_DIR}/include)
target_link_libraries(${PROJECT_SOURCE_DIR} jsoncpp_lib)
```


## nlohmann json
![여기에서 release버전 다운로드](https://json.nlohmann.me/home/releases/)

zip파일 압축을 풀면 include 디렉토리가 생기는데 include 디렉토리의     
nlohmann 디렉토리를 자신의 프로젝트 인쿠르드 디렉토리 이동 시켜준다  

find_package() 를 할 필요는 없고, include 디렉토리만 잘 지정해주고 헤더파일만 include 해주면 문제 없이 빌드 된다.

CMakeLists.txt 에서 include_directories를 지정
```
include_directories(
    ${PROJECT_SOURCE_DIR}/include
)
```


