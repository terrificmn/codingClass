- manipulators (책 416)
(act에 해당)

좌표변환 (TF) Coordinate Transformations



협동로봇 - 수직다관절형 (햅팁 센서로 감지)

    - manipulator components
    기저(base)
    링크(link)
    기저 - 관절 - 말단 장치 연결
    
    관절(joint)
    로봇의 움직임을 만들어 냄 회전 (revolute) 운동형
    병진 (prismatic) 운동형

    말단 장치 (end effector)
    손에 해당하는 마지막 장치


Joint에는
Revolute Joint(회전 관절), Prismatic Joint(병진 관절), Screw Joint, 
Spherical joint (구형관절)(예: star wars의 bb-8 )

DOF, Degrees of Freedom

위치좌표(x,y,z), 각도 (roll, pitch, yaw) 의 6개만 있으면 물체의 위치/자세가 표현 가능
6개의 자유도라고 한다


Forward Kinematics (순 운동학)
    - 솔루션이 한개 (가리키는 방향이 한개)
    - 

Inverse Kinematics (역 운동학)
    - 솔루션이 여러개 (가리키는 방향이 같지만 그걸 하는 방향은 여러개)
    - 말단 장치의 위치와 자세가 주어졌을 때 관절 각도 및 위치를 구하는 것



링크 (link) 와 관절 (joint) 가 중요하다

로봇 청소기를 예를 들면
2개 메인 바퀴 링크, 2개의 따라만 가는 바퀴 이것도 링크
원형의 구 형태의 본체도 링크

바퀴는 또한 joint 앞으로만 돌아가는 회전을 한다 (Revolute Joint)


로봇 모델링을 할 때 확장자는 urdf 를 사용 (xml을 사용)

```
cd ~/catkin_ws/src
catkin_create_pkg testbot_description urdf   
cd testbot_description
mkdir urdf
cd urdf
```

catkin_create_pkg 는 패키지 만드는 것



urdf 문법 검사 및 그래프 표시
check_urdf # 문법 검사

robot_description   #로봇 모델을 xml로 만들어줌

joint_state_publisher  #관절의 각도 값 퍼블리시 해주는 패키지

robot_state_publisher  #관절 각도 값을 받아 관절과 링크간의 3차원 위치, 자세 정보를 퍼블리시








catkin workspace를 만들어 줘야한다
catkin_make를 해주면 만들어 준다
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```

source devel/setup.bash
를 실행해서 
매번 실행하기 귀찮으므로 .bashrc 파일에 넣어준다
```
source ~/.catkin_ws/devel/setup.bash
``






https://github.com/ROBOTIS-GIT/ros_tutorials 을 git clone 하자
(422 p)


먼저 클론받은 파일 중에 testbot_description 디렉토리 내용을 복사해준다
```
$ cp -r testbot_description/ ~/catkin_ws/src
```

catkin_ws 디렉토리에서 
```
catkin_make
```
를 해주면 빌드가 되면서 패키지가 ros 에 등록이 된다 

그리고 나서 
```
roslaunch testbot_description testbot.launch 
```
를 해준다

그러면 작은 창과 함께 실행이 됨

이제 다른 터미널을 열어서 
```
rviz
```
실행




___

소스 코드 분석

CMakeLists.txt
```
cmake_minimum_required(VERSION 2.8.3)
project(testbot_description)
find_package(catkin REQUIRED COMPONENTS urdf)
catkin_package()
include_directories(${catkin_INCLUDE_DIRS})
```
위 파일의 project() 명이 프로젝트 명이 된다.


package.xml
```xml
<?xml version="1.0"?>
<package>
  <name>testbot_description</name>
  <version>0.1.0</version>
  <description>ROS turtorial package to learn the URDF</description>
  <license>Apache License 2.0</license>
  <author email="pyo@robotis.com">Yoonseok Pyo</author>
  <maintainer email="pyo@robotis.com">Yoonseok Pyo</maintainer>
  <url type="bugtracker">https://github.com/ROBOTIS-GIT/ros_tutorials/issues</url>
  <url type="repository">https://github.com/ROBOTIS-GIT/ros_tutorials.git</url>
  <url type="website">http://www.robotis.com</url>

  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>urdf</build_depend>
  <run_depend>urdf</run_depend>
  
  <export></export>
</package>
~                 
```
위의 <name>부분이 패키지 이름이 된다.
그리고 

launch디렉토리의 
testbot.launch 의 내용
```
<launch>
  <arg name="model" default="$(find testbot_description)/urdf/testbot.urdf" />
  <arg name="gui" default="True" />
  <param name="robot_description" textfile="$(arg model)" />
  <param name="use_gui" value="$(arg gui)"/>
  <node name="joint_state_publisher" pkg="joint_state_publisher" type="joint_state_publisher" />
  <node name="robot_state_publisher" pkg="robot_state_publisher" type="state_publisher" />
</launch>
~                                                                               
~                   
```

