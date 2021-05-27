# 라즈베리파이에 docker를 설치하자~
도커를 설치해보자~ 라즈베리파이는 오히려 스크립트로 설치할 수 있게 되어 있다.  
다른 CentOS, Ubuntu에서 적용되는 도커 사이트에 나오는 방식대로 하면 설치가 안된다.

<img src=0>
<br>
공식 사이트를 보면 설치 명령어를 사용하는 방법이 나와있는데    
위의 사진을 보면 Raspbian 사용자는 그 방식을 사용할 수 없다고 되어 있다  
대신에 편한 스크립트로 할 수 있게 깃허브를 제공한다. 
그래서 인지 더 쉬운 것 같다    

[도커엔진 공식 사이트](https://docs.docker.com/engine/install/debian/)

<br>

라즈베리파이는 따끈따근하게 처음으로 구워진 상태 입니다.
(한글 관련 프로그램만 설치된 상태)

<img src=1>
<br>

먼저 apt update를 합니다.
```
$sudo apt update
```

위에서 언급 한 것 처럼   
[도커 깃허브-docker-install](https://github.com/docker/docker-install)

<br>

편하게 스크립트로 실행할 수 있게 되어 있다. 클론 받을 필요는 없고 코드 한 줄이면 된다

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

위의 코드는 바로 스크립트 파일을 다운받은 후 쉘에서 실행 시키는 방식
이제 알아서 설치를 진행 한다.

설치가 다 끝나게 되면 sh파일은 지워도 무방하다. (명령어를 실행한 위치에 파일이 저장됨)

무난하게 설치가 완료되면..실행을 확인해보는데 간단하게 docker image ls 를 실행
```
$docker image ls
```
그러면
```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json: dial unix /var/run/docker.sock: connect: permission denied
```

위처럼 퍼미션 거부가 된다.  

물론 sudo를 사용해서 하면 되지만, 혹시라도 sudo 없이 하고 싶으면
docker 그룹에 pi 유저를 등록해준다.

```
sudo usermod -aG docker pi
```
이제 sudo를 안붙여도 된다.

<br>

## (옵션사항) docker작동 확인하기
docker가 작동이 잘되는지 확인해 보려면 도커를 실행해 본다. 
```
docker run hello-world
```
으로 작동을 하면 메세지가 나온다.
확인해보자

```
Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
...
...
```
docker가 정상적으로 작동을 하고 있다

이제 받은 이미지 지우기
```
docker image rm hello-world
```

<br>

# docker-compose 설치하기
이제 두 번째로 docker-compose를 설치해줘야하는데   
>잠깐: docker에서는 명령어로 이미지를 받고 컨테이너를 실행하게 된다. 
예를 들어서 우분투 이미지를 받아서 bash셀을 실행하고 싶다면 docker run -it ubuntu:18.04 /bin/bash 이렇게 하면 컨테이너가 실행이 되는데 이런식으로 명령어를 일일이 쳐줘야한다. 다행한 명령어가 있게 된다. run, ps, image 등등.. 다양한 명령어가 있다.

> 그래서 Dockerfile과 docker-compose.yml 파일을 이용해서 작성을 해주면 docker를 쉽게(?) 생성할 수 있게 해주는 것이 된다.

<br>

여기에서도 다른 리눅스 디스트리뷰션과는 다른 방식을 사용해야하는데, 

왜냐하면 ARM 패키지이기 때문에 안된다고 한다. 원래는 미리 빌드가 된 binaries를 이용해서 설치를 하는데  
라즈베리파이는 아키텍쳐가 64비트가 아니여서 설치가 안됨.

다행히 파이썬으로 설치가 가능해서 설치를 진행할 수 있다.  
그래서인지 docker-compose 설치도 더 쉽다. 

먼저 필요한 의존성 패키지를 깔아줘야한다.  
라즈베리파이에서 apt update까지 하면 파이썬 버전은 3.7이 설치가 되어 있는데 이를 이용하면 된다.

```
sudo apt update
sudo apt install -y python3-pip libffi-dev

```

그리고 docker-compose를 본격 설치, 
```
sudo pip3 install docker-compose
```
> 원래 파이썬에서 패키지를 관리해주는 pip으로 install를 할 때에는 sudo 사용 안하는 것이 좋다.
왜냐하면 sudo권한으로 설치가 되어서 패키지를 실행할 권한이 꼬일 수 있기 때문이라고 한다.
하지만 docker-compose는 예외이다. sudo 없이 하면 제대로 설치가 안되므로 꼭 sudo 를 넣어서 설치해준다

<br>

이제 버전 확인 해보기
```
$docker-compose version
```
```
docker-compose version 1.29.2, build unknown
docker-py version: 5.0.0
CPython version: 3.7.3
OpenSSL version: OpenSSL 1.1.1d  10 Sep 2019

```
처럼 나오면 성공!

<br>

# apache2 서버의 root 디렉토리 설정하기
아파치 default.conf 파일을 조정함에 따라서 보여지는 어느 디렉토리에 따라 달라지는데  

DocumentRoot /var/www/html  
위처럼만 하면 브라우저에 localhost 만 입력하면 메인페이지가 작동한다.

docker-wordpress로 이동해서 설정파일을 수정한다.
```
cd ~/Projects/docker-wordpress
vi default.conf
```
을 열어준다

그리고 아래처럼 수정해준다
```
DocumentRoot /var/www/html  
```
저장 후 빠져나온다.

이제 Dockerfile이 있는 디렉토리에 보면 src 디렉토리가 있다.  
이동 후 index.php 파일을 만들어보자

```
$ cd src
$ vi index.php
```
파일이 열리면
```
hello world
```
만 적어주고 저장을 한다. (html을 알면 html태그를 적어도 좋다)   
(php코드는 생략)

이제 브라우저에 localhost를 입력하자 
hello world가 잘 나올 것이다.

> 먼저 docker-compose up 으로 도커 컨테이너가 실행이 되어야한다

<br>

이제 wordpress를 다운받은 후 src 디렉토리 안에다가 이동시키자

브라우저에 localhost/wordpress 만 입력하면 설치페이지가 뜨게 된다!

<br>

## 아파치2 서버의 root디렉토리를 wordpress의 디렉토리로 맞춰주기

원래 wordpress 다운받았으므로 localhost/wordpress 라고 입력을 해줘야 하지만   
아파치 서버의 root 디렉토리를 wordpress까지 해주면 -> 이게 src/wordpress 로 연결이 되게 된다.

결과적으로 localhost만 브라우저에 입력해주면 된다.

wordpress.org 에서 wordpress를 받은 다음에 src 디렉토리 아래에 이동시키고    
src/wordpress 이렇게 위치했다면

다시 default.conf 파일을 수정해준다.
```
DocumentRoot /var/www/html/wordpress
```
저장 후 나온다.

위의 설정을 바꾸려면 다시 docker-compose build를 해야하는데

```
error checking context: 'can't stat '/home/pi/Workspace/docker-wordpress/mysqldata/mysql''.
ERROR: Service 'php' failed to build : Build failed
```
다시 build를 하려면 에러가 발생  

mysqldata 디렉토리 안에 있는 파일을 지워준다.
```
cd mysqldata
$sudo rm -rf ./*
```

그리고 다시 빌드를 해준다. 빌드가 끝나면 up으로 도커가 실행이 되게 해주면 된다.
```
$docker-compose build
$docker-compose up
```

이제 마치 심볼릭링크가 되어 있는 것 처럼 아파치 웹 서버의 기본 루트가 /var/www/html 인데  
wordpress 까지 해주면은 /var/www/html/wordpress 가   
내 프로젝트의 src/wordpress로 연결되는 것 같다
(정확한 비유인지는 모르겠다. ㅋㅋ)

이제는 브라우저에 localhost만 입력해주면 된다. 
wordpress 설치 페이지가 나오면 잘 된 것이다

<br>

# wordpress 설치
먼저 홈페이지에서 다운을 받거나 zip파일과 tar.gz 형태를 제공
wget으로 받아도 된다. (wget으로 받으면 현재 경로에 받아지므로 주의)


```shell
$wget https://wordpress.org/latest.tar.gz
```
압축을 해제해준다
```
$cd ~/Downloads
$tar -zxvf wordpress-5.7.2.tar.gz
```

도커 파일이 위치한 곳으로 옮겨 준다. 도커파일일 위치한 디렉토리의 src 디렉토리 안으로 옮김

```
$mv wordpress/ ~/Projects/docker-wordpress/src/

```
이러면 압축이 풀린 디렉토리의 파일 전체가 이동된다

그리고 나서, 권한 관련해서 소유자와 소유그룹을 apache2로 반반 나눠갖기
```
$cd ~/Projects/docker-wordpress/src
$sudo chown -R pi:www-data wordpress/
```
-R 옵션을 넣었기 때문에 wordpress 이하의 소유권도 바뀐다 


# 이후는 wordpress 초기설정
처음에 브라우저에 아파치루트를 안바꿨다면 localhost/wordpress 또는 (바꿨다면) localhost
라고 하면  이제 초기 셋팅이 시작된다.

Database에는 wordpress
이는 초기 도커-컴포즈 파일에서 만든 데이터 베이스
username과 password 는 root가 아닌 일반 사용자로 만들었던 것으로 하자
Database Host 에는 그대로 localhost로 하면 된다



## wordpress 관련 db설정하기
또 트러블 슈팅;;
wordpress에서 유저 정보를 넣는 곳에서 넘어가지를 않는다.
유저 db 정보를 .env 파일을 만들어서 다시 리빌드를 해줘야한다.

```
WORDPRESS_DB_HOST=mysql:3306
WORDPRESS_DB_USER=wpraspi
WORDPRESS_DB_PASSWORD=wpraspi1234
WORDPRESS_DB_NAME=wordpress
```
db host는 mysql 컨테이너 이름이 된다. mysql로  적어주면 된다. 

정리하자면,, wordpress 관련해서 디비정보를 넘겨줄 수가 없는 것 같다.. 
그래서 ..env 파일을 만들어서 하면 환경변수 도커내에서 생성이 되어서 잘 실행 되는 것 같다

만약 docker unable to write to wp-config.php file 에러가 발생한다면

/src/wordpress의 권한을 아파치 권한으로 바꿔줘야한다
```
$sudo chown -R www-data:www-data wordpress
```


원래대로라면 mariadb에 접속해서 해당 디비인 wordpress의 권한을 갖는 사용자를 만들어주는게 좋지만
도커를 만들 때 이미 유저를 만들었기 때문에 그대로 사용하면 되어서 그냥 끝




혹시라도 문제가 있을 경우 
[워드프레스 how to install WordPress 참고하기](https://wordpress.org/support/article/how-to-install-wordpress/)

이제 워드프레스 페이지가 로딩이 되면서 기본 설정 및 
그리고 db관련해서 설정도 해준다
워드프레스로 사용할 아이디/비번을 등록하게 된다
위에서 만들어준 mariadb 유저인 wp_admin 및 데이터베이스는 wordpress 비번 등을 입력해주게 되면 된다.

이제 로그인을 해서 원하는 테마로 바꿔주면 된다