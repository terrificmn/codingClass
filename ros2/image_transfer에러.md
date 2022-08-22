camera.cpp:(.text._ZN12CameraDriverC2Ev[_ZN12CameraDriverC5Ev]+0x40e): undefined reference to   `image_transport::ImageTransport::ImageTransport(ros::NodeHandle const&)'


이런식으로 undefined reference to ... 에러가 발생할 시에는 CMakelists.txt와 package.xml 에 해당 라이브러리를 
넣어줘야 한다 

```yaml
find_package(catkin REQUIRED COMPONENTS
  roscpp sensor_msgs cv_bridge image_transport
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cam_pub
  CATKIN_DEPENDS roscpp sensor_msgs cv_bridge image_transport
#  DEPENDS system_lib
)
```

물론 package.xml에도 넣어주는 것 잊지 말자  


```xml
<build_depend>image_transport</build_depend>
<exec_depend>image_transport</exec_depend>
```

