# entrypoint.sh 
[entrypoint-shell.md] 에서 사용한 entrypoint.sh 와 Dockerfile, docker-compose.yml 등을 사용해서  
devel vs release 모드로 따로 사용할 수 있다. 

그 전에는 docker-compose.yml 에서  
command 를 주석처리해서 실제 실행파일이 실행되지 않는 식으로 했었는데, 필요할 시에만 주석 해제해서 사용   
```
# command: tail -f /dev/null
```
이렇게 해도 크게 문제가 없지만, 매번 이미지가 새로 생성될 수도 있다. 

docker-compose 파일을 override 해서 사용할 수 있는 방법이 있음  

먼저 original 파일인 docker-compose.yml 은 그대로 두고  

새로운 docker-compose-dev.yml 같은 파일을 만들고  
다른 것은 필요없고, 서비스명, 컨테이너 명 등만 적어주고   
딱 변경시켜서 사용할 것만 넣어준다. 

```
services: 
  ros2:
    command: ["tail", "-f", "/dev/null"] # dev
    restart: no
```

끝, 이거면 끝이다. 그러면 docker 에서 실행을 할 때, 이 dev 파일이 사용하면 위의 command, restart 부분만 사용해주게 된다.  


## docker compose up
사용할 경우에는  기존의 release / production 로 수행할 경우에는 

```
docker compose -f docker-compose.yml up -d
```
로 파일을 지정해서 실행을 해준다. 

> 보통처럼 docker compose up 을 해버리면 모든 compose 파일이 override 된다고 하니, 파일을 지정해준다.  

development 일 경우에는 
```
docker compose -f docker-compose.yml -f docker-compose-dev.yml up
```
> 순서를 오리지널 먼저, 그 다음 override 할 파일  


이렇게 해준 후에 컨테이너에서 작업을 해주면 된다. tail -f /dev/null 덕분에 컨테이너가 계속 실행되어 있게 된다.  

`docker exec -it ros2 bash`



