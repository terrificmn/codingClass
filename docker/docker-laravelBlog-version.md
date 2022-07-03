# Jun 23 2021 LaravelBlog version
여태껏 정리해놓은게 없어서 현재 사용하고 있는 내 블로그 버전을 올려놓음

그리고 처음 환경 셋팅 시 현재 내용을 복사해서 사용해도 되고, 
그 이후 설정은 

blog프로젝트 시작 composer_frontend.md 를 참고해서 실행



# Dockerfile
```Dockerfile
FROM php:fpm

RUN docker-php-ext-install pdo pdo_mysql mysqli

RUN pecl install xdebug && docker-php-ext-enable xdebug
```

# docker-compose.yml
```
version: "3.8"

services:
    web:
        image: nginx:latest
        container_name: nginx
        ports:
            - "8000:80"
        volumes:
            - ./default.conf:/etc/nginx/conf.d/default.conf  #최상위 디렉토리에 default.conf만들기
            - ./src:/var/www/html  # src 디렉토리도 생성한다해서 도커 nginx 서버와 >매칭

        depends_on:
            - php
            - mysql
        networks:
            - laravel

    php:
        container_name: php
        volumes:
            - ./src:/var/www/html  #이제 php를 src 디렉토리로 연결
        build:
            context: .
            dockerfile: Dockerfile
        ports:
            - "9000:9000"
        networks:
            - laravel

    composer:
        image: composer:latest
        container_name: composer
        volumes:
            - ./src:/var/www/html
        working_dir: /var/www/html # 컨테이너 어디에 파일들이 있을 지를 결정
        networks:
            - laravel
        #$ docker-compose run --rm composer require tailwindcss(필요한라이브러리)

    npm:
        image: node:14.16 #stable 버전
        container_name: npm
        volumes:
            - ./src:/var/www/html
        working_dir: /var/www/html
        entrypoint: ['npm']
        networks:
            - laravel
        #entrypoint: ['npm', '--no-build-links']  # docker-composer run 이 실행될 때 실행된다고 함
    # $ docker-compose run -rm npm install
    # npm으로 로컬에서 하듯이 json파일을 이용 패키지들을 다운 되어 진다
    # 이후 
    # $ docker-compose run --rm npm run dev 
    # 으로 실행을 하면 mix를 진행하게 됨 

    artisan:
        build:
            context: .
            dockerfile: Dockerfile
        container_name: artisan
        volumes:
            - ./src:/var/www/html
        depends_on: # dependency 필요 
            - mysql
        working_dir: /var/www/html
        entrypoint: ['/var/www/html/artisan']
        networks:
            - laravel
        # docker-compose run --rm artisan migrate 로 하면 된다! 오 굿!! (짧아짐!!)

    mysql:
        image: mariadb:latest
        container_name: mysql
        restart: unless-stopped
        ports:
            - "3306:3306"
        environment:
            MYSQL_ROOT_PASSWORD: blogroot
            MYSQL_DATABASE: laravelblog
            MYSQL_USER: larablog
            MYSQL_PASSWORD: larablog89MD
            SERVICE_TAGS: dev
        volumes:
            - ./mysqldata:/var/lib/mysql
        networks:
            - laravel

    phpmyadmin:
        image: phpmyadmin
        container_name: phpmyadmin
        networks:
            - laravel
        restart: always
        ports:
            - "8080:80"
        environment:
            - PMA_ARBITRARY=1
            - PMA_HOST= mysql
            - PMA_PORT= 3306

networks:
    laravel:

volumes:
    mysqldata: {}
```


# default.conf
```conf
server {
    listen 80 default_server;
    index index.php index.html index.htm;
    server_name localhost;
    error_log /var/log/nginx/error.log;
    access_log /var/log/nginx/access.log;
    root /var/www/html/public;
    # root /app/public; # 라라벨 없이 php만으로 서비스 할 때 - 실제로 로컬 프로>젝트디렉토리에 /app/public/index.php 로 테스트
    #/var/www/html/public 까지 올려주면 라라벨이 작동 - laravel로 새로운 프로젝>트를 app 로 최상위 디렉토리에 만듬

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