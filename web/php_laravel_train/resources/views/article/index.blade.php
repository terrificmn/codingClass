@extends ('layout')

@section ('content')


<div id="wrapper">
	<div id="page" class="container">
		@forelse ($articles as $article)
			<div id="content">
				<div class="title">
					<a href="{{ route('article.show', $article->id )}}" >
						<h2> {{ $article->title }} </h2> </a>	

					<span class="byline">
						<p>{{ $article->excerpt }}</p>
					</span> 
				</div>
				<p><img src="images/banner.jpg" alt="" class="image image-full" /> </p>
				<p> {{ $article->body }} </p>
		</div>
		@empty
			<p>No relevant articles yet<p>
		@endforelse
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