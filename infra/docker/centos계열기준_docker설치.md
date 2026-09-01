## docker engine 설치 _ centos 계열 almalinux

!!!!!!!! 깃허브에 올라가 있는 예전 자료 정리할 것

codingClass/setup installation txt_files/docker설치하기_dockerfile설명.md 
이 파일이 ubuntu랑 centos 버전이 막 섞여있음;;;;;
정리 필요함
!!!!!!!!!!!!!!!!!!!!!!!!!!!


https://docs.docker.com/engine/install/centos/

yum-utils를 설치 및 stable repository 설정
```
sudo yum install -y yum-utils

sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

Docker Engine 설치
```
 sudo yum install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
Docker CE Stable - x86_64 
Importing GPG key 0x621E9F35: 를 한다고 물어보는데 y 눌르자


원하는 버전으로 설치하려면 위의 처음 링크에서 다시 한번 확인


docker시작
```
sudo systemctl start docker
```



## compose 설치
binary manually로 설치

한줄한줄 실행하면 된다~ 단, stable버전은 조금씩 업데이트 되므로 메뉴얼 페이지를 다시 **한번 확인하자!**
[](https://docs.docker.com/compose/install/)


```
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}

 mkdir -p $DOCKER_CONFIG/cli-plugins

 curl -SL https://github.com/docker/compose/releases/download/v2.5.0/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose
 ```


/home/유저/.docker/cli-plugins 의 위치에 있는 docker-compose 를 실행권한 주기
```
chmod +x $DOCKER_CONFIG/cli-plugins/docker-compose
```

설치 후 버전 확인
```
docker compose version
```

도커도 업데이트가 되면서  docker compose 식 으로 한 칸 띄워서 사용하는 것 같고;;   
그리고 docker-compose 명령어로 사용하려면   

그리고
-bash: docker-compose: command not found

```
sudo ln -s $HOME/.docker/cli-plugins/docker-compose /usr/bin/docker-compose
```
도커를 자신의 디렉토리에 설치를 했기 때문에 심볼릭 링크를 /usr/bin/docker-compose 로 만들어준다



## 삭제
To uninstall Docker Compose if you installed using curl:

```
 rm $DOCKER_CONFIG/cli-plugins/docker-compose
```
or if you choose to install Compose for all users

```
 sudo rm /usr/local/lib/docker/cli-plugins/docker-compose
```


