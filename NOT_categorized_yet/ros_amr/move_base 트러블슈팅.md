# The robot's start position is off the global costmap

맵 파일의 yaml 파일을 위치를 중간으로 바꿔본다 
예: -100, -100

답은 아니다;;; 테스트 해봐야함

그리고 move_base에서 config 파일이 param 정의해놓은 파일에서  
resolution 을 맵 파일이랑 일치되게 적어야 하는 듯 하다?



odom 토픽을 받을 수 있도록 한다   
기존의amr에서 받는다면 /odom  
ekf 노드에서 받는다면 /odometry/filtered

```xml
<remap from="odom" to="/odometry/filtered"/>
<!-- <remap from="odom" to="/md_odom"/> -->
```


네비게이션 스택  
https://github.com/husky/husky/tree/melodic-devel/husky_navigation


Warnings like Map update loop missed its desired rate of *.*Hz ... are because of not enough computing power and are almost unavoidable. You can ignore them because it doesn’t affect system efficiency.


레이져 관련 읽어보기
https://community.husarion.com/t/solved-timed-out-waiting-for-transform-from-base-link-to-map-during-map-navigation/1004/9


```
[ WARN] [1659598016.954809723, 873.067000000]: The origin for the sensor at (0.45, -0.01) is out of map bounds. So, the costmap cannot raytrace for it.
[ WARN] [1659598020.291880073, 876.400000000]: The origin for the sensor at (0.40, -0.05) is out of map bounds. So, the costmap cannot raytrace for it.
[ WARN] [1659598036.981946004, 893.067000000]: The origin for the sensor at (0.32, -0.05) is out of map bounds. So, the costmap cannot raytrace for it.
```
일단 2개가 나오는 것은 voxel 을 사용을 안했기 때문에 2개 만 나오고 

map_type을 voxel로 하면 3개 배열로 나오는데 이때는 z-voxel을 높여줘야한다. 숫자 2면 20cm high라는 말   
10정도 주면 1m  



> bug 가능성?? global_costmap에서 계속 벗어나 있다고 하는데 outdoor용 로봇과 터블봇 시뮬레이션 했을 때랑  
결과가 같은 결과가 나와서 ;; 버그 인줄 알았으나 아직 해결 못함

sudo apt remove ros-melodic-navigation

```
The following packages were automatically installed and are no longer required:
  ros-melodic-carrot-planner ros-melodic-fake-localization
  ros-melodic-global-planner ros-melodic-move-slow-and-clear

The following packages will be REMOVED:
  ros-melodic-navigation
```

그 외에    
ros-melodic-global-planner ros-melodic-move-base ros-melodic-navfn

이 정도를 지워주면 거의 다 지워지는 듯 하다 


이제  
지웠다면 navigation stack을 깃허브에서 클론  



https://github.com/ros-planning/navigation/tree/melodic-devel

git clone -b melodic-devel 주소

워크스페이스에서 아무래도 catkin build 해봤자 의존성 때문에 에러나므로 rosdep을 해주자 
```
rosdep install --from-paths src --ignore-src -r -y -i
```

그 다음에 
catkin build navigation


으하하하 소용없음!! ㅡㅡ; 