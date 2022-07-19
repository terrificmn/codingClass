config 파일인 yaml 파일에서   

odom0: 는 wheel odometry를 말하고  
자율주행차에서 보내주는 odom 토픽을 적어주면 된다  

예: odom0: /husky/odom

odom_config 는 true는 fusing을 하겠다는 의미  


gps_navigation을 할 때 먼저 ekf_localizion_node를 실행해서 바퀴 odom를 받고 
다시 두 번째로 또 ekf_localizion_node를 실행해서 wheel odom과 gps odom를 처리할 수 있게 한다   

예: 런치파일
```xml
<node pkg="robot_localization" type="ekf_localization_node"         
name="ekf_localization_odom">
    <rosparam command="load" file="$(find gps_navigation)/config/gps_localization_config.yaml"/>
    </node>

    <node pkg="robot_localization" type="ekf_localization_node"         
name="ekf_localization_gps_map">
    <remap from="odometry/filtered" to="odometry/filtered_map"/>
    
```
이 부분은 테스트를 해봐야함


> odometry는 robot이 처음으로부터 얼마나 움직였는지를 보여줌  
단, 오도메트리는 오류가 많다  


odom과 gps를 사용하게 된다  

odom0은 기존과 동일하게 odometry 이고   
odom1은 gps를 사용  


```
frequency: 30
sensor_timeout: 0.1
two_d_mode: true
transform_time_offset: 0.0
transform_timeout: 0.0
print_diagnostics: true
debug: false

publish_tf: true

publish_acceleration: false

map_frame: map              # Defaults to "map" if unspecified
odom_frame: odom            # Defaults to "odom" if unspecified
base_link_frame: base_link  # Defaults to "base_link" if unspecified
world_frame: map           # Defaults to the value of odom_frame if unspecified
# gps를 사용하려면 map로 world_frame을 해준다(?)

## wheel odometry
odom0: /odom
odom0_config: [false, false, false,   #[     x    ,     y     ,    z    ]
     false, false, false,             #[  roll    ,   pitch   ,   yaw   ]
     true, true, true,               #[  x_vel   ,   y_vel   ,   z_vel ]
     false, false, false,             #[ roll_vel , pitch_vel , yaw_vel ]
     false, false, false]             #[ x_accel  , y_accel   , z_accel ]
odom0_queue_size: 10
odom0_nodelay: true
odom0_differential: false
odom0_relative: false


### gps odometry
odom1: /odometry/gps
odom1_config: [true, true, true,   #[     x    ,     y     ,    z    ]
     false, false, false,             #[  roll    ,   pitch   ,   yaw   ]
     false, false, false,               #[  x_vel   ,   y_vel   ,   z_vel ]
     false, false, false,             #[ roll_vel , pitch_vel , yaw_vel ]
     false, false, false]             #[ x_accel  , y_accel   , z_accel ]

odom1_queue_size: 10
odom1_nodelay: true
odom1_differential: false
odom1_relative: false

### imu
imu0: /imu/data
imu0_config: [false, false, false,
              true,  true,  false,
              false, false, false,
              true,  true,  true,
              true,  true,  true]
imu0_nodelay: true
imu0_differential: false
imu0_relative: false
imu0_queue_size: 10
imu0_pose_rejection_threshold: 0.8                 # Note the difference in parameter names
imu0_twist_rejection_threshold: 0.8                #
imu0_linear_acceleration_rejection_threshold: 0.8  #
imu0_remove_gravitational_acceleration: true

use_control: false

process_noise_covariance: [0.05, 0,    0,    0,    0,    0,    0,     0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0.05, 0,    0,    0,    0,    0,     0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0.06, 0,    0,    0,    0,     0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0.03, 0,    0,    0,     0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0.03, 0,    0,     0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0.06, 0,     0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0.025, 0,     0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0.025, 0,    0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0.04, 0,    0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0,    0.01, 0,    0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0,    0,    0.01, 0,    0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0,    0,    0,    0.02, 0,    0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0,    0,    0,    0,    0.01, 0,    0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0,    0,    0,    0,    0,    0.01, 0,
                           0,    0,    0,    0,    0,    0,    0,     0,     0,    0,    0,    0,    0,    0,    0.015]


initial_estimate_covariance: [1e-9, 0,    0,    0,    0,    0,    0,    0,    0,    0,     0,     0,     0,    0,    0,
                              0,    1e-9, 0,    0,    0,    0,    0,    0,    0,    0,     0,     0,     0,    0,    0,
                              0,    0,    1e-9, 0,    0,    0,    0,    0,    0,    0,     0,     0,     0,    0,    0,
                              0,    0,    0,    1e-9, 0,    0,    0,    0,    0,    0,     0,     0,     0,    0,    0,
                              0,    0,    0,    0,    1e-9, 0,    0,    0,    0,    0,     0,     0,     0,    0,    0,
                              0,    0,    0,    0,    0,    1e-9, 0,    0,    0,    0,     0,     0,     0,    0,    0,
                              0,    0,    0,    0,    0,    0,    1e-9, 0,    0,    0,     0,     0,     0,    0,    0,
                              0,    0,    0,    0,    0,    0,    0,    1e-9, 0,    0,     0,     0,     0,    0,    0,
                              0,    0,    0,    0,    0,    0,    0,    0,    1e-9, 0,     0,     0,     0,    0,    0,
                              0,    0,    0,    0,    0,    0,    0,    0,    0,    1e-9,  0,     0,     0,    0,    0,
                              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,     1e-9,  0,     0,    0,    0,
                              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,     0,     1e-9,  0,    0,    0,
                              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,     0,     0,     1e-9, 0,    0,
                              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,     0,     0,     0,    1e-9, 0,
                              0,    0,    0,    0,    0,    0,    0,    0,    0,    0,     0,     0,     0,    0,    1e-9]

```