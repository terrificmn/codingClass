# ros2 패키지만 지운 후에 WARNING 관련

```
[0.360s] WARNING:colcon.colcon_ros.prefix_path.ament:The path ‘/home/user/ros2_ws/install/py_prac in the environment variable AMENT_PREFIX_PATH
doesn’t exist
[0.361s] WARNING:colcon.colcon_ros.prefix_path.catkin:The path ‘/home/user/ros2_ws/install/py_prac in the environment variable CMAKE_PREFIX_PAT
H doesn’t exist
```

ros2의 워크스페이스에서 패키지를 지웠으나 install 디렉토리에는 관련 파일이 남아있어서 warning이 뜨는 경우

간단하게.. 그냥 build/ install/ log 를 지워주면 된다. 그리고 나서 다시 colcon build 해주면 됨

전체를 다 날리는 게 아니라면 특정 패키지만 지우는 상황이라면

특정 패키지만 지워주면 된다

py_prac 이라는 패키지를 지우려고 하면

```
cd ~/my_ws/build
rm -rf py_prac
```

install 디렉토리의 패키지 지우기
```
cd ~/my_ws/install
rm -rf py_prac
```


