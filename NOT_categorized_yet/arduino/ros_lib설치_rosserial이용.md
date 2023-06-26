# rosserial로 ros 관련 패키지 설치
rosrun 을 해서 필요한 ros 패키지를 ros_lib 형태로 설치해 줄 수가 있다   

먼저 `sudo apt install ros-noetic-rosserial-arduino` rosserial-arduino가 설치되어 있어야 한다  

rosserial_arduino 패키지를 이용해서 make_libraries.py 실행 한다. 파라미터로  아두이노/esp32등의 패키지 디렉토리를 지정해준다   
```
rosrun rosserial_arduino make_libraries.py /home/user/Documents/PlatformIO/Projects/esp32_mypkg/lib
```

또는 특정 디렉토리로 이동 후에 
```
cd ~/my_pkg
rosrun rosserial_arduino make_libraries.py .
```
해당 디렉토리에 ros_lib 디렉토리를 만들어준다 


> 현재 ros 에 설치되어 있는 패키지, msg 등을 다 가지고 와서 만들어주는 듯 하다    
PlatformIO (vscode)를 사용할 경우에는 프로젝트(패키지)의 lib 까지 경로로 만들어주면 되고   
아두이노 같은 경우에는 프로젝트(패키지) 안에 libraries 에 넣어주면 될 듯하다   

ros.h, 나 std_msgs, geometry_msgs 등과 같은 type 등을 만들어준다 

**esp32에서는 ros serial이 잘 작동을 안하는 것 같다. 좀 더 테스트를 해봐야 할 듯**


## platformIO 
플랫폼 IO 에서는 platformio.ini 파일에   
```
lib_deps = ros_lib
```
로 추가해준다  

## eps32 에서 트러블 슈팅
ros_lib 이 만들어진 이후에 ros_lib/ros.h 파일을 열어서   

```h
## 원래 이 코드에서 아래 코드로 변경 해준다 #if defined(ESP8266) or defined(ESP32) or defined(ROSSERIAL_ARDUINO_TCP)
#if defined(ROSSERIAL_ARDUINO_TCP)
  #include "ArduinoTcpHardware.h"
#else
  #include "ArduinoHardware.h"
#endif
```

ros에서 wifi로 먼저 연결하려고 하는 것을 방지한다고 하는데..  
별 소득은 없었다.   


## 전체적인 std_msgs 를 보내기
실패는 했지만 전체적인 흐름은  

esp32 쪽에서 ros_lib 라이브러리의 ros.h 파일을 이용해서   
ros를 이용해서 msg를 만들고 퍼블리쉬하는 프로그램이 하나 필요하고 (예제 파일이 많이 있다)   

그리고 
host com에서 `roscore`를 하고 나서 
```
rosrun rosserial_python serial_node.py /dev/ttyUSB0
```

파이썬 코드인 rosserial_python 노드를 실행해 준다   

이제 rostopic list 를 확인해서 나온다면 잘 되는 것임   

> 아직 esp32에서는 잘 안되고 있음  

추가 테스트 후 업데이트 하기!!

