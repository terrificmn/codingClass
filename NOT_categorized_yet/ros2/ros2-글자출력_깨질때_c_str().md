direction_str_vec 이 vector string 일 때 그냥 출력을 하면 글자가 깨진다

```cpp
std::vector<std::string> direction_str_vec = {"Up", "Right", "Down", "Left"};
RCLCPP_INFO(this->get_logger(), "Turning  %s ", direction_str_vec[val];
```

```
[INFO] [1650916618.849497323] [maze_action_server]: Turning  �Z���U 
```
이런식으로..

그래서 뒤에다 c_str()함수를 써주면 잘 나온다
```cpp
RCLCPP_INFO(this->get_logger(), "Turning  %s ", direction_str_vec[val].c_str());
```

또는  
이럴때는 cout을 사용해도 잘 표시가 된다
```cpp
std::cout << direction_str_vec[val] << std::endl;
```


