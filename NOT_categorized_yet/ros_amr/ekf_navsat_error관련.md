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
