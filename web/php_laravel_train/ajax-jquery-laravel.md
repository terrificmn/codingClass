# ajax laravel
전체 흐름은 대충 아래처럼 진행   
html form 데이터에서 post 방식으로 전송 ==>   
jquery ajax 에서 해당 url 데이터 전송,(생략도 가능) 로 처리 ==> 이때 새로 고침이 안 되게 됨   
라라벨의 router쪽에서 주소 및 지정된 controller 클래스의 메소드로 연결 ==>  
해당 함수에서 데이터 처리, DB저장, 뭔가 진행한 후에 json으로 리턴해주기 ==>   
보통 view 페이지로 넘겨주던 것을 그냥 json 결과만 넘겨주면 된다. (특정 페이지로 넘어가지 않기 때문에(새로고침이 안되므로, url이 동일하다면 그대로 있기 때문))   
이후 php에서 넘겨준 데이터로 jquery ajax의 success()부분에서 처리할 수가 있다. ==> 특정 input를 지우거나, 메세지를 띄우거나 등..


### html form 만들기
form 의 action은 POST method로 만들어 준다.

form 에서  input 만들어 준다. 
```
<input type="text" name="title">
<input type="text" name="input_text">
```
그리고 submit 을 하나 만들어 준다.
```
<input type="submit" name="submit">
```
예 :
blade 구문으로 만들어서 url을 지정
```
<form action=" {{ url('ajax_upload') }} " method="POST" id="add_post">   
@csrf
    <input type="text" name="title">
    <input type="text" name="input_text">
    
    <input type="submit" name="submit">
</form>
```

form외에 받을 값을 text로 넣어준다. 
`<div id="message"></div>`
이후 리턴값을 받은 후 js 에서 활용

html 페이지에 script을 src를 넣어준다.
```js
<script type="text/javascript"> 
    $(document).ready(function() {
        // html의 form id를 가져온다.
        $('#add_post').on('sumbit', function(event) {
            event.preventDefault();  // 페이지가 reload가 되는 것을 막아주는 함수
            /// preventDefault()를 빼고 확인 해보기
            alert("hello ajax")

            jQuery.ajax({
                url:"{{ url('ajax_uplad') }}", 
                data: jQuery("#add_post").serialize(),  // form id
                type: 'post',
                

                /// success 일 경우에 함수 호출
                success:function(result) {
                    
                    $('#message').css('display', 'block');
                    /// controller 에서 return 해준 json을 받을 수가 있다.
                    jQuery('#message').html(result.message);
                    jQuery('#add_post')[0].reset(); /// 해당 form의 input박스 내용을 지워준다.

                }

            })
        })
    
    });
```


[cdnjs.com/libraries/jqeury에서 cdn주소 넣어주기-여기 참고](https://cdnjs.com/libraries/jquery)   
cnd의 jquery.min.js 를 넣어주면 된다.   
해당 사이트에서 주소를 복사해서 script 태그에 넣어준다. (html 의 head 안에 )
```
<head>
// 생략
    <script src="https://cdnjs.cloudfalre.com/....생략" > </script>
</head>
```

> jquery에서는 id는 `#이름` 으로 사용할 수 있고, class는 `.이름`으로 사용할 수가 있다.  
라라벨에서는 그냥 name 속성만 가지고 받을 수 있다.   


위에서 `$(document).ready()` 와 비슷한 기능
```js
    // 아래의 2개 함수는 거의 비슷한 기능, $이 붙은 것은 jquery를 사용하는 것이고, document로 하는 것은 javascript로 사용
    // Handler when the DOM is fully loaded
    // $(document).ready(function() {} == document.addEventListener("DOMContentLoaded", function() {
```

`jQuery.ajax({});`부분은 `$.ajax({});` 처럼 사용해도 된다.   

## token 관련 만들어주기 
ajax를 사용할 때 token이 일치하지 않으면 csrf token 관련 에러가 발생한다.   

라라벨 공식 문서에도 나와 있음  
```js
$.ajaxSetup({
    headers: {
        'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
    }
});
```
ajaxSetup() 함수를 사용해서 headers를 설정   
물론 이때 html head 태그에 csrf 관련 token이 들어가야 한다.   


다른 방법으로는 ajax() 함수내에서 data에 token을 넣어준다.
```js
$.ajax( {
    url: //생략
    data: {
        "_token": "{{ csrf_token() }}"
    },
    // 생략
})
```

첫 번째 방법으로 사용하자. 


## data 만들어 주기
```js
$.ajaxSetup({
    ///...생략
}) 
jQuery.ajax({
    url:"{{ url('ajax_uplad') }}", 
    data: jQuery("#add_post").serialize(),  // form id
    type: 'post',

    /// success 일 경우에 함수 호출
    success: function(result) {
        // do something        
    },
    error: function(xhr, status, error) {
        // Handle error
        $('#response').html('Error: ' + xhr.status + ' ' + error);
    }
})
```
data: 부분을 만들어서 php 쪽으로 보내주는 것이 중요한데,  

어쨋든 php쪽에서 return 을 스트링이나, 200 을 리턴하거나,   
db에서 받은 값을 넘겨줄 경우에는 ajax 함수에서 다시 처리할 때 문제가 없는 듯 하다.   

사실 딱히 보내지 않아도  
php 쪽에서는 Request 로 form 데이터에서 넘어온 것을 처리할 수가 있다.  
(리턴된 결과를 ajax( )의 success function에서 받아서 처리할 수가 있다.)

> 정확한 이유는 모르겠지만, 보안? csrf_token 등과 관련이 있는지는 몰라도   
아마도 뭔가를 잘 못해서 그럴 가능성이 높아 보이지만...   

그러므로 `data: `을 처리할 경우에는 serialize()함수로 form 데이터를 전체를 넘기거나  
아니면 val() 함수로 읽어서 데이터를 만들어서 넘겨주면 된다.   

```js
data: jQuery("#add_post").serialize(),  // form id
또는 
data: {'title' : $("#title").val(), },
```
이렇게 만들어야지 문제가 없다. 임의의 키값으로 넘겨주게 되면 예를 들어 'title' 대신 (input의 name값)  
'subject' 식으로 만들어서 넘겼을 때   php쪽에서 request->title 로 받아서  리턴을 해준 값을   
'subject': $request->title 이런식으로 넘겨준다면,  js에서 받았을 때 null이 된다.   
(계속 null 이 나와서 시간만 많이 뺐긴 듯 하다... )    
데이터를 다시 만들어서 보내주는 것이라 문제가 없을 줄 알았으나,  보안 문제인지, 변수가 소멸되는지 잘 모르겠다.  

이래저래 정리 안되게 말이 많은데,...;;   
js쪽에서는 어차피 form데이터를 변수로 만들어서 클라이언트쪽에서 가지고 있을 수 있고   
php 서버 쪽에서는 db 처리 후 필요한 데이터를 리턴해주거나, 아니면 필요한 새로운 변수 값등을 리턴   
이런식으로 충분히 사용할 수 있으니   
input 데이터에 있는 중복되는 데이터를 넘겨주느라고 고생 안해도 될 듯 하다.   
(이유는 구지 js로 안넘겨도 php쪽에서 데이터를 확인 가능하기 때문)   

본연의 기능인 **새로고침이 안 되게** 해주는 것에 좀 더 집중을 하면 좋을 듯 하다. 


## post method 사용
form 태그 및 ajax 를 post 방식으로 사용할 경우에는 php, nodejs 등 서버사이드에서 처리할 수가 있어야 한다.  
단순히 html과 js만 가지고 테스트 하려고 했더니, 405method not allowed 에러가 발생한다.

대신, *get* 방식으로 변경하고 html, js만 가지고 테스트는 할 수 있을 듯 하다.


## laravel 코드
라라벨의 web.php 의 route를 연결해준다.  
route::post("/ajax_upload", myController클래스::메소드 연결);

Http/Controllers 디렉토리에서 해당 myController클래스.php 파일에서 
해당api 함수 만들기


예 
```php
use App\Models\Post;

class 내... {
    public function upload(Request &request) {
        $data = new Post;  // Post 모델 인스턴스 해주고
        // 물론 migration포함 db테이블 만들어져 있어야 함
        $data->title = $request->title;
        $data->input_text = $request->input_text;

        $data->save(); ///db 저장

        // return response()->json([]); // json 으로 view페이지로 리턴해주기 // 추후 json 만들어서 보내야함
        return response()->json(['message'=>'upload successfully']); // json 으로 view페이지로 리턴해주기 // 추후 json 만들어서 보내야함
        // view 관련 페이지에서  blade로 연결된다.
    }
}
```
