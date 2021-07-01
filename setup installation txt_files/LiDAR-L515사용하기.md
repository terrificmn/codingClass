http://wiki.ros.org/pcl/Overview
포인트 클라우드 확인하기
sensor_msgs::PointCloud2



기존방식으로 rs_camera.launch파일을 실행하면 

/diagnostics
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
/l515/realsense2_camera_manager/bond
/l515/rgb_camera/parameter_descriptions
/l515/rgb_camera/parameter_updates
/rosout
/rosout_agg
/tf
/tf_static


토픽이 많이 나오지만~ 중요한 point cloud 에 대한 토픽이 안나온다
intra도 안 나옴

아래처럼 enable_infra을 실행해야
```
roslaunch realsense2_camera rs_camera.launch enable_infra:=true
```

roslaunch 

```
/l515/infra/camera_info
/l515/infra/image_raw
/l515/infra/image_raw/compressed
/l515/infra/image_raw/compressed/parameter_descriptions
/l515/infra/image_raw/compressed/parameter_updates
/l515/infra/image_raw/compressedDepth
/l515/infra/image_raw/compressedDepth/parameter_descriptions
/l515/infra/image_raw/compressedDepth/parameter_updates
/l515/infra/image_raw/theora
/l515/infra/image_raw/theora/parameter_descriptions
/l515/infra/image_raw/theora/parameter_updates
```
정보가 나온다. 그리고 보면 
l515/depth/ 부분에서 color가 없다~ 이 토픽이 point cloud인데 ㅠ

그래서 
```
roslaunch realsense2_camera rs_camera.launch filters:=pointcloud
```

이제는 토픽이 나온다
```
/l515/depth/color/points
```


## 다른 방법은 컨맨드로 대신에 런치파일 수정하기
rs_camera.launch 파일에서 

아규먼트 중에서  enable_pointcloud를 찾는다 false에서 true로 수정해준다
<arg name="enable_pointcloud"         default="false"/>

그러면 그냥 roslaunch로도 실행이 잘 된다


## 새로 안 방법은
위의 방법으로 해도 topic은 나오는데 rviz를 실행하면 출력되는 것을 확인할 수가 없다

demo_pointcloud를 실행하면 rviz가 실행되면서 잘 나옴
```
 roslaunch realsense2_camera demo_pointcloud.launch 
```
그래서 demo를 실행하면 rviz가 제대로 나오면서 실행이 된다

이 중에서 
/camera/depth/color/points
토픽으로 확인하면 될 듯

아무래도 
<node name="rviz" pkg="rviz" type="rviz" args="-d $(find realsense2_camera)/rviz/pointcloud.rviz" required="true" />

이 노드 때문인 거서 같다. rs_camera.launch파일에는 없다

