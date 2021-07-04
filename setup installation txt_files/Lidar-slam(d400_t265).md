Resource not found: rtabmap_ros
ROS path [0]=/opt/ros/melodic/share/ros
ROS path [1]=/opt/ros/melodic/share
The traceback for the exception was written to the log file

이런식으로 나오면 
```
sudo apt install ros-melodic-rtabmap-ros
```

먼저 중요 토픽을 살펴보면
/camera/accel/sample
/camera/gyro/sample

둘 다 같은 타입 Type: sensor_msgs/Imu

accel 같은 경우에는 

linear_acceleration: 
  x: -1.51071441174
  y: -9.504114151
  z: 0.0

gyro 같은 경우에는 
angular_velocity: 
  x: -0.0479383654892
  y: -0.00852237548679
  z: -0.0106529695913
을 받는다



/t265/odom/sample 토픽 (앞에는 /camera가 될 수도 있음 )

두개를 합친 것 보 topic으로 있다

twist: 
    linear: 
      x: 0.00136115774445
      y: 0.00256334243947
      z: -0.00384404936954
    angular: 
      x: -0.00160790188236
      y: -0.011475427665
      z: 0.00293196970717



L515와 같이 실행을 할려면
rs_rtabmap.launch 파일을 수정해준다
<arg name="device_type_camera2"    		default="l515"/>	<!-- Note: using regular expression. match D435, D435i, D415... -->
<arg name="camera2"              			default="l515"/>



