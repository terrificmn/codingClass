# colcon build 시에 Clock skew detected 라는 warning이 나올 때

colcon build를 해서 컴파일을 할 때 아래와 같은 워닝이 나오고 빌드가 안될 수도 있다고 나온다
```
--- stderr: maze_turtlebot3                                
make[2]: Warning: File '/home/sgtubun/colcon_ws/src/maze_turtlebot3/src/maze_client_turtlebot.cpp' has modification time 18020 s in the future
make[2]: Warning: File '/home/sgtubun/colcon_ws/src/maze_turtlebot3/src/maze_server_turtlebot.cpp' has modification time 29204 s in the future
make[2]: warning:  Clock skew detected.  Your build may be incomplete.
make[2]: warning:  Clock skew detected.  Your build may be incomplete.
```

먼저 위의 메시지대로 해당 위치를 가서 보면
```
cd ~/colcon_ws/src/maze_turtlebot3/src/
sgtubun@sgtubun:~/colcon_ws/src/maze_turtlebot3/src$ ls -l
total 32
-rw-r--r-- 1 sgtubun sgtubun 10213 May 18  2022 maze_client_turtlebot.cpp
-rw-r--r-- 1 sgtubun sgtubun 17716 May 18  2022 maze_server_turtlebot.cpp
```
시간이 이상하게 되어 있다. 직접 usb로 카피해서 옮겼더니 이런 현상이 발생한 듯 하다1
(아마도 년도만 표시한 것 같은데?...)

이때에는 touch명령어를 사용해보자
```
$ touch ./*
```

이제 확인을 해보면 
```
$ ls -l
total 32
-rw-r--r-- 1 sgtubun sgtubun 10213 May 18 11:51 maze_client_turtlebot.cpp
-rw-r--r-- 1 sgtubun sgtubun 17716 May 18 11:51 maze_server_turtlebot.cpp
```

시간이 정상적으로 표시되는것을 알 수 있다

다시 colcon build 하면

에러 없이 packages들이 빌드 된 것을 알 수 있다.
```
Summary: 3 packages finished [17.4s]
```