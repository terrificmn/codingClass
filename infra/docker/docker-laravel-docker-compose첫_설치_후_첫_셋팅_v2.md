# Laravel blog on server/local using docker 설치 마스터! (과연?)
2025 Aug 26 버전 (서버, 로컬 총 정리)

최신 싹다 정리해야할 듯

(codingClass/setup installation txt_files/docker_ngnix정리버전.md 은 outdated 
참고만 할 것.) 


- prerequisite  
docker, docker-compose가 설치되어 있어야함


먼저 워크 스페이스 디렉토리부터 만들어 준다
```
mkdir ~/Workspace
```

~~현재는 일단 docker-compose.yml, Dockerfile, default.conf 파일을 만들어줘야함~~

깃허브에서 도커파일 클론
```
cd ~/Workspace
git clone https://github.com/terrificmn/docker-laravel.git
```

이제 다운받은 docker-laravel 디렉토리로 이동

이동
```
cd docker-laravel
```

(옵션) 디렉토리명 바꾸기
```
mv docker-laravel docker-laravel-blog
```

> server 에서 진행하는 것이라면 .git 을 지워버려도 된다.
rm -rf .git 

mysql 컨테이너와 연결한 볼륨지정하기 위해 mysqldata 만들어주기
```
mkdir mysqldata
``` 

<br/>

## laravel project (app) 기존의 작업 중인 blog 깃허브 클론

이제는 실제 blog app 내용을 받을 차례 (실제 laravel app)

또 한번 깃허브를 클론해서 받아준다. 현재 docker-laravel-blog 위치에서 클론해준다
```
git clone https://github.com/terrificmn/laravelBlog.git
```

그러면 laravelBlog 가 만들어지고 그거를 디렉토리를 도커에서 연결할 수 있게 이름을 변경

```
mv laravelBlog/ src
```

> docker-laravel 깃에서 src 디렉토리자체가 gitingnore에 포함되어 있음     
실제 blog는 포함되지 않음 (mysqldata 디렉토리도 포함되어 있음)   
서버에서는 LaravelBlog project 디렉토리 안에서 git을 사용하면 될 듯하다

## build 하기전, 더블 체크!
이제  build를 하기 전에 docker-compose의 DB등의 비번을 다시 한번 확인한다   
(.env 파일에서 변경한다 - laravel의 .env 파일 아님)   

31May 2022변경   
먼저 복사를 한 뒤에 .env 파일을 수정해준다
```
cp .env-example .env
```

그리고 혹시라도 권한을 조정해준다
```
sudo chmod 600 .env
```
그룹이랑 외부에서 혹시라도 못 보게 해준다

이때 생성될 때의 비번이 확정되기 때문에 잘못 만들면 다시 지우고 다시 만들어야 하므로 체크한다

만약 다시 지우고 만들 때에는 
```
cd ~/Workspace/docker-laravel-blog
rm -rf mysqldata
```

<br/>

## docker-compose build and up
확인 되었으면 빌드
```
cd ~/Worspace/docker-laravel-blog
sudo docker-compose build
```
완료가 되었다면
```
docker-compose up
```

다 되었다면 ^C를 눌러서 종료


(php_laravel_train/blog프로젝트 시작 composer_frontend.md 참고하고 정리되면 진짜 정리필요)

<br/>

## vendor 디렉토리 포함 패키지 설치하기. docker-compose run
src 디렉토리를 들어가서 보면 vendor, node_modules 같은 디렉토리가 없다.  
왜냐하면 기존 gitignore에 포함되어 있기 때문에 포함이 안되어 있어서    
기본으로 라라벨에서는 ignore가 되어 있다~

> 혹시라도 다음에는 vendor를 깃허브에 올리고 되는지 확인해봐야할 듯- 테스트필요   

이 부분을 위해서 필요한 부분을 받아줘야한다. 도커 컨테이너를 활용한다

위치는 docker-laravel-blog로 이동

먼저 php 버전이 8.16이 설치되면서 의존성 문제가 나오므로 composer를 먼저 업데이트 해주자

> php 이미지를 php-fpm 으로 되어 있어서 최신 버전을 받게 되어 있는데, 아무래도 버전을 정해주는게 좋을 것 같다. 이것도 테스트를 해봐야할 듯 하다. 

최초 상태에서 접속을 시도하면 
```
Warning: require(/var/www/html/public/../vendor/autoload.php): Failed to open stream: No such file or directory in /var/www/html/public/index.php on line 34
```
에러 발생. 그래서 아래의 compose update 를 해야한다. 


# 처음 도전 이대로만 하면 된
최초 깃허브 클론 한 후에

```
docker compose run --rm composer update
```

아쉽게도 vendor 만 다 설치됨

npm관련 tailwind는 설치 까지는 필요 없고, 위에 처럼 composer 업데이트만 해준다.  
~~`docker-compose run --rm npm install -D tailwindcss postcss autoprefixer`~~
> tailwindcss는 설치가 되고 설치할 때 했던 것들은 이미 되어있으므로 할 필요가 없음


소유권 조정
```
The stream or file "/var/www/html/storage/logs/laravel.log" could not be opened in append mode: Failed to open stream: Permission denied The exception occurred while attempting to log: The stream or file "/var/www/html/storage/logs/
```
사이트를 새로고침하면 위의 에러가 발생

어쨋든 src(laravelBlog)의 storage 디렉토리의 권한을 바꿔준다. 
```
cd src
sudo chown 33:33 -R ./storage/
```

[자세한 내용은 여기를 참고](#storage-소유권-변경)  


키가 없다고 하는 경우에 generate key를 해줘야 하는데, 컨테이너 artisan이 잘 안된다.  
TODO: artisan 컨테이너 실행 안 되는 것 해결해야함
docker run으로 실행이 되어야 하는데 현재는 실행이 안되고 있다.   
`artisan no configuration file provided: not found` 이런식으로 에러 발생한다. 참고

```
file_get_contents(/var/www/html/.env): Failed to open stream: No such file or directory
```
.env 파일 관련해서 에러가 발생하므로 먼저 .env 파일을 만들어 준다.  
```
DB_HOST=mysql
DB_DATABASE=
DB_USERNAME=
DB_PASSWORD=
```
.env 파일을 복사해서 .env.example 에서 복사   
위의 변수들은 도커의 .env에서 설정했던 것과 같이 만들어 준다.  해당 DB 정보를 넣어준다.  
[중요] DB_HOST 는 127.0.0.1 에서 mysql 로 변경해준다.    
> 안그러면 SQLSTATE[HY000] [2002] Connection refused 발생

이제 key를 만들어준다.
```
docker compose run --rm artisan key:generate
```

임시 또는 직접 컨테이너에 들어가서 실행할 수는 있다.  `docker exec -it php bash`

이후 성공 메세지
```
php artisan key:generate
   INFO  Application key set successfully.  
```

새로 고침을 하게 되면 디비 에러 발생 한다.  
SQLSTATE[42S02]: Base table or view not found: 1146 Table 'my_db.posts' doesn't exist 

도커 php 컨테이너에서 이어서.. 실행
```
docker compose run --rm artisan migrate
```

모든 dB가 다 만들어지면 DONE 되었다는 메세지를 볼 수가 있다. 

> docker compose up 인 상태에서 실행.  
페이지는 새로고침을 해보자 . 이렇게 하면 잘 될 것이다.


storage에 저장된 자료가 잘 안 나올시에는 
```
docker compose run --rm artisan storage:link
```
The [/var/www/html/public/storage] link has been connected to [/var/www/html/storage/app/public].
The links have been created.

public/storage 심볼릭 링크를 만들어서 storage/app/public까지 연결되게 한다

확인을 해보면
```
cd src/public

ls -l
lrwxrwxrwx. 1 root  root     32 May 28 23:05 storage -> /var/www/html/storage/app/public
```

이제 영상도 잘 나온다

이미지도 딱 이상태
```
[linlb@172-104-72-222 docker-laravel-blog]$ docker images
REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE
docker-laravel-blog_artisan   latest    a38aed2ada7c   40 minutes ago   452MB
docker-laravel-blog_php       latest    a38aed2ada7c   40 minutes ago   452MB
composer                      latest    9e416c6634d5   2 days ago       199MB
mariadb                       latest    784190069700   5 days ago       389MB
nginx                         latest    de2543b9436b   11 days ago      142MB
phpmyadmin                    latest    6f7edac389f2   2 weeks ago      510MB
node                          16.13     304de6a23023   4 months ago     905MB
```


### storage 소유권 변경 
~~그 다음에는 src 디렉토리를 권한을 docker가 사용할 수 있게 해준다~~   
src 디렉토리 자체를 권한 조정할 필요는 없다.
   
일단 도커 컨테이너 nginx(웹서버) 에서 해당 디렉토리를 사용할 수 있게 권한을 줘야한다   
이게 우분투에서는 www-data user, group으로 되어 있다.
현재 도커 이미지가 Debian/Ubuntu 계열 이미지 이므로   

centos는 apache라고 알고 있는데, 해당 uid로 연결을 해주는 것 

```
$ sudo chown -R $USER:33 src
```

| user : group | Debian/Ubuntu (uid:gid) | Alpine (uid:gid) |
| --- | --- | --- |
| www-data : www-data | 33 : 33 | 82 : 82 |
| xfs : xfs | - | 33 : 33 |

> 약간의 트릭으로 host 컴에서 원활히 수정할 수 있게 userid는 본인 $USER로 하고  
나머지는 그룹은 웹서버 권한으로 주기  
Rocky 에서는 (centos계열)에서는 33번이 tape 이므로 그냥 그러려니 하자

혹시 이렇게 까지 했는데도 코드를 수정하다가 수정이 안된다고 할 시에는 권한을 보자  
만약 그룹에 rw- r-- r--  644 이라면 그룹에도 쓰기 권한이 없어서 안되므로 바꿔주자
```
sudo chmod 644 특정파일
```

`ls -l`을 해보면 rw- rw- r-- 로 바뀌고 저장도 잘 된다

<br/>

src 디렉토리의 권한을 다 바꿀 필요없고, storage만 바꿔준다. 단, 소유:그룹 모두 바꿔준다.

## 백업 restore
먼저 카피할 경로들   
src/public/images  
> Post 등의 대표 이미지로 사용됨  
> storage 이하의 images 와는 다른 디렉토리임  

scr/public/storage 는 심링크로 연결된다.  
src/storage/app/public/ 이하 경로에 복사를 해줘야 하는데  

> src/storage/app/public/footage/portfolio_clips/* (영상들)  
src/storage/app/images/tmp 일단 복사 안해도 될듯 하다

```
app
│   └── public
│       ├── footage
│       │   └── portfolio_clips
│       └── images
│           ├── note_images
│           │   ├── 60db012c-1624965420
│                 ...
│           ├── portfolio_images
│           │   ├── 611068c6-1628465350
│                 ...
│           └── post_images
│               ├── 60aae365-1621812069
│                 ...
```

storage에 저장된 자료가 잘 안 나올시에는 
```
docker compose run --rm artisan storage:link
```
> 단, 소유권이 www-data 로 바뀐다 

## sql 데이터 백업 phpmysql
dump한 sql 파일이 있다면 import를 통해서 불러올 수 있다. restore  

웹페이지로 접속을 한다. ip주소를 치고 포트번호를 입력, 
예를 들어 171.10.15.100:8080  
> 포트번호 compose 파일 확인  

phpmyadmin 페이지에서 mysql 로 접속을 해준다. id와 password를 넣어서 로그인 후   
artisan migrate 명령으로 DB 및 table이 만들어 졌는데

백업을 restore를 하려면 table이 없어야 한다   
drop table을 해준다. 너무 많으므로 laravelblog를 데이터베이스를 선택 후에  
Structure 탭을 선택한 후에 테이블들을 체크박스로 선택을 해준다음에 (check all)    
with selected: 선택 창을 고른 후에 drop을 해준다

그리고 나서 import 메뉴를 통해서 백업파일.sql 파일을 선택해서 백업을 진행한다   
기본 디폴트 설정으로 import 해준다.    

## 서버에서 적용시에 ssl https 로 최초 인증서 받기
.env 파일에서 `CONF_STATUS=prod` 를 dev로 변경을 해준다.  
그리고 다시 `docker compose up` 를 실행

docker compose up을 함과 동시에 certbot 디렉토리가 생성이 됨   
ls를 해보면 certbot이 생겼을 것 임 (.gitignore 에 추가되어 있음)  

이제 인증서 발급 실행 하는데 도커 컨테이너로 실행을 한다
```
docker compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
```
> example.com 부분에 자신의 도메인을 쓴다

그러면 
```
Enter email address (used for urgent renewal and security notices)   
 (Enter 'c' to cancel): 
```
적어준다

그 다음에 Please read the Terms of Service 에 동의를 해준다
Y 를 눌러준다

그 다음은
email address 를 the Electronic Frontier Foundation에 쉐어해줘서 
EFF news, campaigns 등을 메일로 보내준다는 것   
이거는 optional이니깐 N 까지 해주면 

```
Successfully received certificate.
Certificate is saved at: /etc/letsencrypt/live/qspblog.com/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/qspblog.com/privkey.pem
This certificate expires on 2022-09-04.
These files will be updated when the certificate renews.
```

certificates 이렇게 생성이 되었다.

이제 웹 브라우저에 https: 붙이게 되면 웹서버를 찾지 못하므로  
다시 .env 파일에서 `CONF_STATUS=dev` 를 prod로 변경을 해준다.  
```
`CONF_STATUS=prod`
```

그리고 nginx_conf/default_prod.conf 의 파일을 열어준다
```
vi nginx_conf/default_prod.conf
```

> 아래 내용은 처음 깃 허브에서 클론하고 적용할 때 처음만 바꿔주면 되고 server에서 commit는 최대한 자제하자  
> default_dev.conf 는 변경할 필요 없음  

여기에서 server_name 등은 바꿔줘야 한다 (내 도메인으로 이름으로 )  

주석으로 바꿔야 한다고 표시된 부분을 모두 바꿔준다.   
먼저 첫 번째 server {} 블럭 내용에서 server_name을 바꾼다 (내 도메인 네임으로)  
그리고 두 번째 server {} 블럭의 server_name 변경,   
ssl_certificate, ssl_certificate_key 경로 중 example.org 경로도 변경 (도메인 이름)  
 
`예: server_name qspblog.com`   
```
server_name qspblog.com; ## your server name

ssl_certificate /etc/letsencrypt/live/qspblog.com/fullchain.pem;  
ssl_certificate_key /etc/letsencrypt/live/qspblog.com/privkey.pem; 
```
저장을 한 후에 다시

`docker compose up` 을 해준다  
> 이때 certbot 디렉토리안에 conf/live/renewal/ 에 보면 conf 파일이 내 도메인 이름으로 변경되어 있다.



웹 브라우저에 http://도메인이름.com 으로 하면 자동으로 https://도메인이름.com 으로 넘어가고   

주소창 옆에 connection secure 아이콘으로 바뀐다 

## 이하 라라벨 9 및 다른 트러블 슈팅은 아래 참고
docker-laravel-docker-compose첫_설치_후_첫_셋팅_v1.md