 여기 읽어보기!!!
https://github.com/introlab/rtabmap/issues/574

[참고 튜토리얼 사이트 꼭 보기](http://wiki.ros.org/rtabmap_ros/Tutorials/HandHeldMapping)

[참고 사이트Rtab slam](https://sudonull.com/post/18423-Localization-and-navigation-in-ROS-using-rtabmap)


## IMU tools 설치하기
[깃허브 ](https://github.com/ccny-ros-pkg/imu_tools)

브랜치만 클론
```
$ cd ~/catkin_ws/src
$ git clone -b melodic https://github.com/ccny-ros-pkg/imu_tools.git
```

rosdep을 이용해서 dependency를 해결
```
$ rosdep install imu_tools
```
rosdep이 없다면 
```
$ sudo apt-get install python-rosdep
```

catkin_ws 디렉토리에서 빌드를 해준다
```
$ catkin_make
```
imu_filter_nodelet, imu_filter_node, rviz_imu_plugin
이렇게 설치되는 듯하다


<br/>

## rtabmap실행

실행하기
```
$ roslaunch realsense2_camera rs_rtabmap.launch 
```

# 한번 실행해볼 것 
l515 에 있는 것인데, 흔들리는 것을 잘 잡아줄 지 ? 단독 사용시 사용하는 듯
```
roslaunch realsense2_camera rs_camera.launch \
    align_depth:=true \
    unite_imu_method:="linear_interpolation" \
    enable_gyro:=true \
     enable_accel:=true

rosrun imu_filter_madgwick imu_filter_node \
    _use_mag:=false \
    _publish_tf:=false \
    _world_frame:="enu" \
    /imu/data_raw:=/camera/imu \
    /imu/data:=/rtabmap/imu
```
따로 rviz로 실행하면 imu를 add해서 볼 수가 있는데 떨림이 심하다. 못쓸 것 같음



D400+T265 런치 파일을 특별히 넣어줄 아규먼트가 없는 듯 하다


## mapping mode - 테스트 해볼 것
rtabmap.launch 실행할 때 
set rviz:=true to open rviz 
rtabmapviz:=true to open rtabmapviz (default true) for visualization. 

```
rosrun nodelet nodelet standalone rtabmap_ros/point_cloud_xyz \
    _approx_sync:=false  \
    /depth/image:=/camera/depth/image_rect_raw \
    /depth/camera_info:=/camera/depth/camera_info \
    _decimation:=4

$ roslaunch realsense2_camera rs_rtabmap.launch\
    rtabmap_args:="\
      --delete_db_on_start \
      --Icp/VoxelSize 0.05 \
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


```
위의 런치코드는 실행이 안됨 --;


 D400+T265 mapping 을 할 때, l515로 수정해서 되는지 테스트 해 볼 것
 
 [ICP odometry example-ref](http://official-rtab-map-forum.67519.x6.nabble.com/Kinect-For-Azure-L515-ICP-lighting-invariant-mapping-td7187.html)

안됨;;;


<br/>

## 맵 저장되는 위치

An exception has been thrown: failed to set power state
[ERROR] [1625561305.606543840]: Exception: failed to set power state
에러 발생시는 다시 USB케이블 분리 후 다시 연결 후 실행

파일이 아래 위치에 저장이 된다.
~/.ros/rtabmap.db 

rs_rtabmap.launch 파일이 시작되면 rviz의 왼쪽 디스플레이 패널에서 
MapClout를 활성화 시켜준다. 토픽은 /rtabmap/mapData 이고 
```
rostopic info /rtabmap/mapData
Type: rtabmap_ros/MapData
```
체크박스를 눌러주면 활성화가 되면 퍼블리싱을 시작한다


rostopic info /rtabmap/grid_map
위의 토픽이 맵을 퍼블리싱해준다

이제 이동이 다 끝났다면 (무선조종이나 teleop키보드로) 
2D 맵으로도 저장을 해줘야한다~ rs_rtabmap이 실행되고 있을 때
```
rosrun map_server map_saver map:=/rtabmap/grid_map
```
이렇게 하면 2D로 맵을 저장해준다. map.pgm, map.yml 파일로 만들어 준다

<br/>

## 이미 완료 되어 있는 db데이터 이용해서 2D 만들기
또는 이미 완료되어 있는 rtabmap.db를 이용해서 하는 방법
rosrun rtabmap_ros rtabmap _database_path:= 이하는 경로를 설정

```
rosrun rtabmap_ros rtabmap _database_path:=~/.ros/rtabmap.db
```
그리고 다른 터미널에서 rostopic list 를 해보면
여러 토픽을 볼 수가 있는데 이중에서 /grid_map 를 이용. 같은 디렉토리에서 실행해야함 (rtabmap.db가 있는 디렉토리에서)
```
rosrun map_server map_saver map:=/grid_map

```
참고로 /proj_map 은 deprecated되므로 /grid_map을 하면 됨. (example에서는 /proj_map 으로 되어있으나)

이제 다른 창에 rosservice list 쳐보면 /publish_map 이라는 서비스가 있는데 
아규먼트를 넣어서 아래처럼 실행해준다
```
rosservice call /publish_map 1 1 0
```
그러면 서비스요청을 하게되고 바로 응답으로 파일을 만들어 준다


만약 map_server가 없다고 할때는 설치해준다
```
$ sudo apt-get install ros-melodic-map-server
```

맵보기 rtabmap_ros 패키지의 rtabmap 이 실행이 되면 맵을 다운로드 할 수 있다.
```
roslaunch rtabmap_ros rtabmap.launch localization:=true rgbd_odometry:=true
```

localization:=true rgbd_odometry:=true

맵을 보기 (rtabmap.db의 경로 확인 .ros 디렉토리 안에 있음)
```
rtabmap-databaseViewer rtabmap.db
```

처음실행했을 때부터 보여준다. 특징점도 보여주는 듯


## localization 모드
미리 만들어진 rtabmap database를 이용해서 Detection 의 Localization를 이용
그리고 아규먼트를 localization:=true 를 해줘야함

rtabmap_args:="--delete_db_on_start"  는 넣어주면 안됨!!

rosservice call /rtabmap/reset_odom 
를 이용하거나 GUI 모드를 이용하면 리로케이션을 한다

"Mem/IncrementalMemory" 파라미터도 "false"가 되어야하는데 (예전버전 인 듯)
localization:=true만 넘겨주면 안에 파라미터에 if문이 들어가 있어서 알아서 false로 만들어준다

그리고 메뉴에서 Downlaod map을 해준다


첨고 사이트: 맵변환 
```
https://answers.ros.org/question/217097/export-2d-map-from-rviz-andor-rtab-map/
```

참고할 사이트 
https://www.theconstructsim.com/ros-qa-navigate-with-rtab-map/

move-base가 없을 경우 설치
```
sudo apt-get install ros-melodic-move-base
```
패키지 디렉토리로 이동
```
$ roscd move_base
```