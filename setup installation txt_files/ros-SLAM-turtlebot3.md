# 터틀봇3 개발환경

[참고페이지-TurtleBot3 페이지](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/)

설치
```
$ sudo apt-get install ros-melodic-joy ros-melodic-teleop-twist-joy \
  ros-melodic-teleop-twist-keyboard ros-melodic-laser-proc \
  ros-melodic-rgbd-launch ros-melodic-depthimage-to-laserscan \
  ros-melodic-rosserial-arduino ros-melodic-rosserial-python \
  ros-melodic-rosserial-server ros-melodic-rosserial-client \
  ros-melodic-rosserial-msgs ros-melodic-amcl ros-melodic-map-server \
  ros-melodic-move-base ros-melodic-urdf ros-melodic-xacro \
  ros-melodic-compressed-image-transport ros-melodic-rqt* \
  ros-melodic-gmapping ros-melodic-navigation ros-melodic-interactive-markers
```

소스파일로 설치하기
```
cd ~/catkin_ws/src/
$ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/DynamixelSDK.git
$ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
$ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
$ git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
$ cd ~/catkin_ws && catkin_make
```

소스파일로 설치를 안하고 apt-get으로도 설치할 수 있다
```
$ sudo apt-get install ros-melodic-dynamixel-sdk
$ sudo apt-get install ros-melodic-turtlebot3-msgs
$ sudo apt-get install ros-melodic-turtlebot3
```


이제 터틀봇3를 실행보자
먼저 로봇을 정해줘야하는데 환경변수로 설정해준다. 터미널이 꺼지면 인식을 못하므로 ~/.bashrc파일에 저장해도 좋다

```
$ export TURTLEBOT3_MODEL=waffle
```

```
$ vi ~/.bashrc
```
맨 아래에 내용 추가 후 저장
```
export TURTLEBOT3_MODEL=waffle
```

그리고 실행 (로봇만 덩그라니 있다)
```
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
```

가제보에서 터블봇을 확인했다면 이제 프로그램을 종료한다 

이번에는 벽이 있는 공간으로 같이 불러온다
```
roslaunch turtlebot3_gazebo turtlebot3_world.launch
```

이제 키보드로 조정을 해보자
```
roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch 
```

여기에다가 rviz를 이용해서 화면을 볼 수가 있다

```
$roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
```



## 이제 가상 SLAM을 해보자

각 다른 4개의 터미널을 띄워야하고

가제보실행
```

```

slam실행
```
roslaunch turtlebot3_slam turtlebot3_slam.launch 
```

여기서 rviz실행하는데 조금 다른 방식으로 실행한다
```
rosrun rviz rviz -d 'rospack find turtlebot3_slam'/rviz/turtlebot3_slam.rviz
```

teleop실행을 하면 된다



