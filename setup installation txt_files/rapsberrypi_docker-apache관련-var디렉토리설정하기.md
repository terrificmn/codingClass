# (추가 옵션 테스트) docker apache2 서버의 root 디렉토리 설정하기 (기본으로 설정)
docker 로 wordpress를 설치할 때 아파치 웹 서버의 Root directory를 설정할 수 있는데  
이에 따라 접속할 수 있는 주소가 달라진다

DocumentRoot /var/www/html  
이게 보통 기본 아파치 웹 서버의 경로이다  
위처럼만 하면 브라우저에 localhost 만 입력하면 위 경로에 있는 index.html 이나 index.php가 실행이 된다

깃 허브에 있는 docker-compose.yml 파일을 이용해서 도커 컨테이너를 만들면  
```yml
volumes:
      - ./src:/var/www/html/  
```
yml파일에 위처럼 src 디렉토리를 /var/www/html으로 연결해 주었기 때문에   
src 디렉토리에 index.php 파일을 만들어 주면 되게 된다

docker-wordpress 디렉토리로 이동해서 설정파일을 수정한다.
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

위에서도 언급했던것 처럼  
원래 도커 없이 사용하는 것이라면 /var/www/html에 파일을 생성해야겠지만
이제는 src 디렉토리 안에 파일을 만들면 된다.

Dockerfile이 있는 디렉토리에 보면 src 디렉토리가 있다.  
이동 후 index.php 파일을 만들어보자

```
$ cd src
$ vi index.php
```
파일이 열리면
```
<h1> hello world </h1>
```
저장 후에 

이제 브라우저에 localhost를 입력하자~ 
hello world가 잘 나올 것이다.

> 먼저 설정이 바뀌었으므로 docker-compose build 를 해준 후 docker-compose up 으로 도커 컨테이너가 실행이 되어야하고, 실행은 Dockerfile 이 있는 경로에서 실행을 한다

만약 아래와 같은 에러가 발생 시에는 
```
error checking context: 'can't stat '/home/pi/Workspace/docker-wordpress/mysqldata/mysql''.
ERROR: Service 'php' failed to build : Build failed
```

mysqldata 디렉토리 안에 있는 파일을 지워준다.
```
cd mysqldata
$sudo rm -rf ./
```

그리고 build & up을 해주면 된다

>참고로 이 상태에서는 src 디렉토리에 다운받은 wordpress를 위치 시키는데  
이렇게 되면 웹 브라우저에서 주소는 localhost/wordpress 가 된다


<br>


# 이번에는 /var/www/html/wordpress 로 바꿔보자
위처럼 했다면 wordpress를 접속하려면 웹 브라우저에    
localhost/wordpress 라고 적어야한다  

wordpress 경로자체를 생략한 상태로 사용하려면 default.conf 파일을 수정해야한다

```
vi default.conf

# 아래처럼 수정
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

그리고 다시 빌드를 해준다. 빌드가 끝나면 up으로 도커가 실행이 되게 해주면 된다.
```
$docker-compose build
$docker-compose up
```

>이제 마치 심볼릭링크가 되어 있는 것 처럼 아파치 웹 서버의 기본 루트가 /var/www/html 인데  
wordpress 까지 해주면은 /var/www/html/wordpress 가   
내 프로젝트의 src/wordpress로 연결되는 것 같다
(정확한 비유인지는 모르겠다. ㅋㅋ)

이제는 브라우저에 localhost만 입력해주면 된다.   
wordpress 설치 페이지가 나오면 잘 된 것이다