터틀봇3의 gmapping.launch 파일을 참고한다   

gmapping 패키지 설치는  (noetic)
```
sudo apt install ros-noetic-slam-gmapping
```

먼저 my_slam_gmapping 패키지의 launch 의 런치파일을 보면   
arg를 base_frame을 지정해준다. 만약 로봇이 base_link 프레임으로 시작하면 base_link로 바꿔주기  
base_footprint를 사용한다면 그대로 사용   

그리고 odom, map 프레임 (토픽이 아님에 주의) 확인   
> 로봇에서 TF를 만들어서 보냄   

라이다 frequency는 30 이상이 되어야 하는 듯하다. 예를 들어 10 이면 gmapping이 작동을 안한다 

rplidar 기준, 
```xml
<param name="scan_frequency"      type="double"    value="30.0"/>
```

이제 launch 파일을 실행하고 rviz를 실행해보자  

rviz에서 map을 추가해준다  
여기의 map은 topic /map임, 이제 지도가 표시된다  

teleop_key를 이용해서 로봇을 움직인 다음에 맵을 저장해준다  

rosrun map_server map_saver -f 맵이름   (현재 위치에 만들어준다)
```
rosrun map_server map_saver -f new_map
```

map파일을 maps 디렉토리에 넣어준다 


## localize

이번에는 turtlebot3_navigation의 amcl.launch 파일을 참고한다  

런치파일에서 scan_topic  
base_frame_id
odom_frame_id
global_frame_id 를 확인해서 바꿔준다  

scan_topic: indicates from which topic the laser data is obtained  
base_frame_id: (default: base_link) indicates the name of the frame of the center of the mobile base   
odom_frame_id: (default: odom) indicates the name of the frame attached to the odometry system  
global_frame_id: (default: map) indicates the global frame of reference from which the robot will localize  --> map의 정보를 가지고 있는 프레임을 말하는데 이는 로봇의 위치를 찾기 위해서 필요


런치파일을 실행하기전에  
위에서 저장된 map을 map_server를 이용해서 실행해준다

rosrun map_server map_server 맵이름.yaml
```
rosrun map_server map_server new_map.yaml
```

my_localizer 패키지를 만들었는데 여기의 런치 파일을 실행해준다   


rviz를 실행했을 때 처음에는 로봇의 위치가 맞지를 않는다. 2D Pose Estimate 를 해서 위치를 잡아준다 
(방금 시작을 했기 때문에 실제 로봇의 위치를 모르기 때문에 그렇다)

fixed frame은 map으로 고정을 해주고  
로봇이 실제로 위치한 곳으로 2D Pose Estimate를 눌러서 클릭 앤 드래그로 해주는데  
로봇이 바라보고 있는 방향으로 마우스 방향을 맞춰주면 된다  

rviz에서 Pose Array를 추가해준다  
그리고 topic을 /particlecloud 를 선택해준다  
로봇 주위에 파티클이 생김  

로봇 위치를 찾음  

