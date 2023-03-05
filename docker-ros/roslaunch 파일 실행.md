## yaml파일에서 roslaunch
melodic 버전에서는 docker-compose.yml 파일에서 command 설정으로 안 되었던 것 같은데   
noetic 버전에서는 잘된다.

> 아마도 melodic 버전에서는 뭔가 실수가 있었을 수도 있다  

이것도 그것의 차원에서 계속 roslaunch 가 안되서 Dockerfile에서 ENTRYPOINT로 실행을 하면서   
sh script를 실행하게 했는데 $ROS_DISTRO 변수가 실행이 안되서 그런것 이였음

아마도 실제 ROS가 설치가 되어 있는 환경에서 테스트를 하다가 그렇게 된것일 수도 있고... 

방법은 어쨋든 환경 변수를 사용하지 않고 직접 하드코딩해서 하면 될듯 하다 

```
RUN echo 'source /opt/ros/noetic/setup.bash' >> ${HOME}/.bashrc
RUN echo "source ${HOME}/docker_ws/devel/setup.bash" >> ${HOME}/.bashrc
```

#### 장점은 docker-compose.yml command 명령을 적고, 빌드가 필요없다
Dockerfile의 ENTRYPOINT를 사용하게 되면 런치파일 내용이 바뀌게 되면 재 빌드를 해야하는데  
docker-compose 파일을 사용할 경우는 한번 빌드 후에 roslaunch 내용을 바꿀 수 있다

```yml
services:
    ros:
        ..생략...
        command:
            - roslaunch ros_package ros_launch_file
```
> 디버깅 할 때는 command: - roscore 가 편하다



## Dockerfile에서 ENTRYPOINT를 지정하기
~~Dockerfile, docker-compose.yml에서 roslaunch 파일을 실행하려고 했지만 잘 안됨~~

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


> 원래는 이렇게 Dockerfile 안에 `RUN chmod +x /ros_entrypoint.sh` 처럼 줘야하는데   
root권한 때문에 실행이 안된다.    
아마도 user를 만들어서 사용해서 그럴지도 모르겠음   

그래서 COPY명령어를 사용한다. 왜냐하면 실제 host 컴에서 복사를 하면서 권한도 같이 복사를 해주기 때문!   
그래서 entrypoint로 실행할 때에도 실행권한으로 파일이 실행이 되게 된다  

그리고 ENTRYPOINT를 지정해준다. 마찬가지로 container안의 ./ 즉 현재 디렉토리로 했으므로  
```
ENTRYPOINT ["./ros_entrypoint.sh"]
```

이 sh스크립트에서는 source로 각 setup.bash 파일을 해줘야한다   
~~.bashrc 파일이 만들어져 있으므로 .bashrc 파일만 source 해줬더니 실행이 안된다.  
분명히 Dockerfile에서 RUN으로 만들어서 파일도 있으나 (확인) .bashrc만 실행할 경우에는   
roslaunch 명령어를 인식하지 못한다. 즉, /opt/ros/로스버전/setup.bash 가 필요하다~~

아마도 .bashrc 파일에 ros setup.bash가 제대로 실행이 안되서 그런 듯 하다  
그러므로 .bashrc 파일만 잘 실행해도 될 듯 하다  

테스트 해보기


## docker build & up
이제 docker를 build 한 후에 docker-compose 혹은 docker compose up을 해주면  
런치파일이 실행된다   



필요하다면 shell script에 추가 (해보지는 않음)
```
export ROS_MASTER_URI=http://$(hostname --ip-address):11311  
export ROS_HOSTNAME=$(hostname --ip-address)
```