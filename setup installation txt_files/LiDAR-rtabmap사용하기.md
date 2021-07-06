 여기 읽어보기!!!
https://github.com/introlab/rtabmap/issues/574

[참고 사이트Rtab slam](https://sudonull.com/post/18423-Localization-and-navigation-in-ROS-using-rtabmap)

실행하기
```
$ roslaunch realsense2_camera rs_rtabmap.launch 
```

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

map_server가 없다고 할때는 설치해준다
```
$ sudo apt-get install ros-melodic-map-server
```

맵보기 rtabmap_ros 패키지의 rtabmap 이 실행이 되면 맵을 다운로드 할 수 있다.
roslaunch rtabmap_ros rtabmap.launch localization:=true rgbd_odometry:=true

맵을 보기 (rtabmap.db의 경로 확인 .ros 디렉토리 안에 있음)
rtabmap-databaseViewer rtabmap.db


네비게이션 예제 설치 후 다시 한번 해볼 것
http://wiki.ros.org/rtabmap_ros/Tutorials/MappingAndNavigationOnTurtlebot#Turtlebot3_on_Melodic_and_Noetic

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