source /opt/ros/foxy/setup.bash
source ~/turtlebot3_ws/install/local_setup.bash

export ROS_DOMAIN_ID=30 # Default ROS2 Domain ID for TurtleBot3
export LDS_MODEL=LDS-02
export TURTLEBOT3_MODEL=burger

.bashrc 파일에 들어가 있는 것


터틀봇은 현재 오버레이가 되어 있음

오버레이 해주기
. install/setup.sh



ssh에 비번 물어보는 메세지
ubuntu@192.168.0.102's password:



ros2 launch turtlebot3_bringup robot.launch.py




트러블슈팅

[ WARN:0] global ../modules/videoio/src/cap_gstreamer.cpp (480) isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
[INFO] [1652926942.831622533] [camera_publisher]: 
---- Images are being published... ---

You would have to specify V4L capture backend for using V4L controls. Seems here that without specifying it, gstreamer backend is used, and it instanciates a pipeline with v4l2src, but you cannot change the resolution after creation.

So the simplest solution is just using V4L2 capture backend:

usb_cap = cv2.VideoCapture(1, cv2.CAP_V4L2)

이렇게 하면 조금 해결되기는 워닝도 안 뜨고 토픽도 잘 날리는 듯 하다
하지만 터틀봇과 함께 실행시에는 터틀봇이 버거워 하는 듯 하다
그래서 result 가 실패가 많이 뜸;;

위처럼 하면 워닝은 뜨지 않지만 토픽상, 제대로 검출이 안되는 듯~
색깔 검출 잘 되던것이 실패로 나옴
(아마도 V4L2에 대한 설정이 전혀 안되어 있어서?? 아직 모르겠다)

워닝은 뜨지만 결과는 만족스럽다. 물론 PC에서;;
터틀봇3에서는 제대로 수행이 안되는 듯 하다~ 토픽을 받아보면 원할하게 퍼블리싱이 안되는 거 같다
마치 렉이 있는 듯하게 지연이 있는 것 같다


