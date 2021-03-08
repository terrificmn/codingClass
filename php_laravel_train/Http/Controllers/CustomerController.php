<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\Customer;
use App\Mail\WelcomeMail; 
use Illuminate\Support\Facades\Mail;
        

class CustomerController extends Controller
{
    public function index(Request $request) {  //use Illuminate\Http\Request; already imported, so just use Request
        //dd(request()); //reuqest() help function's result is the same as $request
        // dd(request()->query('active')); // and you can type ?active=1 in the url 
        
        
        //$customers = Customer::where('active', 1)->get(); // only get() which column of 'active' is 1
        $customers = Customer::where('active', request()->query('active', 1) )->get(); // only get() which column of 'active' is 1
        // query('active') 라고만 해도 동작은하나 1이라고 파라미터를 넘겨주면 기본이 1을 query해줌
        // instead of using 1 above code, simply add request() help function
        // just input ?active=0, or 1 in the url

        //$customers = Customer::all();

        //$customer = new Customer(); // Null 값이 객체를 생성해주고 넘겨준다 
        //이유는 create과 edit 페이지의 공통되는 form을 만들어서 각각 @nclude하게 되는데 이려면
        // create에서는 넘어간 것이 없어서 에러가 남// 그래서 빈 값을 넘겨줘서 에러가 안 나가게 한다

        return  view('customer.index', compact('customers'));
    }

    public function create() {
        
        $customer = new Customer(); // Null 값이 객체를 생성해주고 넘겨준다 
        //이유는 create과 edit 페이지의 공통되는 form을 만들어서 각각 @nclude하게 되는데 이려면
        // create에서는 넘어간 것이 없어서 에러가 남// 그래서 빈 값을 넘겨줘서 에러가 안 나가게 한다

        return view('customer.create', compact('customer'));
        
    }

    public function store() {
        
        // update와 validate가 겹치므로 함수 만들어서 호출
        // validatedData()에서는 validate한 후 리턴

        $customer = Customer::create($this->validatedData()); //DB 에 insert

        // 메일보내기
        Mail::to($customer->email)->send(new WelcomeMail()); // customer의 email을 가지고 온 다음에 WelcomeMail() 클래스 이용해서 바로 보내줌
        // 현재 mailtrap으로 설정되어 있어서 거기서 메일 확인할 수 있고
        // 위에 use로 import를 해줘야한다. Mail과 WelcomeMail 둘다
        //use App\Mail\WelcomeMail; 
        //use Illuminate\Support\Facades\Mail;
        
        return redirect('/customers/' . $customer->id );   /// 입력이 끝난 후 show()메소드 show페이지가 연결될 수 있게 해준다 id를 넘겨줌
        
    }

    public function show(Customer $customer) {  //url로 부터 받아온 데이터 user의 id
        //dd($customer);
        // $customer = \App\Models\Customer::findOrFail($customerId); //없으면 404 에러 발생시킴 
        // 여기에서는 파미미터와 리턴하는 변수명 같아서 파라미터 변수명을 바꿔줌 $customerId, web.php 파일도 {$customerId} 로 바꿔줘야함

        // Route Model binding 모델과 라우팅하는것을 묶은 기능 
        // 파라미터에 모델명을 입력해버리고 변수명을 $customer 해준다 //없으면 404도 발생시킴 
        // convention은 web.php 파일의 URI의 {}안의 써준것과 파라미터로 받는 변수명이 같아야 한다
        // /customers/{customer} 였으면 == 위의 파라미터도 $customer 
        
        return view('customer.show', compact('customer'));

    }

    public function edit(Customer $customer) {  //url로 부터 받아온 데이터 user의 id

        return view('customer.edit', compact('customer'));

    }

    public function update(Customer $customer) {  //라우트 모델 바인딩
        // ** put이나 patch를 @method('put') or @method('patch') 라고 form 태그안에 넣어줘야한다 
        //update를 하기위해서 인데, html에는 get/post 방식밖에 없으므로 라라벨방식으로 넣어준다
        
        // 위의 store()메소드와 겹치는 코드가 겹치므로 여기에서만 사용할 수 있게 
        // protected 함수를 따로 만들어서 호출해준다 //
        // $data = request()->validate([       
        //     'name' => 'required',
        //     'email' => 'required | email'
        // ]);

        $customer->update($this->validatedData());
        
        return redirect('/customers');

    }

    public function destroy(Customer $customer) {  //라우트 모델 바인딩
        // ** @method('delete') 라고 form 태그안에 넣어줘야한다 (edit페이지에서 삭제 버튼 (form)을 만들어 준다)
        //delete를 하기위해서 html에는 post로 넣어주고 라라벨 방식으로 넣어준다

        $customer->delete();
        
        return redirect('/customers');

    }

    protected function validatedData() {
        
        return request()->validate([       
            'name' => 'required',
            'email' => 'required | email'
        ]);
    }
}