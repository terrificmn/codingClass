<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\PostController;
use App\Http\Controllers\ArticleController;
/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/template', function () {
    return view('template');
});

Route::get('/test', function () {
    return view('test');
});

// 여기에서 라우트만 해주면 컨트롤러에서 보여주기, 인덱스, 삭제, 삽입 등등을 다 해야함--이게 중요
Route::get('/article', 'App\Http\Controllers\ArticleController@index');

// 예전 버전은 이렇게 사용했으나, 안됨 
// Route::get('/article/{article}', 'ArticleController@show');
// use App\Http\Controllers\ArticleController; 라고 맨 위에 명시해도 
// Target class [ArticleController] does not exist. 없다고 함;;
// 그래서 아예 직접 컨트롤러 앞에다가 적어줘야 한다
Route::post('/article', 'App\Http\Controllers\ArticleController@store');
Route::get('/article/create', 'App\Http\Controllers\ArticleController@create');
Route::get('/article/{article}', 'App\Http\Controllers\ArticleController@show')->name('article.show');
Route::get('/article/{article}/edit', 'App\Http\Controllers\ArticleController@edit');
Route::put('/article/{article}', 'App\Http\Controllers\ArticleController@update');

// GET, POST, PUT, DELETE
// url을 통해서 하는 방법으로 보기, 쓰기, 지우기 
// GET /articles
// GET /articles/:id

// POST /articles

// PUT /articles/:id
// DELETE /articles/:id/

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




Route::get('/contact', function () {
    return view('contact');
});

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


/*
Route::get('/', function () {
    # 변수로 만들어 주면 url에서 get방식으로 들어온 데이터를 처리할 수 있음
    $name = request('name');
    
    # view()호출해서 test 페이지를 보여주고
    #또는 json?형태를 만들어 주기 []리스트? associative array 형태로 만들어 주기
    # 여기에서 key값은 다 변수처럼 사용할 수 있다

    return view('test', [
        'name' => $name
    ]);
    # 그러면 이것을 views/test.blade.php 파일에 적용해서 each

});
*/

/* 컨트롤러 사용으로 주석처리 
# /posts/바로 뒤에 { }컬리브라켓으로 묶으면 어떤 단어가 들어와도 받는다 
# 숫자 문자 문자-문자, 아무거나
Route::get('/posts/{post}', function ($post) {
    
    # associative array로 DB를 흉내낸다고 가정
    $posts = [
        'my-first-post' => 'Hello, this is my first blog post!',
        'my-second-post' => 'Now I am getting the hang of this blogging thing'
    ];

    #만약 에러처리가 안되있는 상태에서 다른 키값을 찾는다면 에러가 남
    # 그래서 에러 처리
    if (! array_key_exists($post, $posts)) {
        abort(404, 'Sorry, that post was not found.');
    }

    # 그리고 데이터를 보내주기
    return view('post', [
        # associative 형태로 보내기 {post}로 된 것은 변수$post에 받아서 위에서 정의한
        # $posts[$post] ---- [안은 키값이 되고, 키값은 사용자가 url에서 입력한 값]
        'post' => $posts[$post]
    ]);
});
*/

# 컨트롤러 호출하기 라라벨 8이후로 업데이트된 내용
# use App\Http\Controllers\UserController; 맨위에 이 내용 선언해주고 (UserController는 여기서는 PostController임)
// Using PHP callable syntax...
#Route::get('/posts/{post}', [PostController::class, 'show']); 작동 ok 
#또는
// Using string syntax...
Route::get('/posts/{post}', 'App\Http\Controllers\PostController@show'); #둘다 ok!


// 라라벨8 이전 방식
// Route::get('/posts/{post}', 'PostController@show');
//  이렇게 하면 이제 작동하지 않음


