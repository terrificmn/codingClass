# docker 설치  CentOS 8, Ubuntu

yum-tils 설치 (이미 설치되어 있음)
```
$ sudo yum install -y yum-utils
``` 

우분투 같은 경우 먼저 업데이트 
```
 sudo apt-get update

 sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

우분투 공식 GPG 키 추가
```
 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

우분투 x86_64 / amd64
리포지터리 추가
```
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```


리포지터리 추가 
설명:Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.
```
$ sudo yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
```

-우분투 경우
도커 엔진 설치
다시한번 apt-get update 를 해준다
안 그러면 도커 패키지를 못 찾음
```
sudo apt-get install docker-ce docker-ce-cli containerd.io
```



docker engine 설치
```
$sudo yum install docker-ce docker-ce-cli containerd.io
```
try to add '--allowerasing' to command line to replace conflicting packages 라는 메세지가 나옴

만약 패키지가 호환이 안된다고 나오는 경우에는 --allowerasing 옵션을 넣어준다

```
$sudo yum install docker-ce docker-ce-cli containerd.io --allowerasing
```
docker를 설치하고 호환되지 않는 것은 삭제하며 설치를 시작한다

도커 시작해 주기
```
sudo systemctl start docker
```

## Docker compose 설치

[도커컴포즈 설치~ docs확인하기](https://docs.docker.com/compose/install/)


여기는 공통!!
docker-compose를 설치하기   (여기는 centos/ubuntu 같은 듯)

~~먼저 binaries 다운받기~~

예전 방법
~~sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose~~


Docker Compose binary 을 깃허브어서 다운 받은 후에 $HOME/.docker/cli-plugins 에 docker-compose로 카피하게 된다고 한다

```
DOCKER_CONFIG=${DOCKER_CONFIG:-$HOME/.docker}

mkdir -p $DOCKER_CONFIG/cli-plugins

curl -SL https://github.com/docker/compose/releases/download/v2.4.1/docker-compose-linux-x86_64 -o $DOCKER_CONFIG/cli-plugins/docker-compose

```

그 다음 퍼미션 실행가능하게 만들기
```
sudo chmod +x /usr/local/bin/docker-compose
```
이제 docker-compose 실행은 되나 docker-compose --version 하면  
버전 정보 잘 나옴   
그러나 
sudo docker-compose build 하면  
sudo: docker-compose: command not found  이렇게 나옴  
그래서 링크를 걸어준다 

Note: If the command docker-compose fails after installation, check your path.  
You can also create a symbolic link to /usr/bin or any other directory in your path.

```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```


버전확인
```
docker-compose --version
```

버전 1.28.5 이런식으로 나오면 OK!

참고 매뉴얼 
https://docs.docker.com/engine/install/centos/


옵션사항
docker 그룹 추가 및 현 사용자 도커 그룹에 추가
```
sudo groupadd docker
sudo usermod -aG docker $USER
```
아마도 도커 그룹은 있다고 할 것..
groupadd: group 'docker' already exists

```
newgrp docker   
```
newgrp는 바로 다시 적용을 시켜준다. 아니면 로그아웃 한다음에 다시 로그인

이제 sudo 없이 도커 명령어 사용가능


시작할 떄 재시작 등록
```
 sudo systemctl enable docker.service
```
```
 sudo systemctl enable containerd.service
```
취소는 disable

재부팅 후   
```
sudo systemctl status docker
```
로 잘 되는지 확인




