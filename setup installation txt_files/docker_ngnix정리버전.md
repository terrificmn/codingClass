docker_ngnix_php 디렉토리에 만들어둔 copy파일 참고할 것
projects/docker_nginx_php/nginx_php_mysql_phpmydamin_docker-compose copy

httpd 서버와 거의 비슷함
다만, ngnix 용 conf파일 설정만 다름
ngix의 ports  8000 이나 80으로 설정 
만약 로컬에서 httpd가 돌아가거나 다른 서비스가 하고 있으면 안될 수 있으니 적절히 열어주자

# 처음 라라벨 프로젝트를 도커로 진행할 시에 아래처럼 할 것!

디렉토리는 app 으로 연결함, 즉 app 디렉토리도 만들어 주기
Dockerfile은 최상단 경로에 복사해 만들어 놓으면 됨

nginx설정파일도 만들어 줘야함 default.conf로 최상위디렉토리에 만들어 주고
설정 파일내용은 그냥 php와 라라벨용이 있으니 먼저
라라벨이 설치가 안되어 있으면 라라벨용으로 docker-compose up 하면 웹서버 작동안함


mysql은 mysqldata와 연결시킴
mysqldata 디렉토리 만들어주기

서버 테스트는 app/public/index.html or index.php 를 만든 후 
localhost 를 브라우저에 쳐본다 (포트번호 설정한 것에 주의)

phpmyadmin은 localhost:8080 를 브라우저에 쳐본다
비번은 yml파일에 mysql 부분의 environment에 정의된 것을 참고
(유저id와 비번을 사용하면 됨)

그냥 php일때는 app/public/index.php 로 테스트
라라벨로 할때는 app 이 라라벨프로젝트 자체이면 됨

즉, 잘 되는 거 확인했으면 이제 app 디렉토리를 지우고 프로젝트의 루트 디렉토리에서
app으로 라라벨 new 프로젝트를 생성
아예 첫 프로젝트를 진행할 때만 아래처럼 진행할 것~ 이미 있는 프로젝트이면 깃허브 clone하자
```
$ laravel new app
```

그리고 다시 localhost로 가면
처음 라라벨 home이 나오면 완성!

php artisan 명령어를 사용하려면 docker-comopser exec 로 명령을 내려야함
풂패스를 적어준다
docker-compose exec php php /var/www/html/artisan migrate


# git clone 으로 다운받아서 진행
일단 docker-* 로 만들어진 디렉토리에서 깃 클론으로 다운받기
```shell
$git clone 내github_리포지터리.git
```

기존의 app 이 root:root 소유로 만들어져 있을텐데 지워준다 
```shell
$rm -rf app
```

이제 git 리포지터리 이름으로 다운이 되어 있을 텐데 app으로 바꿔주던가 
docker-compose.yml파일의 디렉토리 설정을 바꿀지 결정- 그냥 프로젝트를 app 변경함

```shell
$mv laravelproject app
```
vendor 디렉토리가 포함되어 있지 않다. 원래 gitignore에 포함됨.
그래서 먼저 필요한 npm 설치를 해준다  
**blog프로젝트 시작 composer_frontend.md** 파일을 참고한다

그리고 권한 문제가 발생하므로 소유권을 변경해준다
```shell
$ sudo chown -R $USER:33 app
```

**중요!!** 설정파일 계정 비번 디비명 등을 먼저 바꾼 후에 진행할 것. 처음에 그냥 테스트용으로 만들고 
다시 바꾼다음에 하려고 하면 생성이 자동으로 안되서 로그인 안됨. (컨테이너에 직접 접근해서 명령어를 쳐서 할 수 있을 것 같기는 한데.. 어쨋든)
docker-compose.yml파일의 mariadb 관련 루트비번 디비 네임등을 다시 바꿔준다, root와 일반유저 각각 비번을 바꾼다.
그리고 프로젝트내의 env파일이 없다. .env.example 파일을 복사해서 .env 파일로 만들고 DB부분를 수정한다. 위의 yml파일에서 설정한 것을 넣어주면 된다

그리고 docker-compose build 및 up 해준다
```shell
$sudo docker-compose build
$sudo docker-compose up
```

이제 localhost:8000으로 접근을 하면 아마도 라라벨 키를 만들어야 한다고 나올 것임 키 생성 눌러주면 됨
그리고 db에 데이터베이스까지만 만들어져 있고 테이블이 없는 상태이므로 migration을 해준다
절대경로로 접근해야한다
중요! .env 파일의 DB_HOST를 127.0.0.1 에서 mysql로 바꿔줘야한다. 
```shell
docker-compose exec php php /var/www/html/artisan migrate
```

이제 디비 테이블이 만들어졌다. 이제 아이디를 만들어보고 테스트를 해보면 된다 


# <트러블슈팅>

이제 웹브라우저에 localhost:8000 을 입력하면
아마도.. 이런 에러가 
```
UnexpectedValueException
The stream or file "/var/www/html/storage/logs/laravel.log" could not be opened in append mode: Failed to open stream: Permission denied 
```
아래 내용 참고

현재 23mar2021 기준으로 다시 안되고 있음  
2주 스트림릿 하느라고 안했더니 작동을 안함;; 아래 내용이랑 유투브랑 다시 해서 해결할 것!!
트러블슈팅!!
처음에 잘되는거 확인하고나서 나중에 다시할려고 이런 퍼미션 에러가
The stream or file "/var/www/html/storage/logs/laravel.log" could not be opened in append mode: Failed to open stream: Permission denied 
퍼미션 에러 일때

도커 설정을 잘못한줄 알고, 퍼미션 에러인지도 모르고 반나절을 넘게 고생 ㅠ

소유자가  www-data 소유그룹 www-data가 되서 
sudo chown -R www-data:www-data blog 이런식으로 된다고 하는데 
그래서 chown을 하면 그룹이 없다고 함. 그래서 유저를 새로 만들려다가 찾아보니

ngnix는 uidd와 gid을 찾을 수 있는데..
먼저 docker-compose up을 먼저 시킨 상태에서 아래 명령어로 실행을 해보면
$sudo docker-compose exec web id www-data
결과:
uid=33(www-data) gid=33(www-data) groups=33(www-data)
이렇게 나오는데 

도커 라라벨 프로젝트에 권한을 주게되면 된다. 그러면 컨테이너도 그 권한으로 사용하게 된다고 함.  
chown 을 해서 소유자 변경을 해준다. 라라벨 프로젝트 디렉토리를 경로로 써주면 된다
$ sudo chown -R 33:33 myblogapp 단
여기에서 소유자는 해당 소유자user로 남겨보자

```shell
$ sudo chown -R $USER:33 myblogapp
```
방법을 찾아야 할 듯... 왜냐하면 이제 여기에서의 git clone은 pull 만 할 것이고 
push는 안할 것임. (서버용이므로)
그래서 문제가 있을지 없을지 아직 잘 모르겠음. -테스트 필요


암튼 소유자:그룹을 변경해주면 
웹페이지는 뜨지만 
새로운 에러
```
No application encryption key has been specified. 
Generate your application encryption key using php artisan key:generate.
```
웹브라우저상에서 generate key 버튼을 누르라고 나온다. 눌러주면 
(아니면 artisan 커맨드를 사용)
The solution was executed successfully. Refresh now. 과 함께 새로고침을 하라고 함

그러면 이제 잘 뜨는 것이 보일 것임

하지만 여기에도 문제가 있음.. git clone으로 생성한 다음에 
pull 을 한 후에 
어쩔 수 없이 npm 으로 필요 패키지를 깔아줘야하는데 
그러면 layouts/app.blade.php 파일이 변경되어 있다. 
아마도 npm ui설치하면서 기본으로 바뀌는 듯..
그래서 이미 pull 을 한 상태이므로 더이상의 pull 도 안됨
그래서 깃허브 소스를 보고 app.blade.php 파일의 내용을 다 수정해주고 저장
이때 (이름바꾼 laravel프로젝트에서 app으로) app 디렉토리 (상위에서)
소유권을 유저로 바꿔준뒤 저장해야하고 
다시 라라벨 페이지를 보려면 33:33으로 소유권을 바꿔준다.
흠.. 이거 문제인듯;;;;

우분투의 경우:
그리고 나면 이제 페이지가 잘 보이는데 ;;
회원가입을 하려고 하면  SQLSTATE[HY000] [2002] Connection refused
phpmysql 접속이 안된다.. 이전에는 오히려 라라벨 프로젝트가 실행이 안되더니
이번에는 phpmysql이 root로 로그인이 안됨;;;
처음에 만들었던 이미지랑 달라서 그러는지;;; 연구필요함

centOS의 경우는 
```
Not Found

The requested URL was not found on this server.
Apache/2.4.38 (Debian) Server at localhost Port 8080
```

원래 네트워크로 묶었는데 그걸 안한거 같다.. 원래 참고했던 유투버에서는 네트워크를 라라벨로 하고 
그걸로 그래서 그 네트워크가 형성이 되었던거 같은데 

그 사람은 phpmyadmin을 사용을 안 했기 때문에 다른 사람꺼를 또 참고 했고 그렇게 하다보니 
네트워크가 빠지고 이래저래 학교에서 집에서 왔다가 갔다가 조금씩 다른 환경에서 했더니 조금씩 엇나간거 같음
(왜냐하면 그 전에는 라라벨 페이지가 안 뜨더라도 phpmyadmin 접속 및 sql로 db 생성이 가능했었음)

일단 docker 매뉴얼을 보면 docker-compose.yml 파일의 버전은 3.9가 되어야하는듯하다
현재 도커 엔진 버전은 20.10.5 

docker-compose.yml 에서 네트워크를 설정해주고, 이름은 backend로 해서 업데이트 함
그리고 phpmysql 컨테이너 부분에서 link를 빼고 networks로 넣어줬다

접속은 localhost:8080으로 하면 되고
server는 mysql, 계정 및 패스워드는 mysql 컨테이너에 적었던 것을 넣어주면 됨

테스트! phpmysql 컨테이너에 networks항목을 뺀다음에 다시 빌드 후 up해보니
phpmyadmin에는 잘 접속이 되는데 로그인이 안된다. mysql서버에 로그인 할 수 없다고 나옴
확실이 네트워크가 중요한가보다. 아무래도 컨테이너들 끼리는 서로 모르는 관계? 라고 해야하나

두번째 문제는 기존에 테스트로 시작하면서 mysql관련 비번이랑 유저를 tutorial 식으로 해놓았는데 
원래 비번으로 바꿔서 다시 진행하려고 해도 뭔가 안된다. 바뀐 유저랑 비번을 알아먹지를 못함
그래서 docker-composer down 후 build && up해도 결과는 똑같음
volumes로 연결해뒀던 mysqldata 디렉토리를 가서 sudo로 안의 파일을 지우고 다시 docker-composer를 up시키고 
localhost:8080하니 아예 페이지를 못찾음 ㅋㅋ
다시 docker-composer down 후 build && up 했더니 
어떻게 보면 mysql관련 파일이 없어졌으니 다시 새로 시작된것 같다
그래서 처음에 새로설정한 비번, 유저, 디비이름으로 다시 다 만들어준다
그리고 처음에 시작하면서 루트 패스워드 설정하는 법도 알려주는데.. docker-composer exer로 가능할 것 같기도 해서 참고로 남겨둠
```
PLEASE REMEMBER TO SET A PASSWORD FOR THE MariaDB root USER !
mysql         | To do so, start the server, then issue the following commands:
mysql         | 
mysql         | '/usr/bin/mysqladmin' -u root password 'new-password'
mysql         | '/usr/bin/mysqladmin' -u root -h  password 'new-password'
mysql         | 
mysql         | Alternatively you can run:
mysql         | '/usr/bin/mysql_secure_installation'

2021-04-05 20:46:40+00:00 [Note] [Entrypoint]: Creating database blog
mysql         | 2021-04-05 20:46:40+00:00 [Note] [Entrypoint]: Creating user larauser
mysql         | 2021-04-05 20:46:40+00:00 [Note] [Entrypoint]: Giving user larauser access to schema blog
```

이제 디비 테이블을 만들 차례
```shell
docker-compose exec php php /var/www/html/artisan migrate
```
역시 에러 발생 ㅋㅋ
```
 Illuminate\Database\QueryException 

  SQLSTATE[HY000] [2002] Connection refused (SQL: select * from information_schema.tables where table_schema = laravelblog and table_name = migrations and table_type = 'BASE TABLE')
```
.env 파일을 수정해줘야한다
DB_HOST=127.0.0.1에서 mysql 로 바꿔준다
이러면 Migration table created successfully. 잘 만들어진다
___

일단 완성본 (라라벨 처음세팅에서 완벽하게 작동 25Mar 2021 : 
phpmyadmin 접속 문제로 안되다가 다시 완벽하게 작동 확인 06Apr 2021

nginx 서버로 라라벨 홈 화면 뜨는것 확인  localhost:8000 ,
phpmyadmin 로 접속해서 server: mysql, username, password: docker-compose.yml 파일에 정의된 걸로 로그인 성공, 디비는 toturial로 만들어서 maraiadb와 연동되어 
테이블까지 만들어 보는 걸로 테스트 성공! 
)

___
**Dockerfile**
파일명은 PHP.Dockerfile 로 함

```Dockerfile
FROM php:fpm

RUN docker-php-ext-install pdo pdo_mysql mysqli

RUN pecl install xdebug && docker-php-ext-enable xdebug

#COPY --chown=33:33 . .  
# 일단 로컬 호스트에서  chown -R 33:33 myblog(라라벨) 만 해도 됬었음
```

<br/>

docker-compose.yml 파일 업데이트 - 06APR 2021
```yml
version: "3.9"
services: 
  
  web:
    image: nginx:latest
    container_name: nginx
    networks: 
      - backend
    ports: 
      - "8000:80"
    volumes: 
        - ./default.conf:/etc/nginx/conf.d/default.conf  #최상위 디렉토리에 default.conf만들기
        - ./app:/var/www/html  # app 디렉토리도 생성한다해서 도커 nginx 서버와 매칭
    depends_on:
      - php
      - mysql

  php:
    # image: php:fpm #이렇게만 적으면 가장 최신버전을 받는다. 명시할 수도 있음 php:8.0-fpm , php:7.4-fpm 
    container_name: php
    networks: 
      - backend
    volumes:
      - ./app:/var/www/html  #이제 php를 app 디렉토리로 연결
    build:  # 위의 image는 제거
      context: .  # 현재 디렉토리
      dockerfile: PHP.Dockerfile  #PHP.Dockerfile 에서 필요한 것을 읽어와 build 한다 . 그냥 Dockerfile 로 만들고 이름도 Dockerfile해도 됨
    ports: 
      - "9000:9000"

  mysql:
    image: mariadb:latest
    container_name: mysql
    networks: 
      - backend
    restart: unless-stopped
    ports:
      - "3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: super89MD 
      MYSQL_DATABASE: laravelblog
      MYSQL_USER: larastarter
      MYSQL_PASSWORD: laracent0987
      SERVICE_TAGS: dev 
    volumes:
      - ./mysqldata:/var/lib/mysql
  
  phpmyadmin:
    image: phpmyadmin
    container_name: phpmyadmin
    networks: 
      - backend
    restart: always
    ports:
      - "8080:80"
    environment:
      - PMA_ARBITRARY=1
      - PMA_HOST= mysql
      - PMA_PORT= 3306

networks: 
  backend:

volumes:
  mysqldata: {}

```

<br/>

예전 기록 사용하지 말 것 
___
**docker-compose.yml
```yml
version: '3.5'

services: 
  web:
    image: nginx:latest
    container_name: nginx
    ports: 
      - 8000:80
    volumes: 
        - ./default.conf:/etc/nginx/conf.d/default.conf  #최상위 디렉토리에 default.conf만들기
        - ./app:/var/www/html  # app 디렉토리도 생성한다해서 도커 nginx 서버와 매칭
    depends_on:
      - php
      - mysql
  php:
    # image: php:fpm #이렇게만 적으면 가장 최신버전을 받는다. 명시할 수도 있음 php:8.0-fpm , php:7.4-fpm 
    container_name: php
    volumes:
      - ./app:/var/www/html  #이제 php를 app 디렉토리로 연결
    build:  # 위의 image는 제거
      context: .  # 현재 디렉토리
      dockerfile: PHP.Dockerfile  #PHP.Dockerfile 에서 필요한 것을 읽어와 build 한다 . 그냥 Dockerfile 로 만들고 이름도 Dockerfile해도 됨
    ports: 
      - 9000:9000

  mysql:
    image: mariadb:latest
    container_name: mysql
    restart: unless-stopped
    ports:
      - 3306:3306
    environment:
      MYSQL_ROOT_PASSWORD: my-secret-pw 
      MYSQL_DATABASE: tutorial
      MYSQL_USER: tutorial
      MYSQL_PASSWORD: secret
      SERVICE_TAGS: dev 
    volumes:
      - ./mysqldata:/var/lib/mysql
  
  phpmyadmin:
    image: phpmyadmin
    container_name: phpmyadmin
    links:
      - mysql  
    restart: always
    ports:
      - 8080:80
    environment:
      - PMA_ARBITRARY=1
      - PMA_HOST= db
      - PMA_PORT= 3306

volumes:
  mysqldata: {}

```

___
default.conf (nginx설정파일)  
먼저 순수 php 테스트용, app/pulic/index.php로 테스트
```
# server {
#     listen 80 default_server;
#     root /app/public;

#     index index.php index.html index.htm;

#     location ~ \.php$ {
#         fastcgi_pass php:9000;
#         fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
#         include fastcgi_params;
#     }
# }
```


2번째 본격 라라벨용, app을 지우고. 즉, app디렉토리를 라라벨 프로젝트로 대체  
아예 laravel new app 으로 프로젝트를 만든다 
(이게 좀 헛깔릴 수도 있는데, 중요한 것은 가장 상위 경로에서 뉴 프로젝트를 만들어주면 된다)

```
server {
    listen 80 default_server;
    index index.php index.html index.htm;
    server_name localhost;
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www/html/public;
    # root /app/public; # 라라벨 없이 php만으로 서비스 할 때 - 실제로 로컬 프로젝트디렉토리에 /app/public/index.php 로 테스트
    #/var/www/html/public 까지 올려주면 라라벨이 작동 - laravel로 새로운 프로젝트를 app 로 최상위 디렉토리에 만듬

    location / {
        try_files $uri $uri/ /index.php?$query_string;
    }

    location ~ \.php$ {
        try_files $uri =404;
        fastcgi_split_path_info ^(.+\.php)(/.+)$;
        fastcgi_pass php:9000;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }
}
```