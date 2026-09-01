# ros namespace 사용하기
cli 로 사용할 때 바로 파라미터로 넘겨줄 수가 있다   
예를 들어서 cmd_vel 을 토픽으로 사용하는 텔레옵 프로그램이 있다고 하면   
`/cmd_vel:=네임스페이스/토픽` 이런식으로 전달해서 사용 가능하다
```
rosrun my_teleop teleop_key.py /cmd_vel:=/my_robot1/cmd_vel
```

## launch 파일에서 사용
아예 node 파일을 지정할 때 ns로 네임스페이스를 준다   
```
<node pkg="foo" type="bar" name="my_node" ns="my_namespace" />
```

이렇게 하면 my_node에서 사용하는 모든 토픽들 앞에 `/my_namespace/토픽` 처럼 자동으로 붙게 된다


## c++에서 토픽이름앞에 '/'을 사용 하면..?
토픽명에 /를 넣어서 고정해버리는 효과? 가 있다. 그래서 네임스페이스가 생성이 되지 않는다.   
fully-qualified name 이라고 할 수 있다. 

예를 들어서 /robot_position 이라는 토픽을 발행하고 있을 때  
```cpp
pub = nh.advertise<geometry_msgs::PoseArray>("/robot_position", 1);
```
위 처럼 '/' 까지 넣어서 하게 되면 실행을 했을 때 `rostopic list` 로 확인을 해보면  

> 물론 네임스페이스를 robot1이라고 적용했다고 가정하면 다른 토픽은 제대로 네임스페이스가 되는데,  
위의 토픽만 안 되고 단독으로 있는 걸 확인할 수 있다

```
/robot1/camera/color/image_raw
/robot1/move_base/current_goal
/robot1/move_base/goal

/robot_position
```

그래서 '/'를 빼주게 되면 
```cpp
pub = nh.advertise<geometry_msgs::PoseArray>("robot_position", 1);
```

이제 네임스페이스가 잘 나오게 된다
```
/robot1/otherrobot
```

## 좀 더 편하게 런치파일에서 group ns 로 사용하기
```xml

<group ns="robot1">
    <include file="$(find my_move_base)/launch/my_move_base.launch" />
</group>

<group ns="robot2">
    <include file="$(find my_move_base)/launch/my_move_base.launch" />
</group>
```

이런식으로 적용해주게 되면, 노드가 알아서 네임스페이가 붙어서 실행이 된다   


## 가장 중요한 tf_prefix 사용하기
ros2와 tf_2인가에서는 tf_prefix가 이제는 더 이상 안된다고 함 (deprecated)  
하지만 예전 버전과 호환을 위해서 계속 사용이 가능   

param을 이용해서 tf_prefix을 주면 된다 
```xml

<arg name="ns_1" default="amr_robot1" />
<arg name="ns_2" default="amr_robot2" />

<group ns="$(arg ns_1)">
    <param name="tf_prefix" value="$(arg ns_1)"/>
    <include file="$(find my_move_base)/launch/my_robot.launch" />
    </include>
</group>

<group ns="$(arg ns_2)">
    <param name="tf_prefix" value="$(arg ns_2)"/>
    <include file="$(find my_move_base)/launch/my_robot.launch" />
    </include>
</group>
```

tf_prefix는 노드에 직접 실행하지 말고, include 전에 할 수 있게 해야 잘 되는 듯 하다  


이제 인쿠르드 된  my_robot.launch 에서는  param robot_description 이랑, 노드 robot_state_publisher를 해주면 된다 
```xml
<arg name="robot_name"/>
<arg name="init_pose"/>

<param name="robot_description" command="$(find xacro)/xacro $(find my_package)/urdf/my.xacro" />
    
<node name="robot_state_publisher" pkg="robot_state_publisher" type="robot_state_publisher" />

<node name="$(arg robot_name)_urdf" pkg="gazebo_ros" type="spawn_model" 
    args="$(arg init_pose) -unpause -urdf -model $(arg robot_name) -param robot_description" />
```

