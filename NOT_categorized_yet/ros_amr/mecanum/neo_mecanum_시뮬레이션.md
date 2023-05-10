# neobotix의 gazebo 시뮬레이션 

neobotix 사의 mpo_500 로봇 mecanum 휠

## 클론 및 빌드
먼저 시뮬레이션 클론
[neo_simulation](https://github.com/neobotix/neo_simulation)

```
cd ~/catkin_ws/src
git clone https://github.com/neobotix/neo_simulation
```

그리고 구동에 필요한 kinematics_mecanum 패키지 설치
```
git clone https://github.com/neobotix/neo_kinematics_mecanum
```

빌드 
```
cd ~/catkin_ws
catkin build neo_simulation neo_kinematics_mecanum
```

아주 다행히 프로그램이 잘 되어 있어서 전혀 에러 없이 한번에 빌드 된다  

(ROS noetic 기준)


## gazebo launch
런치파일은
```
roslaunch neo_simulation mmo_500_simulation_basic.launch 
```

teleop_twist_keyboard, 및 arm_controller 가 없어서 워닝, 에러가 발생하긴 하지만   
그냥 무시하고 사용하거나 런치파일 수정


