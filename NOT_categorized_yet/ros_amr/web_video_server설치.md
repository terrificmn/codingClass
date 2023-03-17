# web_video_server 설치
web video server

디펜던시 noetic 기준
```
sudo apt install ros-noetic-async-web-server-cpp
```

깃 클론
```
git clone https://github.com/RobotWebTools/web_video_server.git
```

그리고 catkin build or catkin_make


사용방법은 먼저 usb-camera, realsense 등의 카메라를 작동을 시킨 후에   
(image_raw를 publish 해줘야 함) 

그리고 나서 web_video_server 패키지를 실행
```
rosrun web_video_server web_video_server
```

그리고 web browser에 http://localhost:8080 을 입력해주면 되고   
같은 내부망을 사용할 경우에는 예를 들어 http://192.168.1.1:8080 로 입력해주면 카메라 화면을 볼 수가 있다  


