# ROS2 파라미터 만들기 c++ cpp
파라미터 노드를 만들어 보자

먼저 워크스테이션으로 이동 현재 my_ws로 되어 있으므로 
```
cd ~/my_ws/src
```
이동

패키지를 만들어보자
```
ros2 pkg create --build-type ament_cmake cpp_parameters --dependencies rclcpp
```

해당디렉토리를 보면 파일들이 생성이 되었고

(옵션사항들)
package.xml 의 maiatainer에 이름과 이메일등으로 등록해주고, 
license 는 Apache License 2.0 으로 하기 

<br/>

## C++ node를 만들기
cpp_parameters 패키지 디렉토리에 src 디렉토리를 만들고 
cpp_parameters_node.cpp 파일을 만들고 복사 붙여넣기

```cpp
#include <rclcpp/rclcpp.hpp>
#include <chrono>
#include <string>
#include <functional>

using namespace std::chrono_literals;

class ParametersClass: public rclcpp::Node
{
  public:
    ParametersClass()
      : Node("parameter_node")
    {
      this->declare_parameter<std::string>("my_parameter", "world");
      timer_ = this->create_wall_timer(
      1000ms, std::bind(&ParametersClass::respond, this));
    }
    void respond()
    {
      this->get_parameter("my_parameter", parameter_string_);
      RCLCPP_INFO(this->get_logger(), "Hello %s", parameter_string_.c_str());
    }
  private:
    std::string parameter_string_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char** argv)
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<ParametersClass>());
  rclcpp::shutdown();
  return 0;
}
```
이제 파라미터 노드를 하나 만들었다

위의 코드에서 파라미터를 만들어주는데, 이름은 my_parameter, 기본 값은 world 가 된다   
1초마다 타이머를 작동시키며 respond 콜백 함수를 호출하게 됨
```cpp
    this->declare_parameter<std::string>("my_parameter", "world");
    timer_ = this->create_wall_timer(1000ms, 
                std::bind(&ParametersClass::respond, this));
```

콜백함수 respond()부분에서는 get_parameter()로 "my_parameter" 를 parameter_string_ 변수로  
지정을 해줘서 파라미터를 받아 올 수 있게 하고, 기본값은 이미 파라미터를 만들때 설정한  
world 라는 문자열이 되게 되고, 추후 파라미터를 바꾸는 명령어를 통하면   
parameter_string_ 이 그 값을 받게 되는 것

<br/>

## 빌드하기
CmakeLists.txt 파일을 열어서 기존의 find_package(rclcpp REQUIRED) 다음 줄에 붙여넣어준다  
```c
add_executable(parameter_node src/cpp_parameters_node.cpp)
ament_target_dependencies(parameter_node rclcpp)

install(TARGETS
  parameter_node
  DESTINATION lib/${PROJECT_NAME}
)
```
저장을 하고 워크스테이션으로 이동

```
cd ~/my_ws
```
빌드
```
colcon build --packages-select cpp_parameters
```

setup 파일을 source 실행시킨다음에 
```
. install/setup.bash
```

<br/>

## 실행
```
ros2 run cpp_parameters parameter_node
```

이제 실행결과가 아래처럼 나온다
```
[INFO] [1651628713.631531311] [Parameter_node]: Hello world
[INFO] [1651628714.631502640] [Parameter_node]: Hello world
[INFO] [1651628715.631456525] [Parameter_node]: Hello world
```

<br/>

## 파라미터 변경 명령
이제 노드가 실행된 상태에서 파라미터를 조회하는데   
다른 터미널을 열어서 
```
ros2 param list
```

결과는
```
/parameter_node:
  my_parameter
  use_sim_time
```

노드명은 class를 만들때의 노드 이름이고  
그리고 그 아래 나오는 것이 파라미터명이 된다. parameter_node

param set 명령어로 변경을 할 수가 있는데   
명령어의 형식은 아래 처럼 입력한다  
ros2 param set [노드명] [파라미터명] [변경값]

```
ros2 param set /parameter_node my_parameter friend
```
Set parameter successful 으로 나오며

parameter_node를 실행시켰던 터미널에서는 내용이 변경된 것을 알 수 있다

<img src=0>


<br/>

## 런치파일 만들기 -파라미터 설정하기
런치파일을 작성하고 런치파일을 실행하면서 자동적으로 파라미터를 설정해서 실행이 가능해진다

다시 cpp_parameters 패키지로 이동을 한 후에 launch 라는 디렉토리를 만들어 준다
```
cd ~/my_ws/src/cpp_parameters
mkdir launch
```
또는 편한 에디터를 통해서 만들어준다

아래내용으로 런치파일 저장 cpp_parameters_launch.py 로 저장
```py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="cpp_parameters",
            executable="parameter_node",
            name="custom_parameter_node",
            output="screen",
            emulate_tty=True,
            parameters=[
                {"my_parameter": "Gandalf"}
            ]
        )
    ])
```

executable은 ros2 run으로 실행하는 노드명이 된다. 즉, CMakeLists.txt 에서 지정해놓은 노드명이다   
output, emulate_tty 의 screen과 True 값은 터미널 콘솔화면에서 출력을 볼 수 있게 해준다

이제 parameters=[ {"파라미터명": "바꿀내용"} ]   
이 부분만 지정을 해주면 된다.

이제 다시 CMakeLists.txt 파일을 열어 런치파일을 인식할 수 있게 추가 해준다.  
아래 내용을 넣어주자~
```
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)
```

> 이제 빌드를 하면 launch 디렉토리를 복사해서 install 디렉토리에   
해당패키지 안에 share 디렉토리에 설치하게 된다   

이제 저장 후 다시 워크스테이션로 이동한다
```
cd ~/my_ws
```

빌드를 해주자
```
colcon build --packages-select cpp_parameters
```

```
. install/setup.bash
```

<br/>

## 런치파일 실행
이제 런치파일에서 설정한 파라미터 값이 런치파일을 실행했을 때 잘 변경되어서 나오는지   
확인할 수 있다~ 아래줄 실행
```
ros2 launch cpp_parameters cpp_parameters_launch.py
```

결과는 아래처럼 나오게 된다

<img src=1>

끝
