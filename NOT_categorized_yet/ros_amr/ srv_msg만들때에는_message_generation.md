srv, msg 만들 때에는 
message_generation 이 포함되어야 한다 

CMakeLists.txt 에     
generate_messages() 도 주석 제거가 되어야 한다 
```
find_package(catkin REQUIRED COMPONENTS
  roscpp message_generation
)

....생략...

add_service_files(
  DIRECTORY srv
  FILES
  gps_picker_srv.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs  # Or other packages containing msgs
)

```

package.xml 에도 추가
```
<build_depend>message_generation</build_depend>

<exec_depend>message_runtime</exec_depend>
```


클래스 관련은 여기 참고 
http://wiki.ros.org/roscpp_tutorials/Tutorials/UsingClassMethodsAsCallbacks


객체를 만들었다면  
AddTwo a;
ros::ServiceServer ss = n.advertiseService("add_two_ints", &AddTwo::add, &a);


클래스 내에서라면  
ss = this->n.advertiseService("add_two_ints", &AddTwo::add, this);