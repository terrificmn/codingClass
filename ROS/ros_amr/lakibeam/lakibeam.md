ros 패키지 설치 후 

CMakeLists.txt 파일이 압축푼 파일이름과 다르므로 디렉토리명을 CMakeLists에 있는 project() 안에 있는 것으로 하거나, 프로젝트명을 바꾸거나... 암튼   
> 기본 ros1 용 lakibeam 패키지에서는 파라미터가 잘 안먹힘. 업데이트된 압축파일 사용하기

기본 /scan 토픽 앞에 패키지명이 네임스페이스로 붙으므로 Nodehandler를 private으로 사용하지 않게 한다. nh("~"), 여기에서 nh 이런식으로 **파라미터를 넘기지 말자**



중요한 것은 LAN 케이블을 이용하거나, usb-c 타입을 이용하는 방법인데   

### 먼저 usb-c 케이블을 이용하려면  

RNDISnetwork를 이용한다고 한다. (Usb연결 시 - 그렇다고 한다;;;)

host 컴에는 USB Ethernet이 추가된다. 여기 Host IP로 되어있는 것이 192.168.8.1   

이제 web 브라우저로 접속할 수  있다 
192.168.8.2 로 들어가면 됨  

LiDAR Configuration 메뉴에서  Sensor IP address mode를 DHCP로 바꿔준다   

그리고 save


ros 패키지는 (ros2 패키지도 지원) rosrun 으로는 실행 못함  
> 파라미터 기본 값이 설정이 안되어 있어서 에러 발생, sensor ip 때문인 듯

launch file을 열어보면 scan 이나 scan_view 런치파일  

param중에 hostip는 192.168.8.1 로 하거나 0.0.0.0 (전부 검색한다고 함)   
sensorip는 192.168.8.2 로 해주면 된다   

roslaunch로 실행  

```
roslaunch lakibeam1 lakibeam1_scan_view.launch 
```


### RJ45 Socket (standard Ethernet Port) 사용하기

RJ45 socket에 랜 케이블을 연결하고 PC 연결,  
DC5.5-2.1 socket 은 Power Supply 이므로 전원을 연결해야한다  

랜 (ethernet) 케이블은 CAT.5E 또는 이상으로 하면 된다고 함  

Usb-c 타입과는 다르게 Host ip는 192.168.198.1 로 연결하고  
웹 브라우저에는 192.168.198.2 로 연결한다   

Sensor IP address mode가 기본으로 static으로 되어 있는데 그대로 두면 됨

마찬가지로 ros 패키지에서는 
param중에 hostip는 192.168.198.1 로 하고   
sensorip는 192.168.198.2 로 해주면 된다   



### xy


RICHBEAM 이라고 적혀있고 Led가 들어오는 곳이 x 방향이라고 보면 될 듯 하다    
뒤쪽의 뭉툭한 부분이 레이저 감지가 안되는 부분

뒷쪽 대각선 45도(왼쪽), 315도(오른쪽)이 감지가 안됨  
약 270도 감지가 가능하다  

> ros 기준


Class 1 eye safe  
IP65 

