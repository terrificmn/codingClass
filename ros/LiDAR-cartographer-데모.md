# cartographer 데모
데모 파일 실행해보기
```
wget -P ~/Downloads https://storage.googleapis.com/cartographer-public-data/bags/backpack_2d/cartographer_paper_deutsches_museum.bag

roslaunch cartographer_ros demo_backpack_2d.launch bag_filename:=${HOME}/Downloads/cartographer_paper_deutsches_museum.bag
```

___

먼저 lua 파일을 만들어야하고
cartographer_ros/configuration_files 에 보면 각종(?) .lua 파일이 있는데 
하나를 만들어 주면된다

catkin_create_pkg 를 하나 만들어 주고
```
catkin_create_pkg slam_cartographer roscpp 
```
그리고 만들어진 패키지 디렉토리로 이동

그리고 
mkdir config launch

config 디렉토리에 lua파일을 만들어 주는데 summit.lua 로 만들어 준다

기존에 cartographer_ros 안에 있는 파일을 참고해서 만들어 준다


노드가 실행되고 있을 때 트리 확인하기 pdf 파일로 만들어 준다
```
 rosrun tf view_frames 
```

launch 파일도 비슷하게 참고해서 복사해서 만들어준다

catkin_iso_ws (다른 워크스테이션으로 만듬) 로 이동해서 아래명령어를 해줌
```
cd catkin_iso_ws
source install_isolated/setup.bash
ropack profile
```
이렇게 해줘야지 제대로 인식한다 (이것도 되는 듯 source devel_isolated/setup.bash)
bashrc 파일을 열어서 맨 아래에 추가해주자
```
vi ~/.bashrc
source $HOME/catkin_ws_iso/install_isolated/setup.bash
```


## 데모 실행
런치파일로 데모 파일을 실행할 때 데모 파일명을 같이 넘겨야 실행이 된다    
Downloads 디렉토리에 데모 파일이 있다고 하면 아래 처럼 실행 

[다운은 여기에서 받을 수 있음 - Deutsches Museum](https://google-cartographer-ros.readthedocs.io/en/latest/demos.html#deutsches-museum-1)

2D 데모를 받아 준다. 그리고 실행

```
roslaunch cartographer_ros demo_backpack_2d.launch  bag_filename:=$HOME/Downloads/cartographer_paper_deutsches_museum.bag
```


아마도 런치파일과 lua 파일을 잘 바꿔야지 잘 나올 듯 하다

런치파일을 실행해보면 cartographer_node 가 실행이 되는데

rostopic list 및 echo로 확인을 해보면
```
ubun@ubun-sc:~$ rostopic list

ubun@ubun-sc:~$ rostopic info /points2
Type: sensor_msgs/PointCloud2

Publishers: None

Subscribers: 
 * /cartographer_node (http://ubun-sc:38707/)


ubun@ubun-sc:~$ rostopic info /imu/data
Type: sensor_msgs/Imu

Publishers: None

Subscribers: 
 * /cartographer_node (http://ubun-sc:38707/)

```
위의 두개의 토픽을 cartographer_node에서 구독하고 있는 것을 알 수 있고



rosrun tf_view_frames



그리고 조작은 일단 scout-mini는 시리얼통신으로 무선조종으로 움직이자

rviz에서 Map부분에서 topic을 /map으로 변경 해줘야한다

.lua 파일에서 tracking_frame 은 IMU가 있는 프레임을 써줘야하는데 이게 잘 안된다
tracking_frame = "imu_link", 이 부분을 해결해야한다

rostopic echo -n1 /odom
이 있는지도 확인해 볼 것 - 나오는 것 없음!!!

오도메트리는 처음 전원을 킨 위치가 0이 된다 
(pose와 twist가 있는 )

t265 트랙킹 카메라의 positions을 odometry input으로 사용해보기 . IMU는 잘 안되었다고 함;;;

[참고 블로그](https://medium.com/@explorer51uva/cartographer-odometry-af3c7e1cea00)


lua파일 관련 참고하기
use_odometry = false 로 설정했다고 함
T265 의 IMU data을 카토그래퍼에서 사용하는 것은 실패했다고 함 - 나랑 같은 메세지
(error messages asking for the IMU frame to be colocated with the tracking frame)

x is forward from the starting point, y is to the left, and z is upwards. 

```
    TRAJECTORY_BUILDER_2D.max_range and min_range: I had previously set this to 12, the maximum range reported by our LIDAR, and 0.5 (greater than the minimum 0.15 for our LIDAR to prevent the rover from including its own antennas or wires on the map)

    TRAJECTORY_BUILDER_2D.motion_filter.max_time_seconds = 0.1 (default is 5. It seems that LIDAR data is only inserted every 5 seconds by default)

    TRAJECTORY_BUILDER_2D.ceres_scan_matcher.occupied_space_weight = 10. (default is 1. This apparently gives more weight to previously detected features)

    POSE_GRAPH.optimization_problem.odometry_rotation_weight = 10

    POSE_GRAPH.optimization_problem.odometry_translation_weight = 1.

    POSE_GRAPH.optimization_problem.fixed_frame_pose_translation_weight = 1e-1

    POSE_GRAPH.optimization_problem.fixed_frame_pose_rotation_weight = 1e-1

    The default values for the above settings are 1e5, 1e5, 1e1, and 1e2. Since the odometry wasn’t even being used at all, I assume this change might make the rover less likely to get lost by rotating, as rotation and translation weights are now equal.
```

리맵은 to="/robot_pose"라면 to pull data from the “/robot_pose” 
from은 topic output by cartographer :카토그래퍼가 내보내는 토픽이 됨. 이게 좀 헤깔리지만 (마치 거꾸로 되어 있는 듯하다)
하는 방법은 해당 깃허브나 매뉴얼에서 나오는 subscriber/publisher를 확인해봐야한다
그래서 어떤 토픽을 받고 어떤 토픽을 보내는지 확인


하다하다 정 안 되면 bag파일 저장해서 하는 방식이 되는지도 해보자

2d용은 lua파일은 backpack_2d.lua 를 사용하면 됨 

3d 용도 하나 만들어 놓기
3d shemssm cartographer_node 를 사용 backpack_3d.lua 설정파일 설정
remap은  from="points2_1"  to="horizontal_laser_3d"
remap은  from="points2_2"  to="vertical_laser_3d"
이런식으로 하는 듯 하다

리맵에서 _N 식으로 사용하면 여러개의 센서를 사용

cartographer_occupancy_grid_node 는 ros map 대신에 
submap 이 포맷으로 퍼블리싱하는데 nav_msgs/OccupancyGrid로 바꿔주는 노드임

.lua 파마미터
options.num_subdiviions_per_laser_scan
laser scan 센서 frequency가 떨어지고 로봇의 속도가 빠르면 키워주면 좋다고 함
늘릴수록 속도 느려진다

TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching
속도가 느려지지만 local map의 정확도가 좋아진다.

TRAJECTORY_BUILDER_2D.real_time_correlative_scan_matcher parameters: 
local map의 정확도 제어

TRAJECTORY_BUILDER_2D.submaps.num_range_data:
local map에 들어가는 scan의 갯수를 정하는 파라미터. odometry error가 크면 줄이면 좋다고 한다





## 맵 저장

맵 저장하기 (2D)
```
rosrun map_server map_saver -f map_name
```

2D 맵이 생성이 되었으면 Navigation부분을 만들어줘야하는데 일단 패키지로 만들어준다
패키지에서는 launch, map, src 디렉토리등을 포함하고 위에 만들어진 map.pgm, map.yaml 파일을 넣어준다
launch 디렉토리에는 필요한 amcl, move_base, navigation 런치파일등이 필요하게 된다

(navigation에는 map server, localization, move_base, rviz가 필요하다)
scout-mini 의 acml 과 move_base 참고하기 (description)


https://www.youtube.com/watch?v=GzZGl0kzGOM
이어서 봐야할 듯



https://www.youtube.com/watch?v=bXNK8VTQ4zo 참고



https://www.programmersought.com/article/53468612944/ 추후 참고




# localization Mode 는 
런치파일은 거의 동일하며
```
 <node name="cartographer_node" pkg="cartographer_ros"
      type="cartographer_node" args="
          -configuration_directory
              $(find cartographer_ros)/configuration_files
          -configuration_basename backpack_2d_localization.lua"
          -load_state_filename $(arg load_state_filename)
      output="screen">
    <remap from="scan" to="horizontal_laser_2d" />
  </node>
  ```

lua파일은 backpack_2d_localization.lua 와 여기에서 include하는 backpack_2d.lua 파일정도를 참고해보자
런치파일 구성은 거의 비슷하고
TRAJECTORY_BUILDER.pure_localization = true 를 넣어준다


대신      -load_state_filename $(arg load_state_filename)
이런게 들어감
POSE_GRAPH.optimize_every_n_nodes = 20
이것은 낮은 헤르츠로도 가능하기 때문에 그렇다고 함 (mapping 할 때보다 낮은 값)

이게 pbstream 파일이라는 것인데 맵핑이 끝나면 service 요청을 해서 저장을 해야하는 듯하다
/write_state 토픽을 살펴보자
맞다면 rosservice call /write_state 정도가 될 듯



노드들
cartographer_offline_node
rosbag 파일이 있으면 빠른속도로 맵핑을 할 수 있게해주는 노드 (실시간 아님)

cartographer_assets_writer 노드
rosbag과 생성된 state (pbstream파일로)로 3차원 맵을 만드는 것

cartographer_rosbag_validate
실행해도 되는 rosbag인지 체크해주는 노드


원래는 같은 지역을 계속 반복해서 맵 정확도를 높여 주는게 좋다.
하지만 너무 많이 가면 같은 값만 쌓이므로 메모리만 낭비된다 
-- 그런데 왜 더블링? 오버랩핑이 될까? ㅠㅠ


AMCL은 고정된 곳에서 로컬리제이션을 할 때 주로 사용한다고 함



t265런치파일 참고하기
```xml
<launch>
<!-- change the serial number to the correct one for the camera that is being used -->
  <arg name="serial_no"           default="905312111492"/>  
  <!-- d435I  845112071659 t265 905312111492 -->
  <arg name="json_file_path"      default=""/>
  <arg name="camera"              default="rs_t265"/>
  <arg name="tf_prefix"           default="$(arg camera)"/>
  <arg name="initial_reset"       default="true"/>


  <arg name="fisheye_width"       default="848"/> 
  <arg name="fisheye_height"      default="800"/>
  <arg name="enable_fisheye1"     default="true"/>
  <arg name="enable_fisheye2"     default="true"/>

  <arg name="fisheye_fps"         default="30"/>

  <arg name="gyro_fps"            default="200"/>
  <arg name="accel_fps"           default="62"/>
  <arg name="enable_gyro"         default="true"/>
  <arg name="enable_accel"        default="true"/>

  <arg name="enable_sync"           default="false"/>

  <arg name="linear_accel_cov"      default="0.01"/>
  <arg name="unite_imu_method"      default="linear_interpolation"/>
  <arg name="publish_odom_tf"       default="true"/>
  <arg name="odom_frame_id"         default="odom"/>
  <arg name="topic_odom_in"         default="/rr_robot/mobile_base_controller/odom"/>
  <arg name="calib_odom_file"       default="$(find dev_platform_base)/config/calibration_odometry.json" />"/>
  <arg name="base_frame_id"         default="$(arg tf_prefix)_link"/>
  <arg name="pose_frame_id"         default="$(arg tf_prefix)_pose_frame"/>
  
  
  <group ns="$(arg camera)">
    <include file="$(find realsense2_camera)/launch/includes/nodelet.launch.xml">
      <arg name="tf_prefix"                value="$(arg tf_prefix)"/>
      <arg name="serial_no"                value="$(arg serial_no)"/>
      <arg name="json_file_path"           value="$(arg json_file_path)"/>

      <arg name="enable_sync"              value="$(arg enable_sync)"/>

      <arg name="fisheye_width"            value="$(arg fisheye_width)"/>
      <arg name="fisheye_height"           value="$(arg fisheye_height)"/>
      <arg name="enable_fisheye1"          value="$(arg enable_fisheye1)"/>
      <arg name="enable_fisheye2"          value="$(arg enable_fisheye2)"/>

      <arg name="fisheye_fps"              value="$(arg fisheye_fps)"/>
      <arg name="gyro_fps"                 value="$(arg gyro_fps)"/>
      <arg name="accel_fps"                value="$(arg accel_fps)"/>
      <arg name="enable_gyro"              value="$(arg enable_gyro)"/>
      <arg name="enable_accel"             value="$(arg enable_accel)"/>

      <arg name="linear_accel_cov"         value="$(arg linear_accel_cov)"/>
      <arg name="initial_reset"            value="$(arg initial_reset)"/>
      <arg name="unite_imu_method"         value="$(arg unite_imu_method)"/>
      <arg name="publish_odom_tf"          value="$(arg publish_odom_tf)"/>
      <arg name="topic_odom_in"            value="$(arg topic_odom_in)"/>
      <arg name="calib_odom_file"          value="$(arg calib_odom_file)"/>
      <arg name="odom_frame_id"            value="$(arg odom_frame_id)"/>
      <arg name="base_frame_id"            value="$(arg base_frame_id)"/>
      <arg name="pose_frame_id"            value="$(arg pose_frame_id)"/>
    </include>
  </group>
  <!-- the realsense overrides the URDF transforms from the .xacro, so to over rule it back, we place the 
  base link to realsense link with a static tf -->
  <node pkg="tf" type="static_transform_publisher" name="base_link_to_rs_t265_link" args="0.33 0 0.29 3.1457 3.1457 0 base_link $(arg tf_prefix)_link 100" />
  
</launch>

```

lua파일
```
include "map_builder.lua"
include "trajectory_builder.lua"

-- Cartographer_ros configuration reference:
-- https://google-cartographer-ros.readthedocs.io/en/latest/configuration.html

options = {
  map_builder = MAP_BUILDER,
  trajectory_builder = TRAJECTORY_BUILDER,
  map_frame = "map",
  tracking_frame = "rs_t265_link",
  published_frame = "base_link",
  use_odometry = true,
  provide_odom_frame = true,
  odom_frame = "odom",
  publish_frame_projected_to_2d = false,
  use_pose_extrapolator = on,
  use_nav_sat = false,
  use_landmarks = false,
  num_laser_scans = 1,
  num_multi_echo_laser_scans = 0,
  num_subdivisions_per_laser_scan = 1,
  num_point_clouds = 0,
  lookup_transform_timeout_sec = 0.2,
  submap_publish_period_sec = 0.3,
  pose_publish_period_sec = 5e-3,
  trajectory_publish_period_sec = 30e-3,
  rangefinder_sampling_ratio = 1.,
  odometry_sampling_ratio = 1.,
  fixed_frame_pose_sampling_ratio = 1.,
  imu_sampling_ratio = 1.,
  landmarks_sampling_ratio = 1.,
}
--tunning guide
--https://google-cartographer-ros.readthedocs.io/en/latest/tuning.html

-- Cartographer configuration options:
-- https://google-cartographer.readthedocs.io/en/latest/configuration.html

MAP_BUILDER.use_trajectory_builder_2d = true

--Local Slam
--there are more parameters to tune, but this ones are the ones I found more impactful

--this one tries to match two laser scans together to estimate the position,
--I think if not on it will rely more on wheel odometry
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = true

-- tune this value to the amount of samples (i think revolutions) to average over
--before estimating te position of the walls and features in the environment
TRAJECTORY_BUILDER_2D.num_accumulated_range_data = 1

--use or not use IMU, if used, the tracking_frame should be set to the one that the IMU is on
TRAJECTORY_BUILDER_2D.use_imu_data = true

--bandpass filter for lidar distance measurements
TRAJECTORY_BUILDER_2D.min_range = 0.3
TRAJECTORY_BUILDER_2D.max_range = 8.
TRAJECTORY_BUILDER_2D.max_z = .1
TRAJECTORY_BUILDER_2D.min_z = -.1

--This is the scan matcher and the weights to different assumptions
--occupied_space gives more weight to the 'previous' features detected.
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.occupied_space_weight = 10.
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.translation_weight = 10.
TRAJECTORY_BUILDER_2D.ceres_scan_matcher.rotation_weight = 40.

--this will help continue making the map while the robot is static
--default time is 5 seconds
TRAJECTORY_BUILDER_2D.motion_filter.max_time_seconds = 0.1

--imu configuration parameters
TRAJECTORY_BUILDER_2D.imu_gravity_time_constant = 10.

--map output parameters

--Global Slam
--Setting POSE_GRAPH.optimize_every_n_nodes to 0 is a handy way
--to disable global SLAM and concentrate on the behavior of local SLAM.
--This is usually one of the first thing to do to tune Cartographer.
POSE_GRAPH.optimize_every_n_nodes = 90. --90 default
POSE_GRAPH.optimization_problem.odometry_rotation_weight = 10
POSE_GRAPH.optimization_problem.odometry_translation_weight = 1.
POSE_GRAPH.optimization_problem.fixed_frame_pose_translation_weight = 1e-1
POSE_GRAPH.optimization_problem.fixed_frame_pose_rotation_weight = 1e-1

return options
```

카토그래퍼 런치파일
```xml
<launch>

  <arg name="config_dir" />
  <arg name="config_file" />

  <node name="cartographer_node" pkg="cartographer_ros"
      type="cartographer_node" args="
          -configuration_directory $(arg config_dir)
          -configuration_basename $(arg config_file)">
      <!-- remap the topics for cartographer to find them -->
    <remap from="imu"  to="/rs_t265/imu" />
    <remap from="odom" to="/rr_robot/mobile_base_controller/odom"/>
  </node>

  <node name="cartographer_occupancy_grid_node" pkg="cartographer_ros"
    type="cartographer_occupancy_grid_node" args="-resolution 0.05" />

</launch>
```

코멘트 
n this version I am inputting the imu from my wheels into carto, but IIRC you can input the odom from T265 by changing <arg name="publish_odom_tf" default="true"/> to <arg name="publish_odom_tf" default="false"/> and then in the carto launch file <remap from="odom" to="/rr_robot/mobile_base_controller/odom"/> to <remap from="odom" to="rs_t265/odom/sample"/> 

Hope this helps. Now I am working in making a 3D map (and a 2D for navigation) with carto, RPLidar, t265 and d435i, I am a little bit confused here.

t265 imu를 쓰고 있는 거죠라고 물어본 말에 답변
on those launch files yes, but if you do the modification that is on the end of the comment, you will be also feeding the odometry output of the t265 to cartographer. I am still tunning this at the moment tot make it more reliable. but as it is, with the RP Lidar works fine at low angular speeds.
this is the bit that I am refering to, in the carto launch file:
<remap from="odom" to="/rr_robot/mobile_base_controller/odom"/> to <remap from="odom" to="rs_t265/odom/sample"/> I added the right toipoic name this time


이슈 참고하기
https://github.com/IntelRealSense/realsense-ros/issues/711


