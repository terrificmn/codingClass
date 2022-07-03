[참고페이지 -](https://ckeditor.com/docs/ckeditor5/latest/builds/guides/quick-start.html)

이 부분을 참고한다. 

먼저 CDN 방식으로 스크립트를 넣어줘야한다

```
<!-- ckeditor5는 -->
    <script src="https://cdn.ckeditor.com/ckeditor5/28.0.0/classic/ckeditor.js"></script>
```

이때 메인 레이아웃에 페이지에서 공통으로 쓸 수 있게 yield 기능을 이용해서 
```php
@yield('scripts')
```
공통에 해당하는 부분에 위 처럼 만들고 

그리고 넣고 싶은 페이지에 스크립트를 넣어주는데  
이때 

레이아웃 페이지에서 공통으로가져와서 하는 것이므로 섹션을 만들고 'scripts'로 만들어서 사용  
그 안에 진짜 script 태그를 사용 넣어주면 된다. 
```php
@section('scripts')
    <script>
        ClassicEditor
        .create( document.querySelector( '#editor' ) )
        .catch( error => {
            console.error( error );
        } );
    </script>
@endsection
```

위의 #editor 부분은 textarea태그의 id를 넣어주면 된다. 위 처럼 하면 해당 페이지에 에디터가 뜬다

에디터는 사용할 수 있지만 이미지 업로드가 안된다

Custom image upload adapter 를 사용해야하는데   
이게 무료가 아니라고 하는 것 같다. 대신 커스텀 adapter는 상관없다


자바 스크립트 MyUploadAdapter 클래스를 만들어 줘야하는데 매뉴얼에 나온 코드 바탕으로 만들면 된다  
[cheditor참고하기 ckeditor5](https://ckeditor.com/docs/ckeditor5/latest/framework/guides/deep-dive/upload-adapter.html)  


constructor생성자 메소드와 upload() 메소드 부터 복사

_initRequest() 메소드도 중요

여기에서 
```
xhr.open( 'POST', '{{ route('devnote.imgupload') }}', true ); // 경로수정
xhr.setRequestHeader('x-csrf-token', '{{ csrf_token() }}'); //csrf_token 추가
```
csrf_token 을 추가하는 것 중요, TinyMCE 는 csrf_token을 넣는게 잘 안되서 이걸로 다시 바꿈

그리고 이번에는   
_initListeners() 메소드를 복사한다

이제 서버에서 php로 처리한 다음에 그 결과를 json형태로 돌려줘야한다 그것을 이 메소드가 받는다

그리고   
_sendRequest() 메소드도 복사 붙여넣기

그리고 

MyCustomUploadAdapterPlugin 함수로 추가한다. 이거를 해줘야지 함수 작동하는 듯  

MyUploadAdapter클래스 가 끝나는 부분에 넣어준다

  
이제 ClassicEditor 안에 MyCustomUploadAdapterPlugin 함수를 넣어줘야 하는데   
이때 이 함수의 이름은 변경해도 괜찮다. SimpieUploadAdapterPlugin 으로 바꿈

```
.create( document.querySelector( '#editor' ), {
        extraPlugins: [ SimpleUploadAdapterPlugin ],

        // ...
    } )
```
부분을 추가한다



완성된 코드 넣어주기


이제 해당 페이지에서 새로고침을 하면   
Route [devnote.imgupload] not defined
이라고 뜬다

이제 컨트롤러를 만들어 준다

컨트롤러를 만들고 web.php 에서 url 및 컨트롤러 메소드 등을 지정해주고,  
마지막에 ->name 메소드를 이용해서 url을 넣어줘야지 페이지를 제대로 찾는다

자바스트크립트를 이용해서 클라이언트에서 이미지를 업로드를 하면

xhr.open( 'POST', '{{ route('devnote.imgupload') }}', true );   
이부분의 코드가 실행이 되서 impupload 페이지로 이동을 시켜주고

이제 라라벨에서 컨트롤러가 일할 시간  
imgupload로 메소드에서 이제 코드를 작성해주면 된다 

먼저 잘 되는지 확인해보자

에디터는 화면에 잘 보이고 이상은 없어 보이나   
이미지를 업로드를 하면 업로드를 할 수 없다고 나온다 

<img 이미지 스샷>

이유는 url 정보를 다시 자바 스크립트에게 리턴을 해줘야하는데 그 부분이 당연히 안 되어 있기 때문이다  

```javascript
resolve( {
    default: response.url
});
```
이부분이다. url을 리턴해주자

이제 잘 작동하는지 페이크로 테스트겸 잘 되는지 테스트  

먼저 devnote컨트롤러에서 메소드를 만들고   
return response()->json(['url' =>'http://localhost:8000/storage/images/post_images/60c7c47f-1623704703/Screenshot%20from%202021-06-09%2005-20-39.png']);

이렇게 바로 리턴을 해주자~  
이것은 포스팅해놓았던 이미지 주소이다 ㅋㅋㅋ

그리고 나서   
다시 새로고침후 아무 사진이나 올려주면 

<img >

올린 사진과는 상관없는 위의 주소, 즉 리턴한 주소에 해당하는 사진이 나오게 된다     
즉, 이제 업로드될 정확한 주소만 적어주면 된느 것. 재미있군 ㅋㅋㅋ


