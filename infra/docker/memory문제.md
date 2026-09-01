### 우분투 docker 버전   
    20.10.17

ros images는 4.09GB   

roscore 커맨드가 들어간 docker 컨테이너를 실행을 시키면 램 용량은 약 100~200MB 정도 사용하는 것 같음   

분명히 문제가 있음~  

### Rocky docker 버전
    23 버전, 20.10.15버전

램을 풀로 사용;; 거의 18GB 계속 상승함;; 
버전이랑은 상관이 없는 듯하고 도커 컨테이너에서 roscore 실행도 문제가 없어 보인다  

증상: roscore를 안 한 상태에서는 별 문제가 없지만 roscore를 docker-compose.yaml 파일에 command 로 넣거나   
컨테이너에 직접 들어가서 실행을 할 경우에 램이 꽉 찬다   

추츤: 악성코드 등에 감염? 찾아봐야겠다;;


`netstat -nlpt` 명령어 실행할 경우   
```
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 127.0.0.1:36453         0.0.0.0:*               LISTEN      38452/code          
tcp        0      0 0.0.0.0:9090            0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:11311           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:11315           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:34399         0.0.0.0:*               LISTEN      7280/code           
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.1:40149         0.0.0.0:*               LISTEN      31090/code          
tcp        0      0 127.0.0.1:36991         0.0.0.0:*               LISTEN      34119/code          
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:8000            0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:7070            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::9090                 :::*                    LISTEN      -                   
tcp6       0      0 :::11311                :::*                    LISTEN      -                   
tcp6       0      0 :::11315                :::*                    LISTEN      -                   
tcp6       0      0 ::1:631                 :::*                    LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
tcp6       0      0 :::8000                 :::*                    LISTEN      -                   
```

비교해보기

