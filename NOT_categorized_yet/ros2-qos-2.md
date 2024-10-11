# qos 적용하기

[기존 qos 참고]((블로그업완)ros2-qos.md)   

image_transport::create_camera_publisher() 처럼 image_tarsport를 사용할 경우에는   

rmw_qos_profile_t 타입을 사용해야하는데   rclcpp::SensorDataQoS() 와 일단 형식이 다르다.   

> rmw 는 rclcpp 에 속해있는 것은 아닌 듯 하고, rmw 에 속하는 듯 하다.   

일단 서브스크라이버와 퍼블리셔 간에 qos가 다를 경우 제대로 통신이 안되므로  
맞춰줄 필요가 있다. 

가령 이런 에러가 발생할 수 가 있다. 
on topic '/camera/image', requesting incompatible QoS. No messages will be sent to it.  
Last incompatible policy: RELIABILTY_QOS_POLICY



이미지를 subscriber, publisher 하는 프로그램을 실행 한 후에 
```
ros2 topic info /camera/image_raw -v
```

Node name: web_cam_server
Topic Type: sensor_msgs/msg/Image   
Endpoint tyhpe: SUBSCRIPTION
// 생략
Qos profile:
  Reliability: RELIABLE
  /// 생략

Node name: cam_publisher
Topic Type: sensor_msgs/msg/Image   
Endpoint tyhpe: PUBLISHER
// 생략
Qos profile:
  Reliability: BEST_EFFORT
  /// 생략



```cpp
rmw_qos_profile_t custom_qos_profile = rmw_qos_profile_sensor_data;
cam_pub = image_transport::create_camera_publisher(this, "image_raw", custom_qos_profile);

```

>  헤더 인크루드가 필요할 수도 있다. `#include <rclcpp/qos.hpp>`

`rmw_qos_profile_sensor_data` 는 BEST_EFFORT


```cpp
rmw_qos_profile_t custom_qos_profile = rmw_qos_profile_default;
cam_pub = image_transport::create_camera_publisher(this, "image_raw", custom_qos_profile);

```

`rmw_qos_profile_default` 는 RELIABLE

