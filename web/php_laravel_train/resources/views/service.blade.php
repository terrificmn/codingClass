@extends('app')

@section('title', 'service title')
    


@section('content')
    <h1> Wecome to 8 from service </h1>

    <ul>
        {{-- foreach랑 같은 기능인데 @empty 써서 변수에 내용이 없을 때 내용을 출력해줌 --}}
        @forelse($services as $service) 
            {{-- <li> {{ $service }} </li> --}}
            <li> {{ $service->name }} </li>

        @empty
            <li>No service available</li>
        
        @endforelse
@endsection