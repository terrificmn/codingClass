# ros service std_msgs
ros service 를 기존 ros에서 있는 msg 타입을 사용해서 리턴을 하려고 하는 경우   

일반 서비스 콜백에서는 **bool** 로 응답을 해줘야하고, response 부분에 std_msgs 등을 이용해서 값을 넣어주면 된다. 
즉, 응답 자체를 std::string 정도를 하고 싶은데, callback에서는 bool로 true/false로 처리를 해주고  
그 전에 response에 string 값을 넣어주면 된다. 

예 서비스 type (MyService)
```
bool request_variable
---
std_msgs/String response_result
```

이때 srv 를 포함한 패키지에서 std_msgs를 포함할 수 있게 package.xml 파일에 build_depend 등을 추가해준다   
```xml
    <build_depend>std_msgs</build_depend>
    <exec_depend>std_msgs</exec_depend>
```

물론 CMakeLists.txt 파일에서도 find_package 부분에 std_msgs를 추가해준다. 
예:  
```c
find_package(catkin REQUIRED COMPONENTS
    std_msgs message_generation
)

add_service_files(
    FILES
    MyService.srv
)
```

이제 cpp 파일에서 service 만드는 것은 거의 같다.  콜백 함수 부분만 본다고 하면..   

```cpp
bool MyServiceClass::serviceCallBack(my_srv::MyService::Request &req, my_srv::MyService::Response &res) {
    if(req.request_variable) {
        res.response_result.data = "hello";
    }

    return true;
}
```

> std::string 자체를 콜백에서 리턴할 수는 없는것 같다...


