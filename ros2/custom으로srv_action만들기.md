cumtom으로 사용할 msg, srv, action등을 만들고 싶다면  직접 만들어 볼 수 있다

먼저 자신의 worksapce 또는 작업할 workspace로 이동해서 패키지를 만들어준다

```
cd ~/my_ws/src
ros2 pkg create --build-type ament_cmake custom_interfaces --dependencies rclcpp
```
custom_interfaces 패키지가 만들어진다


이제 여기에서 만들고 싶은 msg, srv, action 등을 직접 만들어 준다

먼저 디렉토리로 만들어서 준다.
```
cd ~/my_ws/src/custom_interfaces
mkdir action
```

또는 nautilus 프로그램을 이용하거나 vscode등의 에디터에서 쉽게 만들어 준다

[사진 넣기 -편집필요함]

위와 같은 구조가 되게 된다.

그리고 나서 해당 디렉토리를 들어가서 원하는 파일을 만들어 주면 된다
디렉토리와 파일의 확장자는 동일하게 된다

예: srv디렉토리의 example.srv 

파일을 만들고 싶은 형태로 만들어준다~
변수 선언하듯이 적어주게 된다.

예를 들어 srv 파일이라면
```
uint32 time_duration
float64 angular_vel_z
float64 linear_vel_x
---
bool success
```

예를 들어서 action 파일이라면
```
int32 order
---
int32[] sequence
---
int32[] partial_sequence
```
이런식으로 만들어 주게 된다.

<br/>

## CMakeLists.txt 파일 수정
CMakeLists.txt 파일을 열어준다

여기에서 find_package()부분에 rosidl_default_generators 를 추가해준다
```
find_package(rosidl_default_generators REQUIRED)
```

그리고 바로 아래줄에 추가
```c
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/example.msg"
  "srv/test_srv.srv"
  "action/test_action.action"
)
```

사용할 파일들의 경로를 넣어준다



<br/>

## package.xml 수정하기
이번에는 package.xml을 열어서 
```xml
<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime</exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>
```
처럼 넣어준다

<br/>

## colcon빌드
colcon 빌드를 해준다
```
cd ~/my_ws
colcon build --symlink-install
```


<br/>

그리고 다른 예: A라는 패키지에서 custom_interfaces로 만든 msg, srv, action등의 파일을 사용하려고 하면
그 A라는 패키지의 package.xml 파일에 추가를 해준다
```xml
<exec_depend>custom_interfaces</exec_depend>
```

