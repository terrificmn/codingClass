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

이제 이동이 다 끝났다면 (무선조종이나 teleop키보드로) 
2D 맵으로도 저장을 해줘야한다~ rs_rtabmap이 실행되고 있을 때
```
rosrun map_server map_saver map:=/rtabmap/grid_map
```
이렇게 하면 2D로 맵을 저장해준다. map.pgm, map.yml 파일로 만들어 준다


또는 이미 완료되어 있는 rtabmap.db를 이용해서 하는 방법
rosrun rtabmap_ros rtabmap _database_path:=

```
rosrun rtabmap_ros rtabmap _database_path:=~/.ros/rtabmap.db
```
그리고 다른 터미널에서 rostopic list 를 해보면
여러 토픽을 볼 수가 있는데 이중에서 /grid_map 를 이용
```
rosrun map_server map_saver map:=/grid_map

```
참고로 /proj_map 은 deprecated되므로 /grid_map을 하면 됨

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