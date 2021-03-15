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

```yml
version: '3.1'

    services:
        php:
            image: php:7.4-apache 
            dockerfile: Dockerfile
            ports:
                - 80:80
            volumes:
                - ./src:/var/www/html/

        db:
            image: mysql
            command: --default-authentication-plugin=mysql_native_password
            restart: always
            environment:
            MYSQL_ROOT_PASSWORD: example
            volumes:
                - mysql-data:/var/lib/mysql

        adminer:
            image: adminer
            restart: always
            ports:
                - 8080:8080

    volumes:
    mysql-data:
```
위의 image 부분 **youtube 다시 한번 확인해 볼 것**

그리고 Dockerfile 을 만든다 (확장자 없이)
Dockerfile 안에 build할 내용을 적는다 

위의 image 부분 youtube 다시 한번 확인해 볼 것 
여기도 **업데이트 필요**


docker-compose build && docker-compose up -d
-d 는 detached 의미로 백그라운드에서 계속 돌아가게 하는 것




docker 리스트 보기
$ sudo docker ps -aq


$ sudo docker-compose up -d 

다운시키기
$ sudo docker-compose down


host 컴에서 httpd (apache2)가 서비스 중일 때는 
docker-compose up -d 를 실행했을 때 에러가 발생 

```
WARNING: Host is already in use by another container
Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use
ERROR: Encountered errors while bringing up the project
```
이런식으로 에러가 발생한다

```
$systemctl status httpd  #centOS
$systemctl status apache2  #ubuntu

$systemctl stop httpd  #centOS
$systemctl stop apache2  #ubuntu

```
확인 한 후 stop 시킨다

다시 docker-compose 를 실행
```
$ sudo docker-compose up -d
```

Starting dockertest_php_1 ... done 
이런 메세지와 함께 끝나면 성공

이제 브라우저로 
localhost:8080 으로 접속하면 Adminer 로 접속을 할 수 있음
phpmyadmin 같은 프로그램인 듯 한데 좀 더 수월한가봉

그리고 
브라우저에 localhost/index.php 를 입력하면
docker 파일을 만들기 위해서 src 디렉토리에 만들어 놓았던 index.php 가 실행되는 것을 알 수 있음
신기 (httpd 는 작동이 중지되있기 때문)
도커 컨테이너안에서 따로 실행

실행이 잘 되는 것을 확인했으니 이제 다시 down으로 중지 시킴
```
$ sudo docker-compose down
```

___

이번에는 Dockerfile을 수정해서 build를 할 수 있게 한다 
이렇게 하면 .yml 파일에 image로 가져올 수 없고 build로 바꿔줘야 함


일단 아무 디렉토리나 만들고  (docker를 실행할 root dir이 된다)
$ mkdir dockertest
$ cd dockertest

이제 파일 2개를 만든다 , `docker-compose.yml`, `Dockerfile` (확장자 없음)
편하게 vscode에서 만들어도 되고 touch나 echo 명령어로 만들어도 된다 in the terminal (맘대로)

그리고 서버가 잘 작동하는지 테스트 하기 위해서 src 디렉토리를 하나 만들고 
그 안에 index.php 파일을 만듬 
$ touch index.php

(또는 vscode로 만들기)

이제 docker_compose.yml 파일을 열어서 내용을 수정한다
일단 version은 3.1 이고 php 버전도 7.4 임
버전 8.0은 테스트를 해봐야하는데 일단, 7.4는 성공

위에서 만들어진 내용 중에 image 있는 부분을 build로 수정
왜냐하면 Dockerfile에서 이미지를 빌드하는 방법으로 바꿨기 때문


```yml
version: '3.1'

    services:
    php:
        build:
        context: . #current dir
        dockerfile: Dockerfile
        ports:
            - 80:80
        volumes:
            - ./src:/var/www/html/

    db:
        image: mysql
        command: --default-authentication-plugin=mysql_native_password
        restart: always
        environment:
        MYSQL_ROOT_PASSWORD: example
        volumes:
            - mysql-data:/var/lib/mysql

    adminer:
        image: adminer
        restart: always
        ports:
        - 8080:8080

    volumes:
    mysql-data:
```



그리고 나서 
위에서 이미지 파일을 잘 받아서 실행되는 것을 확인했기 때문에 
Dockerfile에서 build 하고 확장 프로그램들을 설치해주는 명령어를 셋팅한다

```Dockerfile
FROM php:7.4-apache
RUN docker-php-ext-install mysqli
```

저장




docker-compose 를 실행한다
```
$ sudo docker-compose up -d
```


Adminer 로그인
아이디 root
비번: example
db 는 비워둘 것

DB를 만들고, 테이블을 만들어 보면 잘 작동하는 것 확인!


