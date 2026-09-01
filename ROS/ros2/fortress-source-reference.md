# fortress gazebo 참고

가제보 관련해서 플러그인을 사용하다보면 sdf 파일에 각종 태그들로 옵션을 넣어주게 되는데  
이때 어떤 tag가 있는지 잘 모를 때가 있는데   

예 imu 에 frame_id는 어떻게 지정하는지 보면  
[여기 github 소스코드를 보면 ](https://github.com/gazebosim/gz-sensors/blob/ec52913e608ce8f64053650bfcced84a70ca12e2/src/Sensor.cc#L158)   

gz_frame_id 를 사용하는 것을 알 수가 있다.  


## 메뉴얼로 파악하기
api 메뉴얼로도 확인할 수가 있다. 하지만 모든 것을 다 알 수는 없는 듯 하다.  
대표적으로 diff_drive 에 대해서는 알 수가 있다.

[여기 사이트에서 확인하기](https://gazebosim.org/api/gazebo/6/classignition_1_1gazebo_1_1systems_1_1DiffDrive.html)

[또 상위 경로에서 해당 클래스들을 확인할 수가 있다](https://gazebosim.org/api/gazebo/6/namespaceignition_1_1gazebo_1_1systems.html)   


