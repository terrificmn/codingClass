MCU를 ROS와 연결해서 사용하려고 하면  

ros serial(USB) 이용해서 ROS에서 msg를 퍼브리싱을 해서 사용을 할 수가 있다

ros-noetic-rosserial-arduino

ros_lib 을 설치해야함


이제 Servo.h를 인쿠르드 한 다음에 사용
```
#include <Servo.h>
#include <ros.h>
```


아마도 GPIO를 통해서 직접 할 수도 있는 듯 하다

https://www.electronicshub.org/raspberry-pi-servo-motor-interface-tutorial/

[라즈베리파이-로 직접 GPIO 연결해서 사용 튜토리얼](https://www.youtube.com/watch?v=xHDT4CwjUQE)

