<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
// DB를 use를 안해주면 namespace에서 찾는데 App\Http\Controllers에서 DB를 찾아서 에러가 남
use DB;
// Post 모델 클래스 사용
use App\Models\Post;

class PostController extends Controller
{
    public function show($slug) {
        // Post 모델을 사용 sql 쿼리 방식으로 보여주기 
        // first()첫번째 결과만 보여주기
        /*
        $post = Post::where('slug', $slug)->first();
        if (! $post) {
            abort(404);
        }
        */

        // firstOrFail() 첫번째 결과만 보여주고 없으면 404메세지를 띄움
        // 아래처럼 쓰고 따로 리턴해도 되고 바로 클래스를 접근해서 넘기라고 해도 됨
        //$post = Post::where('slug', $slug)->first();

        return view('post', [ 
            'post' => Post::where('slug', $slug)->firstorFail()
            ]);
        
    }
    /* Eloquent가 아닌 db에서 테이블 정보 가져오기 (모델을 안 거침)
    public function show($slug) {
        
        $post = DB::table('post')->where('slug', $slug)->first();
        
        // done and die
        // $post 변수가 있는지 확인할 때 사용 
        // 문제가 있으면 값을 보여주고 아니면 그냥 죽는다 (화면에 표시가 안됨)
        // url로 다른값을 넘기면 예; 123, 그러면 화면에 (null)이라고 표시됨
        // dd($post);

        if (! $post) {
            //에러메세지 띄움
            abort(404);
            // abort()함수를 사용안하면 body property를 읽을 수 없다고 에러메세지 나옴
        }

        # 그리고 데이터를 보내주기
        return view('post', [
            # associative 형태로 보내기 {post}로 된 것은 변수$post에 받아서 위에서 정의한
            # $posts[$post] ---- [안은 키값이 되고, 키값은 사용자가 url에서 입력한 값]
            'post' => $post
        ]);
    }
    */

    /* 배열로 보여주기 PostController 클래스안에 넣어주면 됨
    public function show($post) {
        
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
    }
    */

}
