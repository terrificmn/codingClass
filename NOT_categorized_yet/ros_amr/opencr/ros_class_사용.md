# ros 
OpenCR은 ros가 설치되어 있어서 `ros.h` 파일을 include해서 사용할 수 있게 되어 있다  

> 다른 물론 아두이노, 아두이노 나노 등로 roslib을 따로 라이브러리에 넣어주거나,   
platformIO 같은 경우에는 lib에 넣으면 사용 가능하지만   
esp32 은 사용이 좀 어렵다. 일반적으로 ros_lib을 만들어서 넣으면 빌드시에 에러가 발생한다   


## function 콜백 

업데이트 예정....


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