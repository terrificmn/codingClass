# cartographer imu failure
카토 그래퍼에서 imu를 사용할 경우에  
`TRAJECTORY_BUILDER_2D.use_imu_data = true` 로 사용한다면, 

imu 토픽이 제공되어야 하는데 이때 
```
[sensor_bridge.cpp:136] Check failed: sensor_to_tracking->translation().norm() < 1e-5 The IMU frame must be colocated with the tracking frame. Transforming linear acceleration into the tracking frame will otherwise be imprecise.
```
이런 에러로 문제가 발생하는 경우가 생김  (0.00001)

이때에는 카토그래퍼의 tracking_frame이 imu 에서 퍼블리쉬하는 frame_id 를 추적하게 해줘야한다.  

우선 로봇 urdf 나 xacro에서 imu 관련 link를 만들어 주고 imu 또는 imu_link  

특히 Gazebo Fortress를 사용하는 경우에는 imu sensor태그 부분에   
gz_frame_id 부분에서 imu frame_id를 지정할 수가 있는데 이때 urdf 와 맞춰서 링크 이름으로 frame_id 를 지정해주고
예
```xml
<sensor name="imu_sensor" type="imu">
    <!-- 생략 -->
    <topic>imu</topic>
    <gz_frame_id>imu_link</gz_frame_id>
    <!-- 생략 -->
```

> plugin은 ignition-gazebo-imu-system

마지막으로 cartographer 관련 lua 설정에서  
```lua
options = {
    -- 생략
  tracking_frame = "imu_link",
  -- 생략
```




