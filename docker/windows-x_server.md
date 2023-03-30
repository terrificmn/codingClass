# windows 에서 x-server 실행

[windows x server download](https://sourceforge.net/projects/vcxsrv/files/latest/download)

x-server 프로그램을 사용할 때에는 Multiple windows -> Start no client -> 순서로 디폴트 값으로 사용하면 됨   
Extra settings 도 기본값으로 사용하면 된다  

마지막으로 방화벽(?) 액세스 경고 나오는 것도 액세스 하게 해주면 된다.   

## Dockerfile 설정

```
## windows 에서 x-server가 docker쪽을 리스닝하게 된다. (ip 0.0)
ENV DISPLAY=host.docker.internal:0.0
```
> docker-compose 에서 environment 로 설정한 DISPLAY가 있다면 삭제


## X-server 실행, docker up
이제 x-server를 실행하고, docker compose up 해주면 된다  
