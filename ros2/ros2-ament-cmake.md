# ros2 ament cmake colcon
ROS2 패키지는 ament 빌드 시스템을 사용해서 만들고, colcon 빌드 툴을 사용하게 된다. 

CMake 를 사용해서 빌드할 때  

- CMakeLists.txt  빌드 관련 
- package.xml  meta 정보
- inlcude/<package_name>   헤더 파일들, include 안에 패키지 이름으로 다시 한번 만들어진다.   
- src - 소스 디렉토리  

## 패키지 만들기

```
ros2 pkg create --build-type ament_cmake --license Apache-2.0 my_first_pkg --node my_node
```

> --node 옵션을 넣어주면, cpp 파일 까지 만들어주며, CMakeLists.txt 에서도 추가가 된다.   
> --dependencies 옵션을 넣어주면 package.xml, CMakeLists.txt 등에 만들어준다. --dependencies rclcpp


## 빌드

colcon build --packages-select <my_package>   
또는 `colcon build`
```
colcon build --packages-select my_first_pkg   
```

빌드가 완료 되면 source를 해서 overlay를 해준다.

```
. install/setup.bash
```

> . 은 sh 에서 source 같은 기능, '.' 으로 해도 잘 기능한다.

