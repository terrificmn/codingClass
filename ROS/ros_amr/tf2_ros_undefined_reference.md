# tf2_ros undefined reference error
빌드 시 tf2_ros 를 못 찾을 경우
```
undefined reference to `tf2_ros::TransformBroadcaster::TransformBroadcaster()'
```

정답은 find_package()를 해준다
```c
find_package(catkin REQUIRED COMPONENTS
    roscpp tf2_ros
)
```


catkin_package 에 넣어서 한번 더 패키지 리스트를 완성할 수도 있지만, *빌드에는 도움이 안된다*   
tf 도 마찬가지이고, 

```c
catkin_package(
    INCLUDE_DIRS include
    CATKIN_DEPENDS roscpp tf tf2_ros
)
```
이런식으로 catkin_package에 넣어줄 필요는 없다. (해도 상관은 없음)  
단, package.xml 에 넣어줘야 한다 

```xml
<buildtool_depend>catkin</buildtool_depend>
<build_depend>roscpp</build_depend>
<build_depend>tf2_ros</build_depend>

<build_export_depend>roscpp</build_export_depend>
<exec_depend>roscpp</exec_depend>
<exec_depend>tf2_ros</exec_depend>
```

끝