# getenv 환경 변수 받아오기

사용 예, 일반적으로 PATH 환경 변수 내용 받아오기 
```cpp
std::string path = std::getenv("PATH");
ROS_INFO("env path: %s", path.c_str());   // ros경우 
std::cout << "env path: " << path << std::endl;
```

cpp에서는 그냥 getenv()로 받아와서 사용하면 되고,   
ros같은 경우에는 런치파일에서도 env로 만들 수 있어서 그 값을 받아올 수도 있다 