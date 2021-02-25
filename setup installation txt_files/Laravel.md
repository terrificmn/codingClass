# 라라벨 첫 프로젝트 만들기
먼저 프로젝트 디렉토리 만들어주기
```
$mkdir projects
#or
$mkdir workspace
```
그리고 나서는 

새 프로젝트를 만들어준다. 먼저 작업할 디렉토리로 이동한다  
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
```
php artisan serve 
```
http://127.0.0.1:8000 로 브라우저로 열린다


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


vscode extensions 
>Laravel Blade Spacer  
Laravel Blade Snippet 알아보기  
Laravel goto view  
Laravel Extra Intelllisense  
live Sass Compiler  
Beautify css/sass/scss  
PHP IntelliSense
getter/setter

기본 디렉토리 정보들
- app > Models 디렉토리에 
User.php 파일이 있는데 
이것로 controller로 dB랑 연결할 수 있음

- app > Http > Controllers
controller.php 파일
Basecontroller를 extends 상속받은 것

- resources > views
welcome.blade.php 

- database > 
데이터베이스관련 파일

- routes
web.php 
여기 파일에서 리턴 값을 바꿀 수 있음
return env('DB_DATABASE');
라고 바꿔주면 .env파일에 설정되어 변수를 브라우저에 출력할 수 있음

- 로그파일
storage > log

- .env파일
자주쓰는 변수들을 확인할 수 있음
(도메인/ db등 정보를 볼 때 사용)
database 접속 비번, 아이디 db정보



1:11:32 볼 차례