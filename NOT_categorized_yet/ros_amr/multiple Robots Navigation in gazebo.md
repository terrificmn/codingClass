추후 다시 한번 살펴보기   
https://github.com/nocoinman/Multi-Robot-Coverage-Planning

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

https://github.com/gingineer95/Multi-Robot-Exploration-and-Map-Merging/tree/main/launch   
여기확인 - 일단 됨 


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

3. 그 밖에 noetic에서 바뀐 것들 참고할 것  
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

그런데 여기에서 파라미터를 이용해서 tf_prefix를 사용하는 부분이 있었는데 tf_prefix를 사용하는 것도  
**더 이상 지원이 안된다고 한다**  
일단 아래와 같은 방식으로 실행시키는 것을 *참고만* 하자

launch 파일 예
```xml
<launch>
    <param name="robot_description" command="$(find xacro)/xacro.py $(find turtlebot3_description)/robots/urdf/turtlebot3_burger.urdf.xacro">

    <group ns="robot1">
        <param name="tf_prefix" value="robot1_tf" />  ## tf_prefix를 이용해서 앞에 value값이 붙는다 
        <include file="$(find multiple_turtlebots_sim)/launch/one_robot.launch">
            <arg name="init_pose" value="-x 3 -y 1 -z 0" /> ## use different place
            <arg name="robot_name" value="Robot1" />
        </include>
    </group>


    <group ns="robot2">
        <param name="tf_prefix" value="robot2_tf" />
        <include file="$(find multiple_turtlebots_sim)/launch/one_robot.launch">
            <arg name="init_pose" value="-x -4 -y 1 -z 0" />
            <arg name="robot_name" value="Robot2" />
        </include>    
    </group>


    <group ns="robot3">
        <param name="tf_prefix" value="robot3_tf" />
        <include file="$(find multiple_turtlebots_sim)/launch/one_robot.launch">
            <arg name="init_pose" value="-x 1 -y -6 -z 0" />
            <arg name="robot_name" value="Robot3" />
        </include>
    </group>

</launch>

```

아런식으로 되어야 하지만 위에서 말한 것 처럼  
tf_prefix 파라미터가 tf2로 업데이트가 되면서 deprecated가 되었다고 한다.   
그래서 group을 하면 그 그룹내에 있는 노드, topic 등에 자동적으로   
예를 들어 위의 코드에서는 만약 cmd_vel topic을 사용한다고 하면  
하나는 robot1/cmd_vel  
두번째는 robot2/cmd_vel  
이런식으로 되어야 하는데 이것이 이제 안 된다고 한다  

그래서 방법을 살짝 바꿔서 group은 하되 각 노드를 실행시키는 방법으로 변경  
먼저 아규먼트 부분을 살펴보자  
처음 시작할 좌표를 선택해 준 다음에 실행할 노드에서 쓰인다

```xml
<arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/>
    <arg name="first_x_pos" default="-2.0"/>  ## x좌표 
    <arg name="first_y_pos" default="-2.0"/>  ## y좌표
    <arg name="second_x_pos" default="2.0"/> 
    <arg name="second_y_pos" default="-2.0"/>
    
    <!-- combine x / y_pos--> ## 로봇 좌표를 하나의 아규먼트에 넣어준다 -x -y -z 식
    <arg name="init_pose_first" default="-x $(arg first_x_pos) -y $(arg first_y_pos) -z 0.0" />
    <arg name="init_pose_second" default="-x $(arg second_x_pos) -y $(arg second_y_pos) -z 0.0" />

    ## 월드파일을 열어주기
    <include file="$(find gazebo_ros)/launch/empty_world.launch">
        <arg name="world_name" value="$(find multiple_robots_sim)/worlds/office_small.world"/>
        <arg name="use_sim_time" value="true"/>
        <arg name="gui" value="true"/>
    </include>
```

그 다음 로봇 group부분
```xml
<group ns="tb3_1">  ## 이제 토픽명등에서 네임스페이스로 tb3_1/ 붙음
        <include file="$(find multiple_robots_sim)/launch/tb3_robot1.launch">
            <arg name="init_pose" value="$(arg init_pose_first)"/>  ## 위에서 합쳐준 값을 사용하게 됨
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

위에서 world 및 모델 파일을 github 주소 업데이트

