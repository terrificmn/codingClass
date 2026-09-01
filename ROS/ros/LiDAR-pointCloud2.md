http://wiki.ros.org/pcl/Overview
포인트 클라우드 확인하기
sensor_msgs::PointCloud2

[블로거 튜토리얼-한쿡사람](https://limhyungtae.github.io/2019-11-29-ROS-Point-Cloud-Library-(PCL)-0.-Tutorial-%EB%B0%8F-%EA%B8%B0%EB%B3%B8-%EC%82%AC%EC%9A%A9%EB%B2%95/)

[PCL 튜토리얼](https://pcl.readthedocs.io/projects/tutorials/en/latest/)

[슬램관련 Tutorial](https://intel.github.io/robot_devkit_doc/pages/slam.html)

먼저 PCL (Point Cloud Library)를 설치한다
```
$ sudo apt install libpcl-dev
```

기존패키지가 있다면 CMakeList.txt파일만 변경해주면 되지만 
차라리 패키지를 다시 만들어주는게 나은 듯 하다. 

```
$ catkin_create_pkg l515_slam pcl_ros roscpp std_msgs
```

그리고 나서 필요한 패캐지는 pcl_ros 정도이고 더 필요한 것들은 CMakeLists.txt 파일에다가 넣어주면 된다

불필요한 주석을 제거한 것은 
```c
cmake_minimum_required(VERSION 3.0.2)
project(l515_slam)

find_package(catkin REQUIRED COMPONENTS
  pcl_ros
  roscpp
  std_msgs
)

find_package(PCL REQUIRED)

catkin_package(
  LIBRARIES l515_slam
  CATKIN_DEPENDS pcl_ros roscpp std_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${PCL_INCLUDE_DIRS}
)

add_executable(pointcloud_sub src/pointcloud_sub.cpp)

add_dependencies(pointcloud_sub ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(pointcloud_sub
  ${catkin_LIBRARIES}
  ${PCL_LIBRARIES}
)
```

이제 패키지 준비는 끝이남 

코드는 깃허브에 

그리고 L515를 실행해서 토픽을 publish를 할 수 있게 해야하는데 일단
realsence 패키지를 이용해서 demo-pointcloud를 켜준다
(rs_camera.launch를 실행하면 옵션을 넣어도 토픽은 나오지만 실제 데이터가 안넘어간다
그래서 demo-pointcloud를 실행해야함)


(옵션사항)
먼저 demo_pointcloud.launch 파일의 rviz 노드를 실행이 안되게 주석처리 해준다
```xml
<!-- <node name="rviz" pkg="rviz" type="rviz" args="-d $(find realsense2_camera)/rviz/pointcloud.rviz" required="true" /> -->
```

그리고 실행
```
$ roslaunch realsense2_camera demo_pointcloud.launch
```

그리고 만들어놓은 패키지를 실행
```
$ rosrun l515_slam pointcloud_sub
```

그리고 다른 터미널에 rviz를 입력해서 새로운 창을 띄운다
왼쪽 하단에 있는 Add 버튼을 눌른다음에 By topic 탭으로 가보면 토픽을 볼 수가 있는데 
여기에서 /pc_output 이라는 토픽을 선택해준다 ok를 눌러준다

그리고 Global Status:Error 라고 나오느데 Fixed Frame 부분을 map 에서 다른것으로 바꿔주면 
포인트 클라우드 화면이 나오게 된다




참고 사이트
https://www.programmersought.com/article/1861817652/
