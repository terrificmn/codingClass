# gazebo bridge
일단 ros2 의 토픽과 gazebo는 다른 토픽을 사용한다.

예를 들어서 ros2의 cmd_vel 토픽은 geometry_msgs/msg/Twist 메세지 인데   
ign의 gazebo는 ignition.msgs.Twist 를 사용한다. 

이를 연결해주는 것은 gz_bridge 이다






## 예제

```
ros2 run ros_gz_bridge parameter_bridge /keyboard/keypress@std_msgs/msg/Int32@ignition.msgs.Int32
```


cmd_vel
```
ros2 run ros_gz_bridge parameter_bridge /cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist
```


/// TODO: 다시 튜토리얼 진행하기