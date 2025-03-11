# gazebo plugin odom tf 발행하기
> The odom->base_link transform is responsible for keeping track of the motion of the robot based on its odometry sensors.

world 파일 또는 model 파일에서  
플러그인을 사용해서 odom frame 관련 TF 를 퍼블리쉬할 수가 있다. 

```xml
    <plugin
    filename="ignition-gazebo-odometry-publisher-system"
    name="ignition::gazebo::systems::OdometryPublisher">
    <odom_frame>odom</odom_frame>
    <robot_base_frame>base_footprint</robot_base_frame>
    <odom_publish_frequency>50</odom_publish_frequency> <!-- tf관련 hz -->
    <tf_topic>tf</tf_topic> <!-- odom frame 을 publish tf 발행 -->
    </plugin>
```

여기에서 중요한 것은 tf_topic 태그를 이용해서 tf를 다시 발행을 하게 되면  
odom frame 에서 base_footprint 로 이어지는 tf가 만들어 진다.   
물론 robot_statd_publisher가 작동하는 상태에서 해준다.   

## Cartographer 에서 oodm 발행
카토 그래퍼에서 odom tf 를 발행할 수도 있는데  이때에는  
odom topic에 들어가는 frmae_id, child_id? 가 잘 맞아야 한다.  
이유는 odom 토픽을 서브크라이브 에서 tf 를 만들기 때문  

관련 lua 파일에는  odom_frame, provide_odom_frame true 등이 있다.

