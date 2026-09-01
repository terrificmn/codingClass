<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class HelloController extends Controller
{
    public function index() {
        //$coolString = 'Hello from Controller.';
        //return view( 'subviews.hello', compact( 'coolString') ); // 위의 변수 $coolString을 스트링화 해서 넘겨준다
        
        return view('app');
    }

    public function about() {
        //$coolString = 'Hello from Controller.';
        //return view( 'subviews.hello', compact( 'coolString') ); // 위의 변수 $coolString을 스트링화 해서 넘겨준다
        
        return view('about');
    }

    public function service() {
        // $service = [
        //     'service 1',
        //     'service 2',
        //     'service 3',
        //     'service 4'
        // ];

        $services = \App\Models\Service::all();
        
        return view('service', compact('services') );
    }
}
