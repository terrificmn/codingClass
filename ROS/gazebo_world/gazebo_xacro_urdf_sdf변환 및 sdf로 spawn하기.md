
먼저 xacro 파일에서 urdf로 변환해준다   
그리고 gz sdf 파일로 변환
```
rosrun xacro xacro v100_with_gps_urdf.xacro > v100_converted.urdf

gz sdf -p v100_converted.urdf > v100_robot.sdf
```


package.xml 에 의존성도 추가해준다  

```xml
<build_depend>gazebo_ros</build_depend>
<run_depend>gazebo_ros</run_depend>
```

export 태그를 넣어서 가제보 모델이 들어 있는 패스를 지정해줘야한다   
```xml
<export>
    <gazebo_ros gazebo_model_path="${prefix}/models" />
    <gazebo_ros plugin_path="${prefix}/lib" gazebo_media_path="${prefix}" />
</export>
```

그리고 CMakeLists.txt 파일에도 의존성 관련해서 gazebo_ros를 추가해준다  


```
cmake_minimum_required(VERSION 3.0.2)
project(md_gazebo)

## Compile as C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
    gazebo_ros
)

find_package(gazebo REQUIRED)

link_directories(${GAZEBO_LIBRARY_DIRS})
include_directories(${Boost_INCLIDE_DIR} ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS})

catkin_package(
    DEPENDS gazebo_ros
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
# include
# ${catkin_INCLUDE_DIRS}
)
```


변환한 sdf 파일을 같은 패키지내의 models 디렉토리를 만들고  
로봇이름으로 또 디렉토리를 만들어서  예를 들어서 v100 (모델이름으로 한다)   

그리고 model.sdf (변환한 파일이름 model.sdf로 하고 )  
model.config 파일을 만들어서 다음 내용을 적어준다  

```xml
<?xml version="1.0"?>
<model>
    <name>v100_robot</name>
    <version>0.1.0</version>
    <author>
        <name>gunther</name>
        <email>mildsm@gmail.com</email>
    </author>
    <sdf>model.sdf</sdf>
    <description>
        v100_robot test
    </description>
</model>
```
여기에는 sdf 태그에  model파일을 지정해주면 된다 

그리고 런치파일을 만들어준다 
```xml
<launch>

    <include file="$(find gazebo_ros)/launch/empty_world.launch" >
        <arg name="verbose" value="true"/>
        <arg name="world_name" value="$(find md_gazebo)/worlds/empty.world"/> <!-- Note: the world_name is with respect to GAZEBO_RESOURCE_PATH environmental variable -->
    </include>
    <arg name="robot_name" value="v100_robot"/>
    <arg name="x" value="0.0"/>
    <arg name="y" value="0.0"/>
    <arg name="z" value="0"/>
    <arg name="roll" value="0" />
    <arg name="pitch" value="0" />
    <arg name="yaw" value="0" />
    <arg name="sdf_robot_file" value="$(find md_gazebo)/models/v100_robot/model.sdf" />

    <node name="$(arg robot_name)_spawn_urdf" pkg="gazebo_ros" type="spawn_model" respawn="false" output="screen"
            args="-file $(arg sdf_robot_file) -sdf 
                -x $(arg x) -y $(arg y) -z $(arg z) -R $(arg roll) -P $(arg pitch) -Y $(arg yaw)
                -model $(arg robot_name)" />

</launch>
```

이런식으로 만들어 준다 . sdf파일로 가제보에서 모델을 spawn 해보는데   
메쉬 관련해서 좀 더 공부해봐야함  

