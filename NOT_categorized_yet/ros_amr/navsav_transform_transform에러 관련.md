https://answers.ros.org/question/215904/robot_localization-failed-to-transform-warning/

내용 확인할 것 


일단 navsav_transform 노드는 3가지의 토픽이 있어야 한다 
a imu : sensor_msgs/Imu  
a gps : sensor_msgs/NaviSatFix   
a odometry : nav_msgs/Odometry    

이렇게 필요하다. 만약 1개가 없다면은 제대로 작동을 안 한다.  

> 처음에는 imu가 없으니 그냥 하자 했는데, 안됨 ㅋㅋ 근데 rs camera에서 imu가 달려있다;;;; 이런

IMU 관련 토픽이 없어서 계속 안됨. 

일단 위의 노드는 gps를 UTM 좌표로 바꾸는 것이 가장 큰데 , 그럴려면 odom, imu 데이터가 있어야 한다   
바퀴의 위치와, 방위도 알 수 있어야 하기 때문에   

일단 rs_camera는 d435i는 따로 퍼블리쉬 해주는데 
/camera/accel/sample   
/camera/gyro/sample

imu_filter_madgwick 패키지에서 도움을 받을 수 있다.   
관련 내용 imu_filter_madgwick 설치하기.md


remapping의 to에 들어가는 value 값들은 로봇에서 publish되고 있는 토픽으로 연결해주면 된다  
예를 들어 imu같은 경우에는 위의 imu_filter_madgwick에서 imu/data로 퍼블리싱 하니 그대로 써주고  

gps같은 경우는 하드웨어에 따라서 조금씩 토픽이 달라짐   
ublox의 경우에는 ublox/fix 로 해주고   

마지막 odom같은 경우에는 ekf노드에서 퍼블리쉬하는 /odoemtry/filtered 를 넣어주면 된다    
이것을 navsat_transform노드에서 다시 서브스크라이브 한다  


관련  
http://docs.ros.org/en/lunar/api/robot_localization/html/integrating_gps.html  

파라미터 관련 
http://docs.ros.org/en/noetic/api/robot_localization/html/navsat_transform_node.html   

위의 파라미터에서 방위에 관한 것이 나오므로 읽어 보자






answers.ros.org 내용 중  좋은 내용(?) 인 듯 하여 ㅋㅋㅋ 읽어보자

I pulled down your launch and bag file while I had DropBox access the other day, and am just now looking at them. Here are the problems I see. Note that I don't think I have your latest launch file, as the topic names appear to be very different.

    Here is a sample IMU message from the bag file:
```
    header: 
      seq: 756
      stamp: 
        secs: 1439616291
        nsecs: 130379310
      frame_id: Imu_link
    orientation: 
      x: 1.0
      y: 0.0
      z: 0.0
      w: 0.0
    orientation_covariance: [0.01, 0.0, 0.0, 0.0, 0.01, 0.0, 0.0, 0.0, 100.0]
    angular_velocity: 
      x: 0.0
      y: 0.0
      z: -0.05
    angular_velocity_covariance: [1e-06, 0.0, 0.0, 0.0, 1e-06, 0.0, 0.0, 0.0, 1e-06]
    linear_acceleration: 
      x: 0.0
      y: 0.0
      z: 0.0
    linear_acceleration_covariance: [0.02, 0.0, 0.0, 0.0, 0.02, 0.0, 0.0, 0.0, 0.02]
```

    First, the orientation appears to be the identity quaternion, but the identity quaternion should have x = 0.0 and w = 1.0. Second, if your IMU doesn't report orientation, navsat_transform_node will not function. See "Required Inputs" here. You'll need an earth-referenced heading, e.g., from a compass.

    The launch file I'm looking at doesn't appear to show anything to do with the navsat_transform_node, but just looking at the error message above, I think you must have your GPS odometry configuration something like this:
```
     <rosparam param="odom0_config">[false, false, false, 
                                     false, false, false, 
                                     true,  false, false, 
                                     false, false, false, 
                                     false, false, false]</rosparam>
```
    First, make sure that your odom0 setting really is for the GPS odometry. Next, note that the GPS odometry data only has pose information (X, Y, and optionally Z) in it. The configuration settings above are incorrect, because they have X velocity set to true. In your case, the reason I think you have something akin to the configuration above is that the transform failure was from an empty frame_id to base_footprint. The only time the filter attempts to transform into the body frame is when it's attempting to fuse a velocity. Your GPS odometry message has a blank child_frame_id (for the velocity component of the message), and the filter is trying to transform it into the body frame.

In any case, you should first fix your IMU message, and we'll go from there.

EDIT in response to the comments below

We'll pretend for a moment that you have a compass in your IMU so that I can address your question.

The use_odometry_yaw parameter, when set to true, renders the IMU input to navsat_transform_node unnecessary, yes. However, if you were to turn on differential mode or relative mode for your yaw sensor within ekf_localization_node, then you wouldn't be able to use the use_odometry_yaw setting, and you'd have to use your IMU directly with navsat_transform_node. This is because the yaw that you feed to navsat_transform_node must be earth-referenced. In other words, if you make your IMU face directly east, it should always read the same value (preferably 0, but navsat_transform_node lets you specify an offset).

Getting back to your IMU, this is the same problem that you will have. Your IMU reads zero when you first start its driver, regardless of whatever direction you're facing. In order to transform from an earth-referenced coordinate system (WGS-84 or UTM coordinates, as obtained from a GPS device) to your local (map or odom) frame, we need to know which way the robot is facing within that coordinate system at the start of execution. In other words, if your IMU only reports angular velocities, it won't work with navsat_transform_node. You'll get a result, but it won't be correct.

Re: the yaw jumping, I'd have to look at the bag file, which I will check out later tonight.

EDIT in response to question about yaw jumping

    Your navsat_transform launch file as <param name="use_odometry_yaw" value="true" />. See the use_odometry_yaw description on the wiki. This setting should only be true if your heading coming out of the EKF/UKF is earth-referenced. You aren't feeding your mag data to the UKF, so this needs to be false for you, which will force the node to use the IMU data.
    You should have your Y velocity set to true for your wheel encoder odometry. Otherwise, nothing is measuring it, so both yaw velocity and yaw itself will have massive variances, and that will have a knock-on effect of making the covariance values explode for all correlated variables.
    Your navsat_transform launch files is using the wrong UKF output. You have <remap from="/odometry/filtered" to="/odom_ukf" />, but it should be <remap from="/odometry/filtered" to="/odom_gps" />.

I also still don't recommend feeding the output of one UKF into another. It may work just fine, but you're introducing an additional delay before the IMU and odometry data are fused with the map/gps instance of the UKF. Also, the frequency of your sensor data isn't so great that it should really tax your CPU to do the fusion twice.

Anyway, I've uploaded a zip file containing a filtered bag file (with only the raw sensor data in it) and the launch file I put together for your data. Everything appears to be working fine with it, so you can use it as a reference or adapt it to your own needs.



