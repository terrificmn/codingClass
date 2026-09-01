# tf2 ros
항상 기준이 되는 world 프레임이 필요하다   

URDF 파일로부터 parameter로 받은 robot_description 에서   

robot_state_publisher 노드에서  
Fixed joint transforms ---> /tf_static 으로   
Non-fixed joint transforms ---> /tf   
Copy of URDF ---> /robot_description 

으로 퍼블리쉬가 된다  

> robot_description 은 로봇 모델을 rviz에 표시할 때 사용



## static transform

rosrun tf2_ros static_transform_publisher x y z yaw pitch roll parent_frame child_frame

rviz에서 볼 때 child 에서 parent 로 화살표 표시가 된다  


## dynamic transform

필요 패키지  
```
ros-noetic-xacro
ros-noetic-joint-state-publisher-gui
```

다이나믹 tf를 하기 위해서는 맨 위에서 설명했던 robot_state_publisher 노드에  

/joint_states 라는 토픽으로 JointState 메세지가 퍼블리쉬가 되어서   
linear distance, angles 등의 joint 정보를 퍼블리쉬하게 된다   

이 joint_states 메세지는 다양한 곳에서 만들어 줄 수가 있는데   

Running on hardware 에서는 Real actuator feedback 을 통해서   
testing in simulator 에서는 가제보등의 simulated actuator feedback   
Early Development 일 때에는 joint_state_publisher_gui 를 통해서 가능   

tf2_tools view_frames.py



## URDF and TF
로봇 description 파일인 URDF와 TF는 형태라든지 패턴이 비슷하다   

URDF 에서는 links 들이 Joints 로 연결되어 있는 Tree 구조로 되어 있고   
TF 에서는  Frames를  Transforms 로 연결되어 있는 Tree 구조로 되어 있다   

> URDF로 로봇을 만들었다면 TF도 비슷한 패턴으로 사용이 된다  


## 디버깅시 tf 확인은 

```
rosrun rqt_tf_tree rqt_tf_tree 
```
