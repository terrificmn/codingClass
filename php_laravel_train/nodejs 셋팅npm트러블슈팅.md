
# laravel/ui 설치하기
composer require laravel/ui --dev
 
ui 설치

php artisan help ui 를 보면
(bootstrap, vue, react)를 위한 것이지만 로그인, 패스워드 리셋을 위해서 사용

php artisan ui vue --auth
npm install && npm run dev

만약 에러가 나면 트러블슈팅 참고할 것


package.json 파일을 보면
vue, jquery등 
devDenpendencies 키에 추가된것을 알 수 있다

resource/views/auth
resource/views/auth/passwords
디렉토리에 가보면
로그인 패스워드 관련해서 blade.php 파일이 만들어 진 것을 알 수 있음
(매뉴얼로 만들려면 오래걸리는데 쉽게 할 수 있음)

그리고 routes/web.php 를 보면
Auth:가 추가되어 있음

그리고 
$php artisan serve
해보면 
로그인 입력창이 생김


HomeController.php 
middleware 에서 (조금 어렵지만); 여기에서 
로그인 auth를 확인해서 아무나 로그인 할 수 없게 만들어 줌

welcome 블레이드 페이지에서 
@if (Auth::check())
Hi, {{ Auth::user()->name }} //로그인 user()메소드로 로그인정보 가져오기
@else
    Laravel
@endif


@if 대신에 @auth 도 할 수 있는데 위의 코드와 같은 기능을 한다







중간에 
만약 npm install 후에 “npm ERR! code ELIFECYCLE” 에러 발생시

npm cache clean --force
npm install

중요!!!
------- 트러블슈팅
만약 npm 설치 중에 버전에 안 맞아서 에러나면 npm 버전 확인해 볼것

먼저 npm이 없다고 하면 npm을 설치하는데 yum으로 npm을 설치해버리면 nodejs가 딸려오는데 (의존성떄문) 근데 nodejs가 버전이 10.23인가로 너무 낮다, 대신npm은 7.6으로 괜찮지만...
그래서 처음부터 nodejs를 14, 15버전으로 리포지터리 추가해서 설치할 것

gcc 확인 아마 설치되어 있을 것, 없으면 설치 // 대개 centOS경우에는 (Development Tools인가로 설치하면 다 설치 됨)
```
$ sudo yum group install "Development Tools"
```
dnf install gcc-c++ make

리포지터리에 추가 
설명:
First of all, You need to enable node.js yum repository in your system provided by the Node.js official website. You also need development tools to build native add-ons to be installed on your system.

15버전 최신 : 2021. 5월 기준
curl -sL https://rpm.nodesource.com/setup_15.x | sudo -E bash -
또는 
14버전 안정화버전
curl -sL https://rpm.nodesource.com/setup_14.x | sudo -E bash -

둘 중에 선택 실행
그러면 추가가 됨
 
그리고 설치
sudo dnf install nodejs
yum, dnf 상관없음

그러면 완료
버전확인
$ node -v
$ npm -v
--------끝





우분투 버전
편하게 cd ~ 으로 이동

curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh
14버전으로 셋업 파일 받기

여기에서 일단 gcc+ 가 설치 되있어야 한다. 
centos는 gcc gcc-c++
development Tools를 설치하면 된다
$ sudo yum group install "Development Tools"

우분투는 ubuntu gcc  설치 및 필요한 것 몽땅 설치
$ sudo apt-get install build-essential

그리고 나서 
$ sudo bash nodesource_setup.sh
실행

이제 nodejs를 설치할 수 있다
$sudo apt-get install nodejs

node -v 하면 v14.16.0 
npm -v 하면 6.14.11 가 설치된것을 알 수 있음 !

