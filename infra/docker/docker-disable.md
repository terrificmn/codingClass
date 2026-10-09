# docker disable
docker 서비스를 잠시 disable 할려고 할 경우에 사용하는데,  보통 docker.service 정도만 stop 을 걸어놓으면  
컨테이너 등의 restart 옵션이 걸려있으면 자동으로 실행되는 경우가 많다. 재부팅 할 때는 당연히 stop 정도는 무시된다.   

그래서 docker service, socket 등 서비스를 전부 stop 및 disable 해준다. 

먼저 원하는 도커 컨테이너를 먼저 stop 해주고  

```
cd ~/Workspace/mydocker
docker compose stop
```

이후 서비스 stop & disable 해준다. 

```
sudo systemctl stop docker.service docker.socket containerd.service
sudo systemctl disable docker.service docker.socket containerd.service
```


그리고 나서 대충 `docker ps` 등의 명령어를 사용하면  
```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

> 또한 docker ps 했을 경우 컨테이너 정보가 나온다면, disable 된 것은 아님  
그리고 꼭 disable 후 mask 까지는 걸 필요는 없다.  

```
$ systemctl status docker
○ docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; disabled; vendor preset: enabled)
     Active: inactive (dead)
TriggeredBy: ○ docker.socket
       Docs: https://docs.docker.com
```

이런식의 메세지가 나온다면 OK, 최종적으로 재부팅해서 확인해본다.  

