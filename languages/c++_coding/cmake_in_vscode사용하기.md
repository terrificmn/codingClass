# cmake

특정 패키지 디렉토리를 만들고 예를 들어 test_cmake

컨트롤+쉬프트 + p 를 눌러서 검색을 해주는데 cmake라고만 쳐도 자동완성으로 많이 나오는데  
그 중에 *CMake:Quick Start* 를 눌러준다   

컴파일러를 선택해주는데 gcc-9.4.0_x84_64... 를 선택  

그러면 Enter a name for the project 라고 프로젝트명을 입력해준다   (예를 들어: test_cmake)

Library 또는 Executable 이 나오고, Executable을 선택해준다   

그러면 
```c
cmake_minimum_required(VERSION 3.0.0)
project(test_cmake VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(test_cmake main.cpp)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
```
요렇게 만들어진다. 일단 필요없는 것들은 지우거나 주석처리 후 사용

```c
cmake_minimum_required(VERSION 3.0.0)
project(test_cmake VERSION 0.1.0)

add_executable(test_cmake main.cpp)

// set(CPACK_PROJECT_NAME ${PROJECT_NAME})
// set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
// include(CPack)
```

main.cpp 파일도 만들어주므로 혹시 main.cpp 파일이 있다며 주의해야할 지도 모르겟다..


이후 cpp파일을 열어 놓고 (src 안에 넣어준다)  그리고 F7을 눌러주면 컴파일을 시작.. 뭔가 잘 되는 것 같지만  
꼭 그렇지도 않은 듯 하다.  아마도 이것도 설정이 필요할 듯 하다.  

> 그리고 프로젝트가 하위 디렉토리로 되어 있을 경우에도 기본 설정과 맞지 않는 듯 하다

그래서 일단 수동으로 차근차근 하는 것도 나쁘지 않다   
```
cd test_cmake
mkdir build; cd build
cmake ..
```
완료시 build 디렉토리 내에서 `make` 를 해준다 

## Run and Debug
컴파일 완료 후  
F5를 누르면 Run and Debug 가 열리는데  create a launch.json file을 클릭해서 json파일을 만들어준다   

여기에서   
```json
"type": "cppdbg",
"request": "launch",
"program": "${workspaceFolder}/src/main"
```
등으로 선택하고 program 은 실행파일 경로를 잘 선택해주면 된다   

> 처음에 "program": "enter program name, for example.... 이렇게 나오는데  위에 처럼  
경로만 표시해주면 된다. 원래 build에 실행파일이 생기는데, 설정을 안해서 src에 만들어 졌는지는 모르겠다;;;



