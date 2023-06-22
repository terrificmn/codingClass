
## vscode 의 platformIO를 할 경우
플랫폼아이오의 홈 화면에서   
Libraries 탭에서 마찬가지로 검색을 rosserial로 해준다  

Michael Ferguson 이 만든 Library를 사용하면 된다  

Add to Project를 눌러서 현재 진행하고 있는 Project 를 선택해주면 인스톨이 된다   


example 첫 번째 탭에서 코드들을 살펴보면 도움이 된다  

그 중에 
```cpp
/* * rosserial Publisher Example * Prints "hello world!" */ 
#include <ros.h> 
#include <std_msgs/String.h> 

ros::NodeHandle nh; 
std_msgs::String str_msg; 
ros::Publisher chatter("chatter", &str_msg); 
char hello[13] = "hello world!"; 

void setup() { 
	nh.initNode(); nh.advertise(chatter); 
} 

void loop() { 
	str_msg.data = hello; chatter.publish( &str_msg ); nh.spinOnce(); delay(1000); 
}
```


### arduino IDE (참고)
에서는 Tools -> Manage Libraries 에서   
rosserial로 검색 후 install하면 되고 


### 이제 컴퓨터 쪽에서는 
Arduino에서는 rosserial 패키지를 이용해서 ros_lib 디렉토리에 해당 파일들을 만들어 줘서   
libraries 디렉토리에 넣어주거나,  

ESP32도 ros_lib 을 만들어서 ros.h 헤더파일을 인식할 수 있게 해줘야 하는데   

OpenCR 의 장점 R이 robot이다. **ros관련해서 이미 설치가 되어 있다!**

desktop에 rosserial 없다면 설치
```
sudo apt install ros-noetic-rosserial-arduino
```

rosrun으로 실행을 시켜주는데  \_port 로 /dev/ttyACM0 으로 정해준다.  
OpenCR은 위의 포트를 사용함   전송속도도 baud 로 정해주면 됨

```
rosrun rosserial_python serial_node.py _port:=/dev/ttyACM0 _baud:=57600
```

이렇게 하면 
Connecting to /dev/ttyACM0 at 57600 baud   
[INFO] [1675320885.433815]: Requesting topics...   

퍼블리쉬 하고 있는 토픽이 있다면 연결이 된다    

다른 터미널 창에서 rostopic list 혹은 rostopic echo를 해보면 된다   


위의 example 코드를 이용해서 OpenCR 에 업로드를 시켜준 후에  usb를 컴터에 연결 하고 
위의 rosserial_python 연결하면 토픽 메세지를 볼 수가 있다  


터미널에서 실행할 경우이고 런치파일로 하고 싶으면 런치파일을 하나 만들고 실행해주면 된다   
내용은 아래처럼
```xml
<node pkg="rosserial_python" type="serial_node.py" name="rosserial" output="screen">
	<param name="port" value="/dev/ttyACM0"/>
	<param name="baud" value="57600"/>
</node>
```


