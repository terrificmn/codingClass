[참고매뉴얼](http://wiki.ros.org/rtabmap_ros#rtabmap_ros.2Fpoint_cloud_xyz)

[rs-imu-callibration tool](https://github.com/IntelRealSense/librealsense/tree/master/tools/rs-imu-calibration)


roslaunch realsense2_camera rs_camera.launch\
    align_depth:=true \
    unite_imu_method:="linear_interpolation" \
    enable_gyro:=true \
    enable_accel:=true

rosrun imu_filter_madgwick imu_filter_node\
     _use_mag:=false\
     _publish_tf:=false\
     _world_frame:="enu"\
     /imu/data_raw:=/camera/imu\
     /imu/data:=/rtabmap/imu

rosrun nodelet nodelet standalone rtabmap_ros/point_cloud_xyz \
    _approx_sync:=false  \
    /depth/image:=/camera/depth/image_rect_raw \
    /depth/camera_info:=/camera/depth/camera_info \
    _decimation:=4

roslaunch rtabmap_ros rtabmap.launch\
    rtabmap_args:="\
      --delete_db_on_start \
      --Icp/VoxelSize 1 \
      --Icp/PointToPlaneRadius 0 \
      --Icp/PointToPlaneK 20 \
      --Icp/CorrespondenceRatio 0.2 \
      --Icp/PMOutlierRatio 0.65 \
      --Icp/Epsilon 0.005 \
      --Icp/PointToPlaneMinComplexity 0 \
      --Odom/ScanKeyFrameThr 0.7 \
      --OdomF2M/ScanMaxSize 15000 \
      --Optimizer/GravitySigma 0.3 \
      --RGBD/ProximityPathMaxNeighbors 1 \
      --Reg/Strategy 1" \
    icp_odometry:=true \
    scan_cloud_topic:=/cloud \
    subscribe_scan_cloud:=true \
    depth_topic:=/camera/aligned_depth_to_color/image_raw \
    rgb_topic:=/camera/color/image_raw \
    camera_info_topic:=/camera/color/camera_info \
    approx_sync:=false \
    wait_imu_to_init:=true \
    imu_topic:=/rtabmap/imu 



rtabmap 셋팅 windows-preferences
Source 탭

    Source Type RGB-D
    Grabber for RGB-D devices 에서
    Driver Realsense2  선택
    IR Emitter enabled
    IR mode unchecked
    Use Depth... unchecked.
    640 Stream width
    480 Stream height
    30 Hz rate
    In the standalone app should work.

IR모드를 언체크하면 ICP odometry를 하면서 RGB이미지를 레코딩 가능하다고 함

L515와 T265를 동시에 사용할 때 trajectory 가 same scale이 아니여서 
t265를 odometry로 사용할 때 벽이 완벽하게 overlap이 되지 않는다고 함


IR모드를 unchecked 해주고 RGB/IR stream width를 1280, height는 720 rate는 30hz
해주면 overlapping sectioins 을 줄이는데 도움이 된다고 함


IMU 필터링은 Madgwick Filter
하지만

Laser scans는 
Generate laser scan from depth image. 체크
Downsample step size for laser scans 은 4
Voxel size은 0.050 m
K nearest neighbors는 20



I wonder if there is a possibility to include the RGB information in the final pointcloud? 


You could do the same in ROS. Launch rtabmap node with T265 odometry as input, and feed L515 data for RGB/depth images. Make sure to adjust static TF between L515 and T265. 


848x480x60Hz parameters are ignored when L500 is detected, 640x480x30 is hard-coded:

업데이트가 되서 위처럼 고정된다고 함