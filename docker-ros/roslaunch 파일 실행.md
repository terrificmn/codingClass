ros  | Aborted (core dumped)
ros  | [gazebo-2] process has died [pid 86, exit code 134, cmd /opt/ros/melodic/lib/gazebo_ros/gzserver -e ode /home/docker_melodic/docker_ws/src/turtlebot3_simulations/turtlebot3_gazebo/worlds/turtlebot3_house.world __name:=gazebo __log:=/home/docker_melodic/.ros/log/121e0a88-b8cc-11ed-a793-0242ac120002/gazebo-2.log].
ros  | log file: /home/docker_melodic/.ros/log/121e0a88-b8cc-11ed-a793-0242ac120002/gazebo-2*.log
ros  | Aborted (core dumped)
ros  | the rosdep view is empty: call 'sudo rosdep init' and 'rosdep update'
ros  | [gazebo_gui-3] process has died [pid 96, exit code 134, cmd /opt/ros/melodic/lib/gazebo_ros/gzclient __name:=gazebo_gui __log:=/home/docker_melodic/.ros/log/121e0a88-b8cc-11ed-a793-0242ac120002/gazebo_gui-3.log].




먼저 docker-compose.yml 에서 noetic 버전에서는 command - roscore 가 가능하다   
melodic 버전에서는 에러가 발생하므로 빼고 사용  

Dockerfile, docker-compose.yml에서 roslaunch 파일을 실행하려고 했지만 잘 안됨  

일단 docker exec -it 모드로 터미널 모드로 들어가게 되면  
.bashrc 파일을 잘 만들었기 때문에 터미널이 열리면서 bashrc가 실행되서 roslaunch 등의 명령어를 인식하는데   

Dockerfile 등에서 CMD 로 넣게 되면 bashrc가 실행이 안되었기 때문에 명령어를 인식하지 못함  

> 그래서 setup.bash 등을 실행하려고 했지만 다 실패;;



## sh 스크립트를 만들어서 복사를 해서 쉘 스크립트 실행
먼저 sh스크립트를 만든다  

```
#!/bin/bash
source "/opt/ros/melodic/setup.bash"
source "/home/docker_melodic/docker_ws/devel/setup.bash"
## docker-compose.yml 에서 이미 bashrc를 만들기 때문에 container에 exec 로 직접 실행하게 되면
## 무리없이 작동하나 ENTRY_POINT로 지정할 때에는 다시 한번 setup.bash를 읽어 들어야 한다
## container 안에서 확인하면 이미 source 처리가 되어 있으나,
## source "/home/docker_melodic/.bashrc" 처럼 하나만으로 실행하려고 하면 roslaunch 명령 자체를 인식 못함
export TURTLEBOT3_MODEL=waffle
# roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch ## 런치파일 자체는 실행되는 것 확인
roslaunch turtlebot3_gazebo turtlebot3_house.launch ## rosdep 문제 발생
```
아래에서 다시 설명


그리고 이 파일을 Dockerfile 에서 COPY를 시킨다  
```
COPY ./ros_entrypoint.sh ./
```

현재 host컴의 docker파일이 있는 위치에서 컨테이너의 현재 위치에 복사

> 아 현재 디렉토리를 지정하려면 WORKDIR로 지정하면 된다   
> `WORKDIR /home/user명`  예를 들면...


그리고 권한이 필요하다  sh 스크립트이므로 실행권한이 있어야 하는데 root 권한으로 줘야하는데 이게 잘 안됨   

그래서 어차피 host 컴과 공유를 하기 때문에 host쪽에서 권한을 실행 권한을 준다.  
즉, Dockerfile등에 안하고 직접 터미널 열어서 해당파일 권한을 +x 시켜준다 
```
sudo chmod +x ./ros_entrypoint.sh
```


> 원래는 이렇게 Dockerfile 안에 `RUN chmod +x /ros_entrypoint.sh` 처럼 줘야하는데 권한 때문에 실행을 못하게 됨
> 아마도 user를 만들어서 사용해서 그럴지도 모르겠음   

그리고 ENTRYPOINT를 지정해준다. 마찬가지로 container안의 ./ 즉 현재 디렉토리로 했으므로  
```
ENTRYPOINT ["./ros_entrypoint.sh"]
```


이 sh스크립트에서는 source로 각 setup.bash 파일을 해줘야한다   
.bashrc 파일이 만들어져 있으므로 .bashrc 파일만 source 해줬더니 실행이 안된다.  
분명히 Dockerfile에서 RUN으로 만들어서 파일도 있으나 (확인) .bashrc만 실행할 경우에는   
roslaunch 명령어를 인식하지 못한다. 즉, /opt/ros/로스버전/setup.bash 가 필요하다


## docker build & up
이제 docker를 build 한 후에 docker-compose 혹은 docker compose up을 해주면  
런치파일이 실행된다   



필요하다면 shell script에 추가 (해보지는 않음)
```
export ROS_MASTER_URI=http://$(hostname --ip-address):11311  
export ROS_HOSTNAME=$(hostname --ip-address)
```