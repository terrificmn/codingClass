빌드 및 인스톨도 문제 없이 진행 되었지만   
ROS에서 caktin build를 하니 패키지를 찾지를 못한다 ㅠ  

```
Could not find a package configuration file provided by

"behaviortree_cpp_v3" with any of the following names:

 
behaviortree_cpp_v3Config.cmake

behaviortree_cpp_v3-config.cmake
```

바쁘면 결론부터 아래처럼 설정해준다 (CMakeLists.txt에...)
```cmake
set (behaviortree_cpp_v3_DIR /usr/local/lib/cmake/behaviortree_cpp_v3)
```

## 찾기
1.  find로 찾아보자 
```
find / -name behaviortree_cpp_v3Config.cmake > result
```

결과가 너무 많이 나와서 리다이렉트로 result에 저장  
이제 열어보면  결과가   
```
gedit result
```

/usr/local/stow/absl/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Config.cmake

이제 CMakelists.txt 파일에 set() 이용해서 설정 

```
set (behaviortree_cpp_v3_DIR /usr/local/stow/absl/lib/cmake/behaviortree_cpp_v3)
```

그랬더니 BT 클래스가 레퍼런스 하고 있는 파일이 없다고 한다  

그래서 .. 좀더 찾아봤다.. 아니 잘 모르겠다.

2. 다시 install 
다시 처음에 build를 했던 디렉토리로 가서 다시 make install을 했고  
```
cd ~/BehaviorTree.Cpp/build
```
다시 
```
sudo make install
````

설치가 끝나면서 설치된 장소가 로그로 출력된다. 찬찬히 살펴봤더니  

```
/usr/local/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Targets.cmake
-- Up-to-date: /usr/local/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Targets-noconfig.cmake
-- Up-to-date: /usr/local/lib/cmake/behaviortree_cpp_v3/behaviortree_cpp_v3Config.cmake
```
여기에 설치가 되었다 . .... lib/cmake/ 에 있었군 ㅠ

다시 CMakeLists.txt 파일에 다시 /usr/local/lib/cmake/behaviortree_cpp_v3 바꿨더니  
catkin build 성공!


## CMakeLists.txt  ROS 기준
ROS melodic 기준으로  
```cmake
cmake_minimum_required(VERSION 3.0.2)

project(my_bt)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++14)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
 
set (behaviortree_cpp_v3_DIR /usr/local/lib/cmake/behaviortree_cpp_v3)

find_package(catkin REQUIRED COMPONENTS
	roscpp move_base_msgs std_msgs geometry_msgs roslib tf behaviortree_cpp_v3
)

catkin_package(
	CATKIN_DEPENDS roscpp move_base_msgs std_msgs geometry_msgs tf
)

###########
## Build ##
###########

include_directories(
	${catkin_INCLUDE_DIRS}
)

add_executable(${PROJECT_NAME}_node src/waypoints_client.cpp)

target_link_libraries(${PROJECT_NAME}_node
	${catkin_LIBRARIES}
	BT::behaviortree_cpp_v3
)
```


