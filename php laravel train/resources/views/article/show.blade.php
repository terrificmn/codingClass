@extends ('layout')

@section ('content')


<div id="wrapper">
	<div id="page" class="container">
		<div id="content">
			<div class="title">
				<h2>{{ $article->title }}</h2>
			</div>
			
				<p><img src="/images/banner.jpg" alt="" class="image image-full" /> </p>
			
            {{ $article->body }}

			<p style="margin-top: 1em">
				@foreach ($article->tags as $tag)
					{{-- <a href="/article?tag={{ $tag->name }}">{{ $tag->name }} </a> --}}
					{{-- 위와 같은 효과 --}}
					<a href="{{ route('article.index', ['tag' => $tag->name ]) }}">{{ $tag->name }} </a>
				@endforeach
			</p>
		</div>
		
	</div>
</div>

@endsection