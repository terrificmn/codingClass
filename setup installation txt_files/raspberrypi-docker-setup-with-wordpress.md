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
[도커 깃허브-docker-install 방문하기](https://github.com/docker/docker-install)

<br>

편하게 스크립트로 실행할 수 있게 되어 있다. 클론 받을 필요는 없고 코드 한 줄이면 된다

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
```

위의 코드는 바로 스크립트 파일을 다운받은 후 쉘에서 실행 시키는 방식


무난하게 설치가 완료되면..docker가 잘 실행이 되는지 확인해 보는데 간단하게 docker image ls 를 실행
```
$docker image ls
```
그러면
```
Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get http://%2Fvar%2Frun%2Fdocker.sock/v1.24/containers/json: dial unix /var/run/docker.sock: c
```
위처럼 퍼미션 거부가 된다.  

**(옵션)** 물론 sudo를 사용해서 하면 되지만 sudo 없이 하고 싶으면
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
docker로 할 수 있는 것을 추후 포스팅 할 예정이다~

<br>

# docker-compose 설치하기
이제 두 번째로 docker-compose를 설치해줘야하는데   
>잠깐: docker에서는 명령어로 이미지를 받고 컨테이너를 실행하게 된다. 
예를 들어서 우분투 이미지를 받아서 bash셀을 실행하고 싶다면 docker run -it ubuntu:18.04 /bin/bash 이렇게 하면 컨테이너가 실행이 되는데 이런식으로 명령어를 일일이 쳐줘야한다. 다행한 명령어가 있게 된다. run, ps, image 등등.. 다양한 명령어가 있다.

> 그래서 Dockerfile과 docker-compose.yml 파일을 이용해서 작성을 해주면 docker를 쉽게(?) 생성할 수 있게 해주는 것이 docker-compose 이다

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

>하지만 이번 경우는 예외 sudo 를 안 사용하면 제대로 설치가 안되는 문제가 발생~ 그래서 sudo를 꼭 사용해 주자

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

# 깃허브에서 다운받아서 준비하기
github에서 Dockerfile과 docker-compose.yml 파일을 다운로드 받는다.

<img src=2>
<br>

[제 깃허브에 가서 다운로드를 받으세요](https://github.com/terrificmn/docker-wordpress)

원하는 곳에 압축을 플어준다. 
```
$ cd ~/Downloads
$ unzip docker-wordpress-main -d docker-wordpress
```
그리고 원하는 디렉토리에 위치시켜준다.
내 경우에는 Projcest 디렉토리 안에 이동시켜줌

```
mv docker-wordpress ~/Projects/
```

디렉토리안에는   
.env
Dockerfile
default.conf
docker-compose.yml 파일이 있다.

이제 docker-wordpress 디렉토리로 이동한 후 src 디렉토리를 만들어 준다. 그리고 추가로 mysql데이터로 사용할 디렉토리도 만들어준다 
```
$ cd docker-wordpress
$ mkdir src
$ mkdir mysqldata
```

이렇게 되면 docker-compose를 사용하기 위한 준비가 됨.

> 중요~ mysqldata 디렉토리는 mysql의 데이터가 저장되는 장소가 되고
src 디렉토리안에는 wordpress를 설치하게 된다.

<br>

# DB 정보 설정해주기
도커를 사용 안하고 했다면 database를 만들어 주고 테이블도 만들어야 합니다. 하지만 도커로 build를 해서 도커가 실행될 때 데이터 베이스가 만들어 집니다.

docker-compose.yml 파일을 열어서 DB정보를 수정해 줍니다.
```
vi docker-compose.yml
```
파일 내용 중에 mysql의 environment 부분을 찾아서 정보를 수정하자
```
mysql:
    image: jsurf/rpi-mariadb 
    ...
    생략
    ...
    environment:
      MYSQL_ROOT_PASSWORD: secret-password  
    environment:
      MYSQL_ROOT_PASSWORD: root비번  
      MYSQL_DATABASE: wordpress
      MYSQL_USER: user아이디
      MYSQL_PASSWORD: user패스워드
```
database는 그대로 wordpress 로 해주면 되고 나머지는 원하는 id/비번을 넣어주면 된다.    
그리고 저장 하고 빠져나오기


이번에는   
.env 파일을 열어서 위와 같은  유저네임과 비번을 입력해주는데   

왜 비슷한 설정을 또 하냐면.. 추후 wordpress 프로그램 설치 후 db설정을 하는데  
이때 wordpress에서 환경 변수가 없으면 위에서 설정한 db id,패스워드를 인식을 못하는 문제가 발생한다. 그래서 docker 안에 환경변수로 만들어서 wordpress에서 인식할 수 있게 하려고 한다.

(숨김파일임에 주의하세요)

```
$ vi .env

WORDPRESS_DB_HOST=mysql:3306
WORDPRESS_DB_USER=user아이디
WORDPRESS_DB_PASSWORD=user패스워드
WORDPRESS_DB_NAME=wordpress
```
위의 DB_HOST는 mysql:3306 , DB_NAME 그대로 나둔다. (도커의 mysql 컨테이너 이름)  
user아이디, user패스워드를 docker-compose.yml 파일에서 설정한 그대로 해주세요  
저장 후 빠져나감 


<br>

# 이제 docker-compose를 실행해 보자~
다운받은 Dockerfile 이 있는 디렉토리로 이동하자
```
$cd ~/Projects/docker-wordpress
```
build를 해 준다
```
$ docker-compose build
```
Dockerfile과 docker-compose 파일에 되어 있는 그대로 각각의 컨테이너 이미지를 다운을 받아서 설치를 한다.

시간이 조금 걸릴 것이다.

그리고 나서 up 이라는 명령어를 실행한다. 그러면 컨테이너들이 실행되는데    
첫 실행이므로 필요한 다운로드 및 설치를 추가로 진행한 후 실행이 되게 된다.
```
$ docker-compose up
```
끌때는 control + c 를 눌러서 종료시키면 된다.

실행이 잘 된다면 이제 마지막으로 wordpress를 받을 차례다

<br>

# wordpress 다운 및 설치
먼저 홈페이지에서 다운을 받거나 zip파일과 tar.gz 형태를 제공
wget으로 받아도 된다. (wget으로 받으면 현재 경로에 받아지므로 주의)


```shell
$wget https://wordpress.org/latest.tar.gz
```
만약 다운이 안된다면 wordpress.org 에서 다운로드를 받으세요~  

이제 압축을 해제해준다
```
$cd ~/Downloads
$tar -zxvf wordpress-5.7.2.tar.gz
```

도커 파일이 위치한 곳으로 옮겨 준다. 도커파일일 위치한 디렉토리의 src 디렉토리 안으로 옮김

```
$mv wordpress/ ~/Projects/docker-wordpress/src/

```
이러면 압축이 풀린 디렉토리의 파일 전체가 이동된다

이제 wordpress의 소유권한을 미리 조정해 준다. 아파치 서버가 파일을 바꿀 수 있도록 www-data로 바꿔주는데   
www-data는 아파치 아이디를 뜻한다. (데비안계열에서 그러하다)

```
$ cd src
$ sudo chown -R www-data:www-data wordpress
```

<br>

# 이후는 wordpress 초기설정
웹 브라우저를 실행 시킨 후 localhost 라고 입력해주세요
이제 wordpress가 실행이 되면서 초기설정을 위한 화면이 나온다

<img scr=3>

처음으로 DB셋팅을 한다. docker-compose.yml 파일에서 했었던 대로  
입력해주면 되고, root로 해도 되고 user id로 설정했던 것을 해도 된다.

> 실무에서는 root보다는 하나의 유저를 만들어서 하나의 DB만 사용할 권한을 부여한다고 한다. 
왜냐하면 root는 너무 막강한 권한을 가지고 있기 때문에 권한을 나누는 것이다.

<br>

이 성공적으로 되었다면 이제 Wordpress 테마를 적용하고 꾸미면 된다!

<br>


