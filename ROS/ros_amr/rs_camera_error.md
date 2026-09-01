(messenger-libusb.cpp:42) control_transfer returned error, index: 768, error: Resource temporarily unavailable, number: 11

(messenger-libusb.cpp:42) control_transfer returned error, index: 768, error: Resource temporarily unavailable, number: 11



The guide states: "The D435i depth camera generates and transmits the gyro and accelerometer samples independently, as the inertial sensors exhibit different FPS rates (200 / 400Hz for gyro, 63 / 250Hz for accelerometer). Each IMU data packet is timestamped using the depth sensor hardware clock to allow temporal synchronization between gyro, accel and depth frames"


https://www.intelrealsense.com/how-to-getting-imu-data-from-d435i-and-t265/


rs_camera를 실행시킬 때 파라미터로 initial_reset:=true 값을 주면 런치를 할 때 리셋을 함 

어차피 imu만 사용할 예정이라서 color만 true로 하고 
```
  <arg name="enable_fisheye"      default="false"/>
  <arg name="enable_infra1"       default="false"/>
  <arg name="enable_infra2"       default="false"/>
  <arg name="enable_depth"        default="false"/>
  <arg name="enable_color"        default="true"/>
```

파라미터 fps 값을 낮춰본다 (다른놈들은 어차피 실행안됨.color만 낮춰보기 )   
그리고 gyro/accel_fps 도 낮춰본다. 이것은 정해져 있다. 2가지 중 선택, 주석 참고
```
  <arg name="fisheye_fps"         default="30"/> <!-- fps: 30 or 15-->
  <arg name="depth_fps"           default="30"/> 
  <arg name="infra_fps"           default="30"/>
  <arg name="color_fps"           default="15"/> 
  <arg name="gyro_fps"            default="200"/>  <!-- or 400 -->
  <arg name="accel_fps"           default="63"/> <!-- or 250 -->
  <arg name="enable_gyro"         default="true"/> 
  <arg name="enable_accel"        default="true"/>
```

이렇게 하고 나서 워닝 메시지가 계속 반복되지 않는다면 무시해도 된다   
하지만 셀 수 없이 나오면 문제..;;

일단은 이렇게 하면 imu/data 잘 받아진다. 
(unite_imu_method:=linear_interpolation 런치 파라미터 넣어주거나 런치파일 수정 후 )






 28/07 11:13:40,760 WARNING [140021721405184] (ds5-motion.cpp:473) IMU Calibration is not available, default intrinsic and extrinsic will be used.

IMU Calibration 워닝이 나오면  
calibration을 해줘야 하는 듯 하다. 공장에서 캘리브레이션이 안되어 있다고 함    

여기 참고   
https://github.com/IntelRealSense/realsense-ros/issues/1368#issuecomment-688764467




