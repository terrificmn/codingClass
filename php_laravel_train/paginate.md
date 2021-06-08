컨트롤러


```php
$data = DB::table('posts')->paginate(10);
reutn view('posts', [
    'data'=>$data
]);

```
비슷한 예:
$posts = Post::with(['user', 'like'])->orderByDesc('id')->paginate(2);

paginate()를 해주면 자동으로 offset 과 limit을 설정해준다

또는 
simplePaginate(2) 도 있는데 
Previous 와 Next 만 만들어 준다


blade파일에서 표시할 때 
<div>
@foreach($data as $item) 
    {{$item->title}}
@endforeach

</div>

<div>   
    {{data->links()}}
</div>


data->links() 메소드를 호출하면 페이지를 자동으로 나눠준다(?) 
테스트를 해봐야함

$data->appends(['sort'=> 'desc'])->links() 로 하면 
중간에 정렬을 해주는 듯 하다.. 테스트 해봐야함
