
catkin_create_pkg 부터 시작  

 catkin_create_pkg global_planner_test roscpp


그 다음 헤더파일  만들기   
클래스 이름만 하고 싶은 걸로 변경   

인쿠르드 할 패키지들이 꽤 되는데 path planner 를 위해서 필요한 라이브러리 들임  

costmap_2d_ros, costmap_2d 는 Costmap2D 클래스는 path planner로 input map으로 사용된다   
cost map을 받기 위해서 costmap2d를 구독할 필요는 없다고 한다  

GlobalPlannerTest 로  class 명 정하고 (하고픈 걸로), 중요한 것은 nav_core::BaseGlobalPlanner 클래스를 상속 받는다   

네임스페이스도 바꿀 수 있다  

GlobalPlannerTest 클래스의 메소드들은 즉, 상속받아서 사용하는 메소드들은 원래의 상속 클래스에서 모두 override가 되어야 한다


클래스의 생성자는 costmap initialize를 해주고 planning에(costmap_ros) 사용할 map 
여기에서 넘겨줄 argument로는 std::string name, costmap_2d::Costmap2DROS* costmap_ros  로 2개 인데   첫번째는 costmap_ros로 사용할 map을 초기화, planner의 이름이 사용됨

makePlan(start, goal, plan) 메소드는 override 해서 사용한다   


### cpp 파일

클래스명은  GlobalPlannerTest
```
PLUGINLIB_EXPORT_CLASS(global_planner::GlobalPlannerTest, nav_core::BaseGlobalPlanner)
```
그러면서  BaseGlobalPlanner로 플러그인 등록하는 코드
그 전에 pluginlib/class_list_macros.h 파일을 인쿠르드한다   

makePlan()메소드  
start, goal 파라미터는 initial localtion 과 target location 의 초기화를 하는데 필요  
예제 코드에서는 20개의 dummy location이 스택으로 (statically) 추가가 된다   (plan.push_back(start))   

그리고 만들어진 vector plan은 move_base global planner 모듈로 전송되고 nav_msgs/Path 토픽으로 publish된다


### 컴파일 하기 위해서 CMakeLists.txt 파일

 find package 는 헤더파일의 include한 파일들을 참고해서 넣어주고  
add_library()를 해준다  

그러면 빌드 시에  ~/catkin_ws/devel/lib/libglobal_planner_test 로 만들어진다 

> lib+패키지 명    = 패지키명이 global_planner_test  로 만들었으니 libglobal_planner_test



### 플러그인 등록
위에서 설명한 PLUGINLIB_EXPORT_CLASS(....) 을 통해서 현재 만든 클래스가 plugin으로exporting 해서 등록된다고 한다   class가 dynamic 방식으로 로드가 될 수 있게 해주며 반드시 exported class로 마크해야한다. 이 부분은 PLUGINLIB_EXPORT_CLASS 을 통해서 된다고 함  

그러면 nav_core::BaseGlobalPlanner 클래스의 plugin으로 등록이 된다 


plugin description file 만들기 . xml 파일  

파일명은 global_planner_plugin.xml
```xml
<library path="lib/libglobal_planner_test">
	<class name="global_planner/GlobalPlannerTest" type="global_planner::GlobalPlanner" base_class_type="nav_core::BaseGlobalPlanner">
		<description>This is a global planner plugin by iroboapp project.</description>
	</class>
</library>
```

library패스에 lib형태로 패키지 이름 넣고, 네임스페이스/만든클래스를 넣어준다  

이 파일이 있어서 ROS에서 자동으로 발견 후 load 한다고 한다  


package.xml에는 위의 만든 global_planner_plugin.xml 을 export 한다   

${prefix} 는 global_planner_plugin.xml의 전체경로 의미   

그리고 build_depend를 해줘야한다. exec_depend 포함 . 특히 nav_core를 

> run_depend 에서 exec_depend



## 이제 빌드
인쿠르드의 header 파일을 찾지를 못할 때는 (스펠링 오류가 없을 경우 )

CMakeList.txt 에 추가
```
include_directories(
	include
	${catkin_INCLUDE_DIRS}
)
```


빌드가 성공하면 rospack으로 query 하게 되면 사용할 수 있게 됨
```
rospack plugins --attrib=plugin nav_core
```


사용 move_base의 파라미터 사용
```
<param name="base_global_planner" value="global_planner/GlobalPlannerTest"/>
```



실패시 
Failed to create the global_planner/GlobalPlannerTest planner, are you sure it is properly registered and that the containing library is built?   


이런식으로 나올 경우에  source devel/setup.bash 를 다시 해준다  

그리고 다시 rospack plugins ... 

```
build] Runtime: 0.9 seconds total.                                            
[sgtubunamr@sgtubunamr catkin_ws]$ . devel/setup.bash 
[sgtubunamr@sgtubunamr catkin_ws]$ rospack plugins --attrib=plugin nav_core
rotate_recovery /home/sgtubunamr/catkin_ws/src/navigation/rotate_recovery/rotate_plugin.xml
global_planner /home/sgtubunamr/catkin_ws/src/navigation/global_planner/bgp_plugin.xml
move_slow_and_clear /home/sgtubunamr/catkin_ws/src/navigation/move_slow_and_clear/recovery_plugin.xml
carrot_planner /home/sgtubunamr/catkin_ws/src/navigation/carrot_planner/bgp_plugin.xml
clear_costmap_recovery /home/sgtubunamr/catkin_ws/src/navigation/clear_costmap_recovery/ccr_plugin.xml
navfn /home/sgtubunamr/catkin_ws/src/navigation/navfn/bgp_plugin.xml
local_planner_test /home/sgtubunamr/catkin_ws/src/local_planner_test/lp_plugin.xml
global_planner_test /home/sgtubunamr/catkin_ws/src/global_planner_test/global_planner_plugin.xml
dwa_local_planner /home/sgtubunamr/catkin_ws/src/navigation/dwa_local_planner/blp_plugin.xml
base_local_planner /home/sgtubunamr/catkin_ws/src/navigation/base_local_planner/blp_plugin.xml

```

이번에는  잘 인식한다   

[이후 wiki.ros 테스트 해보기](http://wiki.ros.org/navigation/Tutorials/Writing%20A%20Global%20Path%20Planner%20As%20Plugin%20in%20ROS/)




## 다른 방식
거의 같으나 조금 다름 패키지에 plugins 디렉토리를 만들어서 거기에서 .cpp .h  파일을 넣고   
빌드하는 방식   

위의 방식으로 해도 빌드 및 인식은 되는데 지금 이 방식이 더 나을 지도 모르겠다 

원래 global_planner pkg가 navigation 안에 있는데 그 컨벤션을 따라서 하는 듯 하다   

어쨋든 global_planner가 있어서 global_planner_plugin 으로 패키지 이름을 하고  클래스 이름도 동일하게 함   


위의 global_planner 추가 방법과 거의 동일 함     

CMakeLists.txt 파일에서는   
find_package(), catkin_package() 추가, add_library()

다른 것들은 필요 없는 듯 하다. 예를 들어 위에서 했던 방식들... add_dependencies()
target_link_libraries() 등은 필요없다  

그리고 빌드하면 빌드가 잘 된다   

> global_planner_plugin 패키지 참고 (CMakeLists.txt 파일 및 소스)

순서는 패키지 만들고 catkin_create_pkg   
그리고 plugins 디렉토리 만들고 그 안에 .h파일 .cpp 파일 만든다.  
내용 및 상속은 거의 같다 .. 

실제로 makePlan() 메소드가 작동할 수 있게 해보며, 실제 global path가 작동한다   


package.xml 에서 nav_core plugin을 등록시켜주며, global_planner_plugin.xml 파일을 export 태그로 등록    
물론 build_depend, exec_depend의 nav_core를 해줘야한다 


rospack으로 plugin 인식시켜줄 필요는 없다   


마지막으로 move_base의 파라미터에 
```
<param name="base_global_planner" value="global_planner/GlobalPlannerPlugin"/>
```
넣어주고 시뮬레이션 돌리기 쉬운 터블봇3 가제보 및, navigation 패키지를 해준다.  
가제보는 house로 하면 좋고, slam이 되어서 map 있어야 한다   


global_planner_plugin.cpp 파일에서 makePlan() 메소드가 중요한데   
Goal을 지정해주면 지그재그로 global path가 생성이 되는데.. 
시작점과 마지막(goal) 지점을 받아서 그 중간의 패스를 만드는 코드이고  

std::vector<geometry_msgs::PoseStamped>인 plan으로 받아서  
계속 push_back() 로 만들어 주면서 

현재 클래스에서 publish를 하지는 않지만 msg 즉, plan 벡터 변수에 차곡차곡 담아주는 것  그러면 
최종적으로 return을 하게 되면 nav_msgs/Path 로 퍼블리쉬가 됨  


> 실제 global path로 생성이 되어도 그 경로로만 가지는 않는데, 이유는 local planner가 계속 path를 조정하기 때문이다   







