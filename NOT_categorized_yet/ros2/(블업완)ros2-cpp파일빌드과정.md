## 패키지 만들기
c++을 빌드 하기 위해서 패키지를 하나 만들어 준다 

먼저 워크스페이스 디렉토리 아래 src 디렉토리까지 이동 한다  
파이썬과는 다르게 --build-type 이 ament_cmake인 걸 알 수 있다. 의존성 rclcpp도 넣어준다  
```
cd ~/my_ws/src
ros2 pkg create cpp_prac --build-type ament_cmake --dependencies rclcpp
```
이동해보면 cpp_prac 패키지가 만들어진다
```
cd ~/my_ws/src/cpp_prac
```

<br/>


## C++ 코드
cpp_prac 패키지 디렉토리에 가보면 src 디렉토리가 만들어져 있는데 여기에 파일을 하나 생성하는데     
파일명은 simple_opp.cpp 로 만들었다    
```cpp
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
//rclcpp/rclcpp.hpp
//표준 c++ 헤더파일 인크루드, 위의 ROS2 시스템을 사용할 수 있게 해준다
//std_msgs/msg/string.hpp
//빌트인 메세지 타입을 포함해서 publish 하는데 사용한다
//include에 추가를 하게 되면 package.xml 파일에 의존성을 추가해줘야한다 아래에서 살펴보자

// Node 클래스 상속
class Talker : public rclcpp::Node {
private:
// Node를 주기적으로 실행시켜 줄 timer  rclcpp::TimerBase
    rclcpp::TimerBase::SharedPtr m_timer;
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
    size_t m_count;
    size_t count_;

    //콜백함수
    void timer_callback() {
        m_count++;
        auto message = std_msgs::msg::String();
        message.data = "Hello, world! " + std::to_string(count_++);
        
        // log를 남기기
        RCLCPP_INFO(this->get_logger(), "OPP example, count : %d", m_count);

        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());
        //publish하기
        publisher_->publish(message);
    }

public:
    // constructor
    Talker() : Node("simple_opp_node") {
        publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
        // create_wall_timer 함수에 timer와 실행시킬 함수를 전달하면 주기적 실행을 할 수 있음
        // create_wall_timer는 3개의 매개변수를 std::bind를 이용해서 넘겨야 함
        // o.5초
        m_timer = this->create_wall_timer(std::chrono::milliseconds(500), std::bind(&Talker::timer_callback, this));
    }

};

int main(int argc, char* argv[]) {
    rclcpp::init(argc, argv);  //초기화

    rclcpp::spin(std::make_shared<Talker>());
    rclcpp::shutdown();
    return 0;
}
```

<br/>

## package.xml 파일 수정하기 
package.xml 파일을 열어서 아래부분을 넣어준다  
패키지를 만들때 --dependencies를 넣어줬다면 자동으로 만들어짐
```xml
<depend>rclcpp</depend>
<depend>std_msgs</depend>
```
없다면 위처럼 추가해준다   
패키지가 rclcpp와 std_msgs가 필요하다고 선언해주는 것 (코드가 실행될 때)   
앞으로 사용할 코드에서 std_msgs를 필요로 하기 때문에 넣었지만 코드에 필요없다면 빼주면 된다  

> package.xml 파일에서는 패키지 버전, 설명, maintainer의 메일 주소 등을 적어줄 수 있다 

<br/>

## CMakeLists 파일 수정하기
이번에는 CMakeLists.txt를 열어주자

```c
# find dependencies
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
```
를 추가해준다 (필요한 의존성 패키지를 넣어준다)

그리고 바로 아래줄에 추가를 해주는데 실행가능한 파일을 지정해준다   
add_executable을 추가해주자
```c
add_executable(talker src/simple_opp.cpp)
ament_target_dependencies(talker rclcpp std_msgs)
```
talker는 ros2 run으로 실행할 때 실행하는 이름(자동완성)이 되고 
src/cpp파일명을 적는다   
ament_tager_dependencies에는 먼저 노드명을 적어주고 필요한 의존성 적어준다 

마지막으로 ros2 run할 때 실행할 Destination을 알 수 있게 추가해준다  
이거를 해야하지 ros2 명령어를 실행할 때 파일을 맞게 찾는것 같다
```c
install(TARGETS
  talker
  DESTINATION lib/${PROJECT_NAME})
```

정리해보면 아래처럼 된다 
```c
# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(talker src/simple_opp.cpp)
ament_target_dependencies(talker rclcpp std_msgs)

install(TARGETS
  talker
  DESTINATION lib/${PROJECT_NAME})
```
최종적으로 저장을 한다

<br/>

## 빌드하기 
이제 패키지를 빌드를 해보자. (자신의 워크 스페이스로 이동)
```
cd ~/my_ws
colcon build --symlink-install --packages-select cpp_prac
```

source해주기
```
. install/setup.bash
```

<br/>

## 실행
ros2 run 해주는데 이상이 없다면 잘 되었다면 탭을 눌르면 자동완성이 된다  
```
ros2 run cpp_prac talker 
```

잘 출력이 된다
```
[INFO] [1647531376.636813526] [simple_opp_node]: OPP example, count : 1
[INFO] [1647531376.637111417] [simple_opp_node]: Publishing: 'Hello, world! 0'
[INFO] [1647531377.136783016] [simple_opp_node]: OPP example, count : 2
[INFO] [1647531377.136912917] [simple_opp_node]: Publishing: 'Hello, world! 1'
[INFO] [1647531377.636776913] [simple_opp_node]: OPP example, count : 3
```

다른 터미널을 띄운 후에 
```
source /opt/ros/foxy/setup.bash
```

> .bashrc 파일에 넣어뒀다면 안해도 무방

토픽 리스트를 확인해보자
```
ros2 topic list
```
그러면
```
...
/topic
...
```
code에서 publish를 할 때 topic이란 이름으로 만들었으므로 topic명이 /topic으로 나옴   
이제 echo로 받아보자
```
ros2 topic echo /topic
```

그러면 잘 받아지는 것을 봐서 publish가 잘 되고 있는 것을 알 수 있다
```
data: Hello, world! 1
---
data: Hello, world! 2
---
data: Hello, world! 3
```

> 앞서 talker 노드를 실행했을 때 OPP example, count : 1    
이런식으로 나왔던 것은 퍼블리싱된 것이랑 상관없이   
get_logger()를 이용한 메세지 출력이었음을 참고하자


<br/>

## 실행할 노드가 더 많아 진다면? 
새로운 의존성이 더 추가가 되었다면   
package.xml 파일을 열어 depend 태그에 추가해준다   
예를 들어 geometry_msgs 가 필요해서 노드의 코드에 추가했다면 아래 처럼 추가해준다
```xml
  <depend>rclcpp</depend>
  <depend>std_msgs</depend>
  <depend>geometry_msgs</depend>
```

또한 CMakelists.txt 파일도 추가를 해줘야한다  
include에 메세지 타입관련 hpp파일을 더 추가했다면 패키지 dependencies를 추가해줘야한다 

그리고 실행할 cpp파일 노드를 추가할려면 add_executable에 더 추가한다
install (TARGETS ..) 에도 추가한다 

예를 들면 이런식이 된다
```c
# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(talker src/simple_opp.cpp)
ament_target_dependencies(talker rclcpp std_msgs)

add_executable(cmd_vel_pub_node src/cmd_vel_pub.cpp)
ament_target_dependencies(cmd_vel_pub_node rclcpp std_msgs geometry_msgs)

install(TARGETS
  talker
  cmd_vel_pub_node
  DESTINATION lib/${PROJECT_NAME})
```

> 여기 package.xml 와 CMakelists.txt와 의존성을 안추가해주면 빌드할 때 에러가 발생한다   
그리고 ros2 run 을 실행했을 때 노드를 제대로 찾아 실행해주지 못한다  


[참고 유투브-roadbalance-서울G캠프](https://www.youtube.com/watch?v=bj8AoKFmnWg)

[참고 메뉴얼 docs.ros.org](https://docs.ros.org/en/foxy/Tutorials/Writing-A-Simple-Cpp-Publisher-And-Subscriber.html)