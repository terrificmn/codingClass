<div>
    <label for="name" >Name </label>
    <input type="text" name="name" value="{{old('email') ?? $customer->name }}">
    @error('name') <p style="color: red">{{ $message }} </p> @enderror
</div>

<div>
    <label for="email" >Email </label>
    <input type="text" name="email" value="{{old('email') ?? $customer->email }}"> 
    @error('email') <p style="color: red">{{ $message }} </p> @enderror
</div>

@csrf

{{-- 공통 form으로 만드는 이유는 create와 edit의 싱크를 계속 맞춰서 갈 수 있기 때문이다
만약 처음 회원정보를 업데이트를 하면 예를 들어 주소, 전화번호 이런것들이 추가 된다면 
create페이지도 추가해줘야하고 edit페이지에도 추가해줘야하는데 
이렇게 form페이지를 @include('customer.form') 하는 방법으로 효과적으로 만들 수 있기 때문 --}}
