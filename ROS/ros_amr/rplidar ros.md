
[Slamtec의 rplidar ros깃허브](https://github.com/Slamtec/rplidar_ros)

catkin_ws/src 경로에 깃 클론을 한 후에 catkin build (또는 catkin_make) 한 후에 
런치파일을 실행하면 됨

라이다 제품에 맞는 것으로 런치파일 실행하면 됨


만약 
```
*** buffer overflow detected *** error
```

에러가 발생한다면 /dev/ttyUSB0 의 권한 문제

```
sudo chmod 777 /dev/ttyUSB0
```

또는 udevadm 을 이용해서 /etc/udev/rules.d/ 에 rule을 새로 만들어준다
해당 스크립트 참고



urdf rpy 바꾸기
```

  <joint name="horizontal_laser_link_joint" type="fixed">
    <parent link="base_link" />
    <child link="horizontal_laser_link" />
    <origin xyz="0.0 0.0 0.0" rpy="0 0 3.141592"/>
  </joint>

```