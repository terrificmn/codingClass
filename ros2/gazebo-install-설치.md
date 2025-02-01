# gazebo 설치
ros2 와 사용할 때에는 GZ fortress 를 추천


[Gazebo Fortress 설치 페이지](https://gazebosim.org/docs/fortress/install_ubuntu/)]


실행은 `ign gazebo` 으로 실행한다.  

Citadel, Fortress, Harmoic 등은 LTS 버전이고, 알파벳 순서로 되어 있는 듯 하다.  
Garden 은 EOL 


> Harmonic 버전은 `gn sim` 처럼 실행하는데, ros2 humble 호환성은 GZ Fortress(lTS) 더 좋다.


ROS2 Jazzy(LTS) 버전은 오히려  Gz Harmonic 버전과 호환성이 좋다. (Harmonic 버전이 최신인 듯 하다)  

## gazebo sim
먼저 foress 를 설치하고 나서 해당 리포를 클론 

새로운 workspace 를 만들어서 사용 
```
mkdir -p ~/ros_gz_ws/src
```


https://github.com/gazebosim/ros_gz/   
 여기에서 humble 브랜치로 설치

`GZ_VERSION=fortress` 로 지정해서 사용   

rosdep install  시에는 humble 로 버전 명시   

> ros2 브랜치는 rolling 버전

colcon build 후에  
example로 ros2 sim 실행해 볼 수 있음

```
ros2 launch ros_gz_sim gz_sim.launch.py gz_args:="shapes.sdf"
```


자세한 예시는 

https://github.com/gazebosim/ros_gz/tree/ros2/ros_gz_sim
 의 리드미 확인
 

## ros default gazebo 
아마도 classic 버전?  
`sudo apt install ros-${ROS_DISTRO}-ros-gz` 으로 설치하는 듯 하다.



