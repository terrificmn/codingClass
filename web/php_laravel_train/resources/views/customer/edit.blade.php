<h1> Customer Details </h1>

<form action ="/customers/{{$customer->id}}" method="post">
    @method('PATCH')

    @include('customer.form')

    <button>Save Customer</button>

</form>