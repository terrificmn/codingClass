```
sudo apt install libgflags-dev  ros-$ROS_DISTRO-image-geometry ros-$ROS_DISTRO-camera-info-manager ros-$ROS_DISTRO-image-transport ros-$ROS_DISTRO-image-publisher libgoogle-glog-dev libusb-1.0-0-dev libeigen3-dev
```


libuvc 클론 후 빌드 설치
```

mkdir lib-uvc
cd lib-uvc
git clone https://github.com/libuvc/libuvc.git
cd libuvc
mkdir build; cd build
cmake .. && make -j4
sudo make install
sudo ldconfig
```


ros_astra_camera 패키지 설치
```
cd catkin_ws/src
git clone https://github.com/orbbec/ros_astra_camera.git
```

깃 클론 후에 패키지 디렉토리 이름을 변경해준다 
```
mv ros_astra_camera/ astra_camera
```

> catkin build 할 때 패키지 이름을 인식을 못한다. CMakeLists.txt, package.xml의 패키지명을 바꾸거나 그냥 귀찮으니 디렉토리명만 변경하자

빌드 
```
catkin build
```


빌드 후 source 한번 해주고 
```
cd ~/catkin_ws
. devel/setup.bash
```

script 디렉토리에 있는 create_udev_rules 스크립트를 실행
```
cd astra_camera/scripts
./create_udev_rules
sudo udevadm control --reload && sudo  udevadm trigger
```

그러면 /etc/udev/rules.d 디렉토리에 56-orbbec-usb.rules 파일이 생김

실행

기본 런치파일을 실행을 하게되면 그냥 color의 image_raw 가 퍼블리쉬가 안되고   
No color sensor found, depth align will be disabled 없다고 나온다   

또는 Stream color is disabled


~~그래서 패키지 내의 params 디렉토리에서 use_uvc_camera를 true로 변경해주면 보통 카메라 이미지도 퍼블리싱 된다~~

astra_camera 깃허브가 최신화 되면서 아예 파라미터 디렉토리 자체가 없어졌다;;


main.cpp에서 OBCameraNodeFactory를 생성하면서 시작하는데...   
src 디렉토리의 ob_camera_node_factory.cpp 파일에 보면

init 메소드에서 use_uvc_camera 변수를 설정해주는데 파라미터를 받게 되어 있는데, 기본값이 false로 되어 있다   
**true**로 고쳐서 catkin build를 다시 하거나,   
```cpp
  use_uvc_camera_ = nh_private_.param<bool>("use_uvc_camera", false);
```

아니면, 로스런치파일에 파라미터를 추가해준다. 이게 더 편할지도.;; 추후 테스트를 해봐야겠다 


```
roslaunch astra_camera astra.launch
```

rqt_image_view나 rviz를 실행한 후 토픽을 color의 image_raw를 선택해준다. 
ir infrared, depth 이미지도 사용가능


