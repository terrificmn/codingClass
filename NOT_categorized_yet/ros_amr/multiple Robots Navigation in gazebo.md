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

노드에서 robot_state_publisher를 런치파일에 넣을 때 noetic에서는   
type=state_publisher deprecated!!  됨
```xml
    <node pkg="robot_state_publisher" type="state_publisher" 
        name="robot_state_publisher" output="screen" /> 
```
그래서 state_publisher 에서 **robot_state_publisher** 로 바꿔줘야 함



xacro.py 도 deprecated   
xacro.py 에서 xacro 로 변경해서 사용할 것 

예를 들어서 아래처럼 사용해야함
```xml
<param name="robot_description" command="$(find xacro)/xacro '$(find mybot_description)/urdf/mybot.xacro'"/>
```


그 밖에 참고할 것  
https://wiki.ros.org/noetic/Migration




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

여기에서 중요한 것은 param을 tf_prefix 를 사용해서 value의 내용이 붙을 수 있게 해서   
파라미터를 이용해서 다 똑같은 로봇을 이름을 다르게 준다   
그렇지 않으면 다 똑같은 tf를 사용하게 된다  

arg init_pose를 이용해서 다른 위치를 사용할 수 있게 한다


launch 파일을 아래와 같다
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

아런식으로 되어야 하지만 tf_prefix 파라미터가 tf2로 업데이트가 되면서 deprecated가 되었다고 한다.   
그래서 group을 하면 그 그룹내에 있는 노드, topic 등에 자동적으로 tf_prefix에서 지정한 value 값이   
예를 들어 위의 코드에서는 만약 cmd_vel topic을 사용한다고 하면  
하나는 robot1/cmd_vel  
두번째는 robot2/cmd_vel  
이런식으로 되어야 하는데 이것이 이제 안 된다고 한다  





