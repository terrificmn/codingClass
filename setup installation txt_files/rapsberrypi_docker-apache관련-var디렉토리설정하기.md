# (추가 옵션 테스트) apache2 서버의 root 디렉토리 설정하기 (기본으로 설정)

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
이제 Dockerfile이 있는 디렉토리에 보면 src 디렉토리가 있다.  
이동 후 index.php 파일을 만들어보자

이제 브라우저에 localhost를 입력하자 
hello world가 잘 나올 것이다.

> 먼저 docker-compose up 으로 도커 컨테이너가 실행이 되어야한다


# /var/www/html/public

이제 Dockerfile이 있는 디렉토리에 보면 src 디렉토리가 있다.  
이동 후 index.php 파일을 만들어보자
/wordpress 라고 입력을 해줘야 하지만   
아파치 서버의 root 디렉토리를 wordpress까지 해주면 -> 이게 src/wordpress 로 연결이 되게 된다.

결과적으로 localhost만 브라우저에 입력해주면 된다.

이제 Dockerfile이 있는 디렉토리에 보면 src 디렉토리가 있다.  
이동 후 index.php 파일을 만들어보자

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
$sudo rm -rf ./
```

(도커의 mysql 컨테이너 이름)  
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