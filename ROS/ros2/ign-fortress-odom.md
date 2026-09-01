# fortress odom
diff_drvie 플러그인을 이용하는 경우  
기본 frame_id 및 child_frame_id 는 각각 모델명/으로 시작
```
frame_id: myModel/odom
child_frame_id: myModel/base_footprint
```

모든 센서 데이터들이 각각의 토픽을 퍼블리쉬 할 때  
각각 frame id 등이 있는데 이것이 모두 urdf에 나오는 프레임(link)들과 일치를 해야  
tf 와 연동 및 cartographer 에서 문제가 없다.  

```
[cartographer logger]: W0305 02:16:00.000000 29544 tf_bridge.cpp:53] "s10myModel0a/base_footprint" passed to lookupTransform argument source_frame does not exist. 
```

> 역시 tf에서 해당 frame을 못찾고 있다.

그래서 frame_id, child_frame_id 를 이용해서 지정을 해줄 수가 있다.

예 world 관련 sdf 나 model sdf 에 플러그인에서 지정

```xml
<plugin 
    filename="libignition-gazebo-diff-drive-system.so"
    name="ignition::gazebo::systems::DiffDrive">
    <left_joint>left_wheel_link_joint</left_joint>
    <right_joint>right_wheel_link_joint</right_joint>
    <wheel_separation>0.6</wheel_separation>  <!-- the distance between the two wheels.-->
    <wheel_radius>0.0220</wheel_radius>  <!-- wheel link 의 raduius 태그-->
    <topic>cmd_vel</topic>
    <odom_topic>odom</odom_topic>
    <frame_id>odom</frame_id>
    <child_frame_id>base_footprint</child_frame_id>
    <odom_publish_frequency>30</odom_publish_frequency>
```

> topic 관련해서는 플러그인에서 직접 지정하면 해당 토픽으로 받을 수가 있다   
물론 gz_bridge 관련에서도 같은 토픽으로 맞춰야지 토픽을 받을 수가 있음에 주의

