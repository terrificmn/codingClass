<h1>Customer Details </h1>

<div><a href="/customers">< back </a></div>

<strong>Name</strong>

<p>{{ $customer->name }}</p>

<strong>Email</strong>
<p> {{ $customer->email }}</p>

<div>
    <a href="/customers/{{ $customer->id }}/edit">Edit</a>

    <form action="/customers/{{ $customer->id }}" method="post">
        @method('delete')
        @csrf
        <button>Delete</button>
    </form>
</div>