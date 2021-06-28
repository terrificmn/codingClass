ROS
https://github.com/IntelRealSense/realsense-ros/releases/tag/2.3.0

에서 소스코드 다운로드


먼저 README.MD 파일을 봐도 되고 

먼저 설치 
melodic 버전으로 설치한다 
ros가 멜로딕으로 설치되어 있으므로 

echo $ROS_DISTRO 해보면 melodic으로 잘 나옴

```
sudo apt-get install ros-$ROS_DISTRO-realsense2-camera
```

realsense2와 의존성 패키지를 설치해준다


이렇게 설치해주면 될 듯 하다

(터미널 새로 열어줘서 bashrc 실행해주고)

런치파일 실행
```
roslaunch realsense2_camera rs_camera.launch 
```

그리고 실행이 되면 
```
$ rostopic list로 확인해본다
```

토픽이 겁나 많음
```
/camera/depth/camera_info
/camera/depth/image_rect_raw
/camera/depth/image_rect_raw/compressed
/camera/depth/image_rect_raw/compressed/parameter_descriptions
/camera/depth/image_rect_raw/compressed/parameter_updates
/camera/depth/image_rect_raw/compressedDepth
/camera/depth/image_rect_raw/compressedDepth/parameter_descriptions
/camera/depth/image_rect_raw/compressedDepth/parameter_updates
/camera/depth/image_rect_raw/theora
/camera/depth/image_rect_raw/theora/parameter_descriptions
/camera/depth/image_rect_raw/theora/parameter_updates
/camera/l500_depth_sensor/parameter_descriptions
/camera/l500_depth_sensor/parameter_updates
/camera/motion_module/parameter_descriptions
/camera/motion_module/parameter_updates
/camera/realsense2_camera_manager/bond
/camera/rgb_camera/parameter_descriptions
/camera/rgb_camera/parameter_updates
```

분석을 통해서 잘 알아보자


이번에는 서비스 
```
$ rosservice list
```


이것도 겁나 많다

```
/camera/depth/image_rect_raw/compressed/set_parameters
/camera/depth/image_rect_raw/compressedDepth/set_parameters
/camera/depth/image_rect_raw/theora/set_parameters
/camera/enable
/camera/l500_depth_sensor/set_parameters
/camera/motion_module/set_parameters
/camera/realsense2_camera/get_loggers
/camera/realsense2_camera/reset
/camera/realsense2_camera/set_logger_level
/camera/realsense2_camera_manager/get_loggers
/camera/realsense2_camera_manager/list
/camera/realsense2_camera_manager/load_nodelet
/camera/realsense2_camera_manager/set_logger_level
/camera/realsense2_camera_manager/unload_nodelet
/camera/rgb_camera/set_parameters

```


topic중에 처음에 있는 쉬워 보이는 놈으로 하나 만들어 보기

```
rostopic info /camera/depth/camera_info
```

```
Type: sensor_msgs/CameraInfo

Publishers: 
 * /camera/realsense2_camera_manager (http://ubun-sc:34955/)

Subscribers: None
```

topic type을 넣어서 패키지 만들어보기

cd ~/catkin_ws/src
catkin_create_pkg intel_lidar_test std_msgs roscpp

그리고 vscode열어서 
src파일 작성


소스파일의 topic의 type 확인 한 것대로 적어주고 

subscribe를 한 후에 callback 함수 내에서 사용할 변수들을 알아본다

```
rosmsg show sensor_msgs/CameraInfo
```


먼저 잘 되는지만 확인해보자

대충 소스코드

```cpp
#include <ros/ros.h>
#include <sensor_msgs/CameraInfo.h>
#include <iostream>


void msgCallback(const sensor_msgs::CameraInfo::ConstPtr &msg) { 
    std::cout << msg->distortion_model << std::endl;
    std::cout << msg->height << std::endl;
    std::cout << msg->width << std::endl;
}


int main (int argc, char** argv) {
    ros::init(argc, argv, "intel_lidar_test");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("/camera/depth/camera_info", 10, msgCallback);
    ros::spin();

    return 0;
}
```

string distortion_model, height, width 만 찍어보기


CMakelist.txt도 바꿔주고 

시간관계상 생략

그리고 
rosrun 해보면 
```
plumb_bob
240
320

```

이렇게 잘 받아온다~
