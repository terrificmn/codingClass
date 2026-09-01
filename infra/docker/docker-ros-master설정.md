# ROS_MASTER_IP

ros master ip 설정은 ~/.bashrc 스크립트에 export로 환경변수를 넣어주면 되는데... 

2대를 이상을 연결하는 경우에는 잘 된다  


## docker container와 연결 시 
아래처럼 
```
742aba6d47cf   docker-ros-ros   "/ros_entrypoint.sh …"   13 minutes ago   Up About a minute   0.0.0.0:11311->11311/tcp   ros
```
일단 의심가는 부분은 컨테이너 이름이 742aba... 로 되는 것이고   

docker-compose.yml 파일에 Env로 master ip로 설정이 되었지만, remote에서 master로 보내면 master에서 받지를 못한다   

### docker remote 상황
```
    environment:
      - ROS_MASTER_URI=http://${MASTER_IP}:11311
```
위의 환경변수에는 master ip가 들어가 있다   

그 밖에 docker컨테이너의 `~/.bashrc` 에도 ROS_MASTER_IP가 잘 들어가 있다  

그래서 마스터쪽에서 `roscore`를 하면 `rostopic list`로 remote(클라이언트), master쪽 모두 잘 나온다   

docker는 일단 0.0.0.0:11311로 되어 있기 때문에 어느 ip이든 다 받는 상황  
그래서 master에서 보내는 주는 토픽은 subscribe가 된다   

**하지만** master쪽에서는 ROS_IP 환경 변수 등으로 remote쪽 ip를 설정했음에도   
리모트 클라이언트 쪽에서 보내는 topic를 수신하지 못한다  
```
Type: geometry_msgs/Twist

Publishers: 
 * /turtlebot3_teleop (http://742aba6d47cf:39149/)

Subscribers: None
```

위처럼 http://에 컨테이너 이름이 나오는 것이 혹시 단서가 아닐까 생각 됨

~~docker rename 명령을 이용해서 컨테이너 이름을 바꿔보았다.~~ ㅋㅋ 실패

역시 삽질 ㅋ

아마도 host name과 관련이 있는 듯 하다   

```
docker_noetic@742aba6d47cf:~$
```
~~도커 컨테이너의 프롬프트 앞 부분.. user는 그렇다 치고 ..~~ 이것도 아님;;


ROS_IP를 bashrc에 해주면 (remote쪽) 또는 ROS_HOSTNAME
```
Type: std_msgs/String

Publishers: 
 * /rostopic_170_1680245073677 (http://192.168.111.111:44917/)

Subscribers: None

```
잘나온다  


하지만. 역시 master에서 받지를 못함 

sudo ufw disable
소용없음

마스터쪽의 방화벽 문제도 아닌 듯 하고   
docker쪽에서 통신이 안나가는 것일 수도 있겠다 ;; 모르겠따

또한 master쪽의 /etc/hosts 에 
remote ip와 hostname을 적었더니,, 이번에는 master와 연결이 안된다   


```
127.0.0.1       localhost
127.0.1.1       sgtubunamr-MS-7D46
192.168.111.111   win_docker
```


