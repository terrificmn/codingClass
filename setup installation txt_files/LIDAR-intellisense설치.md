https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md
여기에 나온방식대로 안됨

gpg: keyserver receive failed: No keyserver available

이렇게 나옴

```
sudo apt-update
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
```

```
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u
```

이제 apt-key가 설치되었으므로 위의 명령어가 실행이 됨


이제 리포지터리 등록 후 인스톨

sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils


시간관계 상 이거는 나중에 해보자

Optionally install the developer and debug packages:
sudo apt-get install librealsense2-dev
sudo apt-get install librealsense2-dbg

usb-c 타입을 컴퓨터와 라이다 카메라와 연결 후 

이제 실행은 터미널에서 
realsense-viewer 

그러면 viewer가 실행되고 
Intel RealSense L515 를 발견했다며 Version 업데이트를 하라고 한다. 눌러준다

시간이 좀 걸림


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
