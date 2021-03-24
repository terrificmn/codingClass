우분투에서 php8.0 설치
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php

Once the PPA is enabled, you can install PHP 8.
Installing PHP 8.0 with Apache

If you’re using Apache as a web server, you can run PHP as an Apache module or PHP-FPM.
Install PHP as Apache Module

Installing PHP as an Apache module is a straightforward task:

sudo apt update
sudo apt install php8.0 libapache2-mod-php8.0

근데 여기에서 당장 아파치는 필요하지 않아서 php8.0-fpm으로 설치함
PHP-FPM (“fastCGI process manager”)


Once the packages are installed, restart Apache for the PHP module to get loaded:

sudo systemctl restart apache2

php 버전 확인하기
$php -v
PHP 8.0.3 (cli) (built: Mar  5 2021 07:53:56) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.3, Copyright (c) Zend Technologies
    with Zend OPcache v8.0.3, Copyright (c), by Zend Technologies

상태확인하기
systemctl status php8.0-fpm

바로 active 상태인걸 알 수 있음

** 트러블 슈팅
(우분투 18.04 기준)
라라벨 뉴 프로젝트할 때 ext-mbstring 없다고 할 때 
sudo apt-get install php-mbstring

ext-dom이 없다고 할 때 
sudo apt install php-xml

위 2개를 설치 해주면 잘 설치된다 
