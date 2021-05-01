docker 설치  (centOS 8)
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

우분투
리포지터리 추가
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null



리포지터리 추가 
설명:Before you install Docker Engine for the first time on a new host machine, you need to set up the Docker repository. Afterward, you can install and update Docker from the repository.
```
$ sudo yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
```

도커 엔진 설치
다시한번 apt-get update 를 해준다
안 그러면 도커 패키지를 못 찾음

sudo apt-get install docker-ce docker-ce-cli containerd.io




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




여기는 공통!!
docker-compose를 설치하기   (여기는 centos/ubuntu 같은 듯)
먼저 binaries 다운받기
sudo curl -L "https://github.com/docker/compose/releases/download/1.28.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


그 다음 퍼미션 실행가능하게 만들기
sudo chmod +x /usr/local/bin/docker-compose

이제 docker-compose 실행은 되나 docker-compose --version 하면
버전 정보 잘 나옴 
그러나 
sudo docker-compose build 하면
sudo: docker-compose: command not found  이렇게 나옴
그래서 링크를 걸어준다

Note: If the command docker-compose fails after installation, check your path. You can also create a symbolic link to /usr/bin or any other directory in your path.

```
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```


버전확인
docker-compose --version

버전 1.28.5 이런식으로 나오면 OK!

참고 매뉴얼 
https://docs.docker.com/engine/install/centos/


옵션사항
docker 그룹 추가 및 현 사용자 도커 그룹에 추가

sudo groupadd docker
sudo usermod -aG docker $USER

아마도 도커 그룹은 있다고 할 것..

newgrp docker 
newgrp는 바로 다시 적용을 시켜준다. 아니면 로그아웃 한다음에 다시 로그인

이제 sudo 없이 도커 명령어 사용가능


시작할 떄 재시작 등록
 sudo systemctl enable docker.service

 sudo systemctl enable containerd.service

취소는 disable

재부팅 후 
sudo systemctl status docker
로 잘 되는지 확인





준비

docker 파일들을 넣어둘 디렉토리를 하나 만든다
이름은 아무거나
```
$ mkdir dockertest
$ cd dockertest
```

## Dockerfile Docker 실행하기

Dockerfile 을 만든다 (확장자 없이)
Dockerfile 안에 build할 내용을 적는다 

```Dockerfile
FROM php:8.0-fpm
COPY . /usr/src/myapp
WORKDIR /usr/src/myapp
CMD ["php", "./index.php"]
```

그리고 src 서브 디렉토리를 하나 만들고 
```
$ mkdir src
```
src 디렉토리 안에 테스트 페이지로 index.php 하나 만든다 
index.php 내용안에는 간단하게 아무런 내용 상관 없음

```php
<?php
echo 'Hello from Docker!';
?>
```

빌드하기
$sudo docker build -t my-php-app 

만들어진 이미지로 실행
$sudo docker run -it --rm --name my-running-app my-php-app

잘 실행이 된다면 
**Hello from Docker!** 라는 메세지가 나오면 성공!

___

## docker-compose 사용하기
docker-compose.yml 파일을 만들어서 사용
상위 디렉토리에 파일을 하나 만든다 (그냥 vscode로 만드는게 편함)

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


docker-compose build && docker-compose up -d
-d 는 detached 의미로 백그라운드에서 계속 돌아가게 하는 것

테스트!
브라우저를 열고 http://localhost/index.php 입력한다

index.php에 입력한 내용이 잘 나오면 성공!

참고 Adminer도 dbtool
Adminer 로그인
아이디 root
비번: example
db 는 비워둘 것

DB를 만들고, 테이블을 만들어 보면 잘 작동하는 것 확인!


### 트러블 슈팅

트러블 슈팅
(centOS 8에서 에러)
docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', PermissionError(13, 'Permission denied'))

또는 (우분투에서 에러)
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.

sudo로 했는데도 이런 에러가 난다면

그 docker 그룹을 추가하고 현재 내 계정을 docker 그룹에 추가해 준다
sudo gpasswd -a $USER docker
newgrp docker

그러면 해결!


### 트러블 슈팅

또 문제 발생 시

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

자~ 다시
```
$ sudo docker-compose build && docker-compose up -d
```
Creating php ... done 이렇게 나오면 굿!


docker를 내린다
$docker-compose down

이제 docker를 다시 내린 후에 
어떤식으로 돌아가는지 감이 좀 잡혔으니
mysql 대신에 maria db와 adminer 대신에 phpmyadmin으로 진행
문제는 거기에 필요한 extesion들을 어떤식으로 추가할지가 관건인듯

Dockerfile을 열어서 이제 기존의 Dockerfile 을 이용해서 이미지를 빌드
아예 만들어져 있는 것을 받는게 아니라 extension등을 더 받아서
하게 하는 것
내용 수정 (전체 수정) 일단 이게 기본이 될 듯한데 필요한것을 더 깔아야 할 듯 하다

```Dockerfile
FROM php:8.0-apache
RUN docker-php-ext-install mysqli 
```

다시 
docker-compose.yml 파일을 열고 내용 추가

조금씩 수정하고 보완하면서 다시 실행을 반복
```
$docker-compose down

$ sudo docker-compose build && docker-compose up -d
```

그러면 mariadb와 phpmyadmin 같은 경우는 이미지를 새로 다운 받는다
Creating dockertest_db_1         ... done
Creating dockertest_phpmyadmin_1 ... done
Creating php                     ... done
요렇게 나오면 성공!



phpmyadmin 테스트 해보기

브라우저에 
http://localhost:8080/ 
이렇게 입력하면 접속됨



docker 리스트 보기
$ sudo docker ps -aq

활성화
$ sudo docker-compose up -d 

다운시키기
$ sudo docker-compose down



## yml 파일 개념

yml 파일 개념 정리

일단 위의 yml 파일이 정의되는 방식은 다음과 같다
네트워크로 묶고 laravel 로 묶음

그리고 그 안에 service가 들어가 있는데
네트워크 이름을 적어준다

version: '3.8'

networks:
    laravel:

services:
    php
        networks:
            laravel:
    
    db
        networks:
            laravel:    
    
    phpmyadmin
        networks:
            laravel:

그래서 위와 같은 그림이 되고
각각 컨테이너는 3개를 생성, 그 다음에 
각 컨테이너들의 각 설정을 하게 된다

services:
    apache:
        depends_on:
            - php
            - mariadb

이렇게 의존성을 추가할 수 있고 php mariadb가 실행되고 실행이 될 수 있게 하는거라고 함
현재는 php-apache 버전을 이미지로 선택해서 
apache를 설치를 따로 안했는데 이것도 차차 알아봐야겠음. (centos에서는 httpd인데)


image : 이름:버전-버전명
이런식으로 써 주는데.. 
docker 사이트에서 검색을 하면 대표적이 이미지가 나오는데 
거기에서 버전과 맞는 것을 고르면 된다



docker사이트
[httpd](https://hub.docker.com/_/httpd)
[php](https://hub.docker.com/_/php)
[마리아db이미지](https://hub.docker.com/_/mariadb)
[phpmyadmin](https://hub.docker.com/_/phpmyadmin)


[docker compose 사용법](https://docs.docker.com/compose/profiles/)





## 완성본은 아니지만 그대로 일단 설명

이제 대충 완료된 docker-compose.yml 파일
설명은 주석으로 
```yml
version: '3.8'

networks: # entworks 라는 것으로 묶어줌 이름 laravel
  laravel:

services:
  php:
    #image: php:8.0-apache #직접 이미지를 받을 때 사용
    build:
      context: .   # .은 현재 디렉토리를 의미하므로 dockerfile을 사용해서 build 하겠다
      dockerfile: Dockerfile
    container_name: php  #컨테이너 네임 정해주기
    ports:
      - 80:80   #lccalhost에서 80포트로 docker container 80포트로 통신 
      # 여기도 php를 로컬로 사용하고 있다면 9000:9000 포트를 바꿔줘도 됨
    volumes:
      - ./src:/var/www/html/   # ./src 는 현재디렉토리부터 src 서브디렉토리를 web service 디렉토리인 /var/www/html/ 연결
    networks: 
      - laravel

  # Use root/example as user/password credentials
  db:
    image: mariadb # 도커hub에서 이미지를 받아온다
    container_name: mariadb
    restart: unless-stopped  #재시작하지 않음 unless-stopped 어떤 이유로 든지 멈추지 않으면 재시작 하지않음, 멈추면 재시작 
    tty: true # db와 통신 가능하게함
    ports: 
      - 4306:3306  # 포트를 로컬은 4306으로 설정한 이유는 이미 로컬에서 db가 돌아가고 있어서 4306으로 설정 없다면 3306:3306으로 하면 됨
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw  #root 패스워드가 됨 안써도 디폴트라고 하는 듯
      MYSQL_DATABASE: app_db
      MYSQL_USER: db_user
      MYSQL_PASSWORD: db_user_pass
      SERVICE_TAGS: dev # 옵션 (없어도 무관)
    volumes:
      - ./mysql:/var/lib/mysql  # 데이터를 저장하려면 연결해줘야함 #mysql 디렉토리는 만들어야 함
    networks: 
      - laravel

  phpmyadmin:
    image: phpmyadmin
    container_name: pma
    links:
      - db   # 여기에서 db로 연결했으니 phpmyadmin으로 들어갈때 server를 db라고 하면 됨 ,, 외부에서 연결할때는 고민을 좀 해봐야할 듯
    restart: always
    ports:
      - 8080:80
    environment:
      - PMA_ARBITRARY=1
      - PMA_HOST= db
      - PMA_PORT= 3306
    networks: 
      - laravel
```


위의 걸로 compose build를 해서 실행이 되면
index.php에 phpinfo(); 를 해보면 
단 여기에서는 pdo 드라이버가 설치가 안되어 있다
이미지를 build 해야함

그래서 php는 image에서 build 로 (docker-compose.yml)
Dockerfile을 추가한다

FROM php:8.0-apache
RUN docker-php-ext-install mysqli pdo pdo_mysql

RUN 은 php install 하겠다는 의미 이후 mysqli pdo pdo_mysql를 설치




----------------------------------------------------------
윈도우 버전은 docker desktop 을 받은 후 설치
그리고 여기 공식 사이트 참고
https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package

Step 5까지 하고 6번은 리눅스 설치는 안했음

