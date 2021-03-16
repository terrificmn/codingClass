참고 사이트:
https://inovector.com/blog/minimal-configuration-docker-to-run-laravel-application


dockerfile.yml에 
web부분 environment: 설정에서 
bulid:
    context: ./httpd  # 현재 httpd 디렉토리를 하나 만들고 그 안에 default.conf 파일을 만든다

그러면 대충 이런 yml파일의 모습은 아래처럼 됨

version: '3.5'

services: 
  web:
    environment:
    - APACHE_RUN_USER=#1000
    build:
      context: ./httpd
    ports:
    - 8000:80
    volumes:
    - ./app:/var/www/html
    

대개 cotext에서 Dockerfile로 연결되게 되는데 context로만 연결해놓으면 그 안의 default.conf만 읽는 듯 하다

default.conf 만들고 내용 추가
----------------------------default.conf------------------------------------
<VirtualHost *:80>
    ServerName localhost

    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/public

    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

여기에서 DocumentRoot를 설정해줌 /var/www/html/public

그러면 이 default.conf파일을 도커 컨테이너에 copy를 해주는 것 같다 
그 내용은 다시 Dockerfile을 만들어서 그 안에 넣는다

-----------------------------------------Dockerfile을----------------------------
그 내용임
FROM php:8.0-apache

RUN apt-get update && apt-get install -y \
    		libfreetype6-dev \
    		libpng-dev \
    		libwebp-dev \
    		libjpeg62-turbo-dev \
    		libmcrypt-dev \
    		libzip-dev \
    && docker-php-ext-install \
    pdo_mysql \
    gd \
    zip \
    && a2enmod \
    rewrite

# Add the user UID:1000, GID:1000, home at /app
RUN groupadd -r app -g 1000 && useradd -u 1000 -r -g app -m -d /app -s /sbin/nologin -c "App user" app && \
    chmod 755 /var/www/html

RUN php -r "readfile('http://getcomposer.org/installer');" | php -- --install-dir=/usr/bin/ --filename=composer

#upload #php.ini 파일 업로드 맥스 제한 하는 것
RUN echo "file_uploads = On\n" \
         "memory_limit = 500M\n" \
         "upload_max_filesize = 500M\n" \
         "post_max_size = 500M\n" \
         "max_execution_time = 600\n" \
         > /usr/local/etc/php/conf.d/uploads.ini

USER app

WORKDIR /var/www/html

USER root

COPY default.conf /etc/apache2/sites-enabled/000-default.conf

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80



-----------------------------------------------


대충정리한  버전
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

COPY default.conf /etc/apache2/sites-enabled/000-default.conf

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

EXPOSE 80