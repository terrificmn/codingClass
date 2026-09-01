@extends('app')

@section('title', 'service title')
    


@section('content')
    <h1> Wecome to 8 from service </h1>

    <form action="/service" method="post">
        <input type="text" name="name" autocomplete="off">
        
        <button>추가 확인 </button>
        @csrf
    </form>
    <p style="color:red">  @error('name') {{ $message }} @enderror </p>

    <ul>
        {{-- foreach랑 같은 기능인데 @empty 써서 변수에 내용이 없을 때 내용을 출력해줌 --}}
        @forelse($services as $service) 
            {{-- <li> {{ $service }} </li> --}}
            <li> {{ $service->name }} </li>

        @empty
            <li>No service available</li>
        
        @endforelse
@endsection