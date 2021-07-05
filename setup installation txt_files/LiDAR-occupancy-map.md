# 설치
브런치만 따로 설치해주기~  realsense가 설치가 되어 있는 경우 에러가 날 수도 있다.
아마도 
변경: sudo apt-get install ros-$ROS_DISTRO-realsense2-camera 로 설치하기

prerequisites:  필요한 라이브러리 SDK2.0 필요
librealsense2-dkms
librealsense2-utils
ros-melodic-realsense2-camera
ros-melodic-ddynamic-reconfigure 

따로 깃허브에서 클론을 받아서 catkin_make를 시도해봐야할 듯
[realsense-ros](https://github.com/IntelRealSense/realsense-ros)

확인이 필요함. 도커내에서는 작동 잘 됨 (branch만 클론하기)
```
$ git clone -b occupancy-mapping --single-branch https://github.com/IntelRealSense/realsense-ros
```

catkin_make를 해주기 전에 충돌이 나므로 occupancy 디렉토리만 남기고 다른 패키지는 지워준다

catkin_make 를 해준다
```
Resource not found: realsense2_camera
ROS path [0]=/opt/ros/melodic/share/ros
ROS path [1]=/home/ubun/catkin_ws/src
ROS path [2]=/opt/ros/melodic/share
The traceback for the exception was written to the log file
```
이런 에러가 발생하면 

realsense2_camera가 없으므로 설치
```
sudo apt-get install ros-melodic-realsense2-camera
```

현재 occupancy만 브랜치에서 가져와서 설치하고 나머지는 지웠고 
apt패키지에서의 realsense-camera를 사용하려고 함

> 이유는 브랜치로 따로 깃 클론한 occupancy-mapping을 사용하려고 하면 그 안에도 
realsense2-camera 패키지가 있어서 이미 apt-get으로 설치한 realsense2-camera패키지를 
지워준 것이고 (충돌), 그러면 occupancy는 실행이 되는데 rs_camera등을 런치할 때 
제대로 안되는 것 같아서, occupuncy만 남김

```
 roslaunch occupancy occupancy_live_rviz.launch 
```

시리얼 번호 확인하는 법
먼저 학교에서 launch파일 먼저 실행해보면 에러 발생
```
[ERROR] [1625433706.500848039]: The requested device with serial number D400_SN is NOT found!
[ERROR] [1625433706.841606223]: The requested device with serial number T265_SN is NOT found!
```

It won't work without serial numbers.  시리얼 번호를 넣어보자!
아래 명령어를 입력하면 연결된 정보를 볼 수가 있다
```
rs-enumerate-devices
```

occupancy/launch/cameras.launch파일의 시리얼 번호를 넣어준다
```
    <arg name="serial_no_camera1" value="943222110188"/> 			<!-- Note: Replace with actual serial number (camera1 default: t265)-->
    <arg name="serial_no_camera2" value="f0460650"/> 			<!-- Note: Replace with actual serial number (camera2 default: d400)-->
```
시리얼 번호를 넣어줘야지 실행이 됨
그리고 실행 
```
roslaunch occupancy occupancy_live_rviz.launch
```

carmeras.launch 파일에서는 rs_d400_and_t265.launch 파일을 포함하므로 
수정해야함

apt-get으로 설치했으므로 catkin_ws 디렉토리에는 없고 

이동
```
 cd /opt/ros/melodic/share/realsense2_camera/launch/

```

rs_d400_and_t265.launch 파일을 수정

여기에서 arg태그들을 수정해줘야하는데 시리얼번호랑 카메라 이름 바꿔준다
<arg name="device_type_camera2"    		default="l515"/>
<arg name="camera2"              			default="l515"/>

그리고 <group ns="$(arg camera2)"> 그룹 2에 
내용을 추가해주고 filters:=pointcloud 라고 되어 잇는 부분을 확인해보자

<arg name="enable_infra1"     value="false"/>
<arg name="enable_infra2"     value="false"/>
<arg name="enable_fisheye"    value="false"/>
<arg name="enable_gyro"       value="false"/>
<arg name="enable_accel"      value="false"/>
<arg name="enable_pointcloud" value="true"/>
<arg name="enable_sync"       value="true"/>


<arg name="filters"               value="pointcloud"/>
는 놔둬도 될 듯~ 그 전에는 rs_camera에서는 filters 값이 안 먹혔는데 잘 된다


이제 camera2의 arg를 l515로 바꿔놓았기 때문에 코드를 수정해준다

occupancy패키지의 occpancy_node.cpp 를 수정해야함
subscriber를 하고 있는 토픽을 수정해준다

큰 효과는 없는 듯 하다
그리고~ /occupancy 토픽이 퍼블리쉬가 안되고 있음
type /nav_msgs/OccupancyGrid

 여기 읽어보기!!!
https://github.com/introlab/rtabmap/issues/574