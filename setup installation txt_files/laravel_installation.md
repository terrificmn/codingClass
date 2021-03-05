# 라라벨 첫 프로젝트 만들기
먼저 프로젝트 디렉토리 만들어주기
```
$mkdir projects
#or
$mkdir workspace
```
그리고 나서는 

새 프로젝트를 만들어준다. 먼저 작업할 디렉토리로 이동한다  
laravel new 프로젝트명
```
$laravel new firstproject
```
그러면 프로젝트가 (각종 필요한 파일들이) 만들어 진다

필요없는 프로젝트 지우기. rm명령어를 사용하면되나,  
rm사용할 때는 정말 주의할 것
```
$pwd
$rm -Rf firstproject

```

프로젝트 만드는 다른 방법, 이번에는 composer를 사용함
```
$ composer create-project --prefer-dist laravel/laravel firstproject
```

페이지 열어 주기  
먼저 프로젝트 디렉토리로 이동
```
$cd myproject
$php artisan serve 
```
http://127.0.0.1:8000 클릭하거나 입력하면 브라우저로 열린다

만약 api 작업 중에 8000포트가 겹친다면
프로젝트 만든 곳으로 이동
```
cd firstprojects
php artisan serve --port=8001
```

호스트명 변경
```
$sudo vi /etc/hosts
```
파일명에서 localhost 첫번째 줄을 삭제하거나 주석처리
```
#127.0.01 localhost 
127.0.0.1 firstproject.test
```
이렇게 변경하게 되면 브라우저에 아이피를 쳐도 되고, firstproject.test 입력해도 됨

VirtualBox 나 vmware로 가상으로 돌리고 있을 경우
만약 호스트 컴퓨터(자신의 메인? 로컬 컴)
먼저 ip확인 `ipconfig` 또는 `ip address show` 명령어로 확인 후 

```
$ php artisan serve --host 192.168.0.100
```
이렇게 하면 로컬 host에서 접속할 수 있음.. 흠.. 
외부라 해봤자 가상머신이면 로컬에서 접속하거나,,큰 것은 아니지만 테스트할 때 사용할 수 있을 듯


VSCODE 확장팩들
- vscode extensions 
- Laravel Blade Spacer  
- Laravel Blade Snippet 알아보기  
- Laravel goto view  
- Laravel Extra Intelllisense  
- live Sass Compiler  
- Beautify css/sass/scss  
- PHP IntelliSense
- getter/setter

