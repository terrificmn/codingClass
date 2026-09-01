roslaunch ssl_slam ssl_slam_L515.launch 
했을 때 확인 가능한 토픽중...



/camera/color/image_raw
/camera/depth/color/points
/clicked_point
/cloud_pcd
/diagnostics
/initialpose
/l515/color/camera_info
/l515/color/image_raw
/l515/color/image_raw/compressed
/l515/color/image_raw/compressed/parameter_descriptions
/l515/color/image_raw/compressed/parameter_updates
/l515/color/image_raw/compressedDepth
/l515/color/image_raw/compressedDepth/parameter_descriptions
/l515/color/image_raw/compressedDepth/parameter_updates
/l515/color/image_raw/theora
/l515/color/image_raw/theora/parameter_descriptions
/l515/color/image_raw/theora/parameter_updates
/l515/depth/camera_info
/l515/depth/color/points
/l515/depth/image_rect_raw
/l515/depth/image_rect_raw/compressed
/l515/depth/image_rect_raw/compressed/parameter_descriptions
/l515/depth/image_rect_raw/compressed/parameter_updates
/l515/depth/image_rect_raw/compressedDepth
/l515/depth/image_rect_raw/compressedDepth/parameter_descriptions
/l515/depth/image_rect_raw/compressedDepth/parameter_updates
/l515/depth/image_rect_raw/theora
/l515/depth/image_rect_raw/theora/parameter_descriptions
/l515/depth/image_rect_raw/theora/parameter_updates
/l515/extrinsics/depth_to_color
/l515/l500_depth_sensor/parameter_descriptions
/l515/l500_depth_sensor/parameter_updates
/l515/motion_module/parameter_descriptions
/l515/motion_module/parameter_updates
/l515/pointcloud/parameter_descriptions
/l515/pointcloud/parameter_updates
/l515/realsense2_camera_manager/bond
/l515/rgb_camera/parameter_descriptions
/l515/rgb_camera/parameter_updates
/laser_cloud_edge
/laser_cloud_surf
/map
/move_base_simple/goal
/odom
/rosout
/rosout_agg
/ssl_slam/trajectory
/tf
/tf_static
/velodyne_points_filtered


image 토픽, point cloud 토픽, 등이 있다고 하는 듯

이중에 /l515/depth/color/points 토픽은
```
rostopic info /l515/depth/color/points
```
```
Type: sensor_msgs/PointCloud2

Publishers: 
 * /l515/realsense2_camera_manager (http://ubun-sc:45539/)

Subscribers: None
```

```
rosmsg show sensor_msgs/PointCloud2
```
포인트 클라우드를 볼 수 있는데 
PointCloud2는 PCL로 해서 볼 수 있게 해준다고 함?


```
 roslaunch realsense2_camera rs_rtabmap.launch 
```
했을 때는 
/d400/depth/color/points

d400으로 인식해서 나오나~ 작동은 하긴하는 것 같음



다만, roslaunch realsense2_camera rs_camera.launch 를 했을 때는 위의 토픽이 나오지 않음

어쨋든 슬램 예제 SLAM with T265 and D400 일 경우에 나오는 토픽들
```
/camera/depth_registered/camera_info
/camera/depth_registered/image
/camera/rgb/image_rect_color
/d400/align_to_color/parameter_descriptions
/d400/align_to_color/parameter_updates
/d400/aligned_depth_to_color/camera_info
/d400/aligned_depth_to_color/image_raw
/d400/aligned_depth_to_color/image_raw/compressed
/d400/aligned_depth_to_color/image_raw/compressed/parameter_descriptions
/d400/aligned_depth_to_color/image_raw/compressed/parameter_updates
/d400/aligned_depth_to_color/image_raw/compressedDepth
/d400/aligned_depth_to_color/image_raw/compressedDepth/parameter_descriptions
/d400/aligned_depth_to_color/image_raw/compressedDepth/parameter_updates
/d400/aligned_depth_to_color/image_raw/theora
/d400/aligned_depth_to_color/image_raw/theora/parameter_descriptions
/d400/aligned_depth_to_color/image_raw/theora/parameter_updates
/d400/color/camera_info
/d400/color/image_raw
/d400/color/image_raw/compressed
/d400/color/image_raw/compressed/parameter_descriptions
/d400/color/image_raw/compressed/parameter_updates
/d400/color/image_raw/compressedDepth
/d400/color/image_raw/compressedDepth/parameter_descriptions
/d400/color/image_raw/compressedDepth/parameter_updates
/d400/color/image_raw/theora
/d400/color/image_raw/theora/parameter_descriptions
/d400/color/image_raw/theora/parameter_updates
/d400/confidence/camera_inforos-Project D400공부중
/d400/confidence/image_rect_raw
/d400/confidence/image_rect_raw/compressed
/d400/confidence/image_rect_raw/compressed/parameter_descriptions
/d400/confidence/image_rect_raw/compressed/parameter_updates
/d400/confidence/image_rect_raw/compressedDepth
/d400/confidence/image_rect_raw/compressedDepth/parameter_descriptions
/d400/confidence/image_rect_raw/compressedDepth/parameter_updates
/d400/confidence/image_rect_raw/theora
/d400/confidence/image_rect_raw/theora/parameter_descriptions
/d400/confidence/image_rect_raw/theora/parameter_updates
/d400/depth/camera_info
/d400/depth/color/points
/d400/depth/image_rect_raw
/d400/depth/image_rect_raw/compressed
/d400/depth/image_rect_raw/compressed/parameter_descriptions
/d400/depth/image_rect_raw/compressed/parameter_updates
/d400/depth/image_rect_raw/compressedDepth
/d400/depth/image_rect_raw/compressedDepth/parameter_descriptions
/d400/depth/image_rect_raw/compressedDepth/parameter_updates
/d400/depth/image_rect_raw/theora
/d400/depth/image_rect_raw/theora/parameter_descriptions
/d400/depth/image_rect_raw/theora/parameter_updates
/d400/extrinsics/depth_to_color
/d400/l500_depth_sensor/parameter_descriptions
/d400/l500_depth_sensor/parameter_updates
/d400/motion_module/parameter_descriptions
/d400/motion_module/parameter_updates
/d400/pointcloud/parameter_descriptions
/d400/pointcloud/parameter_updates
/d400/realsense2_camera_manager/bond
/d400/rgb_camera/parameter_descriptions
/d400/rgb_camera/parameter_updates
/diagnostics
/disparity
/gps/fix
/imu/data
/initialpose
/l515/odom/sample
/l515/realsense2_camera_manager/bond
/l515/tracking_module/parameter_descriptions
/l515/tracking_module/parameter_updates
/left/camera_info
/left/image
/move_base_simple/goal
/rgbd_image_relay
/right/camera_info
/right/image
/rosout
/rosout_agg
/rtabmap/cloud_ground
/rtabmap/cloud_map
/rtabmap/cloud_obstacles
/rtabmap/global_path
/rtabmap/global_path_nodes
/rtabmap/global_pose
/rtabmap/goal
/rtabmap/goal_node
/rtabmap/goal_out
/rtabmap/goal_reached
/rtabmap/grid_map
/rtabmap/grid_prob_map
/rtabmap/info
/rtabmap/initialpose
/rtabmap/labels
/rtabmap/landmarks
/rtabmap/local_grid_empty
/rtabmap/local_grid_ground
/rtabmap/local_grid_obstacle
/rtabmap/local_path
/rtabmap/local_path_nodes
/rtabmap/localization_pose
/rtabmap/mapData
/rtabmap/mapGraph
/rtabmap/mapPath
/rtabmap/octomap_binary
/rtabmap/octomap_empty_space
/rtabmap/octomap_full
/rtabmap/octomap_global_frontier_space
/rtabmap/octomap_grid
/rtabmap/octomap_ground
/rtabmap/octomap_obstacles
/rtabmap/octomap_occupied_space
/rtabmap/proj_map
/rtabmap/scan_map
/tf
/tf_static음
/user_data_async
/voxel_cloud

```




