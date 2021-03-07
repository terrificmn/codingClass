<?php

use Illuminate\Support\Facades\Route;

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

// Route::get('/hello', function() {
//     $coolString = 'Hello from Routes. Again';

//     return view( 'subviews.hello', 
//         // [ 'someData' => $coolString  ]  // compact를 이용안 할 때는 []배열로 넘기고, 
//         // blade 페이지 (html)에는 someData 키 값으로 처리하면 됨
//         compact( 'coolString') // 위의 변수 $coolString을 스트링화 해서 넘겨준다
//     );
// });

// closer 함수를 사용안하고 이제 여기서 컨트롤러한테 넘기기
//Route::get('/hello', 'App\Http\Controllers\HelloController@index');
Route::get('/about', 'App\Http\Controllers\HelloController@about');
//Route::view('/about', 'about'); //이렇게 view바로 넘겨주고 'about'블레이드 페이지를 표시해 줘도 됨 //컨트롤러를 안사용하고 바로 view() 기능을 사용할 때
//Route::get('/service', 'App\Http\Controllers\HelloController@service');

Route::get('/service', 'App\Http\Controllers\ServiceController@index');  //get으로 들어온 방식
Route::post('/service', 'App\Http\Controllers\ServiceController@store'); //post로 들어온 방식

//Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

//Auth::routes();

Route::get('/home', [App\Http\Controllers\HomeController::class, 'index'])->name('home');

Route::get('/customers', 'App\Http\Controllers\CustomerController@index');
Route::get('/customers/create', 'App\Http\Controllers\CustomerController@create');
Route::post('/customers', 'App\Http\Controllers\CustomerController@store');
Route::get('/customers/{customer}', 'App\Http\Controllers\CustomerController@show');
Route::get('/customers/{customer}/edit', 'App\Http\Controllers\CustomerController@edit');
Route::patch('/customers/{customer}', 'App\Http\Controllers\CustomerController@update');
Route::delete('/customers/{customer}', 'App\Http\Controllers\CustomerController@destroy');
