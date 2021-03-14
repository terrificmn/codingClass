FROM httpd:2.4
COPY src/public/ /usr/local/apache2/htdocs/


FROM php:8.0-fpm-alpine

RUN docker-php-ext-install pdo pdo_mysql
