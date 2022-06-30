# qos 적용하기
역시 이런 것을 디버깅 하는것이 어려운 것 중에 하나 인 것 같다.   
컴파일을 할 때에도 에러가 없고 실행자체에도 오류가 안나고  
데이터가 전혀 안나오니깐 문제를 인식하는데도 꽤 걸렸다 ㅠㅠ

qos가 뭔지도 모르고 계속 검색이 꼬리에 꼬리를 물면서 여기 까지 온 것 같다.  

여태껏 subscribe노드를 만들면서 파라미터가 메시지, topic명, 큐 정도였는데   
예를 들면  
```cpp
create_subscription<nav_msgs::msg::Odometry>(
    "/odom", 10, ...생략);
```
여기 큐에 해당하는 곳에 qos와 관련이 있었다. 

다행히 어떤 사람이 github에 질문한 내용을 찾았는데 LaserScan 대한 것을 아니였으나   
그래도 나와 비슷한 케이스에 대한 질문에 답변을 해주는 이가 이렇게 말했다

> It seems that there it some kind of QoS misunderstanding.

나를 말하는 줄 알았다 ㅋㅋㅋ 나도 잘 이해를 못하고 ㅋㅋㅋ ㅜㅜ  
QoS에 대해서 더 공부를 해야겠다. ROS1과 ROS2에서 통신이 잘 되게 해주는 것이라는데  

QoS: Quality of Service 이다.  
publish하는 쪽과 subscribe를 받는 쪽이 서로 호환이 되어야 한다고 한다.    

일단 Ros1에서는 tcp만 지원을 했고~ ROS2에서는 tcp/udp를 지원한다고 하는데  
ROS2의 reliability policy에는 UDPROS를 "best effort"로 사용한다고 해서  
ROS1은 TCPROS(기본설정)를 사용 "reliable"를 사용한다고 한다.  

[ROS2 Document 중 QoS](https://docs.ros.org/en/rolling/Concepts/About-Quality-of-Service-Settings.html)


<br/>

## qos 상태 확인하기
먼저 /scan 데이터가 퍼블리쉬가 되고 있는 상태에서 (터블봇3 가동 시켜주고)

CLI 로 topic에 대한 정보를 보자 -v 옵션을 넣어준다
```
ros2 topic info /scan -v
```

그러면 아래처럼 나오는데 
```
Type: sensor_msgs/msg/LaserScan

Publisher count: 1

Node name: ld08_driver
Node namespace: /
Topic type: sensor_msgs/msg/LaserScan
Endpoint type: PUBLISHER
GID: 01.0f.02.0a.81.04.00.00.01.00.00.00.00.00.12.03.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds
```

QoS Profile을 알 수가 있는데  
Reliability: RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT 이 부분을 일단 주목해서 볼 수가 있는데

이번에는 subsribe 받는 곳까지 확인해보자~ 그래서 서로 맞는지 확인해봐야하는 듯하다  

내가 짠 코드, /scan 토픽을 구독하고 있는 노드를 실행을 한 뒤에

다시 topic info 위의 명령어를 쳐보면 퍼블리셔와 서브크라이버가 각 1씩 나오는 것을 알 수 있다
```
Type: sensor_msgs/msg/LaserScan

Publisher count: 1

Node name: ld08_driver
Node namespace: /
Topic type: sensor_msgs/msg/LaserScan
Endpoint type: PUBLISHER
GID: 01.0f.02.0a.81.04.00.00.01.00.00.00.00.00.12.03.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

Subscription count: 1

Node name: maze_action_server
Node namespace: /
Topic type: sensor_msgs/msg/LaserScan
Endpoint type: SUBSCRIPTION
GID: 01.0f.50.0a.8b.32.6b.72.01.00.00.00.00.00.12.04.00.00.00.00.00.00.00.00
QoS profile:
  Reliability: RMW_QOS_POLICY_RELIABILITY_RELIABLE
  Durability: RMW_QOS_POLICY_DURABILITY_VOLATILE
  Lifespan: 2147483651294967295 nanoseconds
  Deadline: 2147483651294967295 nanoseconds
  Liveliness: RMW_QOS_POLICY_LIVELINESS_AUTOMATIC
  Liveliness lease duration: 2147483651294967295 nanoseconds

```
각각 퍼블리셔와 서브스크라이브 각각 1 나온다

내 action_server 에서 구독을 하고 있는데 여기를 좀 더 잘 살펴보면   
QoS profile 중에서 Reliability가 그냥 **RMW_QOS_POLICY_RELIABILITY_RELIABLE** 인것에 반해   
터틀봇3의 Publisher가 **RMW_QOS_POLICY_RELIABILITY_BEST_EFFORT** 베스트 에포트로 되어있다

그래서 이거에 맞춰서  
rclcpp 로 create_subscription을 할 때에 best effort subscriber가 될 수 있게 해줘야하는데
다행히도 어렵지 않게 가능했다

[github demo 데모 페이지 확인하기](https://github.com/ros2/demos/blob/master/demo_nodes_cpp/src/topics/listener_best_effort.cpp)

create_subscription<.....>(); 사용할 때에   
rclcpp::SensorDataQoS() 를 사용해주면 된다.

기존 코드를
```cpp
laser_sub = this->create_subscription<sensor_msgs::msg::LaserScan>(
            "/scan", 10, std::bind(&MazeActionServer::laser_sub_cb, this, _1));
```

아래 처럼 고쳐준다
```cpp
laser_sub = this->create_subscription<sensor_msgs::msg::LaserScan>(
            "/scan", rclcpp::SensorDataQoS(), std::bind(&MazeActionServer::laser_sub_cb, this, _1));
```

이제 다시 빌드를 한 다음에 다시 실행을 해보니  
드디어 LaserScan 데이터를 잘 받아온다~ 아자! 👍👍👍 


### 다른 방법으로는 
아래 코드 처럼도 가능하다
```cpp
auto default_qos = rclcpp::QoS(rclcpp::SystemDefaultsQoS());
subscription_ = this->create_subscription(
                "laser_scan", default_qos,
                std::bind(&MazeActionServer::laser_sub_cb, this, _1));
```

<br/>

## 파이썬에서 QoS 설정

파이썬은 QoS 를 이용해서 하는 예제 코드가 있어서 가져왔다

```py
from rclpy.qos import qos_profile_sensor_data, QoSProfile
from sensor_msgs.msg import LaserScan
import rclpy

def chatter_callback(msg):
    print(msg)

def main():
    rclpy.init()
    qos = QoSProfile(depth=10)
    node = rclpy.create_node('scan_listener')
    sub = node.create_subscription(LaserScan,
                                    'scan',
                                    chatter_callback,
                                    qos_profile=qos_profile_sensor_data)
    try:
        while True:
            rclpy.spin_once(node)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    print('Starting scan listener')
    main()
    print('done.')        
```
혹시 python 코드라면 위의 코드를 참고하자  


