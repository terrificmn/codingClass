<h1> Add New Customer </h1>

<form action ="/customers" method="post">
    {{-- <div>
        <label for="name" >Name </label>
        <input type="text" name="name" value="{{old('name')}}">
        @error('name') <p style="color: red">{{ $message }} </p> @enderror
    </div>

    <div>
        <label for="email" >Email </label>
        <input type="text" name="email" value="{{old('email')}}">
        @error('email') <p style="color: red">{{ $message }} </p> @enderror
    </div>

    @csrf
    <button>Add New Customer</button> --}}

    {{-- 여기 부분이 edit.blade.php 파일과 중복되므로 form.blade.php 파일을 만들어서 
    여기에서는 @include해서 사용
    단, 여기서 쓰인 value="{{old('email')}}는 edit에서는 안되니
    value="{{old('email') ?? $customer->name }}" 식으로 바꿔준다, 그러면 예전입력이(old())가 없으면
    ?? 뒤의 식을 실행함. 하지만 이러면 또 문제가 있음 create할 때는 변수를 받은게 없어서
    null값인 $customer 를 넘겨준다 방법은 CustomerContoller에서 볼 것 --}}

    @include('customer.form')

    <button>Add New Customer</button>

</form>