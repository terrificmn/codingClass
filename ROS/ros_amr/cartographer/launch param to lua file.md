# launch parameter to lua

ros launch 파일에서 env 로 지정을 해준다 
```xml
<env name="robot_name_launch" value="robot_amr1" />
```

이제 lua 파일에서 os.getenv() 를 통해서 파라미터 이름으로 받을 수가 있다  
```lua
robot_name = os.getenv("robot_name_launch")
```

카토그래퍼의 node_options.cpp , trajectory_options.cpp 등에서   
lua_parameter_dictionry 를 통해서 값을 받아올 수가 있는데  
먼저 h 파일에 변수를 하나 만들어주고 그 변수에 넣어주면 된다. 

trajectory_topins.h 또는 node_options.h
```cpp
생략...
struct TrajectoryOptions {
  ::cartographer::mapping::proto::TrajectoryBuilderOptions
      trajectory_builder_options;
 
 std::string robot_name = false;
    생략...
 }
```

이제 cpp 파일에서 
```cpp
options = {
    ... 생략..
 options.namespace_str = lua_parameter_dictionary->GetString("robot_name");

... 생략..
}
```

이런식으로 받아올 수가 있다. 단 문제가 있다면, GetString(), GetInt(), GetBool() 등으로 lua 파일에서 받아올 수가 있지만   
위의 함수 호출하면서 딕셔너리로 추가가 되는 형태인듯 하다. (정확하지 않다.)   
중요한 것은 한 lua파일의 파라미터는 한번만 콜이 되어야 한다. 여러번 콜을 하면 컴파일은 문제가 없지만   
프로그램 작동시 **치명적으로 프로그램이 종료**되게 된다


### 추가로 런치파일에서 받는 다른 예제 
```xml
<env name="MY_ROBOT" value="Robert">
```

루아파일에서 if도 가능
```lua
robot_type = os.getenv("MY_ROBOT")

if robot_type == "Robert" then
  options.use_odometry = false
end
```



## trajectory_builder.lua 파일은 어디에?
보통 메인으로 사용하는 lua 파일에 include 되어 있는 
```lua
include "map_builder.lua"
include "trajectory_builder.lua"
```

이 파일들은 어디에 있을까?

먼저 roscd로 카토그래퍼 접근

```
roscd cartographer
```

lua 관련된 파일들은  /configuration_files 에 있다  

즉 워크스페이스/src/cartographer/configuration_files
