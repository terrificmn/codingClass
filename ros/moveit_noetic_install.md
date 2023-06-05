# move it
noetic 버전에서 설치할 수 있는 moveit 1 이 마지막 버전  

워크 스페이스를 따로 만들어서 실행하게 된다
```
mkdir -p moveit_ws/src
```

> 튜토리얼에서는 ws_moveit

catkin build 시스템 설치
```
sudo apt install ros-noetic-catkin python3-catkin-tools python3-osrf-pycommon
```
이미 설치되어 있는 것

wstool로 설치를 하기 때문에 wstool도 설치

```
sudo apt install python3-wstool
```


## 소스파일 다운
```
cd ~/moveit_ws/src

wstool init .
wstool merge -t . https://raw.githubusercontent.com/ros-planning/moveit/master/moveit.rosinstall
wstool remove  moveit_tutorials  # this is cloned in the next section
wstool update -t .
```

## example 코드 클론
```
cd ~/moveit_ws/src
git clone https://github.com/ros-planning/moveit_tutorials.git -b master
git clone https://github.com/ros-planning/panda_moveit_config.git -b noetic-devel
```

> panda_moveit_config 가 있다고 해서 그냥 무시하라고 하는데, panda_moveit_config 패키지를 지우고   
다시 클론 해줌


## rosdep 의존성 설치
rosdep 으로 설치
```
cd ~/moveit_ws/src
rosdep install -y --from-paths . --ignore-src --rosdistro noetic
```

## 빌드
빌드 전에 Release 빌드로 config 설정
```
cd ~/moveit_ws
catkin config --extend /opt/ros/${ROS_DISTRO} --cmake-args -DCMAKE_BUILD_TYPE=Release
catkin build
```

> 위의 config 설정에서 --extend 를 설정하면 [explicit] 으로 /opt/ros/noetic 이 붙는데   
다른 워크 스페이스를 extending를 못하는 것 같기도 하다. 빼고 테스트를 해봐야겠다


## 트러블 슈팅
catkin build 시에 에러 발생하면서 undefined reference 나올 경우 

예를 
```
undefined reference to `fcl::CollisionGeometry moveit
```

워크 스페이스의 빌드 포함해서 지워 준 후에 다시 빌드 시작
```
catkin clean
catkin build
```


## 튜토리얼 
소스 셋업.bash 해준 후에 

```
roslaunch panda_moveit_config demo.launch rviz_tutorial:=true
```

rviz가 실행되면 add 버튼을 누르고 첫 번째의 moveit_ros_visualization 에서   
MotionPlanning 을 클릭  

그 이후에는 로봇 팔을 드래그 해보고, command, Plan 이나 , Execute 등을 눌러본다   

[더 자세한 튜토리얼은 여기를 참고](https://ros-planning.github.io/moveit_tutorials/doc/quickstart_in_rviz/quickstart_in_rviz_tutorial.html)   

