# wordpress 셋팅 중에 db셋팅 실패시
wordpress 설치를 시작하고 DB데이터를 넣는 부분에서 넘어가지를 않는다.     
디비셋팅을 해도 설정이 잘못되었다는 식으로만 계속 반복되어질 때   
wordpress에서 db정보를 못 찾아온다.

도커 컨테이너가 실행되고 있을 때  
localhost:8080 으로 phpmyadmin을 접속해보면    
서버는 mysql 그리고 아이디 비번을 넣고 접속이 가능하다. wordpress DB도 생성이 되어 있다.  

즉,  wordpress에서 mysql docker 컨테이너 정보를 제대로 못 가지고 오는 것 같다

그래서 .env 파일을 만들어서 하면 환경변수을 도커내에서 사용할 수 있게 해주면  
wordpress에서 설치할 때 인식하게 된다

유저 db 정보를 .env 파일을 만들어 준 후 다시 리빌드를 해줘야한다.  
Dockerfile 이 있는 디렉토리로 이동해서 같은 디렉토리안에 .env를 만들어 주자

```
$cd ~/Projects/docker-wordpress
$vi .env
```
그리고 아래 내용을 추가 후 저장해준다
```
WORDPRESS_DB_HOST=mysql:3306
WORDPRESS_DB_USER=user아이디
WORDPRESS_DB_PASSWORD=user비번
WORDPRESS_DB_NAME=wordpress
```
DB_HOST는 mysql 컨테이너 이름이 된다. mysql로  적어주면 된다.    
(docker-compose.yml 파일에서 이름을 어떤 것으로 지정했는지에 따라 달라지는 듯)

docker 관련해서 수정이 되었으므로 build를 다시 해준다
```
$docker-compose build
```
저장된 파일이 있어서 금방 완료 된다.
```
$docker-compose up
```
도커 컨테이너들을 다시 실행해주고  

이제 wordpress에 DB정보를 입력하면 잘 넘어가진다. 

<br>

## 잠깐만

>여기에서 흥미로운 것이 만약 도커를 사용 안했다면 mysql 프로그램을 실행해서  
mariadb에 접속해서 해당 디비인 wordpress의 권한을 갖는 사용자를 만들어주는게 좋지만  

예를 들면 아래와 같다
```
MariaDB> CREATE USER 'wp_admin'@'%' identified by 'wordpress1234';
MariaDB> grant all on wordpress.* to 'wp_admin'@'%';
```
하지만

도커에서는 mysql 컨테이너가 최초 실행이 될 때 docker-compose에서 db를 만들어 주기 때문에   
위의 과정을 할 필요가 없다

<br>

# 다시 돌아와서 소유 권한 바꿔주기
하나는 해결했지만!

하지만

만약 unable to write to wp-config.php file 에러가 발생한다면
<img src=0>
<br>

자신이 저장한 디렉토리로 이동해서 src 디렉토리까지 이동해준 후에  
/src/wordpress의 권한을 아파치 권한으로 바꿔줘야한다
```
$cd ~/Projects/docker-wordpress/src
$sudo chown -R www-data:www-data wordpress
```

만약 docker-compose build를 했을 때 mysql 관련해서 build failed 되면  
[여기를 참고하세요 - 보러가기](/blog/)

<br>

# docker 시작 시키기
아래와 같은 에러가 발생 시 docker가 실행 중인지 확인해 보세요
```
Traceback (most recent call last):
  File "urllib3/connectionpool.py", line 677, in urlopen
  File "urllib3/connectionpool.py", line 392, in _make_request
  File "http/client.py", line 1277, in request
  File "http/client.py", line 1323, in _send_request
  File "http/client.py", line 1272, in endheaders
  File "http/client.py", line 1032, in _send_output
  File "http/client.py", line 972, in send
  File "docker/transport/unixconn.py", line 43, in connect
FileNotFoundError: [Errno 2] No such file or directory

During handling of the above exception, another exception occurred:
```

상태 체크하기
```
systemctl status docker
```
inactive (dead) 상태라면 바로 시작을 해주세요

```
systemctl start docker
```

