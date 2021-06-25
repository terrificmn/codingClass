# 폼에서 delete 활용하기

이번에는 delete 메소드를 사용한다

하지만 폼 태그에서는 get, post 방식만 지원하므로 (업데이트와 마찬가지로..)
라라벨에서는 약간의 트릭(?)을 사용해야하는데 

먼저 업데이트할 페이지에서 

```php
<form
    action="/devnote/{{ $note->id }}"
    method="post">
    @csrf
    @method('DELETE')
    
```
로 보내준다. 

form 태그 안에서는 action에 url을 지정해 준다. 위의 변수는 컨트롤러한테 넘겨받은 변수이고 (db에서 나온 데이터)
중요한 것은 url 방식이 /devnote/{id} 이런식으로 해주고 
method는 post 방식이다

중요한 @csrf 와 $method('DELETE') 는 꼭 적어준다

의미는 @csrf 토큰을 넘겨주는 것이고 csrf는 Cross Site Request Forgery 로 csrf로 공격을 막기 위해서 사용
자세히는 더 알아봐야...함
'DELETE' 메소드를 사용한다고 적어준다

이제 web.php에서 설명할 차례
```php
Route::delete('/devnote/{id}', 'App\Http\Controllers\DevnoteController@destroy'); //delete (delete 메소드)
```
위에서 delete메소드를 사용한다고 했으므로 Route::delete를 사용한다고 해준다
슬슬 헛깔릴 수도 있으나ㅠ 어쨋든 update와는 다르게 확실하게 지우기 위해서 id를 사용, slug를 이용해도 되나
slug가 중복이 될 수가 있어서 아직 slug 중복되는 것을 방지하는 알고리즘을 짜지 않음

어쨋든... 컨트롤러에서 destory메소드를 사용한다. 
이것도 네이밍 컨벤션을 (이름 짓는 요령/방식)을 그대로 사용하는게 좋다. 그래서 destroy 메소드라고 만들어 준다

DevnoteController에서 
```php
public function destroy($id) {
    $devnote = Devnote::where('id', $id);
    $devnote->delete();

    return redirect('/devnote')->with('message', 'Your devnote-post has been deleted!');
    }

```

이런식으로 사용~ 에디터 페이지에서 넘겨준 것에서 $id 변수로 내용을 받아서 사용하면되고 깔끔하게 삭제가 된다.
참고로 with('message', '블라블라'); 로 보내 준것은

redicrect할 페이지, 위에서는 /devnote 페이지에서 받아주는데 블레이드 파일안에 
```php
@if (session()->has('message'))
    <div class="w-4/5 m-auto mt-10 pl-2">
        <p class="w-2/6 mb-4 text-gray-50 bg-green-500 rounded-2xl py-4 pl-2">
            {{ session()->get('message') }}
        </p>
    </div>
<!-- 파일저장 실패시 -->
@elseif (session()->has('error_msg'))
    <div class="w-4/5 m-auto mt-10 pl-2">
        <p class="w-2/6 mb-4 text-gray-50 bg-red-500 rounded-2xl py-4 pl-2">
            {{ session()->get('error_msg') }}
        </p>
    </div>
@endif
```
로 받아주는데 seession()함수에 message 변수로 받게 되므로 메세지를 보여줄 수가 있다. 



