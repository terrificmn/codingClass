# netstat

포트를 listen하고 있는지 확인하는 명령어 netstat

설치는 
우분투에서는 net-tools 
```
sudo apt install net-tools
```


22번 포트가 정상적으로 실행되고 있는지 확인해보자
```
sudo netstat -natp | grep 22
```

```
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      494/sshd                                tcp        0      0 192.168.0.19:22         192.168.0.157:53502     ESTABLISHED 1446/sshd: pi [priv                     tcp6       0      0 :::22                   :::*                    LISTEN      494/sshd    
```

현재 LISTEN 으로 잘 되어 있고
외부에서 접속을 하니, 상태가 ESTABLISHED로 나오는 것을 알 수 있음


### 옵션
-n -- numeric   
-a -- all : display all sockets   
-p -- programs : show PID/Program name for sockets
-t : tcp 만 보여준다
-u : udp 만 보여준다  

