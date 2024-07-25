# docker ros - host network 

hostname: localhost ## available to omit, when use it, specify the hostname.. /etc/hosts
network_mode: host # it is needed when master ros is another pc or the host network like 127.0.0.1, localhost

일단 network_mode는 사용 안해도 docker내에서 사용하는데 문제 없다.  보통 주석 처리해서 사용

단, api 등으로 host의 네트워크를 사용하려면 localhost 또는 127.0.0.1 등을 사용하려면   
network_mode: host 로 지정해주면 된다. 
여기에 콤보로 hostname: localhost 처럼 정확히 입력한다  



만약 hostname이 다르다면
```
ros-s  | RLException: Unable to contact my own server at [http://anyhost:35197/].
ros-s  | This usually means that the network is not configured properly.
ros-s  | 
ros-s  | A common cause is that the machine cannot connect to itself.  Please check
ros-s  | for errors by running:
ros-s  | 
ros-s  | 	ping anyhost
ros-s  | 
ros-s  | For more tips, please see
ros-s  | 
ros-s  | 	http://wiki.ros.org/ROS/NetworkSetup
ros-s  | 
ros-s  | The traceback for the exception was written to the log file
```

마스터가 종료되버린다.  

`cat /etc/hosts` 등을 확인하면 되지만 보통 localhost 로 하거나, 다른 이름이 있다면 적으면 된다. 

다른 remote 컴퓨터를 마스터로 할 경우에는 hostname 을 정확히 적어줘야 한다. ip가 되는지 확인은 못 해봄
> 물론 remote_mods: host는 사용해야함

물론 port 도 docker-comopse.yaml 파일 등에서 정의를 해줘서   
호스트와 docker내 포트를 해줘야지 해당 도커에서 해당 포트를 사용할 수 있다.  


## 정리
도커에서 ros만 사용한다면 딱히 network_mode는 사용할 필요가 없으나   
api나 웹서버 등과 연동하려면 port 설정 및 network_mode 와 hostname을 설정하자

예
```yaml
##생략 ..
    ports:
      - "11311:11311"
      - "8888:8888" ## for api
    hostname: localhost
    network_mode: host
```

