1. catkin_create_pkg 로 패키지를 만들고 이 패키지에는 헤더파일과 main파일이 있게 되고   
간단하게 출력, 계산을 하는 함수를 만들고 이것을 다른 패키지에서 include 해서 사용할 수 있게 됨

cmake 기초 basic에 참고  

먼저 catkin_create_pkg 로 prac_library 라는 패키지를 만든다   
```
cd catkin_ws/src
catkin_create_pkg prac_library roscpp
```

ros 컨벤션은 include 디렉토리안에 패키지 이름과 같은 디렉토리가 있고 거기에 header파일을 만들어 준다    
그리고 src 디렉토리에는 라이브러리가 될 파일을 만들어준다  

```
cd ~/catkin_ws/src/prac_library/include/prac_library
touch prac_library.h
cd ~/catkin_ws/src/
touch prac_library.cpp
```
또는 vscode같은 에디터로 만들어준다   

prac_library.h 는 함수를 정의해주는 파일
```cpp
#ifndef PRAC_LIBRARY_H
#define PRAC_LIBRARY_H

#include <ros/ros.h>

void display_pos(float x, float y);
void Calculation(float lin, float ang);

#endif
```

prac_library.cpp는 헤더파일을 이용해서 함수 내용이 들어가 있음
```cpp
#include "../../prac_library/include/prac_library/prac_library.h"
 
void display_pos(float x, float y) {
	float pos_x = x;
	float pos_y = y;
std::cout << "Position x: " << pos_x << std::endl;
std::cout << "Position y: " << pos_y << std::endl;
}

void Calculation(float lin, float ang) {
	std::cout << "Linear velocity: " << lin << std::endl;
	std::cout << "Linear Angular: " << ang << std::endl;
}
```

이제 빌드를 하기 위한 CMakeLists.txt 파일에는  
```cmake
cmake_minimum_required(VERSION 3.0.2)
project(prac_library)

find_package(catkin REQUIRED COMPONENTS
	roscpp
)

catkin_package(
	INCLUDE_DIRS include
	LIBRARIES prac_library
	CATKIN_DEPENDS roscpp
)

include_directories(
	${catkin_INCLUDE_DIRS}
)
 
## Declare a C++ library
add_library(${PROJECT_NAME}
	src/prac_library.cpp
)

  
## Specify libraries to link a library or executable target against
target_link_libraries(${PROJECT_NAME}
	${catkin_LIBRARIES}
)

## Mark libraries for installation
install(TARGETS ${PROJECT_NAME}
	ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
	LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
	RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
)

## Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
	DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
# FILES_MATCHING PATTERN "*.h"
# PATTERN ".svn" EXCLUDE
)
```

catkin_package() 에서 INCLUDE_DIRS, LIBRARIES를 설정하고  
include_directories 및 add_library를 해준다  

이렇게 해서 catkin_make 를 하게 되면 다른 패키지에서 사용할 수 가 있다  

다른 패키지에서 마찬가지로 CMakeLists.txt 파일에 find_package()를 이용해서  
```
find_package(
	prac_library
)
```
이런식으로 사용할 수 가 있고,  헤더파일을 include를 해서 사용을 할 수가 있다  


