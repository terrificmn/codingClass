docker_ngnix_php 디렉토리에 만들어둔 copy파일 참고할 것
projects/docker_nginx_php/nginx_php_mysql_phpmydamin_docker-compose copy

httpd 서버와 거의 비슷함
다만, ngnix 용 conf파일 설정만 다름
ngix의 ports  8000 이나 80으로 설정 
만약 로컬에서 httpd가 돌아가거나 다른 서비스가 하고 있으면 안될 수 있으니 적절히 열어주자


# 중요!! 테스트 해볼 것
git push를 다시해서 충돌나는지 확인해볼필요가 있음
modified:   package-lock.json
	modified:   package.json
	modified:   public/css/app.css
	modified:   resources/css/app.css
	modified:   resources/views/layouts/app.blade.php
	modified:   routes/web.php
footer를 pull 서버에서 pull 받았는데 
Updating 9e5a6ab..1ba1aff
Fast-forward
 resources/views/layouts/footer.blade.php | 2 +-

결과:
error: Your local changes to the following files would be overwritten by merge:
	resources/views/layouts/app.blade.php
Please commit your changes or stash them before you merge.
Aborting

app.blade.php 파일도 변경후 서버에서 pull 하니 충돌 ㅠ

서버쪽에서는 파일 수정을 안하려고 했는데 어쩔 수 없이 npm 빌드를 하면서 파일들이 수정이 되었고,
(오히려 초기화면으로 바뀐 부분도 있었음) 그래서
로컬에서는 최신버전일 상태이므로 아무 조금만 손을 봤다, 멘트 글자만 조금 바꿔서 다시 commit
그리고 나서 서버에서 pull을 하려고 하니 위의 파일들이 modified가 되어 있어서 pull이 안되는 것임

근데 몇번 해봤더니 꼭 위 처럼 할 필요가 없음. 상관은 없지만 
git checkout 해서 깃에서 pull받은 상태를 유지하는게 나은 거 같다. (수정 2021 04 28)

해결방안은 오히려 간단했다. 어차피 서버쪽에서는 수정된 것은 무시해버리고 
로컬의 최신 버전만 받아버리면 된다고 생각하니깐 편해짐 ㅋㅋ
서버쪽에서 modified 된 파일을 취소해버리면 되는 것임
```shell
git checkout -- resources/views/layouts/app.blade.php
```
git st를 해보면 resources/views/layouts/app.blade.php 가 빠져있게된다



## <트러블슈팅>

이제 웹브라우저에 localhost:8000 을 입력하면
아마도.. 이런 에러가 
```
UnexpectedValueException
The stream or file "/var/www/html/storage/logs/laravel.log" could not be opened in append mode: Failed to open stream: Permission denied 
```
퍼미션 에러 일때

도커 설정을 잘못한줄 알고, 퍼미션 에러인지도 모르고 반나절을 넘게 고생 ㅠ

소유자가  www-data 소유그룹 www-data가 되서   
sudo chown -R www-data:www-data blog 이런식으로 된다고 하는데    
그래서 chown을 하면 그룹이 없다고 함. 그래서 유저를 새로 만들려다가 찾아보니

ngnix는 uidd와 gid을 찾을 수 있는데..   
먼저 docker-compose up을 먼저 시킨 상태에서 아래 명령어로 실행을 해보면   
```
$sudo docker-compose exec web id www-data
```
결과:
```
uid=33(www-data) gid=33(www-data) groups=33(www-data)
```
이렇게 나오는데 

도커 라라벨 프로젝트에 권한을 주게되면 된다. 그러면 컨테이너도 그 권한으로 사용하게 된다고 함.    
chown 을 해서 소유자 변경을 해준다. 라라벨 프로젝트 디렉토리를 경로로 써주면 된다  
```
$ sudo chown -R 33:33 myblogapp
```

여기에서 소유자는 해당 소유자user로 남겨보자

```shell
$ sudo chown -R $USER:33 myblogapp
```
방법을 찾아야 할 듯... 왜냐하면 이제 여기에서의 git clone은 pull 만 할 것이고   
push는 안할 것임. (서버용이므로)  


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
phpmyadmin 로 접속해서 server: mysql, username, password: docker-compose.yml 파일에 정의된 걸로 로그인 성공, 
디비는 toturial로 만들어서 maraiadb와 연동되어   
테이블까지 만들어 보는 걸로 테스트 성공!   



## Dockerfile, docker-compose.yml 파일 예시
## 예전 버전이므로 사용하지말고 참고만 할 것


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

## 더 예전 기록 사용하지 말 것 
## 더 예전 기록 사용하지 말 것 
## 그냥 참고만

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
```conf
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

```conf
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