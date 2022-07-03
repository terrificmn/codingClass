## 라즈베리파이 호환되는 카메라 프로그램 찾음
> ROS 2 Package to Publish Camera Image as sensor_msgs/msg/Image message. Compatible with Raspberry Pi 64 Bit OS. ROS cv_bridge package is not required. Only depends on OpenCV Python 3.

OpenCV를 이용해서 usb로 연결된 캠으로 캡쳐를 시작해서 그것을 ROS2 메세지로 변환한 후 퍼블리쉬하는 간단한 프로그램을 작성해서 테스트까지 완료 했으나
우분투와 리눅스(rocky linux)에서는 너무 잘 되서 쉽게 넘어갈 것이라고 생각했으나~
역시나 내 사전에 쉽게 넘어갈리가 없지 ㅋㅋㅋ
라즈베리파이에서는 프로그램을 돌리면 퍼블리싱이 제대로 안되는 문제 발생

물론 라즈베리파이에는 라즈베리파이 OS가 설치되어 있는 것은 아니지만, 우분투20.04 설치되어 있음 

어쨋든 계속 시도하다가 cv_bridge 없이도 가능하다는 코드를 찾아서 시도해봤는데 다행히 
잘된다

라즈베리파이에서 OpenCV를 이용해서 퍼블리싱을 하려고 한다면 도움이 될 것이다.

> 처음에는 해결책을 찾아보려다가.. 꽤 삽질을 ㅜ 눈물이 ㅠㅠ

깃 허브 주소
https://github.com/ANI717/ros2_camera_publish.git

먼저 워크스페이스의 src 디렉토리로 이동
```
cd ~/my_ws
git clone https://github.com/ANI717/ros2_camera_publish.git
```

일단 프로그램 내에 
Global Variables 로 선언되어 있는 
TOPIC, PERIOD 를 원하는 토픽으로 먼저 바꿔주고, get_logger().info()로 출력되는 부분 바꾸고
패키지 내의 setting.json 파일의 내용도 똑같이 수정해주고, 위의 토픽과 피어리드로 변경 

ros2 run 실행할 때의 노드명이 execute로 되어 있어서 바꿔줄려면 build하기 전에 
setup.py 의 entry_points 부분 변경
```py
entry_points={
        'console_scripts': [
            'execute = ros2_camera_publish.camera_publish_function:main',
        ],
}
```
execute를 원하는 이름으로 변경

다시 워크 스페이스 root로 돌아와서 build
```
cd ~/my_ws
colcon build
```

라즈베리파이 카메라 캡쳐 이미지 퍼블리싱에서 시간을 꽤 소비해서 일단 현재 내 프로그램 대신에 이걸로 대체, 추후 이걸 토대로 다시 만들어볼 생각

> 코드 자체도 괜찮은 것 같다~ 잘 살펴보면 도움이 될 듯하다

## 그 동안 실패한 것들..
희망을 품고 새롭게 시도 하는 것들이 성공하면 남길려고 작성했는데~ 결국은 잘 안되서 포기함

그 전 기록들...
라즈베리파이에서 이미지 퍼블리싱에서 애를 먹고 있는 중..

일단 확인할 것

```
$ ls /dev/video0*
```

결과가 
```
/dev/video0
```
러 나오는지 확인한다. 일단 usb 카메라는 잘 인식했음


```
[ WARN:0] global ../modules/videoio/src/cap_gstreamer.cpp (480) isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
```
이런 워닝이 발생하는데 사실 이것은 remote 컴인 우분투에서 떳던 워닝 sign 
그대로 이미지 퍼블리싱 하는데는 전혀 문제가 없었다

환경변수를 넣어주면
```
export OPENCV_VIDEOIO_DEBUG=1 
```
해보면

다시 실행했을 때
```
$ ros2 run py_cap_img pub_cam_node 
[ WARN:0] global ../modules/videoio/src/cap.cpp (163) open VIDEOIO(GSTREAMER): trying capture cameraNum=0 ...
[ WARN:0] global ../modules/videoio/src/cap_gstreamer.cpp (480) isPipelinePlaying OpenCV | GStreamer warning: GStreamer: pipeline have not been created
[ WARN:0] global ../modules/videoio/src/cap.cpp (183) open VIDEOIO(GSTREAMER): can't create capture
[ WARN:0] global ../modules/videoio/src/cap.cpp (163) open VIDEOIO(V4L2): trying capture cameraNum=0 ...
[ WARN:0] global ../modules/videoio/src/cap.cpp (174) open VIDEOIO(V4L2): created, isOpened=1
[INFO] [1652085809.316537970] [img_cap_pub_node]: 
--- Images are being published... ---
```

별 소득은 없다.. 퍼블리쉬는 되는 것 같아 보여도 topic echo로 받아보면
한번 정도 메세지가 오고 그 다음은 소식이 없고
다시 ros2 topic echo를 쳐보면 그 다음부터는 전혀 퍼블리싱이 안되고 있는 듯 하다

워닝 메세지 때문에 찾다가

https://gitlab.com/boldhearts/ros2_v4l2_camera

rosdep까지 설치하고 dependencies까지 해결해 주는 것이라 필수이기도 하겠지만
라즈베리파이라서;; 드럽게 오래걸림 ㅋㅋㅋ

하지만; build하면서 컴파일 오류;; 아 놔

그냥 포기 v412_camera는 지웠다. 거창한 프로그램이 필요한게 아니고 그냥 퍼블리싱만
제대로 해주기만 하면 됨 ㅠㅠ

