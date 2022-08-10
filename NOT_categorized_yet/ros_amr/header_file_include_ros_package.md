```yaml
cmake_minimum_required(VERSION 3.0.2)
project(send_pose)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++14)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp nav_msgs geometry_msgs
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES send_pose
  CATKIN_DEPENDS roscpp nav_msgs geometry_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ library
add_library(${PROJECT_NAME}
  src/send_pose.cpp
)

## Declare a C++ executable
## With catkin_make all packages are built within a single CMake context
## The recommended prefix ensures that target names across packages don't collide
add_executable(${PROJECT_NAME}_node src/send_pose.cpp)

## Add cmake target dependencies of the executable
## same as for the library above
add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

## Specify libraries to link a library or executable target against
target_link_libraries(${PROJECT_NAME}_node
  ${catkin_LIBRARIES}
)

#############
## Install ##
#############
# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark libraries for installation
## See http://docs.ros.org/melodic/api/catkin/html/howto/format1/building_libraries.html
install(TARGETS ${PROJECT_NAME}
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_GLOBAL_BIN_DESTINATION}
)

## Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN *.h 
)

```
add_compile_options(-std=c++14) 같은 경우는 libcoap이 그러함


파일구조는 
패키지명/include/패키지명/common.h 파일이 있음 

그리고 common.h 파일에는  
```
#ifndef SEND_POSE_H
#define SEND_POSE_H

#include ....
int 함수(파라미터, 파라미터) 정의

내용... 생략

#endif
```

맨 위와 아래에 #ifndef 패키지명_H, #define 패키지명_H  맨아래에 #endif 를 써준다 

예를 들어 이제 src/main.cpp 에서 
```
#include "패키지명/common.h" 
```
으로 해주면 된다 


참고   
https://roboticsbackend.com/ros-include-cpp-header-from-another-package/



위에서 h파일에 ifndef, define 부터 endif 해준 것은 다른 것은 아닌 듯 하다. 케이스 바이 케이스?  

일단 다른 건도 살펴보면

## cantcoap 불러오기

기존의 cantcoap은 설치는 cantcoap설치.md 파일을 참고하고  
일단 깃으로 클론하게 되면  안에서 Makefile 로 설정을 하는데, CXX, CC 부분을 각각 g++, gcc로 설정해주면 잘 된다   

그래서 libcantcoap.a 라는 static library 파일이 생기는데 이것을 ros에서 cmakelists에서 가능하게 하려고 했는데  
이것저것 하다가 실패  

> 왜냐하면 기존 cantcoap.h 파일에는 클래스의 enum만 정의가 되어 있기 때문에   
클래스 내용이 거의 들어가 있는 cantcoap.cpp가 필요 -> 빌드하면 cantcoap.a 파일이 생기므로  
추후 static library만 CMakelists.txt로 추가할 수 있는지 연구 필요
반대 성격의 파일에는  .so 파일이 있다 (Shared Libraries라고 하는 듯)


결국은 cantcoap.cpp 파일이 클래스만 정의가 되어 있어서 .h 파일로 변경해서  
해당 패키지의 include/패키지명이름 안에 몽땅 넣어버림

필요한 파일
cantcoap.h, dbg.h, sysdep.h, nethelper.cc, libcantcoap.h 파일 필요하다  

클론받은 곳에서 make 한 후에 ros 패키지에 복사 이동 시킨다  

그리고 cantcoap.cpp 파일은 -> libcantcoap.h 로 변경 했고  
nethelper.c 파일은 -> nethelper.cc 로 변경 

원래 nethelper.h 에서 nethelper.c 파일을 인쿠르드 하는데 그럴 거 없이 짬뽕시킴  

nethelper.c 파일 상단에 아래를 추가한 후 cc파일로 분갑 ㅋㅋ
```
int setupAddress(
	char *host,
	char *port,
	struct addrinfo **output,
	int socktype,
	int protocolFamily
);

void printAddressStructures(struct addrinfo *addr);
void printAddress(struct addrinfo *addr);
```

이제 로스 패키지의 src 의 주인공(?) cpp 파일에  
```
#include "send_pose/libcantcoap.h"
#include "send_pose/cantcoap.h"
#include "send_pose/nethelper.cc"
```
인쿠루드를 시켜주면 되겠다. (앞의 디렉토리는 패키지명)

libcantcoap.h 파일에서는 
```
#include "send_pose/cantcoap.h"
#include "send_pose/sysdep.h"
```
추가로 인쿠르드 시켜준다  

이렇게 되면 catkin build 성공

먼저 위와 CMakelists.txt 파일은 비슷하게 가고 


