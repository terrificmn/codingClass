@extends ('layout')

@section ('content')


<div id="wrapper">
	<div id="page" class="container">
		<div id="content">
			@foreach ($articles as $article)
			<div class="title">
				<a href="{{ route('article.show', $article->id )}}" >
					<h2> {{ $article->title }} </h2> </a>	

				<span class="byline">
					<p>{{ $article->excerpt }}</p>
				</span> 
			</div>
			<p><img src="images/banner.jpg" alt="" class="image image-full" /> </p>
			<p> {{ $article->body }} </p>
			
			@endforeach
		</div>
		<div id="sidebar">
			<ul class="style1">
				
				<li class="first">
					<h3>
						
						
					</h3>
					
					
				</li>
				
			</ul>
			
		</div>
	</div>
</div>

@endsection