# ros2 custom msg srv

ros와 비슷하면서 조금 다른 부분이 있다. 


msg, srv 디렉토리를 각 프로젝트 root 이하에 만들어 준다.

프로젝트가 tutorial_interfaces 만들고 
```
ros2 pkg create --build-type ament_cmake --license Apache-2.0 tutorial_interfaces
```

cd tutorial_interfaces
mkdir msg srv

msg 만드는 부분을 상당히 비슷하다.

예
Num.msg
```
int64 num
```

srv 예   
AddThreeInts.srv
```
int64 a
int64 b
int64 c
---
int64 sum
```

### CMakeLists
이제 CMakeLists.txt 파일에 find_package 를 해줘야하는데   
rosidl_default_generators 이다.  

> ros 의 message_generation 정도 되겠다   

만약 커스텀 메세지에서 다른 메세지를 사용한다면 find_package 및 DEPENDENCIES 를 넣어줘야 한다.   

그리고 메시지 파일 등록도 해준다. 

```
# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Num.msg"
  "msg/Sphere.msg"
  "srv/AddThreeInts.srv"
  DEPENDENCIES geometry_msgs
)
```

> install 은 필요 없다. 

### package.xml
의존성 메세지를 depend 로 넣어주고, rosidl_default_generators 등을 buildtool_depend 에 넣어준다.   
member_of_group 이라는 것도 추가

```xml

  <depend>geometry_msgs</depend>
  <buildtool_depend>ament_cmake</buildtool_depend>
  <buildtool_depend>rosidl_default_generators</buildtool_depend>
  <exec_depend>rosidl_default_runtime</exec_depend>
  <member_of_group>rosidl_interface_packages</member_of_group>
```

이제 빌드를 해주면 만들어 진다.

```
colcon build --packages-select tutorial_interfaces
```


### 이제 커스텀 메세지를 사용하기

cpp 파일에서  publisher, subscriber, topic 등에 타입정의를 해당 메세지로 해주면 된다 
```cpp
#include "tutorial_interfaces/msg/num.hpp"

class 생성자에서 {
    publisher_ = this->create_publisher<tutorial_interfaces::msg::Num>("topic", 10); // Node 에 있는 create_publsher 함수
}  rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr publisher_;
/// 콜백함수에서 
void timer_callback() {
    auto message = tutorial_interfaces::msg::Num();
}

rclcpp::Publisher<tutorial_interfaces::msg::Num>::SharedPtr publisher_;
```

위에 같은 방식으로 사용   


커스텀 메세지를 사용하는 패키지에서의 CMakeLists.txt 에 
```
find_package(tutorial_interfaces REQUIRED)
```
정도만 넣어주고 나머지는 add_executalbe() 소스파일 등록해서 사용


package.xml 에는 
```
  <depend>tutorial_interfaces</depend>
```
정도만 해주면 된다. 


## 자세한 것은 ros2 tutorial
메뉴얼 페이지를 확인하거나 

pubsub_customs_msg 패키지, tutorial_interfaces 패키지를 직접 보고 확인


