# 라라벨 페이지 나누기
페이지 나누는 것 직접 만듬  
그래서 기능상 크게 문제가 없어서 그냥 쓰기로 함

## 컨트롤러에서 쿼리 빌더로 만들어 줄 수 있다
하지만 paginate() 메소드로 페이지 나누는 것을 쉽게 할 수 있으므로 나중에 참고하자!  

아래 사용법 예제는 참고하기
```php
$data = DB::table('posts')->paginate(10);
reutn view('posts', [
    'data'=>$data
]);

```
비슷한 예:  
```
$posts = Post::with(['user', 'like'])->orderByDesc('id')->paginate(2);
```

paginate()를 해주면 자동으로 offset 과 limit을 설정해준다

또는   
simplePaginate(2) 도 있는데   
Previous 와 Next 만 만들어 준다


blade파일에서 표시할 때  
```
<div>
@foreach($data as $item) 
    {{$item->title}}
@endforeach

</div>

<div>   
    {{data->links()}}
</div>
```

data->links() 메소드를 호출하면 페이지를 자동으로 나눠준다(?)   
테스트를 해봐야함

$data->appends(['sort'=> 'desc'])->links() 로 하면   
중간에 정렬을 해주는 듯 하다.. 테스트 해봐야함
