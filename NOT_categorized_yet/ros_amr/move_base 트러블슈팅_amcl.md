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

또는 noetic일 경우에는 기본 default를 사용하면 된다 


워크스페이스에서 아무래도 catkin build 해봤자 의존성 때문에 에러나므로 rosdep을 해주자 
```
rosdep install --from-paths src --ignore-src -r -y -i
```

그 다음에 
catkin build navigation


으하하하 소용없음!! ㅡㅡ; 

dwa관련 planner 패키지를 제대로 실행을 못 시키는 듯 하다 navigation stack 재확인하기  

그리고 amcl 노드를 띄울 때 move base도 같이 실행을 해줘야한다. 그래야 map_server의 map을 받을 수 있다   
만약 move_base 노드를 실행을 안 시키면 (테스트 할 시) No map received 및  Request for map failed; trying again...  
라고 나오면서 map을 못 받으니 costmap이 작동을 안 한다.  
정확히 말하면 map은 토픽으로 발행을 하지만 move_base를 통해서 cost_map이 나와야 하는데   
/move_base/global_costmap/costmap  토픽이 안나오는 것.   

> amcl의 파라미터 중 "use_map_topic" 을 true로 하면 map토픽을 직접 받는다  
그러므로 rviz상에서는 당연히 cost_map은 볼 수 가 없다  
기본은 false값이고 false한다면 map_server로 부터 map 토픽을 구독하지는 않는다.  
공통적으로 /tf 로부터 정보를 얻는다  

그리고 amcl 만 (move_base 없이) 실행을 해도 레이저 스캔이랑 벽이랑 딱 맞아 떨어져야 한다.  



## static_layer 문제 - global_costmap 관련

```
/move_base/current_goal
/move_base/feedback
/move_base/global_costmap/costmap
/move_base/global_costmap/costmap_updates
/move_base/global_costmap/footprint
/move_base/global_costmap/inflation_layer/parameter_descriptions
/move_base/global_costmap/inflation_layer/parameter_updates
/move_base/global_costmap/obstacle_layer/parameter_descriptions
/move_base/global_costmap/obstacle_layer/parameter_updates
/move_base/global_costmap/parameter_descriptions
/move_base/global_costmap/parameter_updates
/move_base/goal
/move_base/local_costmap/costmap
/move_base/local_costmap/costmap_updates
/move_base/local_costmap/footprint
/move_base/local_costmap/inflation_layer/parameter_descriptions
/move_base/local_costmap/inflation_layer/parameter_updates
/move_base/local_costmap/obstacle_layer/parameter_descriptions
/move_base/local_costmap/obstacle_layer/parameter_updates
/move_base/local_costmap/parameter_descriptions
/move_base/local_costmap/parameter_updates
/move_base/parameter_descriptions
/move_base/parameter_updates
```
어딜 봐도 static_layer가 없다   분명히 파라미터 파일에는 static_layer가 정의 되어 있는데 ㅠ

```
[ WARN] [1659676621.610299854]: global_costmap: Parameter "plugins" not provided, loading pre-Hydro parameters
[ INFO] [1659676621.634993857]: global_costmap: Using plugin "obstacle_layer"
[ INFO] [1659676621.646747145]:     Subscribed to Topics: 
[ INFO] [1659676621.666002743]: global_costmap: Using plugin "inflation_layer"
[ WARN] [1659676621.731141540]: local_costmap: Pre-Hydro parameter "static_map" unused since "plugins" is provided
[ WARN] [1659676621.731933992]: local_costmap: Pre-Hydro parameter "map_type" unused since "plugins" is provided
[ INFO] [1659676621.733025891]: local_costmap: Using plugin "obstacle"
[ INFO] [1659676621.744956271]:     Subscribed to Topics: laser_scan_sensor
[ INFO] [1659676621.774583449]: local_costmap: Using plugin "inflation"
[ INFO] [1659676621.825276314]: Created local_planner dwa_local_planner/DWAPlannerROS
```
obstacle, inflation 플러그인은 사용한다고 나온다.  
오히려 static 플러그인을 제공하지 않았다고 나옴 ;; 이런 ;; 아무래도 충돌이 있나보다;;



플러그인 이름을 obstacle, inflation 으로 단순하게 했는데 obstacle_layer, inflation_layer 로 변경하고   
그 안에 파라미터 정의 . 그랬더니토픽은 변경되나 static_layer는 변화가 없다 
```
/move_base/global_costmap/costmap
/move_base/global_costmap/costmap_updates
/move_base/global_costmap/footprint
/move_base/global_costmap/inflation_layer/parameter_descriptions
/move_base/global_costmap/inflation_layer/parameter_updates
/move_base/global_costmap/obstacle_layer/parameter_descriptions
/move_base/global_costmap/obstacle_layer/parameter_updates
/move_base/global_costmap/parameter_descriptions
/move_base/global_costmap/parameter_updates
/move_base/goal
/move_base/local_costmap/costmap
/move_base/local_costmap/costmap_updates
/move_base/local_costmap/footprint
/move_base/local_costmap/inflation_layer/parameter_descriptions
/move_base/local_costmap/inflation_layer/parameter_updates
/move_base/local_costmap/obstacle_layer/parameter_descriptions
/move_base/local_costmap/obstacle_layer/parameter_updates
/move_base/local_costmap/parameter_descriptions
/move_base/local_costmap/parameter_updates
```


터틀봇은    
/move_base/global_costmap/static_layer/parameter_descriptions  
/move_base/global_costmap/static_layer/parameter_updates  

static_layer가 나온다;; 뭐가 문제일까?  



일단 해결책은 common_costmap 파라미터에서 플러그인을 정의를 하고 (이름으로 정의: static_layer)  
그리고 각 global_costmap 이나 local_costmap에서 그 플러그인을 쓰겠다고 써주는 건데  

global_costmap 파라미터 설정 하는 부분에서 아예 static layer를 사용안함    
```
global_costmap:
  global_frame: map
  robot_base_frame: base_footprint
  static_map: true 

##  plugins:
##  - {name: static_layer,         type: "costmap_2d::StaticLayer"}
```

아마도 static_map true로 사용한다고 했는데 그래서 충돌나나? 실험해봐야겠다

어쨋든
```
move_base/global_costmap/costmap
/move_base/global_costmap/costmap_updates
/move_base/global_costmap/footprint
/move_base/global_costmap/inflation_layer/parameter_descriptions
/move_base/global_costmap/inflation_layer/parameter_updates
/move_base/global_costmap/obstacle_layer/parameter_descriptions
/move_base/global_costmap/obstacle_layer/parameter_updates
/move_base/global_costmap/parameter_descriptions
/move_base/global_costmap/parameter_updates
/move_base/global_costmap/static_layer/parameter_descriptions
/move_base/global_costmap/static_layer/parameter_updates
/move_base/goal
/move_base/local_costmap/costmap
/move_base/local_costmap/costmap_updates
/move_base/local_costmap/footprint
/move_base/local_costmap/inflation_layer/parameter_descriptions
/move_base/local_costmap/inflation_layer/parameter_updates
/move_base/local_costmap/obstacle_layer/parameter_descriptions
/move_base/local_costmap/obstacle_layer/parameter_updates
/move_base/local_costmap/parameter_descriptions
/move_base/local_costmap/parameter_updates
```

 static_layer로 토픽이 나오고 

 참고로 global_costmap 파라미터를 불러올 때 ns로 namespace 하는 것도 소용 없음   
 (/global_costmap/static_layer) 이런식  
이상하게 안됨  

하지만 static 이 되니 이제 move_base에서 글로벌 코스트 맵이 잘 나온다  
맵이 한 쪽으로 치우쳐서 그 공간안에 안들어가면 무조건 센서가 벗어났다고 나오는 오류는 해결된 듯 하다 






