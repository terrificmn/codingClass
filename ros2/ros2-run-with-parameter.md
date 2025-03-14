# ros2 run 
ros2 run 으로 열때 yaml 파일등 같이 열어주는 옵션

## 파라미터 파일(yaml) 열기  
`--params-file file-to-path.yaml`

예
```
ros2 run my_pkg my_node --params-file ~/colcon_ws/src/my_pkg/config.yaml
```

## 파라미터 직접 설정
`--ros-args`   
parameter 직접 설정 `-p` 옵션으로 설정할 수 있음 
예
```
ros2 run my_pkg my_node --ros-args -p my_param:=my_param_value -p another_int_param:=10
```

## yaml 파일로 파마리터 만들기
일단 기본 형식은 아래..

```yaml
parameter_blackboard:
    ros__parameters:
        some_int: 42
        a_string: "Hello world"
        some_lists:
            some_integers: [1, 2, 3, 4]
            some_doubles : [3.14, 2.718]
```
parameter_blackboard 는 c++로 declare_parameter(s) 로 해서 사용하게 되는데     
c++ 에서 rclcpp::Node::SharedPtr 등으로 통해서 declare_parameter() 로 사용  
> ros__parameters: 는 그대로 사용하는 듯

[여기 github참고](https://github.com/ros2/rcl/tree/foxy/rcl_yaml_param_parser)


## --prefix 옵션
`--prefix` ros2 run 으로 실행하기 전에 실행하는 프로그램을 실행할 수가 있음 .  

예:
```
ros2 run --prefix 'gdbserver localhost:3000' my_pkg my_node
```
