포트를 listen하고 있는지 확인하는 명령어 netstat

22번 포트가 정상적으로 실행되고 있는지 확인해보자
```
sudo netstat -natp | grep 22
```

```
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      494/sshd                                tcp        0      0 192.168.0.19:22         192.168.0.157:53502     ESTABLISHED 1446/sshd: pi [priv                     tcp6       0      0 :::22                   :::*                    LISTEN      494/sshd    
```

현재 LISTEN 으로 잘 되어 있고
외부에서 접속을 하니, 상태가 ESTABLISHED로 나오는 것을 알 수 있음
