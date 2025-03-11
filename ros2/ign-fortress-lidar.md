# fortress lidar
보통 예제를 활용하면 되는데  
libignition-gazebo-sensors-system.so 플러그인을 사용해서  

sensor 태그인 gpu_lidar 부분을 라이다의 link 부분 안에 넣어준다. 

이때 topic 이름 등을 직접 지정해 줄 수가 있고

```xml
<link name="laser_link">
    <pose>0.3 0 0.4 0 0 0</pose>
    <inertial>
        <mass>0.3</mass>
        <!-- 생략 -->
        </inertia>
    </inertial>
    <visual name="visual">
        <!-- 생략 -->
    </visual>
    <collision name="collision">
        <!-- 생략 -->
    </collision>
    <sensor name='gpu_lidar' type='gpu_lidar'>
        <pose>0 0 0 0 0 0</pose>
        <topic>scan</topic>
        <ignition_frame_id>laser_link</ignition_frame_id>
        <update_rate>20</update_rate>
        <lidar>
            <scan>
            <horizontal>
    <!-- 이하 생략 -->
```

ignition_frame_id 값을 지정안하면 기본 값은    
`frame: "myModel::laser_link::gpu_lidar"`

> myModel 은 sdf 의 모델명

## 역시 지정을 안하고 namespace로  사용을 하면 
카토그래퍼 사용 시 
```
[cartographer logger]: W0305 02:05:10.000000 28247 tf_bridge.cpp:53] "myModel/laser_link/gpu_lidar" passed to lookupTransform argument source_frame does not exist. 
```
이런 에러가 발생  
그러므로 ignition_frame_id 지정을 해주는 것이 좋다


## inf 값만 나올 경우  

이때에 sensor 태그 이하의 pose를 기본인 0 0 0 0 0 0 에 맞추게 되면  
만약 내 로봇 모델 안에 들어가 있는 상태라면 scan 데이터가 제대로 안나오게 된다. 

그래서 일단 pose 자체를 lase_link 의 pose와 똑같이 맞추거나 z 값 등으로 올려주던가 해서  
scan 데이터가 inf가 안나오게 해줘야 한다.


만약 gazebo 등에서 플러그인으로 작동할 경우  
scan이 작동을 해도  
```
Queue waiting for data: (0, scan)
[amrslam_app_node-3] W0305 01:57:26.488993 27551 ordered_multi_queue.cc:155] Queue waiting for data: (0, scan)
```
이렇게 계속 기다리는 상황이 생김

## topic 확인
ros2 topic 외 ign 으로 확인할 경우
```
ign topic -e -t /scan
```
`ranges: -inf` 로 나온것을 확인


```
header {
  stamp {
    sec: 76
    nsec: 100000000
  }
  data {
    key: "frame_id"
    value: "laser_link"
  }
  data {
    key: "seq"
    value: "1522"
  }
}
frame: "laser_link"
world_pose {
  position {
  }
  orientation {
    w: 1
  }
}
angle_min: -1.396263
angle_max: 1.396263
angle_step: 0.0043701502347417839
range_min: 0.08
range_max: 40
count: 640
vertical_angle_step: nan
vertical_count: 1
ranges: -inf
ranges: -inf
ranges: -inf
ranges: -inf
ranges: -inf
ranges: -inf
ranges: -inf
```

> 엄청 많으므로 (터미널)이 줄 넘어감에 주의
-n 1 옵션을 넣어서 한번만 볼 수 있음. `ign topic -n 1 -e -t /scan`   



