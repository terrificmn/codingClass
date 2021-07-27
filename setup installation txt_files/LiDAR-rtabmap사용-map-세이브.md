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