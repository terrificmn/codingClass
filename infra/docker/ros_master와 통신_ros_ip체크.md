# docker 에서 ros master 설정시 유의 사항

## 실패 케이스
network_mode host 아닐 경우   
docker 내부 네트워크로 사용할 경우
ros_ip 실패, ros_hostname 실패

host name으로 실행 및 /etc/hosts/ 등록했을 경우
/rostopic_107_1680577522402 (http://docker_noetic_remote:34391/  바뀌나 실패

물론 docker 내부 network를 사용해도   
rostopic list, rostopic info 등 master와 연결이 된 것을 알 수가 있는데   
거기에다가 master에서 퍼블리쉬를 한다면 subscribe 하는 것도 가능하나..   
docker에서 publishing 을 하게 되면 master에서 전혀 못 받게 된다   


## 성공
network_mode 일 경우 
ROS_HOSTNAME 을 넣어주면 성공
 
 또는 
ROS_IP 만 넣어도 성공, without hosts 

ros_IP가 없는 경우에는 받지 못한다. 단, hosts에 정의되어 있으면 받음, 
hosts에 ip는 정의했어도 hostname이 틀리면 못 받는다 
ROS_IP인 경우에는 /etc/hosts 에 ip를 정의해 주면 쉽게 받아진다   



### master 설정 없이 단독 사용하기
반대로 docker 에서 master설정 없이 단독으로 사용하려고 하면   
docker-compose의 network_mode는 사용하면 안됨    
사용할 시에는   
```
RLException: Unable to contact my own server at [http://docker_noetic_remote:36641/].
This usually means that the network is not configured properly.

A common cause is that the machine cannot connect to itself.  Please check
for errors by running:

	ping docker_noetic_remote

For more tips, please see

	http://wiki.ros.org/ROS/NetworkSetup

The traceback for the exception was written to the log file
```
이런식으로 host ip를 이용해서 하려고 할 때 안되는 모습을 보임 

> 물론 master를 local러 셋팅 한 상태  


network_mode를 뺀 다음에 environment의 ROS_MASTER_URI 를 빼거나, 아님 localhost로 하면   
`roscore`를 해도 단독으로 잘 실행이 된다   


## 마스터 설정 후에도 토픽들이 안 보이는 경우
rostopic list 했을 때 (클라이언트쪽 (remote))에서 했을 때 아무것도 안나온다면  
방화벽을 의심해 볼 것   

ubuntu 같은 경우에는 일단 잠깐 멈춰보기
```
sudo ufw stop
# 또는 
sudo ufw disable
```

