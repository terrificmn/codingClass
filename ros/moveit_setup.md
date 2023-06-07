# moveit setup
Moveit Setup Assiatant 를 사용~

소스
```
cd ~/moveit_ws
. devel/setup.base
```

실행
```
roslaunch moveit_setup_assistant setup_assistant.launch 
```


## urdf 변환
xacro 파일로 되어 있다면, urdf 파일 밖에 지원을 안하므로 먼저 변환을 해줘야 한다  

해당 xacro 파일이 있는 곳으로 이동 
```
cd ~/catkin_ws/src/my_description/xacro
```

```
rosrun xacro xacro robot_base_xacro.xacro > converted_robot.urdf
```


## moveit_setup_assistant
이제 다시 moveit_setup_assistant 패키 프로그램으로 돌아가서   

Create New Moveit Configuration Package 를 선택 후   
Urdf 파일을 경로를 선택해준다   

로드가 잘 되었다면 100% 로 된 후에 오른쪽에 모델 파일이 잘 보이게 된다   


- Self-Collisions 에서는 10000%

- Virtual Joint 
robot link를 로봇 팔만 따로 있는 경우에 world 프레임을 parent Frame으로 만들어주는 기능  
또는 mobild robot 인 경우에는 parent Frame을 odom으로 해준다  

Joint Type을 planar 로 해주면 3개의 3 degrees of freedom 갖는다  (x,y,z 축을 가짐)  

- Planning Groups 
kinematics를 정해주는 중요한 기능
그룹명은 나중에 쓰이게됨 manipulator로 해줌    
Kinematic Solver는 *kdl kinematics plugin/KDLKinematicsPlugin* 을 선택 (기본)   

OMPL Planning 은 Group Default Planner를 *RRT* 로 선택   

[ompl 관련 Documentation 참고](https://ompl.kavrakilab.org/planners.html)

그리고 add joint를 클릭해서 설정을 해주는데   

모바일 로봇이랑 같이 붙어 있는 경우에는 로봇 팔만 따로 joint를 선택한 후에 > 버튼을 눌러서 선택 해준다  
save를 해주면  

처음에 지정한 그룹명으로 manipulator로 나오고   
그 이하  joints 에는 따로 지정한 로봇 팔 joint들만 Revolute 형태로 나오게 된다   

> 만약 gripper가 있다면 Add Group을 클릭해서 한번 더 만들어 주는데   
gripper 의 Kinematic Solver는 None으로 해주고 , OMPL Planning도 None 으로 해준다 
그리고 Advanced Options 에서 Add Links를 선택해서 그리퍼가 달려있는 link를 선택해준다   

- Robot Poses 는
디폴트 자세를 지정할 수 있다  Add Pose 를 눌러서   
기본 서 있는 자세를 이를 테면 *stand* 라는 이름으로 지정해서 저장해주고  
Add Pose 후에 원하는 pose를 만들고 *home* , *start* 등으로 이름을 넣어준다   

- End Effectors
add End Effector를 선택 후  
이름을 지정해주는데 아무 이름이나 상관 없다. gripper, hand 등으로 해준다   
 그리퍼가 달려있는 Parent Link는 마지막 링크에 붙어 있으므로 마지막 link를 선택해준다   
그리고 save를 하면 됨  
현재는 일단 skip 함~ gripperㅏ 필요하지만 일단 로봇 팔만 가지고 테스트 먼저 
추후 End Effectors 를 설정 한 후 업데이트하기


- Passive Joints
joints 중에서 actuator가 달리지 않는 joint를 설정할 때 사용한다. 예를 들어서 caster wheel 같은 것   
그래서 joint_states 토픽에서 여기에서 설정한 joint를 publish 안하게 해준다   
로봇팔만 있다면 스킵

- Auther information

- Configuration files 
이제 관련 해당 파일들을 만들어 주게 되는데 save할 곳을 선택하면서 src 디렉토리에 새로운 디렉토리를 만들어준다  
*로봇이름_moveit_config* 이런식으로 만들어 주면 된다   
패키지를 만들어준다. 



## demo 실행해보기
이제 catkin build를 한 번 해준다 
```
cd ~/moveit_ws
catkin build myrobot_moveit_config
```

이제 데모 런치파일을 실행해보면 rviz와 moveit 패키지를 할 수있게 실행이 된다 
```
roslaunch myrobot_moveit_config demo.launch
```


> 데모 파일을 잘 실행되지만 plan 및 execute에서 문제가 있다. 계속 fail 되면서 로봇팔 움직임이 반복됨   
아마도 설정에서 잘못된 부분이 있을 듯 하다.   
추후 업데이트!

[참고 유투브 moveit](https://www.youtube.com/watch?v=9aK0UDBKWT8)







