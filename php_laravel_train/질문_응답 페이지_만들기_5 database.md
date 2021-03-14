<a href=""> 의 path를 메소드로 만들어서 사용하기
우선 html에서 a 태그에서 사용은 이런식으로 했는데

```html
<a href="/questionnaires/{{ $questionnaire->id}}">{{ $questionnaire->title }}</a>
```

주소 경로 다음에 $questionnaire 즉 Questionnarire 모델에서 
받아오는데 이거를 path()라는 메소드를 만들어서 활용성을 높여줄 수 있다

```php
# Questionnarire모델
public function path() {
        // <a href= "/questionnaires/{{ $questionnaire->id}}"</a> 이렇게 주소가 알고 싶을 때
        // '/questionnaires/'.$questionnaire->id 이렇게 되고 $questionnaire는 지금 클래스 자신이니깐 아래처럼 리턴
        //return '/questionnaires/'.$this->id;  이거를 다시 url() 헬퍼함수 사용
        return url('/questionnaires/'.$this->id);
    }
```

그러면 이제 a tag에서 

<a href="{{ $questionnaire->path()}}"> 링크 </a>
처럼 호출해서 사용할 수 있게 된다 그러면 주소가 찍힘


지우기 
만약 유저가 질문 자체를 지우려고 하면 질문이 없어지면 그 해당하는 답변들만 남아있게 되어서 그 해당하는 답변들 (자식들) 지워줘야하는데 
이때에 먼저 질문을 지울 수 있게 버튼을 하나 만들어 주고
그리고 중요한 @method('DELETE')와 @csrf 를 넣어준다
원래 post와 get 밖에 없기 때문에 라라벨에서 DELETE로 하라고 알려주는 것
그러면 delete 방식?을 사용하게 되면서 destroy 메소드를 호출하게 됨

먼저 questionnaire.show.blade.php 의 
```php
<div class="card footer">
    <form action="/questionnaires/{{ $questionnaire->id }}/questions/{{ $question->id }}" method="post">
        @method('DELETE')
        @csrf

        <button type="submit" class="btn btn-sm btn-outline-danger">Delete Question</button>
    </form>
</div>
```
위에서 $questionnaire->id , $question->id 로 각 불러옴  
그리고 그 폼에서 질문이 원래 questionnaire의 id에서 오니깐 id를 받아오고
답변들의 정보도 필요하니깐 답변들의 id도 가져오는 작업을 해줌

questionnaire 모델에 publcPath()메소드를 만들어 주고

```php
public function publicPath() {
    return url('/questionnaires/'.$this->id .'-'. Str::slug($this->title));
}
```

QuestionController에 destroy 메소드를 만든다.
```php
public function destroy(\App\Models\Questionnaire $questionnaire, \App\Models\Question $question)  // route model binding // 한번 더 쓰면 double route model binding
{
    $question->answers()->delete(); //사용자가 질문을 지울려고 할 때, 먼저 그에 해당하는 답변을 먼저 지우고
    $question->delete(); //그 질문을 지움

    return redirect($questionnaire->path());
}
```
여기에서는 더블 라우트 모델 바인딩을 사용했다. 두개의 모델을 가지고 와서 
여기에서 지워주게 됨


