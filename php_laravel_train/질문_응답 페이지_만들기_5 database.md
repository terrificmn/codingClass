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