docker 설치  (centOS 8)
yum-tils 설치 (이미 설치되어 있음)
```
$ sudo yum install -y yum-utils
```
리포지터리 추가 
설명:Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.
```
$ sudo yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
```

docker engine 설치
```
$sudo yum install docker-ce docker-ce-cli containerd.io
```
try to add '--allowerasing' to command line to replace conflicting packages 라는 메세지가 나옴

패키지가 호환이 안되는 것이 있어서 --allowerasing 옵션을 넣어준다

```
docker-ce docker-ce-cli containerd.io --allowerasing
```

docker를 설치하고 호환되지 않는 것은 삭제해준다

시작
```
sudo systemctl start docker
```



docker-compose를 설치하기 
먼저 binaries 다운받기
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

그 다음 퍼미션 실행가능하게 만들기
sudo chmod +x /usr/local/bin/docker-compose

버전확인
docker-compose --version

버전 1.28.5 이런식으로 나오면 OK!



준비

먼저 테스트겸 프로젝트 디렉토리 하나 만든 후 그 안에 yml파일 만들기
touch docker-compose.yml

그리고 Dockerfile 을 만든다 (확장자 없이)
Dockerfile 안에 build할 내용을 적는다 



docker-compose build && docker-compose up -d
-d 는 detached 의미로 백그라운드에서 계속 돌아가게 하는 것

