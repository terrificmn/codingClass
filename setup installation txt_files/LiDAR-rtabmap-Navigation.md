바로 아래 경로에 demo launch 파일들이 있으므로 그 중에서 카피해서 사용하면 될 듯 하다
/opt/ros/melodic/share/rtabmap_ros/launch/demo

크게 ros 파라미터와 rtabmap 의 파라미터가 있음

[참고 rtatmap](http://wiki.ros.org/rtabmap_ros/)

여기 꼭 참고하기!!!!!
[참고사이트-터블봇3](https://emanual.robotis.com/docs/en/platform/turtlebot3/navigation/)


참고:

그 중에 remap 이 있는데
```xml
<remap from="scan" to="/jn0/base_scan"/> 
```
remap 태그는 토픽명을 변경을 해준다. 실제 맞는 토픽으로 변경을 해주면 된다


먼저 터블봇3를 실행해준다. 그냥 터블봇만
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch 
```

그리고 기존의 맵을 실행
```
 roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/.ros/map.yaml

```


rs-sensor-control