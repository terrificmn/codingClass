

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
```
docker.errors.DockerException: Error while fetching server API version: ('Connection aborted.', PermissionError(13, 'Permission denied'))
```
또는 (우분투에서 에러)
```
ERROR: Couldn't connect to Docker daemon at http+docker://localhost - is it running?
If it's at a non-standard location, specify the URL with the DOCKER_HOST environment variable.
```
sudo로 했는데도 이런 에러가 난다면

그 docker 그룹을 추가하고 현재 내 계정을 docker 그룹에 추가해 준다  
```
sudo gpasswd -a $USER docker
newgrp docker
```
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
```
$docker-compose down
```

다시 
docker-compose.yml 파일을 열고 내용 추가

조금씩 수정하고 보완하면서 다시 실행을 반복한다
```
$docker-compose down

$ sudo docker-compose build && docker-compose up -d
```


docker 리스트 보기
```
$ sudo docker ps -aq
```
활성화
```
$ sudo docker-compose up -d 
```
다운시키기
```
$ sudo docker-compose down
```

## yml 파일 개념

yml 파일 개념 정리

일단 위의 yml 파일이 정의되는 방식은 다음과 같다
네트워크로 묶고 laravel 로 묶음

그리고 그 안에 service가 들어가 있는데
네트워크 이름을 적어준다
```yml
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
```
그래서 위와 같은 그림이 되고  
각각 컨테이너는 3개를 생성, 그 다음에   
각 컨테이너들의 각 설정을 하게 된다  
```yml
services:
    apache:
        depends_on:
            - php
            - mariadb
```
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
```
FROM php:8.0-apache  
RUN docker-php-ext-install mysqli pdo pdo_mysql
```

RUN 은 php install 하겠다는 의미 이후 mysqli pdo pdo_mysql를 설치  


