# ros-master 설정

ROS_MASTER_URI 설정을 하게 되면 remote 와 master간에 ~~잘 연결이 된다~~  되는줄 알았으나..   
실제 연결은 되나, 조금 이상한 상황이 ;;; 결론은 실패


## windows에서 docker 실행
windows10에 wsl을 설치 후 docker-desktop 을 설치   
그 이후는 docker ros를 설치한다  

docker-compose.yml 파일의 environment 부분에 ROS_MASTER_URI 를 추가해도 잘 된다 
```yaml
environment:
    - ROS_MASTER_URI=http://${MASTER_IP}:11311
    - ROS_IP=${HOST_COM_IP}
```
위의 환경변수들은 .env 파일에 정의했다  
```
MASTER_IP=192.168.10.111
HOST_COM_IP=192.168.10.112
```

이렇게 하면 .bashrc 파일에 넣을 필요 없이 이미 환경변수로 설정이 되서 편리하긴 하지만...

어쨋든 `rostopic list`를 하면 (master쪽에서 `roscore`를 해주면...)

토픽들을 볼 수가 있다.   

심지어 master 쪽에서는 topic을 publishing 해주면 windows쪽 docker에서는 잘 subscribing이 된다   

## 하지만, docker에서 publishing이 안되는 듯..
**하지만** 여기까지만 보면 정말 잘 되는 것 같지만.. 그렇지 않다   

docker in Windows에서 토픽을 보내게 되면 예를 들어 간단하게  
```
rostopic pub /test std_msgs/Int8 "data: 0"
```

심지어, info을 `rostopic info /test` 로 확인하면 누가 퍼블리싱 하는지도 나오고, type도 잘 찍어준다 
```
Type: std_msgs/Int8

Publishers: 
 * /rostopic_130_1680517462031 (http://192.168.10.112:44043/)

Subscribers: None
```

하지만 정작 중요한 sub 을 하려고 echo를 하게 되면 아무런 응답이 없다. 아마도 메세지가 퍼블리싱이 안되는 듯 하다   


## hosts 파일 수정하기
/etc/hosts 파일을 수정하게 되면 해당 hosts를 더 확실하게 찾지만  

```
sudo vi /etc/hosts
```
내용은 다 ip 다 적어주기, 
```
127.0.0.1   localhost
...생략
192.168.10.111  master
192.168.10.112  win-docker
```
이런식으로 이름을 host이름을 정해주면 예를 들어 ping을 보낼 때에도 ip 대신에 `ping win-docker` 라고 치면  
알아서 그 ip로 ping을 해준다   

암튼 위 처럼, 좀더 확실하게 host를 찾으라고 해주는 듯 하는 것 같은데, master쪽과 remote쪽에 둘 다 같은 내용으로 해봤으나  
별 소용이 없는 듯 하다   


## docker-compose에서 hostname, network_mode
- yml 파일에서 hostname을 설정해주면 그 이름으로 셋팅이 된다.   
/etc/hosts를 설정해준 것과 같은 효과 같다..  이것도 별 소용 없다  


- `network_mode: host`로 하게 되면 host의 ip를 사용하게 된다   

이런 워닝이 발생하지만, 사용하는데는 문제가 없다 
```
# network_mode: host 를 했을 때
ros Published ports are discarded when using host network mode
```

network_mode를 해준 것과 안 해준것은 확실히 ip가 host ip를 사용하는 것 같은데.. 결과적으로 rostopic으로 list 확인은 잘 되나   
한 쪽 방향으로는 여전히 잘 된다   

> master에서 발행하는 topic은 windows쪽 docker에서 잘 받는다.. 역시 remote 쪽인 docker에서 보내는 pub이 안된는 것 같다  
master쪽에서 전혀 받아지지를 않는다   







topic 보내기

```
rostopic pub /chat std_msgs/String "data: 'hello world'" 
```


   


