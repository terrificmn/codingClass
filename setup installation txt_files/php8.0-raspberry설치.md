# 라즈베리파이에서 PHP 8.0 설치 하기

RPG키 다운로드와 레퍼지토리 추가를 해줘야한다.  
차레차례 하면 된다.
```	
sudo wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg

echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php.list

sudo apt update
```
마지막으로 apt update를 하면 필요한 업데이트가 이루어지면서 php8.0을 설치할 준비가 된다.

CLI (Command Line Inferface):가 필요하면 php8.0-cli 설치..  
하지만.. cli는 필요없을 것 같아서 뺏는데 다 설치되는 듯( 아마 의존성 때문에..)  

이제 본격적인 설치를 하자~
```
sudo apt install php8.0-common
```

설치가 완료되면 버전 체크도 해준다.
```
php -v
```

잘 설치가 되었음~
```
PHP 8.0.5 (cli) (built: May  3 2021 11:58:58) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.5, Copyright (c) Zend Technologies
    with Zend OPcache v8.0.5, Copyright (c), by Zend Technologies
```

이제 중요한 익스텐션 설치해주기. 처음에는 상관없지만,   
본격적으로 extension이 필요할 때 없으면 에러가 발생할 것이므로.. 설치를 해준다.
예를 들어 mysqlnd 같은 경우는 PDO를 사용할 때 필요
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

