docker_ngnix_php 디렉토리에 만들어둔 copy파일 참고할 것
projects/docker_nginx_php/nginx_php_mysql_phpmydamin_docker-compose copy

httpd 서버와 거의 비슷함
다만, ngnix 용 conf파일 설정만 다름
ngix의 ports  8000 이나 80으로 설정 
만약 로컬에서 httpd가 돌아가거나 다른 서비스가 하고 있으면 안될 수 있으니 적절히 열어주자

디렉토리는 app 으로 연결함, 즉 app 디렉토리도 만들어 주기
Dockerfile은 이름은 PHP.Dockerfile 로 해놈 
당황하지말고 최상단 경로에 복사해 만들어 놓으면 됨

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
```
$ laravel new app
```

그리고 다시 localhost로 가면
처음 라라벨 home이 나오면 완성!

php artisan 명령어를 사용하려면 docker-comopser exec 로 명령을 내려야함
풂패스를 적어준다
docker-compose exec php php /var/www/html/artisan migrate




현재 23mar2021 기준으로 다시 안되고 있음  
2주 스트림릿 하느라고 안했더니 작동을 안함;; 아래 내용이랑 유투브랑 다시 해서 해결할 것!!

___ 
일단 default.conf (nginx설정파일)
```
server {
    listen 80;
    index index.php index.html index.htm;
    server_name localhost;
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www/html/public;
    # root /app/public; # 라라벨 없이 php만으로 서비스 할 때 - 실제로 로컬 프로젝트디렉토리에 /app/public/index.php 로 테스트
    #/var/www/html/public 까지 올려주면 라라벨이 작동 - laravel로 새로운 프로젝트를 app 디렉토리 안에서 new프로젝트를 만든다(이름은 상관없음: 프로젝트명으로 하면 됨)

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
___


업데이트된 docker-compose.yml
```yml
version: '3.5'

networks:
  laravel:

services: 
  nginx:
    depends_on:
      - php
      - mysql
    networks:
      - laravel
    image: nginx:latest
    ports: 
      - 8000:80
    volumes: 
        - ./default.conf:/etc/nginx/conf.d/default.conf    
        # 아마 os때문일지는 모르겠으나 default.conf 라고 해야 됨(로컬파일을 nginx.conf) #우분투에서는 nginx.conf로 해야할지도
        - ./app:/var/www/html  # 위의 nginx.conf 파일은 같은 경로에 생성, app 디렉토리도 생성한다
  php:
    networks:
      - laravel
    build:  
      context: .  # 현재 디렉토리
      dockerfile: Dockerfile  # Dockerfile 에서 필요한 것을 읽어와 build 한다 . 그냥 Dockerfile 로 만들고 이름도 Dockerfile해도 됨
    volumes:
      - ./app:/var/www/html #이제 php를 app 디렉토리로 연결
    ports:
      - 9000:9000

  mysql:
    networks:
      - laravel
    image: mariadb:latest
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
    networks:
      - laravel
    image: phpmyadmin
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
마지막으로 Dockerfile  현재 유일하게 문제가 없는 파일 ㅠㅠ
```Dockerfile
FROM php:fpm

RUN docker-php-ext-install pdo pdo_mysql mysqli

RUN pecl install xdebug && docker-php-ext-enable xdebug
```





