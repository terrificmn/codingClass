# phpmyadmin 오류 및 트러블 슈팅
phpmyadmin 오류 및 트러블 슈팅

## 트러블 슈팅: phpmyadmin 설치 중에 extensions 에러
phpmyadmin 설치 중.. 에러  (mysqli: extension)   
I receive an error about missing mysqli and mysql extensions.

php-mysql 을 설치하면 거의 해결됨
```
$sudo yum install php-mysql
```

**참고
To connect to a MySQL server, PHP needs a set of MySQL functions called “MySQL extension”.    
This extension may be part of the PHP distribution (compiled-in),   otherwise it needs to be loaded dynamically.   
Its name is probably mysqli.so or php_mysqli.dll. phpMyAdmin tried to load the extension but failed.   
Usually, the problem is solved by installing a software package called “PHP-MySQL” or something similar.   
There are currently two interfaces PHP provides as MySQL extensions - mysql and mysqli.    
The mysqli is tried first, because it’s the best one. (mysql은 deprecated될 예정-더이상 작동안함)   


## The secret passphrase in configuration (blowfish_secret) is too short.
트러블 슈팅 phpmyadmin 에러: phpmyadmin 로그인 할 때 아래 메세지가 나오면서 로그인 안되는 경우

```
The secret passphrase in configuration (blowfish_secret) is too short.
```
이런 경우 환경설정 파일 열기

```
$ sudo vi /usr/share/phpmyadmin/config.inc.php
```

아래 부분을 찾아서 길게 바꿔줘야한다   
```
$cfg['blowfish_secret'] = '84657495123845128452'; /* YOU MUST FILL IN THIS FOR COOKIE AUTH! */
``` 
길게 32케릭터로 바꿔준다   
(Replace the secret with a random string that is at least 32 characters long:)

예:   
$cfg['blowfish_secret'] = 'randomadmin'; 이렇게 되어 있던 것을   
$cfg['blowfish_secret'] = 'randomadmin0123456789randomadminlong'; 요렇게 길게 바꿈   


## ubuntu 우분투에서 phpmyadmin 설치 에러
에러 메세지
```
The requested PHP extension ext-mysqli * is missing on php
```
일때는 설치

```
sudo apt-get install php-mysql
```

아래같은 에러메세지 일때는
```
php-webdriver requires ext-curl 
```
설치 
```
sudo apt-get install php-curl 
```

이번에는 ext-zip 필요하다고 할 때
```
php-webdriver requires ext-zip 
``` 
설치한다
```
sudo apt-get install php-zip
```



## 라즈베리파이  404 page not found
phpmyadmin 설치 중에 (라즈베리파이 os 경우)  
404 page not found 에러가 발생할 경우  

소스 파일을 받아서 설치하는 것은 거의 동일하다   
중간에 경로가 다른게 있는데  
phpmyadmin.conf 파일을 아파치 디렉토리에 넣어줘야 하는데   
CentOS 같은 경우에는 /etc/httpd 디렉토리 로 되는 걸로 기억하는데

데비안 계열은 경로가 다르기 때문에    
당연히 다른 경로로 만들어 줘야하는데   
/etc/apache2 디렉토리쪽으로 만들어서 넣어줘야 한다.

```
$sudo vim /etc/apache2/conf-available/phpmyadmin.conf
```

--자세한 설치는 설치안내 참고--

이제 여기에서 문제인데 웹 브라우저에서 localhost/phpmyadmin   
을 하면 딱 하고 나와야 하는데 안된다.

404 page not found 에러가 발생  
apache2-debian 어쩌구 저쩌구 버전 나오고   
즉.. phpmyadmin 이라는 경로를 못찾는 것!  

의외로 심볼릭 링크를 해주면 쉽게 해결될 수 있다.   

먼저 원본파일 phpmyadmin.conf은 위의 경로에 있는데    
다른곳에 심볼릭 링크를 같은 파일로 만들어 주면 된다

```
$sudo ln -s /etc/apache2/conf-available/phpmyadmin.conf /etc/apache2/conf-enabled/phpmyadmin 
```

원본 파일이 /etc/apache2/conf-available/phpmyadmin.conf   
즉, conf-available 디렉토리 안에 있는 것이 원본임에 주의하자!

그리고 conf-enabled 디렉토리안에 심볼릭 링크를 만드는 것임   

li 명령어로 확인해보면, 심볼릭링크가 원본파일을 잘 가리키고 있다.  
```
$ls -li /etc/apache2/conf-enabled/phpmyadmin.conf
538585 lrwxrwxrwx 1 root root 43 May 12 02:23 /etc/apache2/conf-enabled/phpmyadmin.conf -> /etc/apache2/conf-available/phpmyadmin.conf
```

이제 웹 브라우저에서 localhost/phpmyadmin 엔터를 치면   
phpmyadmin 첫 로그인 페이지가 나온다


