Converts GPS data to UTM coordinate로 바꿔줌

GPS 정보는 latitude, longitude 등 인데 이걸로로는 map에서 로봇위치를 알 수가 없음  
그래서 UTM 으로 바꿔서  
/utm 으로부터 /map 를 publish를 하게 된다   

UTM은 Universal Transverse Mercator로  
Coordinate system uses a 2-dimensional Cartersian coordinate system to give locations  
on the surface of the Earth.

GPS data, IMU data, odometry를 이용하게 된다  


navsat의 config 파일로 적용하거나 런치파일에서 param으로 지정할 수 있다
```
frequency: 30
delay: 3.0
magnetic_declination_radians: 0.00
yaw_offset: 1.570796327
zero_altitude: true
broadcast_utm_transfore: true
publish_filtered_gps: true
use_odometry_yaw: false
wait_for_datum: false
```

그리고 navsat_transform 노드에서는  remap을 해줄것
```
<remap from="/imu/data" to="/imu/data"/>
        <remap from="/gps/fix" to="/ublox/fix"/>
        <remap from="/odometry/filtered" to="/md_odom" />
```

movebase를 husky 참고해보기  
husky_navigation 패키지의 런치파일 move_vase_nav.launch 참고  
path planing과 obstacle avoidance 처리


## Record a trajectory 하기
먼저 robot이 가동되고 , gps_navigation 등이 실행된 상태에서   

텔레옵키를 사용해서 (turtlebot) 특정 지점에 도달하면 y키를 눌러서 현재 로봇의 장소를 저장한다  
omo패키지의 teleop에도 기능이 있는지 확인 후 없으면 turtlebot3 teleop 참고하기  

teleop키에서 아래의 토픽을 발행하는데 (터블봇이 아니라면 husky 패키지 확인해 봐야한다)

rostopic echo /outdoor_waypoint_nav/gps/filtered

y키를 눌렀을 때 subscribe를 해서 파일로 저장하게 된다   points_sim.txt 파일

gps 좌표를 퍼블리싱 해줌


https://www.youtube.com/watch?v=cmOplaq8cHc  
46