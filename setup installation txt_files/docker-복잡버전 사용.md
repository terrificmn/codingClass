# 도커 복잡버전 설치 
일단 
복잡버전Dockerfile 과 복잡버전docker_file.yml 를 사용하는데
깃허브에서 가져온거라 
내가 만든 방식이랑 합쳤음 실행은 잘 되나 
Dockerfile에서 설치하는 것이 너무 많아서 내가 웹 서비스에 
이런것들이 다 필요한지도 아직 다 모르겠고 
일단 PDO Xdebug 이런것들은 필요한 것 같은데 해보면서 
알아가야 할 듯 하다
어쨌든 중요한것은 이렇게 한번에 많이 설치를 하면
분명 어딘가에서는 에러가 나는 듯 하다. 그래서 성공하는데 1시간 넘게 걸림;;

일단 설명만 남겨놓자
아직까지는.. 그렇게까지 많이 설치는 필요없는 듯

아 라라벨로는 성공 못함!
아파치 설정을 어떻게 라라벨로 연결시키는지 모르겠음
 
(경로를 여기로 맞춰주면 되는 것 같은데;;;
root /var/www/html/public;)
참고::
https://blog.quickadminpanel.com/laravel-public-folder-how-to-configure-domains-for-in-apachenginx/

이제 도커 컨테이너가 잘 실행되는 것을 확인했다면 
http:localhost/public/index.php 
(public 디렉토리에 넣었다면)
잘 되는 것을 확인했으면

phpmyadmin 을 확인해본다, 빌드할 때 썼던 비번과 root 아이디 server는 db
http:localhost:8080
로 테스트로 테이블 하나 만들어 보면 잘 만들어지면 ok!


최종적으로 라라벨을 환경을 만들려면은 
docker-compose를 down해야할 것 처럼 보이지만 그렇지 않다
바로 여기서 라라벨 설치하면 됨

먼저
테스트로 썼던 src/public 은 필요없으므로 삭제

다시 scr로 이동해서 여기에서 
먼저 composer로 라라벨을 설치

$composer global require laravel/installer

라라벨 new 프로젝트를 만들어 준다
$laravel new myfirstapp

다시 페이지로 들어가서 확인


https://dev.to/veevidify/docker-compose-up-your-entire-laravel-apache-mysql-development-environment-45ea
참고 사이트

좀 더 완성된 버전에서는 
.env 파일에 UID변수로 설정한 것을 넣어줘야한다
마지막 줄에 
UID=1000
넣은 후 저장

그리고 경로가 다르므로 .env파일을 상위디렉토리로 복사시킨다


안 그러면 build 할 때 
WARNING: The UID variable is not set. Defaulting to a blank string.
WARNING: The UDI variable is not set. Defaulting to a blank string.
이렇게 나옴


그리고 아래의 에러는 
configure: error: Package requirements (oniguruma) were not met:

No package 'oniguruma' found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables ONIG_CFLAGS
and ONIG_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.


해결책:
Just remove mbstring from the docker-php-ext-install instruction.

The error is caused by a dependency problem - the mbstring extension requires the oniguruma library to make multibyte regular expression functions work. From the installation guide:

음.. mbstring을 빼란다



이게 문제가 될 수도 있을 듯
make: Circular jit/zend_jit.lo <- jit/zend_jit.lo dependency dropped.
계속 빨간

configure: error: Package requirements (libzip >= 0.11 libzip != 1.3.1 libzip != 1.7.0) were not met:

No package 'libzip' found
No package 'libzip' found
No package 'libzip' found

Consider adjusting the PKG_CONFIG_PATH environment variable if you
installed software in a non-standard prefix.

Alternatively, you may set the environment variables LIBZIP_CFLAGS
and LIBZIP_LIBS to avoid the need to call pkg-config.
See the pkg-config man page for more details.


해결책은  libzip-dev 설치
For PHP >= 7.3
#install some base extensions
RUN apt-get install -y \
        libzip-dev \
        zip \
  && docker-php-ext-install zip


또 다른 문제 일지도 모름
debconf: delaying package configuration, since apt-utils is not installed

다행히 문제는 안됨 ;;;
하지만 php artisan serve 로 작동을 해야해서 
localhost:8000 번으로 접속이 fobidden임 
좀 더 알아볼것 : 이 부분은 apache를 설정해야하는 것 같음

컨테이너 중지하기
먼저 docker ps -a로 본다. 그 후
docker stop (컨테이너id1) (컨테이너id2) ...
중지한 것은 다시 시작할때 dockerfile등이 변한게 없으면 바로 다시 시작됨


컨테이너 제거하기
먼저 docker ps -a로 본다. 그 후
docker rm (컨테이너id1) (컨테이너id2) ...
팁: 만약 아래와 같은 컨테이너 id가 2개 있다고 하면 다 쓸필요없이 일부분만 써주면 지워진다 (겹치지 않는다면..)
508a2f00e504
bbcaa7d84a10
예:
```
$ sudo docker rm 508 bbc
```

