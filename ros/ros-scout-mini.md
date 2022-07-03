# scout-mini usb 연결하기

먼저 scout-mini와 usb로 컴퓨터와 연결을 해준다음에
```
ls -l /dev/ttyUSB*
```
를 해보면 
```
no such file or directory 
```
이라면서 연결이 안된다.

아래 명령어로 usb 장치가 ttyUSB0으로 연결되게 해준다
```
sudo modprobe usbserial vendor=0x067b product=0x23c3
```

이제 다시 
```
ls -l /dev/ttyUSB*
```
하면

```
crw-rw---- 1 root dialout 188, 0  6월 29 17:00 /dev/ttyUSB0
```
나올 것이다. 

이제 실행할 수 있는 권한으로 바꿔준다

```
$ sudo chmod 777 /dev/ttyUSB0
```

scout_mini_ros ROS 패키지로 이동해준다음에
다시 scout_bringup 패키지로 이동해서 그 안의 런치파일을 수정해준다

```
cd ~/catkin_ws/src/scout_mini_ros/scout_bringup/launch
```

런치 파일을 수정해준다. vi, gedit, code 아무거나
```
code scout_minimal.launch
```

내용중 arg 태그의 default값이 can0로 되어 있는 것을 아래처럼 바꿈
(이유는 can통신을 안하고 시리얼 통신으로 하기 때문에)
```xml
<arg name="port_name" default="/dev/ttyUSB0" />
```

그리고 나서 저장 후 각각 다른 터미널에서
각 scout_minimal.launch 와 scout_teleop_keyboard.launch 을 실행해준다
```
$ roslaunch scout_bringup scout_minimal.launch 
```

```
$ roslaunch scout_bringup scout_teleop_keyboard.launch 
```

