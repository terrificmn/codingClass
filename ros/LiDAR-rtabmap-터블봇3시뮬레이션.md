네비게이션 예제 설치 후 다시 한번 해볼 것
http://wiki.ros.org/rtabmap_ros/Tutorials/MappingAndNavigationOnTurtlebot#Turtlebot3_on_Melodic_and_Noetic

필요한 패키지 (터블봇3를 설치했다면 이미 깔려있을것임)
```
sudo apt install ros-melodic-turtlebot3-simulations ros-melodic-turtlebot3-navigation ros-melodic-dwa-local-planner ros-melodic-rtabmap-ros
```


2개의 터미널에 각각 실행하자
```
$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch

$ export TURTLEBOT3_MODEL=waffle
$ roslaunch rtabmap_ros demo_turtlebot3_navigation.launch
```

맵핑 세션을 했다면

텔레옵 키보드를 실행해서 
```
$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch
```
Localization을 한다. 

Rviz 창이 뜨면 navigation을 할 수가 있는데 상단의 2D Nav Goal 를 눌러서 원하는 곳을 찍어주면
알아서 터블봇이 이동한다

