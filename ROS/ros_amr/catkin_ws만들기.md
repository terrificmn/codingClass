먼저 소스를 해준 다음에
source /opt/ros/noetic/setup.bash


catkin workspace를 만들기. 수동으로 터미널에서 직접 만들어준다
```
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
```

그리고 catkin_make 명령어를 치면 간단하게 워크스페이스가 만들어진다
```
$ catkin_make
```

catkin_ws를 들어가보면 build devel 디렉토리가 생겼다

