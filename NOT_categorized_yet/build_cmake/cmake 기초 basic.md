예제는 clang++으로 되어 있는데  
리눅스이니 gcc++로 생각하면 될 듯  


build_test라는 디렉토리를 만들고 그 안에 src, build, CMakeLists.txt 파일을 만든다  
```
mkdir build_test; cd build_test
mkdir build src CMakeLists.txt
cd src; touch first.cpp first.hpp main.cpp
```

first.hpp파일은 헤더파일로 function을 정의만 하고 있고 
```cpp
#pragma once
void WhatsUp();
void ButWhy();
```

> pragma once는 한 번만 로드하겠다는 의미


first.cpp파일은 정의한 function의 코드
```cpp
#include "first.hpp"
#include <iostream>

void WhatsUp() {
std::cout << "Simple Demonstration to show use of library and build process"
<< std::endl;
}

void ButWhy() {
std::cout << "We are building the project using only command line arguments "
"to understand the process at root level"
<< std::endl;
}
```

먼저 헤더파일을 인쿠르드 시켜준다. 그리고 이 파일은 이제 library가 된다고 생각하면 된다   
그래서 각 함수들에서 작동하는 코딩이 되어 있게 된다   

이제 이 first.cpp  파일을 라이브러리 해서 이 파일을 main.cpp 파일에서 사용하게 됨 

```cpp
#include "first.hpp"

int main() {
	WhatsUp();
	ButWhy();
	return 0;
}
```

이제 CMakeLists.txt 파일을 작성. 패키지의 root 디렉토리에 위치
```
cmake_minimum_required(VERSION 3.10)

project(first_project)

set(CMAKE_CXX_STANDARD 17)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

add_library(first first.cpp)

add_executable(main main.cpp)

target_link_libraries(main first)
```

project 이름을 정해주고, 변수를 설정 (set),. C++ 버전은 17을 사용
add_library()로 first first.cpp 파일로 지정하는 것을 알 수 있고  
실행가능한 파일은 main main.cpp 로 지정

그래서 link가 되어야 하므로 target_link_libraryies(main first)로 실행가능한 파일인  main을 라이브러리 first로 링크를 해주게 된다   

```
cd src
cmake ..
make
```

컴파일들이 완료가 되면 실행을 할 수가 있다 
```
./main
```

