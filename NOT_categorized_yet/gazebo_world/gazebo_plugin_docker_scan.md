# docker 에서 gazebo laser 플러그인 작동 안될 때
docker conatiner에서 gazebo 시뮬레이션을 돌릴 때 크게 문제가 되어 보이지 않았지만  
**scan** 관련해서 제대로 안 되는 경우가 있다.

docker네트워크 관련 문제인가 했지만,전혀 아니다. docker-compose.yaml에서  
network-mode 등은 상관 없다. 그냥 host만 설정해놓고 사용해도 전혀 문제안됨 (예: localhost)  

> network-mode 는 다른 pc와 통신할 때 (예: master를 설정하거나 할 경우)


첫 번째로 
```xml
<visualize>true</visualize>
```
이렇게 해도 전혀 표시가 안된다. 

그리고 텔레옵 키보드로 작동을 시켜도 잘 움직여서 잘 되는구나 할 수 있지만   

scan 토픽을 받아보면 
```
rostopic echo /scan -n1
header: 
  seq: 0
  stamp: 
    secs: 13213
    nsecs: 248000000
  frame_id: "laser_link"
angle_min: -2.268889904022217
angle_max: 2.268899917602539
angle_increment: 0.007101392839103937
time_increment: 0.0
scan_time: 0.0
range_min: 0.07999999821186066
range_max: 15.0
ranges: [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 
```
정상적이지 않다. 만약 이런 현상이라면 scan 값이 없으로 slam등을 수행할 수가 있다.  

## 이유는? 
docker에서 nvidia 관련 컨테이너로 하면 상관이 없지만 (잘 되는 것 확인함)   

`libgazebo_ros_gpu_laser.so` 를 사용할 때 문제가 된다. gpu를 사용하는 레이저 플러그인 인데  
이게 제대로 작동안한다.  

간단하게 urdf gazebo의 파일에서  (gazebo world파일을 열때 불러오는 description에 해당하는 urdf 혹은 xacro파일)
```xml
<!-- 생략 -->
<sensor type="ray" name="lidar_sensor">

<!-- 생략 -->
<plugin name="gazebo_ros_lidar_controller" filename="libgazebo_ros_laser.so">
```
none gpu 버전으로 바꿔준다.  
방법은 sensor type을 gpu-ray에서 **ray** 로 변경  

libgazebo_ros_gpu_laser.so 파일에서 *libgazebo_ros_laser.so* 로 변경

> 참고로 플러그인.so 파일들은 /opt/ros/noetic/lib/ 이하에 있다   
[공식 사이트 gazebo plugin관련](https://classic.gazebosim.org/tutorials?tut=ros_gzplugins#Laser)


이렇게 하고 scan을 보면
```
rostopic echo /scan -n1
header: 
  seq: 0
  stamp: 
    secs: 13201
    nsecs: 769000000
  frame_id: "laser_link"
angle_min: -2.268889904022217
angle_max: 2.268899917602539
angle_increment: 0.007101392839103937
time_increment: 0.0
scan_time: 0.0
range_min: 0.07999999821186066
range_max: 15.0
ranges: [7.570631980895996, 7.64117431640625, 9.912689208984375, 10.023150444030762, 10.117525100708008, 10.129636764526367, 10.254091262817383, 10.38208293914795, 10.47012996673584, 10.601729393005371, 8.895186424255371, 8.861847877502441, 8.812030792236328, 8.788772583007812, 8.740435600280762, 8.718167304992676, 8.673622131347656, 8.78060531616211, 8.900976181030273, 9.011443138122559, 9.129579544067383, 9.260763168334961, 9.322746276855469, 9.425301551818848, 9.592588424682617, 9.712088584899902, 9.85008716583252, 9.989297866821289, 10.058034896850586, 10.224923133850098, 10.37814998626709, 10.558736801147461, 13.949423789978027, 14.080002784729004, 14.325538635253906, 12.19127082824707, 12.151880264282227, 12.10847282409668, 12.070235252380371, 12.041581153869629, 12.010560989379883, 12.181998252868652, 12.403334617614746, 12.684248924255371, 12.851438522338867, 13.113508224487305, 13.41818904876709, 13.590747833251953, 13.903081893920898, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, 11.365864753723145, 11.171651840209961, 11.159164428710938, 11.158247947692871, 11.101746559143066, 11.093714714050293, 11.069384574890137, 11.078021049499512, 11.038816452026367, 11.308677673339844, 11.655715942382812, 11.640820503234863, 11.820780754089355, 12.110252380371094, 12.58758544921875, 12.044329643249512, 12.025769233703613, 12.005705833435059, 12.018746376037598, 11.991029739379883, 11.977490425109863, 12.265104293823242, 14.196358680725098, 14.175636291503906, in
```

잘 나오는 것을 확인 할 수가 있고, 시뮬레이션에서도 visualize 도 제대로 작동하고 파랑색으로 표시된다. 

물론 slam이 가능해진다.

