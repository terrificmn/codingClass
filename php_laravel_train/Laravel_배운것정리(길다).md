
## 기본 디렉토리 정보들

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


routes에 디렉토리에 보면   
web.php 파일이 있는데 여기는 view의 역활을 담당   
일단 사용자가 get quest를 하면 (브라우저에서)   
return view('welcome');   
를 하게되는데 그 페이지를 보여주게 되는 것   
resources/views/welcome.blade.php   

```php
Route::get('/welcome', function () {
    return view('welcome');
});
```

/welcome 이란 경로를 입력하면 처음페이지와 같은 페이지를 보여준다  
return을 스트링으로도 할 수 있는데   
또 json 파일 형태도 가능

return 부분을 수정  
** 참고: =>  associative array에서 키에 해당하는 값을 표시할 때 사용     
It uses the same symbol for processing arrays in foreach statements. The '=>' links the key and the value.
```php
$array = array("key" => "value");
```
이런식으로 사용
```php
return ['foo' => 'bar'];
```

view()를 호출하면 resources/views  
안에 blade.php 파일이 있어야 함  
blade는 템플릿 엔진이라고 함  

만약 
```php
Route::get('/test', function () {
    return view('test');
})
```
했다면  

test라고 썼다면 동일한 파일명으로 만들어 준다


get 방식으로 데이터 처리하기   

?name=mike (url에서 이런식으로 get 방식으로 받아다고 한다면..)

```php
Route::get('/', function () {
    $name = request('name');
    return $name;
});
```

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


json파일에 문제가 생겼을 경우 , 파일이 없다고 가정했을 때
```
rm -rf composer.lock 
```

composer install을 하면 composer.lock 파일이 없으면 다시 업데이트를 해줌  
```
$composer install
```


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
```
$cd firstproject
$composer require mollie/mollie-api-php  
```

vendor 디렉토리에서 보면 composer.lock 파일에서 보면 업데이트 되어 있는 것을 알 수 있음

혹시라도 지워졌을 때는 
```
$composer update
```
를 하면 업데이트가 됨


```php
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

```

이렇게 컨트롤러 관련

```php
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

그 중 덮어쓰기는 아래처럼 한다  옵션 넣기  
--force

***만약 아티잔을 이용해서 만들었는데도  
Target class [PostController] does not exist.  없다고 한다면  
클래스의 메소드를 아직 못 만들어서 그러는건데 
/app/Http/Controllers 경로를 
봐도 파일이 없다  
이건 vscode 버그일 수도 있는데  
파일이 계속 없다고 해서  
터미널로 확인해보니  
해당 디렉토리에 파일 이 있는 것을 확인  
vscode에서 파일 창에 보면 새로고침이 있는데 (마우스를 가져가면 생김) 새로고침을 하니 파일이 보인다  
아... 이거때문에 엄청 고생함;;  
프로젝트 지우고 다시 깔고;; 검색하고 file이 안 생긴다고 검색해도 그런 질문따위는 없고;;; 아;;  
파일에 들어가서 암튼 클래스 및 메소드 지정해주면 됨

--아마도 artisan으로 만든어 진것을 바로바로 새로고침이 안되는듯

```php
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
```

라라벨 8에서 업데이트된 내용  
** 참고  
https://github.com/laravel/docs/blob/8.x/upgrade.md#automatic-controller-namespace-prefixing  


데이타 베이스  
.env 파일에 정의된 것을  
config 디렉토리에   
database.php 파일에서   
env() 로 파일을 가져오는 것을 알 수 있음   
'defalut'로 되어 있는 부분에서 env파일에서 해당 내용을 찾아 올 수 없으면 기본 셋팅으로 되어 있음

그리고 좀 더 내려보면  
connections 부분에서 sql종류가 나오는데 여기에서 자기가 사용하는 이름으로 사용하면 됨  
예를 들어 sqlite이면 env파일에서   
DB_CONNECTION=sqlite 이런식으로 하면 됨



Eloquent 모델 만들기  
내 프로젝트 이동  
```
php artisan make:model Post
```

엘로퀀트 모델은 same api sql query를 지원   
app/Http/Models 에 가보면 Post.php가 생겨있고  
Post extends Model이 생성되어 있음  

참고:  
https://laravel.com/docs/7.x/eloquent#eloquent-model-conventions  

여기 Post클래스에서는   
```php
/ Eloquent 모델은 클래스이름을 보고 테이블을 결정하는데 
    // 클래스이름이 Post인데 복수형으로 테이블을 결정한다고 함(기본)
    // 그래서 posts 가 테이블이 이름이 되어서 찾아옴
    // 이름을 바꾸려면 프로퍼티를 바꿔줘야함 (아래처럼)
    protected $table = 'post';
```

aritsan 이용해서 마이그레이션 할 수 있음  
직접 sql쿼리로 만든게 아니라 

명령어 조합은 create_테이블명_table  
update-테이블명-table  

```
php artisan make:migration create_post_table
```
결과 아래처럼 나온다
```
2021_02_27_211952_create_post_table
```

database/migrations  
에 가보면    
2021_02_27_211952_create_post_table.php 가 만들어져있음

이런식으로 하면 버전 컨트롤을 할 수 있다고 함

해당 파일을 보면  
CreatePostTable이 있는데 여기에 보면  
up()메소드에 컬럼을 지정해줄 수 있음  
```php
$table->string('slug');
            $table->text('body');
            $table->timestamps();
            $table->timestamp('published_at')->nullable();
```
이런식으로 추가해 준다

down()메소드는 drop table을 해주고 롤백할 때 사용한다고 함

그 다음에  
다시 터미널에다가   
```
$php artisan migrate  
```
그러면 마이그레이션 해줌 (테이터베이스 테이블 생성)

DB에서 확인해 보면   
```
MariaDB [myblog]> show tables;  
+------------------+
| Tables_in_myblog |
+------------------+
| failed_jobs      |
| migrations       |
| password_resets  |
| post             |
| users            |
+------------------+
```
요렇게 만들어 진것을 알 수 있음  
///아, db프로그램 깔아야 하는데 귀찮;;


새로운 컬럼 추가하기     
add_컬럼명_to_테이블명_table
```
$php artisan make:migration add_title_to_post_table
```

그리고 다시 daatabase/migrations 디렉토리로 가보면  
또 파일이 생성되어 있음  
2021_02_27_213022_add_title_to_post_table.php

여기에 다시 up() 메소드에 추가해준다  
Schema 클래스 부분 내용안에
```php
$table->string('title');
```
를 넣어준다

그리고 down() 메소드의 Schema클래스 {}안에 적어줌
```php
$table->dropColumn('title');
```

그리고 다서 
```
php artisan migrate
```
을 하면 컬럼이 추가된다

```
Migrating: 2021_02_27_213022_add_title_to_post_table
Migrated:  2021_02_27_213022_add_title_to_post_table (9.82ms)
```
이런메세지와 함께 만들어 짐

이제 테이블 있는지 확인해 보면 만들어져 있다

그런데 이런 것은 사실 product 출시전에 한다고 하고  
대개는 다른방식으로 한다고 함  
일단, db롤백하기  
위에서 down()메소드에 DropColumn 컬럼을 정해놓은것을 실행하게 해준다

```
$php artisan migrate:rollback
```

결과
```
Rolling back: 2021_02_27_213022_add_title_to_post_table
Rolled back:  2021_02_27_213022_add_title_to_post_table (12.96ms)
```

artisan만 입력하면 커맨드를 알 수 있음  
```
$php artisan
```

----

이제 다시 처음 테이블 셋팅으로 돌아가서  
2021_02_27_213022_add_title_to_post_table 삭제 후 

그 전에 작성했던 create_post_table.php로 돌아가서  
테이블 컬럼을 추가  
```
$table->string('title');  
```
그리고 나서 다시 artisan migrate를 하면   
할게 없다고 나옴, 이미 진행했기 때문에   
그래서 2가지 방법이 있다고 함  

하나는 
```
$php artisan migrate:rollback
```
이렇게 해서 다시 완전 처음 상태로 롤백  
데이터는 다 지워진다. 정말 주의할 것  
그리고 나서 다시 migrate를 한다

그러면 수정했던 내용을 기반으로 다시 만들어줌

또 다른 방법은  
데이터가 없을 때 하는 방법 테이블을 모두 드랍시키고 다시 생성 
```
$php artisan migrate:fresh
```

## 같은이름으로 모델과 컨트롤러와 마이그레이션 파일을 동시에 만들기
-m 은 migration  
-c 는 controller  
```
$php artisan make:model Project -mc
```
실무에서는 이런식으로 많이 사용한다고 함



테이블 생성시 
```php
$table->id();
$table->text('body');
// default(false)로 지정하기, false로 지정안하면 기본은 1, 그러면 나중에 처리할 떄 한게 되므로 
$table->boolean('completed')->default(false);
// 0/1으로 처리할 수 있음 0면 not complete, 1이면 completed
//또는
// 타임스탬프로하면 완료된 것도 알 수 있지만, 정확한 시간도 알 수 있는 장점이 있음
// 교육상 일단 boolean방식으로 함
//$table->timestamp('completed_at')->nullable();
$table->timestamps();
```
참고

tinker 사용하기
```
php artisan tinker
```
프롬프트 상태에서 db생성하거나 할때 도움을 줌   
디비 테이블안의 데이터 생성하기

python 명령창에서 사용하는 것과 비슷

```
Psy Shell v0.10.6 (PHP 8.0.2 — cli) by Justin Hileman

>>> $assignment = new App\Models\Assignment;
=> App\Models\Assignment {#3330}
>>> $assignment->body = 'finish first school work';
=> "finish first school work"
>>> $assignment->save();
=> true
```

`$assignment = new App\Models\Assignment;`
로 네임스페이스로 클래스 저장(생성)
`$assignment->body = 'finish first school work';`
프로퍼티 접근해서 내용 저장
`$assignment->save();`
마지막으로 db에 저장

이렇게 하면 db에 저장된 것을 알 수 있음

그 밖에 데이터보기는 
>>> App\Models\Assignment::all();

첫번째꺼만 보기
>>> App\Models\Assignment::first()

조건 지정해서 보기
>>> App\Models\Assignment::where('completed', false)->get();


만약 사용자가 complete()을 할 수 있다고 가정하면서   
\$assignment->complete() 가 필요한데 메소드를 만들어 줘야한다
 
Assignment 클래스 모델에 메소드를 추가해주고    
```php
 public function complete() {
        $this->completed = true;
        $this->save();
    }
```

다시 tinker를 나간후 들어간다
```
$php artisan tinker
```

```
>>> $assignment = App\Models\Assignment::first();

>>> $assignment->complete();
```
이렇게 또 $assignment를 저장해주고 네임스페이를 사용할 것이고 클래스의 first() 첫번째를 가지고 와라 라는 의미

그리고 메소드를 호출 complete()   
그러면 메소드에서 짠 로직으로 completed컬럼이 true로 저장됨

이렇게 하는 이유는 OOP를 하기 위해서 라고 함  
completed컬럼을 직접 바꿀 수도 있으나,   
같은 코드를 매번 반복하지 않기 위해서   
메소드를 만들어서   
바꿀 수 있게 하는 요령을 연습한거라고 이해함




--- blade엔진 php 활용

레이아웃 페이지 만들기

먼저 view 페이지에서 resources/views 에서   
layout.blade.php 파일을 먼저 만들어 준다  
welcome.blade.php 를 활용한다면,   
welcome.blade.php 의 레이아웃을 담당할 부분을 넣어준다   
예: <body> 부분이 빠진 부분 (전체 부분)

그리고 <body> 와 </body> 안에는   
@yield ('content') 라고 입력해주고   

이제 welcome.blade.php 파일에는   
중요한 본문 내용만 남는다  
이제 맨 위에 layout.blade.php 파일에서 나머지 내용이 있는 것을 알려주기 위해서   
맨 위에   
```
@extends ('layout')    
```
이라고 입력하고   
실제 입력 내용이 있는 부분 바로 위와 아래에   
```
@section ('content')   
실제 내용   
예를 들어   
<div> 
..생략
</div>
```@endsection

해주면 됨


정리-   
그리고 다른 페이지도 위에 처럼 layout를 지정한다면     
가장 중요한 view 부분을 수정해줘야함  
/routes  
에서 web.php 파일에서 

```php
Route::get('/contact', function () {
    return view('contact');
});
```

예를 들어 contact 페이지를 만든다고 하면 위에 처럼 써주고  
다시   
resources/views 에서   
contact.blade.php 를 만들어 준다  
그리고 이 파일안에서 layout페이지로부터 확장되었다고 선언?해주고   
센션과 엔드섹션안에 내용을 넣어 주면 된다  

예:
```php
@extends ('layout')

@section ('content')
    <h1>Hello World</h1>
@endsection
```
이러면 url에 /contact  
로 입력하면 해당 페이지가 뜬다 

그리고 layout.blade.php 파일안에는 
```php
@yield ('content')
```
그래서 여기에서 ('header') ('footer') 식으로 만들면 됨




li tag에 쓰인 것을 a tage의 경로와 맞춰서 같으면 나오게 하는 한줄 표현식    
// current_page_item 은 css class인데 한줄 표현식으로 정리  
// Request클래스의 path()호출해서 '/'경로가 같으면 'current_page_item을 echo하고 : 아니면 '' 아무것도 표시하지 않음    ssssssssssssss
<!-- 원래 li class='current_page_item' 임-->
<li class="{{ Request::path() === '/' ? 'current_page_item' : '' }}"><a href="/" accesskey="1" title="">Homepage</a></li>
<li  class="{{ Request::path() === 'clients' ? 'current_page_item' : '' }}"><a href="/clients" accesskey="2" title="">Our Clients</a></li>

참고  
Request::path() 기능 현재 경로를 출력해줌    
만약 현재 경로가 http://127.0.0.1:8000/about 이라면  
about 을 출력함

다른 방법 is()메소드를 사용할 수도 있음  
{{ Request::is('about') ? 'current_page_item' : '' }}   
참고로 is()메소드에는 *와일드카드 사용가능   
에: is('about*')  

 
// 템플릿 html 파일 이용하기  
https://templated.co/simplework  
에서 원하는 것을 다운받은 후   
압축을 푼 후에

public 디렉토리 안에 복사해준다 (index.html파일 빼고)  
정리를 하고 싶으면   
css 디렉토리를 만들어주고 그 안에 css관련 파일을 넣어주고  
이제 index.html 파일의 내용을 모두 복사해서   
resources/views 디렉토리안에   
welcome.blade.php 파일에 넣어준다   
그리고 나서 위의 layout 했던 작업을 통해서 바꿔주면 됨  


/// tinker 사용하기
```
$php article tinker
```

여기서 사용할 때는   
먼저 인스턴스 사용할 model 클래스로 인스턴스 생성해준다  
$article = new App\Models\Article;  
그 후에  
DB에 넣고 싶은 내용 접근해서 입력해주기  
$article->title = 'this is title';  
$article->excerpt = 'this is excerpt';  
$article->body = 'this is body';  

그리고 저장 save()메소드로 저장  
\$article->save():

true 라고 나오면 성공

그리고 db테이블을 확인해보면 내용이 잘 입력되어 있음













-----
db에서 데이터 가져와서 출력하기

먼저 view 쪽에서 Eloquent 모델을 이용해서  
내용을 가져온다

```php
Route::get('/about', function () {
    // 모두 가져옴
    //$article = App\Models\Article::all();
    // 2개만 가져옴
    //$article =App\Models\Article::take(2)->get();
    // 2개만 가져오고 page를 자동으로 나눔
    //$article =App\Models\Article::paginate(2);
    // 최신것부터 정렬해서 보여주기
    //$article =App\Models\Article::latest()->get(); // order by created_at desc 
    // latest('컬럼명')을 넣어주면 그 컬럼 기준으로 정렬해줌
    //$article =App\Models\Article::latest()->get(); // order by created_at desc 
    //return $article; //json 파일로 보여줌
    
    return view('about', [
        'articles' => App\Models\Article::take(3)->latest()->get()
    ]);

    /* 참고: 위의 inline 표현(한줄코드)이랑 
    $articles = App\Models\Article::all(); //복수형으로 변수 만들어주고
    return view('about', [
        'articles' => $articles
    ])
    이거랑 같다
    */
});
```
그 다음 데이터 표시하고 싶은 곳에서 출력하기  
그 중에   
이런 반복되는 ul-li가 있을 때   
```
<ul class="style1">
    <li class="first">
        <h3>Amet sed volutpat mauris</h3>
        <p><a href="#">In posuere eleifend odio. Quisque semper augue mattis wisi. Pellentesque viverra vulputate enim. Aliquam erat volutpat.</a></p>
    </li>
    <li>
        <h3>Sagittis diam dolor sit amet</h3>
        <p><a href="#">In posuere eleifend odio. Quisque semper augue mattis wisi. Pellentesque viverra vulputate enim. Aliquam erat volutpat.</a></p>
    </li>
    <li>
        <h3>Maecenas ac quam risus</h3>
        <p><a href="#">In posuere eleifend odio. Quisque semper augue mattis wisi. Pellentesque viverra vulputate enim. Aliquam erat volutpat.</a></p>
    </li>
</ul>
```

반복시킬 부분만 남기고 삭제
```
<ul class="style1">
    <li class="first">
        <h3>Amet sed volutpat mauris</h3>
        <p><a href="#">In posuere eleifend odio. Quisque semper augue mattis wisi. Pellentesque viverra vulputate enim. Aliquam erat volutpat.</a></p>
    </li>
</ul>
```

그 다음에 
```
@foreach ($articles as $articles)
				<li class="first">
					<h3></h3>
					<p><a href="#"></a></p>
				</li>
@endforeach
```
laravel 벨 스타일로 써줄 수 있음
```php
<?php echo $articles->title;?> ## 처럼 내용을 보여줄 수도 있겠지만  
laravel의 blade를 이용하면  
{{ $articles->title }}     
```
처럼 사용하면 된다  
```php
아래와 같이 됨
<ul class="style1">
    @foreach ($articles as $articles)
    <li class="first">
        <h3>{{ $articles->title }}</h3>
        <p><a href="#">{{ $articles->excerpt }}</a></p>
    </li>
    @endforeach
</ul>
```

이렇게 해주면  
sidebar쪽에 db에서 잘 뽑아와서 보여주는데   
문제는 데이터가 있으면 더 보여준다는 것  
그래서 만약 이럴때는 
  
view()를 수정해줘야한다  
routes 디렉토리로 이동해서  
web.php 
```php
return view('about', [
        //'articles' => App\Models\Article::latest()
        ->get() 에서 아래처럼 바꾸기 take()메소드로 원하는 만큼만 가져오기
        'articles' => App\Models\Article::take(3)->latest()
        ->get()
    ]);
```


모델 db 테이블 만들기   
먼저 articles를 만들려고 하는데 모델을 만들면서 -m 옵션을 넣어서 migrations 도 만들어 준다  
```
$ php artisan make:model Article -m
```
  
```php
public function up()
    {
        Schema::create('articles', function (Blueprint $table) {
            $table->id();
            //$table->bigIncrements('id'); 원래는 이걸로 했어야 함
            $table->string('title');
            $table->text('excerpt');
            $table->text('body');
            $table->timestamps();
        });
    }
```
database/migrations 에   
위와 같은 내용을 입력한 다음에 저장 후   
마이그레이션 

```
$php artisan migrate
```

그러면 db테이블이 만들어 진다

```
$php artisan tinker
```
를 통해서 DB를 만들어 줘도 됨  
위에 나온 것처럼(위에 적었던것 같음) 참고


컨트롤러 만들기
php artisan make:controller ArticleController



레이아웃에서 css파일 경로를 설정했는데   
다른 페이지에서   
하위 디렉토리가 되면서 css경로가 틀어지면 제대로 css가 안나오게 되는데 이때는 
 
경로 앞에 / 를 넣어주면 간단하게 해결됨
예:
 <link href="css/default.css" rel="stylesheet">

 바꿈
 <link href="/css/default.css" rel="stylesheet">

절대경로로 바꿔준 것임 . 맞겠지??;;



컨트롤러의 7가지 기능들..  

```php
// 컨트롤러에는 최소 7개의 기능을 할 수 있게 만들어 줘야함
    // 전체보여주기(index), 하나 보여주기(show), 크레이트, 에디트, 저장, 업데이트, 삭제
    // index, show, create, store, edit, update, destory

    // Reder a list of a resouce.
    public function index() {
        $articles = Article::latest()->get();
        return view('article.index', ['articles' => $articles]);
    }

    // Show a single resource.
    public function show($id) {
        $articles = Article::find($id);
        // aritcle.show 여기에서 .은 하위 디렉토리 의미
        return view('article.show', ['article' => $articles]);
    }

    // Create a view to create a new resource
    // submit 버튼으로 입력하는 것
    public function create(){

    }

    // Persist the new resource
    public function store(){
        
    }

    // Show a view to edit an existing resource
    public function edit(){
        
    }

    // Persist the edited resource
    public function update(){
        
    }

    // Delete the resource
    public function destroy(){
        
    }
```

___

php artisan 으로 해주는 기능이 또 있음   
-r 옵션

php artisan help  
-r, --resource         Generate a resource controller class.
이런 옵션이 있는데   

그래서 
```
$ php artisan make:controller ProjectController -r
```
해보면  자동으로 메소드를 7개를 만들어 준다

ProjectController.php  파일을 지우고   
이번에는 모델도 같이 만들자

```
$php artisan make:controller ProjectController -r -m Project
```

-m 옵션으로 Project 라는 모델 클래스를 만드는데   
모델이 없는데 만들겠냐고 물어본다 그러면 yes

그러면 ProjectController 은 Project의 모델을 참조하면서 만들어진다

routes 디렉토리에서   
이제 web.php 에서 route()하는 법을 살펴보자

일단 컨셉을 살펴보면 url을 어떤식으로 가져가는지와   
어떤방식으로 하는지는 아래 범주를 크게 벗어나지않음  
중요한 것은 아래의 방식을 지키면서 어느정도 유연함을 가지면서 만들면 된다고 함

```
// GET, POST, PUT, DELETE
// url을 통해서 하는 방법으로 보기, 쓰기, 수정, 지우기 
// 기본
// GET /articles
// GET /articles/:id
// POST /articles
// PUT /articles/:id
// DELETE /articles/:id/

비디오라는 페이지를 본다고 할 때 
//리스트 보기
// GET /videos

//비디오에서 새로 입력하기
// GET /videos/create

// 입력 후 저장submit 을 누르면 
// POST /videos

//아이디2의 비디오 보기
// GET /videos/2

//아이디2 비디오를 수정하기
// GET /videos/2/edit

//수정하기 아이디2의 비디오 수정
// PUT /videos/2

//아이디2의 비디오 지우기
// DELETE /videos/2

```


html의 form태그 안에는 항상  
@csrf 를 넣을 것

게시물을 업데이트 할 때나 지울 때는   
라라벨 방식으로 PUT, DELETE, PATCH등을 사용하는데   
html form태그에서는 POST/GET 밖에 모르기 때문에  
```
@method ('PUT') 
```
위와 같은 식으로 정의해준다




update의 validation  
중  create html tag에 required 를 넣어주면   
한번 더 클라이언트 사이드에서 검증할 수 있지만  
이게 서버 쪽에서까지 막아주는 것은 아님  
```php
<input class="input" type="text" name="title" id="title" required>


<input> tag 에러방지

<input class="input {{ $errors->has('title') ? 'is-danger' : '' }}" type="text" name="title" id="title">
    @if ($errors->has('title'))
        <p class="help is-danger">{{ $errors->first('title') }}
    @endif
```
여기서 $errors->has('title') ? 'is-danger' : '' 는 타이틀에 에러 (비어있는 상태에서 확인버튼 시) 이면   
'is-danger' 를 출력해주고 아니면 아무것도 출력안함   
{{ $errors->first('title') }} 은 에러가 있으면   
The title field is required.  이런 메세지를 출력해준다    

라라벨 블레이드에서 처리할 수 있는 방법으로   
헬퍼 $errors 클래스를 이용함

같은 효과의 또 다른 방법
```php
<input class="input @erorr('title') is-danger @enderror" type="text" name="title" id="title">
    @error('title')
        <p class="help is-danger">{{ $errors->first('title') }}
    @enderror
```

에러 전에 입력했던 것 다시 출력해주기   
라라벨 old() 함수를 사용
```php
<input 
    class="input {{ $errors->has('title') ? 'is-danger' : '' }}" 
    type="text" 
    name="title" 
    id="title"
    value="{{ old('title') }}">
```
그러면 에러가 발생하지 않고 다른 입력창에서 에러가 발생하면 바로 전에 입력했던 것을 출력해줌

<textarea>에는 블레이드의 기능을 이용해서 출력만 하게 해주면 됨
```
 <textarea class="textarea @error('body') is-danger @enderror" 
    name="body" 
    id="body"
    >{{ old('body') }}
</textarea>
```


만약 게시글을 id를 매칭해서 보여주는 식으로 되어 있는데   
게시글 타이틀을 url에 입력시킬 경우는 404에러가 남  
이런 경우도 처리해주고 싶을 때는   
해당 클래스에 메소드를 추가해준다  
Article 이라는 클래스를 한다고 할 때는  
```php
public function getRouteKeyName() {
    return 'slug';
    // Article::where('slug', $article)->first(); 의 의미가 됨
}
```


만약에 경로를 바꾼다고 하면  
web.php에서    
Route::get('/article/{article}', 'App\Http\Controllers\ArticleController@show');  
이렇게 지정을 했는데   
 
경로를 /blog/article/{article} 이런식으로 바꾼다고 하면  
html view 를 담당하는 index.blade.php 파일에서   
html의 a tag에 사용한 경로도 바꿔줘야한다    
```
<a href="/blog/article/{{ $article->id }}">
```

이럴 때 사용하는 방법  
name()메소드로 이름을 지정할 수 있다. 경로를 저장하게 됨  
```php
Route::get('/article/{article}', 'App\Http\Controllers\ArticleController@show')->name('article.show');
```

그 다음에   
다시 index.blade.php 파일로 돌아가서  
```php
<a href="{{ route('article.show', $article->id )}}" >
```
위에서 name으로 지정한 article.show로 경로를 정해주고,    
그 경로는 /article/{article} 와이드카드로 되어 있기 때문에 두번째 파라미터에서 id property를 지정해주면 됨  
두번째 파라미터를 $article로만 지정해도 라라벨에서 알아서 id로 처리해줌

그리고 컨트롤러로 돌아와서   
return 해 줄 때  redirect로 리턴해주면 됨  
예: 
```php
return redirect(route('article.show', $article));
```

위와 같은 방식은 모든 route에 ->name()을 넣어서 가능  


더 간결한 코드로 바꾸려면  
아예 Article 모델 클래스에서 메소드를 추가해준다  
```php
public function path() {
    // route을 name() 지정했으면 
    // 아니면 경로 자체를 적어줌
    return route('article.show', $this);
}
```
이런 코드를 넣어주면  
어떤 id 1번의 글을 읽어왔다고 치면  
localhost/article/1   
이런식으로 리턴되기 때문에  
이거를 controller에서 적용하면  

이렇게도 사용할 수 있겠지만  
```php
return redirect(route('article.show', $article));
```

이거를 
```php
return redirect($article->path());
```
이렇게도 사용할 수 있다고 함


___


factory 사용  
PostFactory를 만든다음에   
PostFactory에 만들어 준다음에  

tinker에 들어가서 
```php
\App\Models\Post::factory()->create();
##더미 데이터를 만들어서 DB에 넣어준다
```

```php
\App\Models\Post::factory()->count(2)->create();
##카운트만큼 더미데이터 넣어줌
```
