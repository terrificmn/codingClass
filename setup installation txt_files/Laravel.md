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

composer.json 파일에는 require 키가 있는데 여기는 지우면 웹 크래쉬
require-dev는 그래도 작동함


json파일에 문제가 생겼을 경우
rm -rf composer.lock 파일이 없다고 가정했을 때

$composer install
composer.lock 파일이 없으면 다시 업데이트를 해줌

라이브러리 추가하기
프레임워크 없이 
예를 들어 mollie  
composer installation 설명을 참고로 composer 파일의 업데이트 하거나

여기 사이트에서 
Packagist
https://packagist.org

mollie 를 검색한 후에 
나오는 결과를 클릭해서 들어가면

>mollie/mollie-api-php   
composer require mollie/mollie-api-php  
Mollie API client library for PHP. Mollie is a European Payment Service provider ...생략

이렇게 나오는데 여기에서 두번째 줄을 카피해서 터미널에서 입력하면 바로 설치됨
$cd firstproject
$composer require mollie/mollie-api-php  

vendor 디렉토리에서 보면 composer.lock 파일에서 보면 업데이트 되어 있는 것을 알 수 있음

혹시라도 지워졌을 때는 
$composer update
를 하면 업데이트가 됨

심포니
1:11:32 볼 차례

// get('/') 의 '/'는 루트디렉토리
Route::get('/', function () {
    return view('welcome');
});

// view() 는 resources/views/welcome.blade.php 를 불러옴

/*
Route::get('/', function() {
    return env('CREATOR_NAME');
});
*/

// myweb.com/users == /users
// Route to users - string
// 브라우저에서 get request를 했을 때 return 메세지를 보여준다
Route::get('/users', function() {
    return 'Welcome to the users page';
});

// Route to users - Array(JSON) 배열, 또는 json형식을 보여줌
Route::get('/users', function() {
    return ['php', 'html', 'Laravel'];
});

// response()메소드를 이용해서 json 형식을 보여주게 할 수 도 있음
Route::get('/users', function () {
    return response()->json([
        'name' => 'Mike',
        'course' => 'Laravel Beginners to Advanced'
    ]);
});


//Route to users - function
//특정경로로 (/users) 들어가면 redirect('/') 를 이용해서 최상위 디렉토리로 이동
Route::get('/users', function() {
    return redirect('/');
});


// view('home')
// views 디렉토리에서 home파일을 불러오는데 home.blade.php 이어야한다
// 없으면 하나 만들어 주기
Route::get('/', function() {
    return view('home');
});



이렇게 컨트롤러 관련
```
<?php
//namespace
namespace App\Http\Controllers;
class ProductsController extends Controller {
    //이렇게 namespace로 경로 지정해주고 \백스페이스로 경로표시
    // 현재파일명과 같은 이름으로 클래스를 만들고
    // Controller를 상속 (extends)
}
```
이렇게 만들거나

artisan을 이용한다

먼저 artisan 가능한 메세지 보기
```
$php artisan --help
```
```
$php artisan list
```

위에서 만든 파일을 지우고 artisan을 이용해서 만들기  
이렇게 list에 보면 make명령어 있는데 
형식은 controller 이고 이름은 ProductsController로 만들어줌  
```
$php artisan make:controller ProductsController
```
Controller created successfully.
이런 메세지와 함께 바로 만들어 진다

-help 옵션으로 더 보기
```
$php artisan make:controller ProductsController -help
```
위 처럼하면 옵션 메뉴 들이 나오는데   
--force            Create the class even if the controller already exists  
-i, --invokable        Generate a single method, invokable controller class.
그 중 예로 2줄만 보는데 첫번째 -i 는 줄임표현 , --invokable 이런식으로 하면 전체 키워드를 다 써도 되는 뜻

그 중
덮어쓰기는 아래처럼 한다
옵션 넣기
--force


//Http/Controllers 경로

// /products로 경로로 들어오면 위에서 지정한 
// use App\Http\Controllers\ProductsController; 으로
// [ ]안의 내요은 ProductsController클래스를 사용,
// ProductsController 에서 정의를 해줘야함
// 그 다음은 function인데 일단 'index'라는 메소드를 만들어주기
// laravel 8 (new)
//Route::get('/products', [ProductController::class, 'index']);

//Laravel 8 (also new) 2번째 방법
// 경로를 적어주고, @는 메소드를 찾음
Route::get('/products', 'App\Http\Controllers\ProductsController@index');

//Before laravel 8  // 이제 작동 안함 
Route::get('/products', 'ProductsController@index')



