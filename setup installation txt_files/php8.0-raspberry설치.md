PHP is a programming language that commonly used to create a web applications and dynamic websites. With each release of PHP, new features and various changes are introduced.

This tutorial shows how to install PHP 8.0 on Raspberry Pi.

Connect to Raspberry Pi via SSH and execute commands to download GPG key and add repository.
1
2
3
중요 3개는 반드시 해줘야 함. 차레차례 하면 됨
```	
sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg

echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list

sudo apt update
```

Then install PHP 8.0 with command line interface (CLI):가 필요하면 php8.0-cli 설치

cli는 필요없을 것 같아서 뺏는데 다 설치되는 듯( 아마 의존성 때문에..)
```
sudo apt install php8.0-common
```

버전 체크 
```
php -v
```
잘 설치 된다
```
PHP 8.0.5 (cli) (built: May  3 2021 11:58:58) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.5, Copyright (c) Zend Technologies
    with Zend OPcache v8.0.5, Copyright (c), by Zend Technologies
```

이제 중요한 익스텐션 설치해주기. 이게 없으면 뭔가 실행이 잘 안됨
	
```
sudo apt install -y php8.0-curl php8.0-gd php8.0-mbstring php8.0-xml php8.0-zip php8.0-mysqlnd
```

이제 설치된 모듈 확인해보기.. 흠.. 그냥 확인차원
'''
php -m
```


PHP integration with MySQL or MariaDB

In order to use PHP with MySQL or MariaDB database we need to install the following extension:
1
	
sudo apt install -y php8.0-mysql
PHP integration with Apache


아마 따로 설치하려고 해도 이미 apache2는 설치가 되는 듯 하다.

If we want to integrate PHP with Apache HTTP server then install the following extension:
1
	
sudo apt install -y libapache2-mod-php8.0

Once installation was completed restart Apache.
1
	
sudo service apache2 restart

