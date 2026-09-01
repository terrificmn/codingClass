# free fleet 설치 ROS1

ROS 에서는 오직 client 버전만 설치할 수 있는 듯 하다 (설치가 가능하다)  

그래서 ws 스테이션도 새로 만들고, ros2 빌드 시스템인 colcon으로 빌드를 하게 된다   

의존성 중에 message gereration 부분은 Eclipse Cyclone DDS 를 사용하게 되는데       
여기에서 Maven and JDK dependency 를 사용하게 된다고 한다. 그래서 Java-based components로 빌드가 된다고 함  

> 여기에서 IDL preprocessor 만 Jave 컴포넌트라고 하는데, pure C 코드라고 하고, ROS2에서 DDS 사용할 때   
사용을 하는 것 같다.. 
빌드할 때 Could NOT find Maven 를 안보려면... 그래서 java jdk, apache maven 이 필요하다   
필요없을 시 핵심 core만도 설치를 할 수가 있다고 하는데  일단은 의존성 설치로 해결.. 


의존성 설치
```
sudo apt update && sudo apt install \
  git wget qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools \
  python3-rosdep \
  python3-vcstool \
  python3-colcon-common-extensions \
  maven default-jdk
```

> 눈여겨 볼 부분은 python3-colcon... maven default-jdk 정도인 듯


## ws 새로 만들기
기존에 catkin_ws 워크스페이스로 사용하던 것 외에 따로 워크 스테이션을 만들어 준다 
```
cd ~
mkdir -p ff_ros_ws/src
cd ~/ff_ros/ws/src
git clone https://github.com/open-rmf/free_fleet -b main
git clone https://github.com/eclipse-cyclonedds/cyclonedds -b releases/0.7.x
```

> catkin_init_workspace 는 필요없다 

그리고 rosdep을 이용해서 설치를 해준다 
```
cd ~/ff_ros_ws
rosdep install --from-paths src --ignore-src --rosdistro noetic -yr
```

설치가 다 되었다면 빌드를 해준다 
```
cd ~/ff_ros_ws
colcon build
```
또는 `catkin build` 로 해도 상관은 없어 보인다.
현재까지 fake_client, turtlebot3 실행 등에는 문제가 없지만, 일단 예제를 따라가기 위해서 
*colcon으로 진행했다*

> 처음에는 catkin_make 이나 catkin build는 호환이 안되나 싶었는데, 
처음에 maven 이 설치가 안되어 있었음. 그리고 ros2 관련 패키지를 설치를 안 한다는   
warning 메세지 였음. 



## 예제 실행

client 쪽 밖에 실행을 할 수가 없다  
```
cd ~/ff_ros_ws/
source install/setup.bash

# cakin build를 했다면 
source devel/setup.bash
```

실행은
```
roslaunch ff_examples_ros1 fake_client.launch
```

터틀봇3 시뮬레이션  single용
```
export TURTLEBOT3_MODEL=burger; roslaunch ff_examples_ros1 turtlebot3_world_ff.launch
```
싱글용은 그냥 시뮬레이션 용 인듯하다..;;


**멀티용 실행**
```
roslaunch ff_examples_ros1 multi_turtlebot3_ff.launch 

```
사용방법
rviz에서 Robot Selection에 Fleet 에는 *turtlebot3*, Robot에는 *tb3_0*, *tb3_1*, or *tb3_2* 로 입력을 한다   
그리고 2D Nav Goal 을 이용해서 목적지를 지정해주고 나서   
Send Nav Goal 을 눌러주면 터틀봇3가 움직이게 된다   

> 하나씩 Robot의 이름을 바꿔가면서 (namespace인 듯 하다) 2D Nav Goal을 따로 지정해줘야 한다


이제 여기에 서버를 켜야하는데. 일단 ros2 만 가능하기 때문에  
ros2를 설치하고 나서 다시 정리해야겠다

> ROS2 에서 서버가 가능하나  ROS1 과는 브릿지 형태로 통신을 해야하는데.. 아직까지는 성공 못함 


## ros2 는
docker-ros 깃허브, 브랜치 humble  을 참고하고,  scripts 쉘 스크립트 파일을 참고해서 설치할 수가 있다.   

현재는 도커로 설치 및 실행만 해 본 상태 Apr 2023   

> turtlbot3 을 이용한 가제보 및 rviz2를 띄울 수는 있으나... 딱히 navigation만 되는 상태인 것 같고   
정확히 free_fleet를 어떤식으로 활용해야하는지는 잘 모르겠다;


