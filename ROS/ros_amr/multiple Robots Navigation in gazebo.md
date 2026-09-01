추후 다시 한번 살펴보기   
   
[여기 깃허브는 py script가 있고 런치파일은 별 도움은 안되지만 나중에 py코드나 cpp 코드 필요할 경우 살펴보기](https://github.com/nocoinman/Multi-Robot-Coverage-Planning)


[multirobot 관련 launch파일 참고할 수 있음- 깃허브링크](https://github.com/gingineer95/Multi-Robot-Exploration-and-Map-Merging/tree/main/launch)




먼저 시뮬레이션을 하기 위해서 turtlebot3 패키지를 받아준다 

turtlebot3, turblebot3_msgs, turtlebot3_simulation 이 필요함

디렉토리 만들고 workspace로 만들기
```
mkdir -p turtlebot3_ws/src
```

토픽 수동으로 보내기
```
rostopic pub -1 /tb3_1/cmd_vel geometry_msgs/Twist -- '[0.0, 0.0, 0.0]' '[0.0, 0.0, 0.3]'
```




# deprecated
# deprecated
# deprecated
# deprecated

1. 노드에서 robot_state_publisher를 런치파일에 넣을 때 noetic에서는   
type=state_publisher deprecated!!  됨
```xml
    <node pkg="robot_state_publisher" type="state_publisher" 
        name="robot_state_publisher" output="screen" /> 
```
그래서 state_publisher 에서 **robot_state_publisher** 로 바꿔줘야 함



2. xacro.py 도 deprecated   
xacro.py 에서 xacro 로 변경해서 사용할 것 

예를 들어서 아래처럼 사용해야함
```xml
<param name="robot_description" command="$(find xacro)/xacro '$(find mybot_description)/urdf/mybot.xacro'"/>
```

3. robot_description
```xml
    <!-- Spawn the model in gazebo -->
    <node name="spawn_turtlebot3" pkg="gazebo_ros" type="spawn_model"
        args="$(arg init_pose) -urdf -model $(arg robot_name) -param robot_description"/>
```
에서 -param 은 robot_description 이고 앞에서 /를 붙이면 에러 발생함

4. 그 밖에 noetic에서 바뀐 것들 참고할 것  
https://wiki.ros.org/noetic/Migration




## 런치 파일에서 group로 실행하다
launch 파일에서 robots.launch 파일을 만들고   
group 태그를 이용해서 그룹별로 묶어 준다  
그룹은 그룹이름이 네임스페이스 역할을 한다   
그래서 모든 토픽 등이 그룹이름 다음에 / 가 붙게 된다 

예를 들면 group ns="robot1", group ns="robot2" 로 2개의 그룹이 있다면  
cmd_vel 이나 odom 토픽을 사용하게 되면 앞에 /로 구분지어 사용할 수 있게 된다  
즉, 토픽명 앞에 각각의 그룹명이 네임스페이스로 쓰여지게 된다  

예  
```
robot1/odom     
robot2/odom
```

launch 파일 예 
1. 방법 1 파라미터 tf_prefix를 이용해서 실행   
위의 토픽 예 처럼 되어야 하지만 위에서 말한 것 처럼  
~~tf_prefix 파라미터가 tf2로 업데이트가 되면서 deprecated가 되었다고 한다. 2020년~~   

하지만 Noetic에도 2021 10월쯤 업데이트가 PR이 되어서 Noetic에서도 Melodic에서 사용한 것 처럼 된다고 함

spawn_robots_prefix.launch 파일 중에
```xml
<launch>
    
    <arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/>
    <arg name="first_x_pos" default="-3.0"/>
    <arg name="first_y_pos" default="-2.0"/>
    <arg name="second_x_pos" default="-3.0"/>
    <arg name="second_y_pos" default="-1.0"/>
    
    <!-- combine x / y_pos-->
    <arg name="init_pose_first" default="-x $(arg first_x_pos) -y $(arg first_y_pos) -z 0.0" />
    <arg name="init_pose_second" default="-x $(arg second_x_pos) -y $(arg second_y_pos) -z 0.0" />

    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(find multiple_robots_sim)/worlds/office_small.world"/>
        <arg name="use_sim_time" value="true"/>
        <arg name="gui" value="true"/>
    </include>

    <group ns="tb3_1">
        <param name="tf_prefix" value="robot1_tf"/>
        <include file="$(find multiple_robots_sim)/launch/one_robot.launch">
            <arg name="init_pose" value="$(arg init_pose_first)"/>
            <arg name="robot_name" value="robot1_tf"/>
        </include>
    </group>

    <group ns="tb3_2">
        <param name="tf_prefix" value="robot2_tf"/>
        <include file="$(find multiple_robots_sim)/launch/one_robot.launch">
            <arg name="init_pose" value="$(arg init_pose_second)"/>
            <arg name="robot_name" value="robot2_tf"/>
        </include>
    </group>

</launch>
```
위의 방법은 ros 노드에 namespace를 붙여줌과 동시에 모든 토픽에도 group ns로 지정한 이름이 들어가게 된다.  
tf_prefix는 include 전에 줘서 파라미터를 확실하게 주고,   
include 되는 one_robot.launch 파일 등에서는 직접 파라미터를 적용하지 않음 (tf_prefix) - 잘 안됨


2. 다른 방법으로는 파라미터를 사용 안하고 각기 다른 런치파일을 실행을 시킨다   
(추천하지 않음. 공통의 런치파일을 사용하는 것이 아니고 별개로 계속 만들어줘야 하기 때문)
```xml
    
    <group ns="tb3_1">
        <include file="$(find multiple_robots_sim)/launch/tb3_robot1.launch">
            <arg name="init_pose" value="$(arg init_pose_first)"/>
            <arg name="robot_name" value="tb3_robot1"/>
        </include>
    </group>

    <group ns="tb3_2">
        <include file="$(find multiple_robots_sim)/launch/tb3_robot2.launch">
            <arg name="init_pose" value="$(arg init_pose_second)"/>
            <arg name="robot_name" value="tb3_robot2"/>
        </include>
    </group>
```


이제 위의 런치파일에서 그룹태그로 묶여서 one_robot.launch 파일이 실행됨   
여기에서 robot_description 과 robot_state_publisher spawn_model 실행  
```xml
<launch>
    <arg name="robot_name"/>
    <arg name="init_pose"/>
    <arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/>

    <!-- Load the specific robot decription for turtlebot3 -->
    <param name="robot_description" 
        command="$(find xacro)/xacro --inorder $(find turtlebot3_description)/urdf/turtlebot3_$(arg model).urdf.xacro" />

    <!-- Start the robot state publisher -->
    <node pkg="robot_state_publisher" type="robot_state_publisher" name="robot_state_publisher"
        output="screen">
        <param name="publish_frequency" type="double" value="50.0" />
    </node>

    <!-- Spawn the model in gazebo 가제보 서비스임-->
    <node name="spawn_turtlebot3" pkg="gazebo_ros" type="spawn_model"
        args="$(arg init_pose) -unpause -urdf -model $(arg robot_name) -param robot_description"/>

</launch>
```





위에서 world 및 모델 파일을 github 주소 업데이트


이제 tb3_robot1.launch 파일을 보면  
robot_state_pulisher 와 gazebo_ros 패키지의 spawn_model 이 있는데 이를 살펴보면  

https://wiki.ros.org/gazebo 를 확인해보자 https://wiki.ros.org/gazebo  


roslaunch를 통해서 spawn URDF robots 사용하는 방법에는   
ROS service call Spawn Method가 있음  

