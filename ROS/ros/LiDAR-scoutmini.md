# scout-mini 소스파일 받기

https://github.com/agilexrobotics/scout_mini_ros


위의 깃허브 페이지에서 자세한 설치사항 참고
캔 통신은 사용을 안할 것이므로 캔 통신 관련한 것은 스킵한다

의존성 관련 ROS패키지 설치하기

```
$ sudo apt install ros-melodic-teleop-twist-keyboard
$ sudo apt-get install ros-melodic-joint-state-publisher-gui
$ sudo apt install ros-melodic-ros-controllers
$ sudo apt install ros-melodic-webots-ros
```


catkin_ws/src 디렉토리에 깃 클론을 해준 후에 컴파일을 해준다
```
$ cd ~/catkin_ws/src
$ git clone https://github.com/agilexrobotics/scout_mini_ros.git
$ cd ..
$ catkin_make
```

런치파일에서 can통신이 기본값으로 되어 있으므로 변경을 해준다
원하는 편집프로그램 사용해서 열어준다. vi/code 등

```
$ cd catkin_ws/src/scout_mini_ros/scout_bringup/launch/
$ code scout_minimal.launch 
```

```xml
<!-- <arg name="port_name" default="can0" />  -->
<arg name="port_name" default="/dev/ttyUSB0" />
```
로 변경해준다음에 저장한다


<br/>

# usb 권한 조정해주기
roslaunch를 실행하기 전에

다이얼 그룹에 넣어 주기 
그러면 매번 chmod 로 권한을 변경을 안해도 된다
```
sudo usermod -aG dialout $USER
```
```
$ id 
```
해보면 dialout 그룹이 안나온다

로그아웃을 해준 후에 
다시 id를 해주면 뜬다 
```
ls -l /dev/ttyUSB0 
```
를 해보면 

권한이 
```
crw-rw---- 1 root dialout 188, 0  6월 30 11:28 /dev/ttyUSB0
```
로 되어 있지만 

```
$ id | grep dialout
```
해보면 20(dialout)로 잘 나온다

이제 

roslaunch scout_bringup scout_minimal.launch 로 실행을 해도 
usb퍼미션 관련 문제가 생기지 않는다.

<br/>

# roslaunch 실행하기
이제 scout_minimal런치파일과 telelop 키보드를 작동시켜준다. 각기 다른 터미널에서 열어준다

```
$ roslaunch scout_bringup scout_minimal.launch
$ roslaunch scout_bringup scout_teleop_keyboard.launch
```

i키를 눌러서 작동을 해보면 된다 
속도는 up은 w, 속도 다운은 x