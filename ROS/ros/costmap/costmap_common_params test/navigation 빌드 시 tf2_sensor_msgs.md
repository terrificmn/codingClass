navigation 빌드 하려면 깃 클론하자
```
gin clone https://github.com/ros-planning/navigation.git
```

> default branch는 noetic_devel 이다

그리고 catkin build navigation 해주면 됨

만약...   아래와 같은 에러 발생 시 
```
Could not find a package configuration file provided by "tf2_sensor_msgs"
  with any of the following names:
```

tf2_sensor_msgs를 설치해주면 된다
```
sudo apt install ros-noetic-tf2-sensor-msgs
```



