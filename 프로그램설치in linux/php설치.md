# php 설치
php 설치

## dnf로 php 설치 (common extensions 포함)
dnf로 php 설치
```
$ sudo dnf -y install php php-cli php-php-gettext php-mbstring php-mcrypt php-mysqlnd php-pear php-curl php-gd php-xml php-bcmath php-zip
```
아마 이렇게 하면 7.4버전 쯤이 깔림 

현재는 버전 업이 되어 있을 수도 있음. 하지만 레포지터리에 올리는 것을 보수적으로 접근을 하기 때문에 좀 시간이 걸릴 수도 있다.

libxml2 가 없다고 할 때 
```
sudo yum install libxml2-devel
```


## php 8.0 다운 및 설치
EPEL 받기   
> EPEL, short for Extra Packages for Enterprise Linux, 라고 함

기본적으로 받을 수 없던 추가 패키지를 받을 수 있게 해줌   
```
$sudo yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

Remi repository는 third-party 저장소이며, 7.2~버전 부터 8.0까지 제공 하는 듯   
어쨋든 설치   
```
$sudo yum install http://rpms.remirepo.net/enterprise/remi-release-8.rpm
```
설치한 모듈 리스트 보기

```
$sudo yum module list PHP   
```

맨 아래에 php remi-8.0 이 보일 것임

8.0버전 사용가능하게 만들기 (리셋, enable)  
```
$sudo yum module reset php
$sudo yum module enable php:remi-8.0 
```
이제 설치
```
$sudo yum install php
```
아파치 서버 깔기
```
$sudo dnf install php php-cli php-common
```
만약 아파치 먼저 깔았다면 설치 되어 있다고 나오는

설치 PHP 8.0 for Nginx하려면 (이것도 web server 인듯 하다)
```
$sudo dnf install php php-cli php-common php-fpm
```
사용안하니깐 스킵 (설치 안함)

마지막으로 버전 확인
```
$php -v
```
PHP 8.0.2 ~~~ 나오면 설치 성공

```
$sudo systemctl restart httpd
```

그리고 /var/www/html/에 파일하나 test.php로 만들고 hello world라든가 phpinfo();    
찍어보면 됨
