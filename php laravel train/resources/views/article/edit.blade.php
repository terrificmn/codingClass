@extends ('layout')

@section ('head')
<link href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.5/css/bulma.css" rel="stylesheet">
@endsection

@section ('content')

    <div id="wrapper">
        <div id="page" class="container">
            <h1 class="heading has-text-weight-bold is-size-5">Update Article</h1>
        </div>

        <form method="POST" action="/article/{{ $article->id }}">
        <!-- edit일 때는 method를 PUT로 바꿔준다 
            하지만 브라우저에서는 GET/POST밖에 모르기 때문에 
            라라벨 방식으로 좀 바꿔줘야한다 
            @method ('PUT') 을 입력해준다
            그러면 input 박스가 hidden으로 들어가면서 value='PUT'이 넘어가는데 이걸로 라라벨이 업데이트로 처리해줌
        -->
            @csrf 
            @method('PUT')
            <div class="field">
                <label class="label" for="title">Title</label>

                <div class="control">
                    <input class="input" type="text" name="title" id="title" value="{{ $article->title }}">
                </div>
            </div>

            <div class="field">
                <label class="label" for="excerpt">Excerpt</label>

                <div class="control">
                    <textarea class="textarea" name="excerpt" id="excerpt"> {{ $article->excerpt }}</textarea>
                </div>
            </div>

            <div class="field">
                <label class="label" for="body">Body</label>

                <div class="control">
                    <textarea class="textarea" name="body" id="body"> {{ $article->body }} </textarea>
                </div>
            </div>

            <div class="field is-grouped">
                <div class="control">
                    <button class="button is-link" type="submit">Submit</button>
                </div>
            </div>

        </form>

    </div>


@endsection
