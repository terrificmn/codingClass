# 폼에서 업데이트

patch, put 메소드를 사용하게 되는데 둘다 메소드 이름만 다르고 거의 비슷한 듯 하다

하지만 폼 태그에서는 get, post 방식만 지원하므로 
라라벨에서는 약간의 트릭(?)을 사용해야하는데 

먼저 업데이트할 페이지에서 

```php
<form
    action="/devnote/{{ $devnotes->slug }} " method="post" enctype="multipart/form-data">

    @csrf
    @method('PATCH')
    
```
로 보내준다. 

form 태그 안에서는 action에 url을 지정해 준다. 위의 변수는 컨트롤러한테 넘겨받은 변수이고 (db에서 나온 데이터)
중요한 것은 url 방식이 /devnote/{slug문자열} 식으로 해주고 
method는 post 방식이다

중요한 @csrf 와 $method('PATCH') 는 꼭 적어준다

의미는 @csrf 토큰을 넘겨주는 것이고 csrf는 Cross Site Request Forgery 로 csrf로 공격을 막기 위해서 사용
자세히는 더 알아봐야...함

그리고 위에서 말했듯 정식으로는 html에서 post방식만 지원하므로 'PATCH' 방식을 사용할 것이라고 
laravel에 알려준다


이제 web.php 에 route을 지정해준다
```php
Route::patch('/devnote/{slug}', 'App\Http\Controllers\DevnoteController@update'); //update (patch 메소드)로 함
```
이런식으로 지정한다. 

처음에 에디터에서 데이터를 넘겨주면 DevnoteController (컨트롤러는 그에 맞춰서 바꾸면 됨) 메소드는 update를 사용하게 됨
클래스의 내의 메소드 이름도 변경도 가능하지만 
naming convension에 의해서 그대로 적어주는것이 좋다

> Route를 일일이 지정하기 복잡하다면 Route::resource('/blog', 'App\Http\Controllers\PostController');   
식으로 사용하면 라라벨에서 알아서 분류해서 처리해줌

route 경로를 보고 싶다면.. 도커에서
```
$ docker-compose run --rm artisan route:list
```
일반적으로는 
```
$ php artisan route:list
```


이제는 컨트롤러 클래스에 와서 update메소드를 만들어서 사용하면 된다
DevnoteController에서 
```php
public function edit($slug) {

    return view('devnote.edit')->with('devnotes', Devnote::where('slug', $slug)->first());
}
```

이런식으로 사용~ 에디터 페이지에서 넘겨준 것에서 $slug 변수로 내용을 받아서 사용하면 됨




