ublox gps를 사용하므로   
깃허브를 클론  

```
https://github.com/KumarRobotics/ublox.git
```
깃허브의 READMD를 참고한다 

catkin tools를 이용해서 빌드를 하기전에  
의존성 패키지를 먼저 설치해주자 

```
sudo apt install ros-melodic-rtcm-msgs ros-melodic-nmea-msgs
```

이제 마찬가지로 usb장치 연결된 것을 확인해야하므로   
무선조종이나, 모터 드라이브 연결 시에 했던 것 처럼  
dmesg와 udevadm를 확인해서 연결하고   
스크립트 파일을 역시 다음에 또 사용하기 위해서 ublox_gps 패키지 내에 scripts/create_udev_rules.sh 파일을   
복사해서 만든다  

그리고 스크립트를 실행해서 심볼릭링크로 장치를 만들어 준다   

ublox_gps 런치파일에서 rosparam 으로 command=load 를 해주기 때문에  
config 디렉토리에 yaml 파일을 읽어드리기 때문에   
nmea.yaml 파일을 열어서 device 부분을 위에서 udev_rules로 심볼릭 링크로 만든 것으로 수정해 준다   

아래 부분을 수정
```
device: /dev/ttyUSB0
nmea:
  set: true
  version: 65
  ... 생략
```



런치파일
~/catkin_ws/src/ublox/ublox_gps/launch$ vi ublox_device.launch 

