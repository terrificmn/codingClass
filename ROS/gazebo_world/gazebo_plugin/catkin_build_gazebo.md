# gazebo plugin - cakin build 적용
예제에서는 cmake를 사용하는데, ros의 catkin build를 사용해보자(같은 CMakeLists.txt) 를 사용하므로 조금만 수정하면 된다   

GAZEBO_INCLUDE_DIRS 를 좀 더 넣어주고, add_executable()은 기존 rosrun 실행할 수 있게 해주고   
gazebo plugin은 일단 so 라이브러리로 만들게 되어 있어서  
add_library()로 넣어준다. 이 정도만 해주면 잘 된다 

**`add_compile_options(-std=c++17)`** 중요하다. 안 넣어주면 빌드 실패한다 
```c
cmake_minimum_required(VERSION 3.0.2)
project(my_ros_gazebo_example)

add_compile_options(-std=c++17)

find_package(catkin REQUIRED COMPONENTS
    roscpp
)
find_package(gazebo REQUIRED)

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
    ${GAZEBO_INCLUDE_DIRS}
)

link_directories(${GAZEBO_LIBRARY_DIRS})

add_library(
    so파일로만들_라이브러리이름 SHARED 
    src/model_push.cpp # 플러그인 파일
)

add_executable(${PROJECT_NAME}_node 
    src/main.cpp 
)

target_link_libraries(${PROJECT_NAME}_node
    ${catkin_LIBRARIES}
    ${GAZEBO_LIBRARIES}
)
```

기존 cmake에서 build 디렉토리에 만들었던 것이  catkin build를 해주면    

catkin_ws 워크스페이의 devel/lib/ 디렉토리에 심볼릭 링크로 생긴다. -> ~/catkin_ws/devel 의 .private 디렉토리의  
해당 패키지 디렉토리에 실제 so 파일을 가리키고 있게 된다  


그리고 플러그인을  gazebo에서 인식할 수 있게 환경변수 셋팅도 해준다 
```
export $GAZEBO_PLUGIN_PATH=$GAZEBO_PLUGIN_PATH:/home/sgtubunamr/catkin_ws/devel/lib
```

이렇게 하면 일단 cakin build로 해서 ros 패키지로도 만들 수 있다   


## 예제에서 cc 파일로 클래스가 통으로   
cc 예제 파일이 통으로 header파일 없이 구성이 되어 있는데  
head file과 나눠놓은 것은 

spawn_other_robots 패키지를 참고 한다.  (따로 분리할 수 도 있음-)

