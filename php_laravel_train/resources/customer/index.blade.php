<h1>Customers</h1>

<a href="/customers/create"> Add New Customer</a>
@forelse($customers as $customer)
    <p> 
        <a href="/customers/{{$customer->id}}">
            <strong>
                {{ $customer->name }} 
            </strong> 
        </a>
        {{ $customer->email }} </p>

@empty
    <p>No Customers to show</p>
@endforelse
