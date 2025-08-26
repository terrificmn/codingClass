# Laravel blog on server/local using docker 설치 마스터! (과연?)
2022 May 27 버전 (서버, 로컬 총 정리)

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
docker-compose run --rm composer update
```

아쉽게도 vendor 만 다 설치됨

npm관련 tailwind는 설치를 해야할 듯
```
docker-compose run --rm npm install -D tailwindcss postcss autoprefixer

```
하면  tailwindcss는 설치가 되고 설치할 때 했던 것들은 이미 되어있으므로 할필요없음


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

임시로 또는 직접 컨테이너에 들어가서 실행할 수는 있다.  
```
docker exec -it php bash
```

이후 
```
php artisan key:generate

   INFO  Application key set successfully.  
```

디비 에러 발생 시
SQLSTATE[42S02]: Base table or view not found: 1146 Table 'my_db.posts' doesn't exist 

도커 php 컨테이너에서 이어서.. 실행
```
php artisan migrate
```

모든 dB가 다 만들어지면 DONE 되었다는 메세지를 볼 수가 있다. 

> docker compose up 인 상태에서 실행.  
페이지는 새로고침을 해보자 . 이렇게 하면 잘 될 것이다.


storage에 저장된 자료가 잘 안 나올시에는 
```
docker-compose run --rm artisan storage:link
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




# 새로운 방식 try 라라벨 8에서 9로 업글
[예전에 라라벨 8에서 9로 업데이트 했던 기록입니다. 첫 배포시 여기를 눌러 스킵하세요](#env파일-만들어주기-db-migrate)

composer 업데이트를 하면 vendor 디렉토리를 만들어주면서 필요한 패키지를 다운 받는다
```
docker-compose run --rm composer update
```

laravel/ui 가 필요하다가 하면
docker-compose run --rm composer require laravel/ui 



라라벨8 에서 라라벨9로 가면 이런 문제가
fideloper/proxy 가 없다고 한다 
docker-compose run --rm composer composer require fideloper/proxy

그러면 설치중에 이런 에러가
 Undefined constant Illuminate\Http\Request::HEADER_X_FORWARDED_ALL

application’s “trusted proxy” middleware 를 update 해줘야한다

app/Http/Middleware/TrustProxies.php 열어서

아래처럼 바꾼다
```
//use Fideloper\Proxy\TrustProxies as Middleware; // laravel 8.
use Illuminate\Http\Middleware\TrustProxies as Middleware
```

만약 $headers가 아래처럼 되있다면
```
protected $headers = Request::HEADER_X_FORWARDED_ALL; 
```
내용을

```
protected $headers = Request::HEADER_X_FORWARDED_FOR | Request::HEADER_X_FORWARDED_HOST | Request::HEADER_X_FORWARDED_PORT | Request::HEADER_X_FORWARDED_PROTO | Request::HEADER_X_FORWARDED_AWS_ELB;
```
바꿔준다

마지막으로 지운다
```
docker-compose run --rm composer remove fideloper/proxy
```

Target class [Fruitcake\Cors\HandleCors] does not exist. 없다고 해서 
composer.json 확인해보니 require에 없다
```
 docker-compose run --rm composer require fruitcake/laravel-cors
```


이후 tailwindcss 설치
```
docker-compose run --rm npm install -D tailwindcss postcss autoprefixer
```

> 공식사이트에서는 npx tailwindcss init  명령어를 치라고 하지만 직접 칠 수가 없어서 컨테이너로 접솏한 뒤 실행할 수 있다
```
docker exec -it npm bash
```
그러면 쉘로(?) 들어가지는데 거기에서 
```
npx tailwindcss init
```

위를 안해도 직접 만들면 된다

tailwind.config.js 에 
```
module.exports = {
  content: [
    "./resources/**/*.blade.php",
    "./resources/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

> 중요 content에서 두번째 줄 .js 파일도 추가를 해줘야한다~ 그래야 css가 제대로 작동한다
.js를 안 넣어서 몇시간 고생했다~ npm run watch 가 작동하는데도~ tailwindcss 클래스를 바꿔도 전혀 바뀌지를 않아서 
원인은 content에 .js도 포함시켜줘야함~ (blade.php파일이 작동하는데도 필요한가보다)


webpack.mix.js 파일에 require() 추가
```
const mix = require('laravel-mix');

mix.js('resources/js/app.js', 'public/js')
    .postCss('resources/css/app.css', 'public/css', [
        require('tailwindcss')
    ]);
```

resourece/css/app.css 에 추가
```
@tailwind base;

@tailwind components;

@tailwind utilities;
```

docker-compose run --rm npm run watch
를 하면 
public/css/app.css 를 만들어준다

그리고 여기에 지정된 모든 기능을 사용할 수 있음


app.blade.php (대게는 layouts 으로 사용) 하는 head에 넣어준다 
그리고 마지막으로 
```
<head>>
  <link href="{{ asset('css/app.css') }}" rel="stylesheet">
</head>
```


테일윈드css에서 npm run watch가 실행이 되서 아마 백그라운드에서 계속 실행이 되고 있어야하는데
그래야 코드에서 바뀌면 바로 css를 새로 public/css/app.css 에 추가를 해주는데 
npm을 도커에서 실행이 바로 꺼져버려서 watch가 안되고 있는 듯 하다~
그래서 docker-compose.yml 에 command추가



# 예전방식 (잘못된 방식(?)으로 하고 있었던 것 같다)
[예전 기록입니다. 첫 배포시 여기를 눌러 스킵하세요](#env파일-만들어주기-db-migrate)

composer 업데이트
```
docker-compose run --rm composer update
```

테일윈드 설치
```
docker-compose run --rm composer require laravel-frontend-presets/tailwindcss --dev
```
`Package manifest generated successfully` 이런식으로 나오면 성공

```
docker-compose run --rm artisan ui tailwindcss --auth
```

laravel-mix를 지우고 다시 설치
```
docker-compose run --rm npm remove laravel-mix
```

docker-compose run --rm npm install laravel-mix --save-dev

```
found 35 vulnerabilities (30 moderate, 3 high, 2 critical)
  run `npm audit fix` to fix them, or `npm audit` for details
```
이런식으로 버전이 달라서 약점등이 발견되는데 안내해준것 처럼 다시 


만약 `found 0 vulnerabilities` 이렇게 나온다면 아래는 실행할 필요가 없다

> 깃허브를 설치 후 commit을 해서 최신화 했더니 npm audit fix를 할 필요가 없어짐
이유는 src/package.json 파일에서 이미 버전을 지정해놓았기 때문


## 트러블 슈팅, 버전이 잘 안맞으면 버전등을 바꿔야 하는데 현재 시점에서는 필요없음, 스킵함
[에전 기록. 첫 배포시 여기를 눌러 스킵하세요](#env파일-만들어주기-db-migrate)

```
docker-compose run --rm npm audit fix
```

그래도 다 고치지를 못해서 
```
docker-compose run --rm npm audit 
```
을 해서 나오는 안내에 따라서 설치를 해준다

위로 스크롤을 올려보면 이런식으로 안내가 나오는데 

```
# Run  npm install --save-dev tailwindcss@3.0.24  to resolve 5 vulnerabilities
```
이런식으로 php 버전이 달라지면서 자꾸 깨지는 듯 하다. 그래서 docker image에서 확실하게 해줘야 할 듯 하다

이 아래 명령어는 미래에 다시 설치할 때에는 달라질 수 있다 예로 참고만 하자
```
docker-compose run --rm npm install --save-dev tailwindcss@3.0.24  
docker-compose run --rm npm update postcss --depth 3
```

> tailwindcss가 버전 업이 많이 되었음

<br/>


## env파일 만들어주기, DB migrate
이제 다시 docker-compose up 을 하면 컨테이너들이 잘 실행이 된다

이제 서버의 ip주소를 웹브라우저에 넣어보면  
500 server error

로컬작업시는 (http://localhost:8000)

왜냐하면 라라벨의 .env 파일 설정을 안해서 그렇다

```
cd src
cp .env.example .env
```

상위 디렉토리의 docker-laravel-blog의 .env 파일에 설정된 DB, ID, 패스워드등을   
참고해서 src 디렉토리내의 복사한 .env 파일의 내용을 동일하게 변경

.env 파일을 열어서 수정
```
vi .env
```
그 중에서
```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=database
DB_USERNAME=app
DB_PASSWORD=
```

> 중요!!! 여기에서 DB_HOST는 **mysql** 로 변경해줘야지 도커 컨테이너인 mysql로 연결이 된다


키 문제가 발생한다. 웹 페이지에서 만들기를 눌러도 안됨      
src 디렉토리에 있다면 상위로 이동
```
cd ..
```

key 생성
```
docker-compose run --rm artisan key:generate
```

migrate까지 db 테이블 생성해주자
```
docker-compose run --rm artisan migrate
```

거의 마자믹 storage 심볼릭 링크를 만들어 준다 (이미지관련) 

```
docker-compose run --rm artisan storage:link
```

<br/>

## DB 백업 import 하기
db를 sql 파일로 백업을 해놓았다면 다시 phpmysql 에서 import 기능으로   
복원해줄 수가 있다

웹페이지로 접속을 한다. ip주소를 치고 포트번호를 입력, 
예를 들어 171.10.15.100:8080  

phpmyadmin 페이지에서 mysql 로 접속을 해준다. id와 password를 넣어서 로그인 후   
artisan migrate 명령으로 DB 및 table이 만들어 졌는데

백업을 restore를 하려면 table이 없어야 한다   
drop table을 해준다. 너무 많으므로 laravelblog를 데이터베이스를 선택 후에   
Structure 탭을 선택한 후에 테이블들을 체크박스로 선택을 해준다음에   
with selected: 선택 창을 고른 후에 drop을 해준다

그리고 나서 import 메뉴를 통해서 백업파일.sql 파일을 선택해서 백업을 진행한다     

<br/>

## git 변경된 내용 되돌리기
이제 git status를 해보면 변경된 파일들이 많이 있다  
일단 비교를 해보면 app.css, app.js, composer.lock 등은 아무래도 npm 업데이트   
관련이 있어 보여서 commit을 해주면 될 듯 하고,   

아무래도 이번에는 그럭저럭 패키지 업그레이드가 있었으므로 commit을 했지만

미래에 다시 설치할 일이 있다면 현재 깃 상태가 최신 인것이라고 감안 (가정)해서   
큰 변화가 없다면 commit을 할 필요가 없다 (대충 비교해보고 결정할 것)


### 일단 2개의 파일은 변경이 되면 안된다   
중요한 것은 app.blade.php (resources/views/layouts) 와    
wep.php (routes) 는 변경하면 안됨  

왜냐하면 composer로 설치를 하면서 초기 상태로 돌아간 경우인데   
바뀐 내용은 다시 취소를 해줘서 웹페이지에 변화가 없게 해준다  그래서 위 2개는 취소를 시켜준다

git status 확인 후 git restore 명령을 사용

```
git status
```
그러면 modified 된 file 들이 나오니 잘 확인 후 
```
git restore resources/views/layouts/app.blade.php
git restore routes/web.php
```
> 탭으로 자동완성해가면서 해주면 된다. git checkout 이였는데 git restore로 바뀐듯 하다


<br/>

## 사진 백업 하기
ftp를 사용한다. filezilla를 사용

먼저 카피할 경로들
src/public/images

src/storage/app이하전부
src/storage/app/images/tmp  ---- 여기는 필요없는 0바이트 디렉토리를 지운다음에 올릴것
src/storage/app/public/footage/portfolio_clips/* (영상들)
src/storage/app/public/images/note_images
src/storage/app/public/images/portfolio_images
src/storage/app/public/images/post_images



그리고 권한을 제대로 다시 설정해줘야지 사진을 업로드 할 수가 있다

먼저 storage가 심볼릭 링크가 되어 있는지 확인

그리고 
```
cd src/storage
sudo chown -R 33:$USER app
```
일단 storage/app에 image가 들어가 있으므로 권한 조정을 해준다


혹시라도 웹페이지에서 저장 단계에서 500 에러가 날 경우 Internal Server Error  
현재 크게 돌아가는데 문제가 없기 때문에   
디렉토리 권한 문제일 경우가 높다~
이미지가 저장되는 곳의 uid 쪽 권한이 33이 되게 만들어 줘야함을 기억하자!

현재 저장되고 있는 곳은 public 디렉토리와 , storage/app 쪽 디렉토리임



## certbot 컨테이너 추가~됨
깃허브에서 다운을 받은 다음에 .env 파일을 새로 복사해서 만들고    
현재 docker-compose.yml 및 default.conf 파일 수정이 되어서 certbot 컨테이너가 추가되었다

먼저 docker-comopse.yml 파일에서 web 컨테이너 부분에서 volume 부분에서   
nginx_conf/default_dev.conf 파일로 연결해준다 (yml파일 수정됨)

.env 파일 이용하는 방법으로 변경 됨   
.env 파일에서 변수 value를 dev로 변경  

```
CONF_STATUS=dev
```

그래서 docker-comopse build 를 해서 다시 up을 시키면 웹서버가 실행이 되고   
웹서버가 돌아가고 있을 때 인증을 받을 수 있다.

> 중요한 건 default_prod.conf 파일로 변경은 인증서를 받은 후에 해야한다.   
인증서 발급 자체가 웹서버가 정상적으로 응답을 해야지 발급이 된다.  
그리고 (로컬에서 개발도 계속 해야하기 때문에 분리를 해놓음)

또한 안타깝게도 재갱신에 실패를 해서 재발급을 받았으므로 갱신에 성공한다면 업데이트 필요!

## 서버에서 적용시에 ssl https 로 최초 인증서 받기
env파일의 변수를 dev로 변경을 했다면  
```
docker-compose build
docker-compose up
```
만약 build를 안해도 nginx가 잘 열린다면 (default_dev.conf)이 그렇다면 build는 안 해도 될 듯

docker-compose up을 함과 동시에 certbot 디렉토리가 생성이 됨   
ls를 해보면 certbot이 생겼을 것 임 (.gitignore 에 추가되어 있음)

이제 인증서 발급 실행 하는데 도커 컨테이너로 실행을 한다
```
docker-compose run --rm certbot certonly --webroot --webroot-path /var/www/certbot/ -d example.com
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

이제 웹 브라우저에 https: 붙이게 되면 웹서버를 찾지 못하므로 default_prod.conf를 수정해줘야한다  
왜냐하면 http용 default_dev.conf 파일을 사용하고 있기 때문  

~~nginx_conf 디렉토리에는 default_dev.conf, default_prod.conf파일 지정이 되어 있는데
default_dev.conf 지정되어 있는 것을 default_prod.conf 파일로 바꿔준다. 주석해제 하고    
default_dev.conf 는 주석처리~~

.env 파일에서 설정하는 것으로 변경했음. .env 파일에서 dev로 바꿔준다 

그리고 nginx_conf/default_prod.conf 의 파일을 열어준다
```
vi nginx_conf/default_prod.conf
```

> 아래 내용은 처음 깃 허브에서 클론하고 적용할 때 처음만 바꿔주면 되고 server에서 commit는 최대한 자제하자

이때 server_name 등은 바꿔줘야 한다 (내 도메인으로)

먼저 첫 번째 server {} 블럭 내용에서 server_name을 바꾼다 (내 도메인 네임으로)

그리고 두 번째 server {} 블럭의 server_name도 마찬가지로 바꾸고
 
`예: server_name qspblog.com`   

그리고 ssl_certificate 부분의 경로중에 example.org 부분을 내 도메인 이름으로 바꿔야함
이렇게 된다
```
server_name qspblog.com; ## your server name

ssl_certificate /etc/letsencrypt/live/example.com/fullchain.pem;  
ssl_certificate_key /etc/letsencrypt/live/example.com/privkey.pem; 
```
저장을 한 후에 다시

docker-compose build 를 해준다
docker-compose up 을 해준다

이제 다시 서버를 up해서 가동이 되면   
웹 브라우저에 http://도메인이름.com 으로 하면 자동으로 https://도메인이름.com 으로 넘어가고   

주소창 옆에 connection secure 아이콘으로 바뀐다 



## 개발 후 commit push 하기전에 
css/app.css 파일 자체는 줄어들지만   
/js/app.js 파일이 계속 600kb 가 넘는다~ 그래서 용량을 줄여줘야하는데     

귀찮지만 우선   
```
docker-compose run --rm npm run prod
```
laravel mix를 실행해준다. 

그리고 나서 git commit을 해서 배포를 한다 

하지만 로컬에서 작업 시 npm run watch가 작동중이므로   
js/app.js 파일 용량이 게속 자동으로 커진다   
당분간 귀찮아도 일단 npm run prod를 해주고 commit 하기

더 좋은 방법은 찾아봐야겠다

> js.app 파일이 용량이 무지 큰 상태에서 깃 허브를 올리게되면 딱히 문제는 없지만  
git허브 리포지터리에서 languages 표시해주는 것에서 javascript가 60%이상 차지 하고 있다고 나오게 된다.   

끝!





