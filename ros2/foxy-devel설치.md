## 여기는 PC 셋팅
```
sudo apt install ros-foxy-gazebo-ros-pkgs ros-foxy-cartographer ros-foxy-cartographer-ros ros-foxy-navigation2 ros-foxy-nav2-bringup
```

```
sudo apt install ros-foxy-turtlebot3-msgs ros-foxy-dynamixel-sdx ros-foxy-hls-lfcd-lds-driver
```

ws디렉토리 만들기
```
mkdir -p ~/turtlebot3_ws/src && cd ~/turtlebot3_ws/src
```

깃클론 -b 옵션으로 브랜치 foxy-devel 으로 클론
```
git clone -b foxy-devel https://github.com/ROBOTIS_GIT/turtlebot3
```

이번에는 시뮬레이션 클론 받기
```
git clone -b foxy-devel https://github.com/ROBOTIS_GIT/turtlebot3_simulations
```

이동 후 빌드
```
cd ~/turtlebot3_ws
colcon build --symlink-install --parallel-workers 1
```


## 여기아래는 라즈베리파이 셋팅

slam과 navigation 설치하기
성공여부는 아직 모름

```
cd turtlebot3_ws/src/
```
이동 후에 turtlebot3 를 지워버림
```
rm -rf turtlebot3/
```

그리고 foxy-devel 브랜치로 다시 깃 클론
```
git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3.git
```

turtlebot3_ws 로 이동 후 
```
cd turtlebot3_ws
```

다시 빌드를 해준다. 시간이 꽤 걸림 약 2~3분?
```
colcon build --symlink-install 
```

https://supjav.com/125325.html

https://supjav.com/118285.html

