[ WARN] [1659350400.421836616]: Transform from base_footprint to map was unavailable for the time requested. Using latest instead.

[ WARN] [1659350400.922102244]: Transform from odom to map was unavailable for the time requested. Using latest instead.

[ WARN] [1659350402.688151563]: Transform from base_footprint to map was unavailable for the time requested. Using latest instead.


원인은 navsat_tranform에서 gps를 변환하려고 tf tree를 lookup하게 되는데 이때 ekf 노드에서  
아직 관련 늦어서 이런 현상이 발생 한다고 함  

방법은 gps 를 조금 늦추는 방법이 있다고 함  

https://answers.ros.org/question/330024/robot_localization-transform-from-base_link-to-map-was-unavailable-for-the-time-requested-using-latest-instead/

여기 다시 보기  

tf_monitor로 딜레이를 봐야함 
Try to use rosrun tf tf_monitor to inspect time delays


All Broadcasters:
Node: unknown_publisher 283.144 Hz, Average Delay: 0.00614267 Max Delay: 0.0739601
Node: unknown_publisher(static) 155345 Hz, Average Delay: 0 Max Delay: 0

결과가 엄청 딜레이 되는 것 같다   



## Datum 메세지 출력이 계속 되는 경우 
```
[ INFO] [1659697145.833656241, 32.000000000]: Datum (latitude, longitude, altitude) is (-30.060224, -51.173913, 10.085843)
[ INFO] [1659697145.833729725, 32.000000000]: Datum UTM coordinate is (483236.647952, 6674528.544410) zone 22
```
이런식으로 Datum 메세지가 계속 나오는 것은  
gps 신호는 들어오는데 imu가 안들어 올 경우에 위의 정보만 계속 보여준다  

gps와 imu 토픽을 다 잘 받게되면  

```
 INFO] [1659697231.353374457, 117.432000000]: Datum (latitude, longitude, altitude) is (-30.060223, -51.173913, 10.021106)
[ INFO] [1659697231.353450433, 117.432000000]: Datum UTM coordinate is (483236.646207, 6674528.644351) zone 22
[ INFO] [1659697231.387232383, 117.466000000]: Corrected for magnetic declination of 0.000000, user-specified offset of 1.570796 and meridian convergence of 0.001520. Transform heading factor is now 1.572317
[ INFO] [1659697231.387360577, 117.466000000]: Transform world frame pose is: Origin: (-1.221396774390405336e-05 1.2908305032873257275e-05 0)
Rotation (RPY): (0, -0, 0.010093825845417734796)

[ INFO] [1659697231.387441107, 117.466000000]: World frame->cartesian transform is Origin: (-6678425.7049494991079 425999.03430811967701 -9.8412988974298070133)
Rotation (RPY): (0, 0, -1.562223353063630249)

```
그리고 나서 더 이상 출력이 되지 않는다  



이거 참고하면 tf는 해결되는 듯 하다  
https://answers.ros.org/question/300345/robot-localization-package-transform-from-base_link-to-odom-was-unavailable-for-the-time-requested-using-latest-instead-imugps/  

navsat_transform_node 에서 GPS 토픽 메세지를 받았을 때 EKF 도 imu 관련 topic 메세지를 받는데  
navsat_transform이 사용할 수 있게 EKF 노드는 계산해서 TF를 그 전에 pulbish 해야하는데   
그런데...   
navsta_transform 은 gps를 받자마자 tf를 필요하게 되어서 나오는 현상    
그 때에도 ekf는 imu를 받은 상태이므로 바로 tf를 주는게 불가능한 상황  

transform_time_offset 을 ekf 노드에 줘서 발행할 시간을 준다(?)   
predict_to_current_time: true 를 해서 EKF가 현재 ROS시간을 기준으로 (publish) 하기 전에 예상하게 한다


