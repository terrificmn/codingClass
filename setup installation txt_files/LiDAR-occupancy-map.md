# 설치
브런치만 따로 설치해주기~  realsense가 설치가 되어 있는 경우 에러가 날 수도 있다.
아마도 
sudo apt-get install ros-$ROS_DISTRO-realsense2-camera 로 설치를 하지말고
따로 깃허브에서 클론을 받아서 catkin_make를 시도해봐야할 듯
[realsense-ros](https://github.com/IntelRealSense/realsense-ros)

occupancy와 합쳐서 catkin_make를 해보자!
만약 그래도 에러가 난다면, SDK도 지운다음에 시도?

확인이 필요함. 도커내에서는 작동 잘 됨
```
$ git clone -b occupancy-mapping --single-branch https://github.com/IntelRealSense/realsense-ros
```

catkin_make 를 해준다


시리얼 번호 확인하는 법
먼저 학교에서 launch파일 먼저 실행해보고 잘 되는지 먼저 확인해본다음에 안되면
시리얼 번호를 넣어보자!

```
rs-enumerate-devices
```

occupancy/launch/cameras.launch파일의 시리얼 번호를 넣어준다
```
    <arg name="serial_no_camera1" value="943222110188"/> 			<!-- Note: Replace with actual serial number (camera1 default: t265)-->
    <arg name="serial_no_camera2" value="f0460650"/> 			<!-- Note: Replace with actual serial number (camera2 default: d400)-->
```

그리고 실행 
```
roslaunch occupancy occupancy_live_rviz.launch
```

