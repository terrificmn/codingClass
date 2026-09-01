<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class ServiceController extends Controller
{
    public function index() {
        $services = \App\Models\Service::all();
        
        return view('service.index', compact('services') );
    }

    public function store() {
        // dd() 헬퍼함수 변수나 문자열을 찍어주고 멈춘다
        // dd('inside');  // 만약 @csrf  를 html의 form에 안적어주면 419에러가 난다
        // 라라벨에서는 토큰을 만들어서 서로 비교해서 맞을 때 db에 등록이 되게 되어 있음
        // hidden 레이어로 token이 생성되어 있는것을 알 수 있고 이것을 서버내에서 만들어진 token과 맞춰보는데 
        // 외부에서 생성한것으로는 맞지 않는다고해서 결국은 보안성 향상
        // 암튼.. form태그 안에는 @csrf 를 꼭 적어준다

        //dd(request('name')); //request()는 html에 페이지에서 요청으로 넘어온것을 볼 수 있다 즉 form의 input태그가 name

        // validate하기 중요! 여기를 처리안해주면 아무것도 없이 확인버튼을 눌렀을 때 에러가 난다
        $data = request()->validate( [
            //'name' => 'required' // 여기까지만 해주면 아무일도 일어나지않고 에러도 안남, 사용자한테 알리려면 @error 를 써준다(index.blade.php 에 써줌)
            //  @error('name') {{ $message }} @enderror 이런식으로 써준다. blade기능을 이용하면 좋다!
            'name' => 'required|min:5|max:10'  // 여러 validation을 추가해주려면 | (파이프) 기호를 사용해서 추가한다
            // 매뉴얼 참고 https://laravel.com/docs/8.x/validation#available-validation-rules

        ]);
        
        //-------------------------------------------------------
        // $service = new \App\Models\Service();

        // $service->name = request('name'); //request() 넘어온 name (input이 name) 값을 service 객체의 name속성에 저장 (즉, db컬럼)
        // $service->save();  // db저장
        //-------------------------------------------------------
        // 위와 같은 방식으로 하거나 

        //-------------------------------------------------------
        // 객체에 바로 create()메소드를 이용해서 할 수 있음. 더 간단한 코드가 됨
        \App\Models\Service::create($data);  //이렇게만 하면 더 쉽게 데이터를 처리할 수 있는데 
        // Add [name] to fillable property to allow mass assignment on [App\Models\Service]. 이런식으로 mass assignment 에러가 난다
        // 그래서 모델로 돌아가서 Service 클래스(모델)에 
        // protected $fillable = ['name']; 를 추가해줘야한다. 더 추가할 께 있다면 배열로 계속 추가해준다. ['name', 'title' ...]
        // dd($data);


        return redirect()->back();  //index로 돌아감
    }

    
}
