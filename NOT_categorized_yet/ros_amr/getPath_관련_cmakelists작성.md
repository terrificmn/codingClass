이런 에러 

 undefined reference to `ros::package::getPath(std::__cxx11::basic_string<char, std::char_traits<char>, std::allocator<char> > const&)'


CMakelists.txt 에 추가
```
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  roslib
)

add_executable(main ./src/main.cpp)
target_link_libraries(main ${catkin_LIBRARIES})
```

package.xml에는 추가를 일단은 안해도 된다 

그리고 사용은 cpp
```cpp
#include <ros/package.h>
```


```cpp
std::string pkg_path = ros::package::getPath("package_name"); //패키지명 넣어준다
std::string file_path = pkg_path + "/path/file_name"; //경로와 파일명
```
