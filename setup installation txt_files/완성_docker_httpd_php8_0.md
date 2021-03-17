준비는 디렉토리 app, mysqldata 만들고
httpd도 만들고 안에 default.conf 파일 넣는다

app  디렉토리 안에 public 디렉토리 만들고 index.php 나 index.html
만들어서 아파치 서버 잘 도는지 확인 한 후 
성공하면 app 디렉토리 삭제

그리고 라라벨을 최상위 디렉토리에서 뉴프로젝트로 만들면 라라벨 준비 끝
그리고 라라벨 설치되면 
localhost:8000으로 접속해서 라라벨 페이지 뜨면 성공!


-----------------------default.conf 파일
<VirtualHost *:80>
    ServerName localhost

    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/public

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>


-------------Dockerfile
FROM php:apache

RUN docker-php-ext-install pdo pdo_mysql mysqli

RUN pecl install xdebug && docker-php-ext-enable xdebug

# Add the user UID:1000, GID:1000, home at /app
RUN groupadd -r app -g 1000 && useradd -u 1000 -r -g app -m -d /app -s /sbin/nologin -c "App user" app && \
    chmod 755 /var/www/html

# composer다운 일단 로컬에서 실행할 수 있으니깐 패스
#RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer

USER app

WORKDIR /var/www/html

USER root

COPY ./httpd/default.conf /etc/apache2/sites-enabled/000-default.conf

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80


-------------------------------
docker-compose.yml

version: '3'

services: 
  php:
    environment: 
      - APACHE_RUN_USER=#1000
    build:
      context: ./httpd  # httpd안에 있는 default.conf파일 (아파치)
      context: .
      dockerfile: Dockerfile
    ports: 
      - 8000:80
    volumes:
      - ./app:/var/www/html

  mysql:
    image: mariadb:latest
    restart: unless-stopped
    ports:
      - 4306:3306
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
