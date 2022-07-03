# php 관련 에러 모음

## php로 웹페이지를 볼 때 에러메세지가 아예 안나오고 하얀 화면만 나올 때
php.ini 에러 메세지 (브라우저에서) 나오게 하기  
**참고 CentOs8에서는 /etc/php.ini 파일이 위치한다 (phpinfo();함수를 사용하면 위치를 알 수 있기도 하다)   
파일 열기  
```
$vi /etc/php.ini 
```

**error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT** 부분을 찾는다    
각각 &로 구분하고 ~를 붙이면 관련된 에러메세지는 표시하지 않게 됨  

**참고 설명   
PHP 5.3 or later, the default value is E_ALL & ~E_NOTICE & ~E_STRICT & ~E_DEPRECATED.    
This setting does not show E_NOTICE, E_STRICT and E_DEPRECATED level errors.

그 다음
display_errors = Off 를 On으로 바꿔준다
```
display_errors = On
```

그 후 PHP-FPM 서비스를 재시작 해줘야한다  
```
$systemctl restart php-fpm  
# 또는 
$service php-fpm restart
```

사이트가 실제 돌아가는 상황이라면 보안상 display_errors를 off로 해야함    
off로 했을 경우 php코드로 ini_set을 나오게 할 수는 있다.  
```php
<?php 
error_reporting(E_ALL);
ini_set('display_error', '1');
?>
```

[참고: http://php.net/error-reporting](http://php.net/error-reporting)


## php로 file을 업로드 하는 것을 코딩할 때 파일을 올려도 저장이 안될 때 해결
php로 file을 업로드 하는 것을 코딩할 때 파일을 올려도 저장이 안될 때 해결   
특히 대부분 리눅스 웹서버 세팅에서는 쓰기 권한이 필요한 경우에도    
디렉토리 권한을 755로 설정하라는 안내가 많기 때문에    
move_uploaded_file 함수가 이미지 파일을 옮길 수가 없게 된다.   
이 함수는 임시로 저장된 파일을 이동시키는 것을 하는데 권한 때문에 파일이 안 보이게 됨   

757로 설정하고 나면 업로드가 잘 된다.   
> 중요!!  
단, 디렉토리에 익명 쓰기 권한을 주고 나면 반드시 코딩으로 확장자 체크 등을 통해서   
악성 파일이 업로드되는 것을 막아야 하고 가급적이면 익명 쓰기 권한을 주는 폴더를   최소화해야 한다고 함

sudo chmod 0757 {디렉토리명} 
```
$chmod 0757 uploads
```
이렇게 하면   
drwxr-xr-x. 2     6 Nov 17 18:22  uploads (사용 전)   
drwxr-xrwx. 2     6 Nov 17 18:22  uploads (사용 후)   
변경이 되는것을 알 수 있고, php 에서도 move_uploaded_file()을 사용해도 파일이 잘 저장된다.

other users 권한도 7로 줬기때문에 읽기쓰기실행 다 되므로 보안상 문제일 수 있는데,  
안 그러면 move_uploaded_file()함수로 저장이 안되서 더 좋은 방법이 있는지는 더 공부가 필요 -20.11.18  


## php 에러 Fatal error: Call to undefined function mysqli_connect()
```
Fatal error: Call to undefined function mysqli_connect()
Fatal error: Uncaught PDO Exception: could not find driver in /var/www/html/test.php:43 Stack trace: #0 /var/www/html/test.php(43): PDO->__construct() #1 /var/www/html/test.php(57): Dbh->connect() #2 /var/www/html/test.php(87): Test->getUsers() #3 {main} thrown in /var/www/html/test.php on line 43
```
php 8 버전, 마리아db는 10.5.9 인데, 전에 7.4 설치할 때랑은 다르게 의존성을 많이   안깔아주고 시작한듯 함  
remi-repo 통해서 설치했는데    
처음에 mysqli로 테스트 했는데 실패   
PDO로 했는데도 실패   
계속 에러가 나서 찾다보니, phpinfo()사용해서 보니 sqlite는 표시되는데 mysql은 없는 것 같음

깔려있는지 확인은 
```
$php -m 
```
그러면 php 깔려있는 모듈을 보여줌   
그런데 많은 모듈 중에 pdo_sqlite 만 보임 뭔가 이상

검색 결과 mysql드라이버가 없어서 그랬음

**추가정보:   
php-mysqlnd 에 대해서 정보 보기  
```
$ sudo yum info php-mysqlnd
```

결과
```
Available Packages
Name         : php-mysqlnd
Version      : 8.0.2
Release      : 1.el8.remi
Architecture : x86_64
Size         : 259 k
Source       : php-8.0.2-1.el8.remi.src.rpm
Repository   : remi-modular
Summary      : A module for PHP applications that use MySQL databases
URL          : http://www.php.net/
License      : PHP
Description  : The php-mysqlnd package contains a dynamic shared object that will add
             : MySQL database support to PHP. MySQL is an object-relational database
             : management system. PHP is an HTML-embeddable scripting language. If
             : you need MySQL support for PHP applications, you will need to install
             : this package and the php package.
             : 
             : This package use the MySQL Native Driver
```

그래서 바로 설치
```
$sudo yum install php-mysqlnd
```

재시작
```
$systemctl restart php-fpm
``` 
그리고 해보면 DB에서 데이터 잘 가지고 와서 보여줌  
phpinfo() 를 해보면  
mysqlnd 8.0.2 와 mysqlnd 가 추가됨

PDO항목에도   
PDO drivers 에 sqlite 만 있었는데 mysql 이 추가됨  
PDO Driver for MySQL 도 추가됨 등등..   

다시 설치된 모듈 확인 해보면
```
$php -m 
```

mysqli, mysqlnd, pdo_mysql

가 설치된것 확인 . 굿!


## could not find driver (SQL: select * from information_schema.tables
요런 에러는 (처음에 라라벨 하면서 여기저기 설치하다보니 pdo설치 깜빡함;;)   
```
could not find driver (SQL: select * from information_schema.tables where table_schema = laravelblog and table_name = migrations and table_type = 'BASE TABLE')
```

-m은 설치된 모듈을 보여줌
```
$ php -m | grep -i pdo
```
해보면 PDO는 있는데 드라이버가 안보임 (pdo_mysql가 없음)

우분투에서는 
```
$sudo apt install php-mysql
```
설치하고 다시 $ php -m | grep -i pdo 하면 pdo_mysql이 보이고  
서버 가동해서 phpinfo(); 함수로 호출해봐도 PDO support 부분에  
PDO drivers 가 no value에서 mysql로 생김  

(단, 라라벨이라면 서버를 재가동시킨다. ^c 이후 php laravel serve)

우분투에서 laravel new myproject 로 생성하려고 하면  
```
laravel/framework requires ext-mbstring * -> it is missing from your system. Install or enable PHP's mbstring extension

phpunit/phpunit require ext-dom * -> it is missing from your system. Install or enable PHP's dom extension
```
2가지의 에러, 친절하게도 extension없으니 깔아달라고 한다

```
$sudo apt install php-mbstring
$sudo apt install php-xml
```
위 2개를 를 설치해주면 간단히 해결된다


## localhost로 접근하면 Unable to connect 일때
Firefox can’t establish a connection to the server at localhost.  

위와 같은 에러가 발상할 시

이건 그냥 httpd가 서비스 되고 있는지 확인하면 된다
```
$systemctl start httpd
```
우분투는 
```
$systemctl start apache2
```