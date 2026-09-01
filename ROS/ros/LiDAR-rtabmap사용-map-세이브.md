## 이미 완료 되어 있는 db데이터 이용해서 2D 만들기
또는 이미 완료되어 있는 rtabmap.db를 이용해서 하는 방법  

SLAM을 한번 하게 되면은 데이터가 저장이 되고 다시 한번 프로그램이 실행되기 전에는  
~/.ros 숨김 디렉토리에 저장이 된다.  

이제 각각 3개의 터미널을 실행을 해서 따로따로 실행을 해주게 된다  
첫번째 명령어는 아래의 형식이다  
rosrun rtabmap_ros rtabmap _database_path:= 이하는 경로를 설정

```
rosrun rtabmap_ros rtabmap _database_path:=~/.ros/rtabmap.db
```

두 번째는  
또 다른 터미널에서 rostopic list 를 해보면  
여러 토픽을 볼 수가 있는데 이중에서 /grid_map 를 이용한다  

```
rosrun map_server map_saver map:=/grid_map

```
> 같은 디렉토리에서 실행해야함 (rtabmap.db가 있는 디렉토리에서, ~/.ros 디렉토리)  
참고로 /proj_map 은 deprecated 되므로   
/grid_map 토픽으로 사용을 하면 된다.   
(example에서는 /proj_map 으로 되어있으나 이제 사용이 안 될 수 있다)

마지막 터미널을 띄운 후   
이제 다른 창에 rosservice list 쳐보면 /publish_map 이라는 서비스가 있는데   
아규먼트를 넣어서 아래처럼 실행해준다
```
rosservice call /publish_map 1 1 0
```
그러면 서비스요청을 하게되고 바로 응답으로 파일을 만들어 주게 되는데  
현재의 디렉토리 위치에 map.pgm 파일과 map.yaml 파일을 만들어 준다  

pgm파일은 이미지 파일이므로 쉽게 열어서 확인이 가능하다  
yaml파일은 pgm파일을 정의하고 있고, resolution, origin 정보를 저장하고 있다

<br/>

## 만약 map_server가 없다고 할때는 설치해준다
```
$ sudo apt-get install ros-melodic-map-server
```

맵보기 rtabmap_ros 패키지의 rtabmap 이 실행이 되면 맵을 다운로드 할 수 있다.
```
roslaunch rtabmap_ros rtabmap.launch localization:=true rgbd_odometry:=true
```

localization:=true rgbd_odometry:=true


<br/>

## rtabmap을 이용해서 3D맵으로 보기 

> 위에서도 말했지만 rtabmap.db의 경로 확인해보자  .ros 디렉토리 안에 있음

rtabmap-databaseViewer을 실행한다
```
rtabmap-databaseViewer rtabmap.db
```

처음 실행했을 때부터 저장된 맵을 보여준다.