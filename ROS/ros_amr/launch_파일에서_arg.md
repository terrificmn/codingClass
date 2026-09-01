예를 들어서  
example.launch 파일을 include 했을 때 현재 런치파일(main.launch라 가정)에서 쓰이는 arg는  
example.launch 파일에서도 아규먼트를 같이 만들어줘야하는 듯 하다

예: main.launch파일 중
```xml
<arg name="first_x_pos" default="-3.0"/>
<arg name="first_y_pos" default="-2.0"/>
<arg name="init_pose_first" default="-x $(arg first_x_pos) -y $(arg first_y_pos) -z 0.0" />
<arg name="init_pose_second" default="-x $(arg second_x_pos) -y $(arg second_y_pos) -z 0.0" />

<group ns="tb3_1">
    <param name="tf_prefix" value="robot1_tf"/>
    <include file="$(find multiple_robots_sim)/launch/example.launch">
        <arg name="init_pose" value="$(arg init_pose_first)"/>
        <arg name="robot_name" value="robot1_tf"/>
    </include>
</group>
```

example.launch 에서도  robot_name, init_pose를 만들어줘야한다 
```xml
<arg name="robot_name"/>
<arg name="init_pose"/>
<node name="spawn_turtlebot3" pkg="gazebo_ros" type="spawn_model"
    args="$(arg init_pose) -unpause -urdf -model $(arg robot_name) -param robot_description"/>
```

