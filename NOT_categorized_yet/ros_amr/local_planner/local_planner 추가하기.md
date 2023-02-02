
먼저 catkin_create_pkg 를 한 후에  만들고 싶은 패키지 이름으로 정해준다  
```
catkin_create_pkg local_planner_test roscpp
```

nav_core/base_local_planner.h 파일을 인쿠르드 하며, nav_core::BaseLocalPlanner 클래스를 상속 받아서 만든다.  

클래스명은 하고 싶은 것으로 

헤더파일을 만든 후에 (물론 include 경로에 넣는다)

src 디렉토리 cpp 파일을 만들어준다  

네임스페이스는 변경안하고 local_planner로 그대로 진행 함   
나머지는 클래스명 및 생성자 등만 변경   


이제 라이브러리를 등록해줘야하는데   
lp_plugin.xml 파일을 만들어서 plugin으로 등록할 수 있게 한다   

```

```

라이브러리 패스는 기존 예제에서는 lib_local_planner 로 되어 있는데   
ros 네이밍 컨벤션이 이번에 만든 패키지 이름앞에 lib 붙게 되어 있다. local_planner_test 라고 패키지 이름으로 만들었으니  
liblocal_planner_test 이렇게 됨. lib_local.... 이런식이 아님  


CMakeLists.txt 파일을 완성 시키고 plugin을 등록시키기 위해서  
package.xml 에 위에서 만든 lp_plugin.xml 파일을 적어준다.  

```
```


CMakeLists.txt  업데이트 하기  

빌드를 한 후에 rospack을 터미널에 입력하면 등록할 수가 있다고 한다.  
```
rospack plugins --attrib=plugin nav_core
```


### move_base 노드에서 사용
move_base를 사용하는 런치파일에서 local_planner를 등록하자   

```
<!-- <param name="base_local_planner" value="dwa_local_planner/DWAPlannerROS" /> -->

<param name="base_local_planner" value="local_planner/LocalPlannerTest" />
```


런치파일을 실행하면  
```
[ INFO] [1675162653.956247067, 148.151000000]: Created local_planner local_planner/LocalPlannerTest
[ INFO] [1675162654.171047731, 148.363000000]: Recovery behavior will clear layer 'obstacles'
[ INFO] [1675162654.180497031, 148.373000000]: Recovery behavior will clear layer 'obstacles'

```

자세한 코드 등은 local_planner_test를 참고   


[ros wiki](http://wiki.ros.org/navigation/Tutorials/Writing%20a%20Local%20Path%20Planner%20As%20Plugin%20in%20ROS)


[참고 local planner AgriBot-Local-Planner 좋은 소스인듯 하다](https://github.com/alirezaahmadi/AgriBot-Local-Planner)

[튜토리얼 깃허브 - ros-nav-5days LOCAL PLANNER](https://github.com/rwbot/ros-nav-5days/blob/master/LOCAL%20PLANNER.md)

