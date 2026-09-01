# ros 
OpenCR은 ros가 설치되어 있어서 `ros.h` 파일을 include해서 사용할 수 있게 되어 있다  

> 다른 물론 아두이노, 아두이노 나노 등로 roslib을 따로 라이브러리에 넣어주거나,   
platformIO 같은 경우에는 lib에 넣으면 사용 가능하지만   
esp32 은 사용이 좀 어렵다. 일반적으로 ros_lib을 만들어서 넣으면 빌드시에 에러가 발생한다   


## function 콜백 
기존 ROS 에서 사용하는 방식과 매우 비슷하다 (조금 다름)

헤더파일은 
```cpp
#include <ros.h>
```

보통 아두이노는 libraries 디렉토리 안에, platformIO 같은 경우에는 lib 디렉토리 안에   
OpenCR 같은 경우는 이미 포함이 되어 있어서 라이브러리를 추가안해도 된다   

```cpp

// 콜백 함수 정의 
void myCbFunc(const std_msgs::Int8 &msg);

// ros 전역으로 선언
ros::NodeHandle nh;
std_msgs::String str_msg;

// publisher 정의 
ros::Publisher string_pub("my_pub_topic", &str_msg); 
ros::Subscriber<std_msgs::Int8> int_sub("my_sub_topic", &myCbFunc);   // 토픽, 콜백함수 지정
```

이제 setup()함수에서 
```cpp
void setup() {
    pinMode(/**....생략**/);

    nh.initNode();
    nh.advertise(string_pub);
    nh.subscribe(int_sub);
}
 
```

마지막에서 loop() 함수에서 사용한다 

```cpp
void loop() {
    digitalWrite(/**...생략... **/);

    str_msg.data = "Hi~ It's me!";

    string_pub.publish(&str_msg); // 진짜 메세지 퍼블리쉬~ 시리얼을 통해서 전송
    nh.spinOnce(); // 보통 ROS와 마찬가지로 spinOnce()로 loop를 진행하고, (NodeHandle이 생성이 되어 있어야 한다)
    delay(10);
}

```

서브크라이브는 보통 PC쪽에서 ROS Noetic 에서 메세지를 보내주거나   
`rostopic pub my_sub_topic ...` 식으로 메세지를 보낼 수가 있고  
또는 publish하는 패키지를 만들어서 보내 줄 수도 있겠음  

어쨋든, 마지막으로 서브크라이브한 콜백함수는 아래처럼 작동한다.
```cpp
// loop() 함수 바로 아래 생성
void myCbFunc(const std_msgs::Int8 &msg) {
    if(msg.data == 0) {
        /// 메세지 만들거나 뭔가 처리 하기
        // do something
    }
}
```


## class 형태로 사용
클래스 형태로 사용하려면 사용할 클래스를 만들어주고  


헤더파일
```cpp
#ifndef MY_ROS_H
#define MY_ROS_H

#include <Arduino.h>
#include <ros.h>
#include <std_msgs/Int8.h>
#include <std_msgs/String.h>

class MyRos {
public:
    MyRos();

    void conveyorDirSet();
    void subCallback(const std_msgs::Int8 &msg);
    
    ros::NodeHandle nh;
    ros::Publisher my_pub;
    ros::Subscriber<std_msgs::Int8, ConveyorHandler> my_sub;

    void pulisherWrapper();

private:
    String signal_str;

    // ros msg
    std_msgs::String str_msg;
};

#endif
```


cpp 파일에서는 constructor 에서 

```cpp
ConveyorHandler::ConveyorHandler() : my_pub("topic_for_pub", &str_msg),
                                    my_sub("topic_to_sub", &MyRos::subCallback, this) {
    nh.initNode();
    nh.subscribe(conveyor_sub);
    nh.advertise(conveyor_pub);

}
```



그냥 publish도 사용할 수 있지만 구지(?) publish()함수를 내 클래스 메소드 안에서 실행;; (wrapper해서 사용)
```cpp
void ConveyorHandler::pulisherWrapper() {
    conveyor_pub.publish(&this->str_msg);
}
```