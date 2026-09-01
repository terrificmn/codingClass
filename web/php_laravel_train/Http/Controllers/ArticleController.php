<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Article;
use App\Models\Tag;
class ArticleController extends Controller
{
    // 컨트롤러에는 최소 7개의 기능을 할 수 있게 만들어 줘야함
    // 전체보여주기(index), 하나 보여주기(show), 크레이트, 에디트, 저장, 업데이트, 삭제
    // index, show, create, store, edit, update, destory

    // Reder a list of a resouce.
    public function index() {
        if (request('tag')) {
            // 마지막은 article 메소드 호출 ()를 사용하지 않고 property 쓰듯 사용
            $articles = Tag::where('name', request('tag'))->firstOrFail()->article;
            // 리턴 json 형태로 보여줌
            //return $articles;
        } else {
            // latest()메소드에서 'id'로 정렬, 원래는 파라미터 안넘겨도 되던데 모르겠음;;;
            $articles = Article::latest('id')->get();
        }
        
        return view('article.index', ['articles' => $articles]);
    }
/*
    // Show a single resource.
    public function show($id) {
        //$articles = Article::find($id); 
        $articles = Article::findOrFail($id); // $id로 들어온 값을 DB에서 못 찾으면 404에러 메세지를 출력
        // aritcle.show 여기에서 .은 하위 디렉토리 의미
        return $articles; // 이렇게 리턴시키면 json 형태로 보여준다
        return view('article.show', ['article' => $articles]);
    }
*/
    // Show a single resource.
    public function show(Article $article) {
        /*
        url에서 /article/3 이런식으로 입력된 것을 (web.php에서) 받아서 
        같은 방식으로 매치시켜서 Article::where('id'=3)->first(); 라는 작업을 한 것
        그래서 위의 url /article/3 즉 /article/{article} 형태를 꼭 같이 맞춰주면 됨
        show()파라미터에 {article}와이드카드의 이름과 똑같이 맞춰준다
        */
        // 그래서 이 방식으로 다른 메소드에도 적용시킬 수 있음
        // edit(), update() 메소드에도 적용하고
        // $articles = Article::findOrFail($id); <---를 지워도 같은 기능을 함
        return view('article.show', ['article' => $article]);
    }

    // Create a view to create a new resource
    // submit 버튼으로 입력하는 것
    public function create(){
        return view('article.create', [
            'tags' => Tag::all()
        ]);

    }

    // Persist the new resource
    public function store(){
        // persist the new article
        // 테스트는 하기 -- 요청된것 모두 보기
        //dump(request()->all());

        // validation을 안하면 일단, 아무것도 입력안하고 확인버튼 누르면 sql에러남
        // 하지만 required 를 넣어서 validate()를 해주면 아무것도 안 넣으면 원래 페이지로 돌아간다
        // 라라벨에서는 그 전 페이지로 넘어가게 되어 있음 예: article/create 로 
        // request()->validate( [ 
        //     // 더 추가할 때는 [ ] 배열에 넣어주고 자세한것은 메뉴얼 확인해 보기
        //     //'title' => ['required', 'min:3', 'max:255'],
        //     'title' => 'required',
        //     'excerpt' => 'required',
        //     'body' => 'required'
        // ]);
        // 아래 코드에서 변수에 저장해주면 create() 메소드를 호출할 때 중복을 제거해줄 수 있음
        // 기능은 똑같음

        // 이걸로 메소드로 추가함
        // $validatedAttributes = request()->validate( [ 
        //     // 더 추가할 때는 [ ] 배열에 넣어주고 자세한것은 메뉴얼 확인해 보기
        //     //'title' => ['required', 'min:3', 'max:255'],
        //     'title' => 'required',
        //     'excerpt' => 'required',
        //     'body' => 'required'
        // ]);
        //바로 위의 $validatedAttributes 코드로 작성했을 경우 아래코드와 짝임
        //Article::create($validatedAttributes);

        // DB저장 가장 기본적인 방법 (단, 이런식으로 하면 안됨!!!, 아래서 설명)
        // 왜냐하면 유저가 입력하는 방법을 다 믿으면 안된다 뭐 이런식?
        // 암튼 검증해야한다. 위의 코드가 validate()하는 방법
        // 같은 방법으로 db에 입력해주는 코드, 주석 아래로 나옴
        // $article = new Article();
        // $article->title = request('title');
        // $article->excerpt = request('excerpt');
        // $article->body = request('body');
        // $article->save();
        //create 메소드를 호출해서 값 넘겨주기 db에 입력됨, 위의 코드와 같은 방식
        // *** 참고1번 코드
        // Article::create( [
        //     'title' => request('title'),
        //     'excerpt' => request('excerpt'),
        //     'body' => request('body')
        // ]);

        // 위 처럼 하면 
        // Add [title] to fillable property to allow mass assignment on [App\Models\Article].
        // 에러가 나는데 라라벨에서는 db의 컬럼을 다 입력이 될 때 모든 컬럼이 바꿔지면 안되기때문에
        // 어떤 특정한 컬럼은 사용자가 바꾸면 안되기 때문에 기본적으로 제한이 되어 있음 (보호차원에서)
        // 이거를 문제 없이 되게 하려면 (model) Article 클래스에 $fillable에 배열로 추가해주면됨
        // Article class에서 입력할 것
        // protected $fillable = ['title', 'excerpt', 'body'];

        // 또 코드 줄이기;;;
        // 위의 validate() 와 create() 메소드에서 사용된것이 중복이 됨 
        // 그래서 처음 validate()에서 했던 것을 변수에 넣어줘서 
        // 그 값을 리턴해주면 더 깔끔한 코드가 됨

        // 그래서 이렇게 됨
        // return $validatedAttributes; // json형태로 입력한 것을 그대로 받은것을 알 수 있음
        // 이 변수를 create()메소드에 넘겨서 리턴해주면 위의 참고1번 코드와 같은 기능을 한다
        //dd(request()->all());
        $this->validateArticle();
        // 키값 순서대로 지정해주기 , 그러면 태그를 순서대로 선택안해도 에러 안나게 됨
        $article = new Article(request(['title', 'excerpt', 'body']));
        $article -> user_id = 1; // 원래는 auth()->id(); 이런식으로 한다고 함, 지금은 하드코딩
        // auth()->user()->article()->create($article); 이런식도 가능하다고 함
        $article->save();

        $article->tags()->attach(request('tags')); // [1, 2, 3] 으로 넘어오고 이것은 article_tag 테이블로 연결
        return redirect('/article');
    }


    // Show a view to edit an existing resource
    public function edit(Article $article){
        
        // find the article associated with the id
        return view('article.edit', ['article' => $article]);
        // 또는 
        //return view('article.edit', compact('article'));
    }

    // Persist the edited resource
    public function update(Article $article){
        // 여기에서도 validation 작업을 store()메소드에서 했던 것 처럼 똑같이 해준다
        $validatedAttributes = request()->validate( [ 
            // 더 추가할 때는 [ ] 배열에 넣어주고 자세한것은 메뉴얼 확인해 보기
            //'title' => ['required', 'min:3', 'max:255'],
            'title' => 'required',
            'excerpt' => 'required',
            'body' => 'required'
        ]);

        // update()파라미터에서 Article $article 을 넘겼기 때문에 아래코드는 필요없어 짐 == 같은기능
        // $article = Article::findOrFail($id);

        //update (기능상 문제없으나 중복되는 거 제거 차원에서 제거)
        // 아래의 update()호출 한줄와 같은 기능
        // $article->title = request('title');
        // $article->excerpt = request('excerpt');
        // $article->body = request('body');
        // $article->save();

        $article->update($validatedAttributes);
        
        // 여기도 위의 store()메소드에서 했던 것 처럼 똑같이 적용할 수 있다


        // 중간에 ,가 아니고 . (dot) // 이상없으나, 아래코드로 바꿈 
        // return redirect('/article/'. $article->id);

        // web.php에서 route()에서 ->name()메소드를 'article.show'로 지정했을 경우
        return redirect(route('article.show', $article));
    }

    public function validateArticle() {
        return request()->validate( [ 
            // 더 추가할 때는 [ ] 배열에 넣어주고 자세한것은 메뉴얼 확인해 보기
            //'title' => ['required', 'min:3', 'max:255'],
            'title' => 'required',
            'excerpt' => 'required',
            'body' => 'required',
            'tags' => 'exists:tags,id'

        ]);
    }


    // Delete the resource
    public function destroy(){
        
    }
}
