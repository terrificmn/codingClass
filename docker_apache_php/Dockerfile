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