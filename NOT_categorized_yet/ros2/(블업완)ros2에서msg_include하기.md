# ROS2에서 message 타입 include 하기
먼저 ros에서 include를 하는 것을 살펴보기 전에  
변수명, 클래스명 각종 이름을 지을 때 사용하는 camel과 snake라는 방식을  
알아보려고 한다  

지금도 그렇지만 변수명을 어떤식으로 해야하는지 고민이 되기도 했고   
왜 어떤 것은 _(언더스코어)가 들어가 있고 대소문자를 구분하는데 중간에 대문자가 들어가기도 하고  
상황별로 어떻게 쓰는게 효과적인지 궁금하기도 했다  

<br/>

## camel 방식과 snake 방식
camel 방식은 말 그대로 낙타등 모양처럼 생겼다고(?) 해서 카멜이라고 하고  
변수, 이름 등을 지을 떄 사용한다.   
소문자로 시작해서 대문자로 이어지는 소문자 방식이 있고   
대문자로 시작되는 방식이 있다  

또한 snake 방식은 두 단어 사이를 _(언어스코어)로 구분하는 방식  

왜 이 두 방식이 생겼을까? 뇌피셜입니다.  
변수명은 중간에 스페이스바가 허용이 안 되므로  
변수명 등이 길어지게 되면 쉽게 알아 볼 수 있는 것을 만들어야 했었을 것 같다  
그래서 하나는 단어를 붙인다음 대문자로 구분을 하고 (camel)  
또 하나는 사이에 언어스코어를 붙인 것이라고 생각한다 (snake)  

> 스네이크 방식이 카멜 방식보다 더 알아보기 쉽다고 하기도 한다   
개인적으로는 카멜 방식이 좋아요~   
근데 왜 스네이크지?

예를 들면...   

| 이름방식 | 사용 예 | 
| --- | --- |
| 소문자 camel | userNumber, localImageShow, textElements ... | 
| 대문자 camel | UploadController, MyClass, MappingSub, LaserScan ... | 
| snake |  user_name, df_load, df_by_name, laser_scan ... |

<br/>

## ROS와 ROS2에서 include 방식
이제 본격적으로(?) ros, ros2의 include를 할 때의 방식을 살펴보겠다  
ROS2에서는 include 할 때에 msg타입 ROS에 비해 입력하는 방식이 바뀌었다.

- ROS에서는   
```cpp
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/LaserScan.h>
```
이런식이였는데 geometry_msgs/Twist.h 로 인쿠루드

- ROS2에서는  
```cpp
#include "geometry_msgs/msg/twist.hpp"
#include "sensor_msgs/msg/laser_scan.hpp"
```
이런식으로 바뀌었다.  

- 차이점은   
    1. 먼저 중간에 sub directory인 msg 가 생겼다  
    2. 파일도 h 파일에서 hpp로 바뀌었다  
    2. ROS에서는 최종 메세지 타입을 대문자로 시작을 하는 대문자 camel 형식이다  
    3. **ROS2**에서는 snake 방식으로 바뀌었다. 그리고 중간에 필요하면 _ (언더스코어)가 들어가진다.  

<br/>

## ROS2에서 include 방식
먼저 ROS2를 기준으로 보면 cmd_vel 토픽의 타입인 Twist를 사용할 때  
camel 방식이 아닌 그냥 소문자이다.
```cpp
#include "geometry_msgs/msg/twist.hpp"
```

대신 2개의 단어로 이루어지는 경우에는 예를 들어서  
2D laser sensor를 사용할 때의 타입을 인쿠르드 할 때는 snake 방식을 사용해서  
laser_scan이 된다.  
```cpp
#include "sensor_msgs/msg/laser_scan.hpp"
```

<br/>

## 다른 코드내에서 사용법
이제 실제 코드에서는 또 다르게 쓰인다. 띠로리~  
ROS2도 ROS와 마찬가지로 코드내에서 메세지 타입을 정의할 때는 다시 카멜(대문자) 방식으로 돌아간다  

선언을 할 때  예)
```cpp
rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr cmd_vel_pub;
rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr laser_sub;
```

위 처럼 인쿠루드만 할 때와는 다르게 다시 카멜 방식이 쓰였다. 

> 아놔 헤깔리게;;; 😤 

<br/>

## 어쨋든 마무리를...   
ROS2에서는 위의 Twsit를 예를 들면 이라고 하면 

/opt/ros/foxy/share/sensor_msgs/msg 디렉토리안에   
LaserScan.msg 파일이 있고

그래서 실제로 코드에서 정의할 떄에도 
```
sensor_msgs/msg/LaserScan -----> sensor_msgs::msg::LaserScan
```

어느 정도 서로 통하는게 있다고 생각된다. 파일명도 카멜 케이스로 되어 있다  

> 물론 예외는 있지만, include 를 하는 부분에서는 snake방식

그 밖에 ROS나 ROS2에서는 클래스 이름은 Camel 방식을 사용하는 것 같고  
그 외에 변수이름 함수 이름등은 snake 방식을 사용하는 것 같다.   
스네이크 방식이 엄청 많이 사용되는 것 같다.   

물론 여러 환경과 사용하는 언어 따라 다 다르게 사용이 되겠지만  
정말 유용하게 사용할 수 있는 방식인 듯 하다.

<br/>

## 마지막으로 네이밍 컨벤션 a Naming Convention
네이밍 컨벤션은 이름을 짓는 방법이라고 해야할까?  
변수, 타입, 함수, 클래스 등등의 이름을 만드는 방식 또는 규칙 정도  

어느정도 서로 이름 짓는 방식을 약속을 해서, 규칙을 정해서  
프로그램이 잘 돌아갈 수 있게 된다. 그래서 소스코드를 읽고 이해하는데 도움이 된다고 한다

그리고 어떤 관계를 나타날 때에도 사용이 될 수도 있다고 한다  

특정 언어나 팀 별로 서로 사용하는 것이 다를 수 있다고 한다  

이제 예를 들면 s가 붙은 복수형 변수를 loop를 돌릴 때에는 그것을 하나씩 받아올 떄는  
단수형 변수로 쓴다던가?  
그래서 변수를 보았을 때 '이것은 배열 같은 것 이겠네' 하고 쉽게 알아 볼 수 있다던지..(?)

```cpp
    std::vector<std::string> animals {"tiger", "lion", "cat", "dog"};
    for (auto animal : animals) {
        std::cout << animal << " ";
    }
```

또는 클래스를 만들 때에는 대문자 카멜 케이스로 한다던가?  
```cpp
class ImgSubscriber : public rclcpp::Node {
//....
}
```

또.. 상수 같은 것은 대문자로 사용한다던가?  

> 물론 초짜 이므로 맞는 예인지는 모르겠다 ㅋㅋㅋ 😝😝 그냥 참고만..


암튼.. 끝
