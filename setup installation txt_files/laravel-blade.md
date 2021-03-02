# 라라벨 블레이드
블레이드 엔진을 이용해서 php if statement 문법

```php
@if(5 > 10)
    <p> 5 IS LOWER THAN 10</p>
@elseif (5 == 10)
    <p> 5 is indded lower than 10</p>
@else
    <h2>All condditions are wrong!</h2>
@endif
```

@unless
```php
@unless (empty($name))
    <h2>Name is not empty!</h2>
@endunless
```
empty인지 확인해 줌
@empty()
```php
@empty()
    <p>Name is empty!</p>
@endempty
```

php isset도 지원
```php
@isset()
    <p>Name is empty!</p>
@endisset
```

대개 php에서 있는 함수들은 @싸인을 붙여서 사용할 수 있는 듯.

switch문
```php
@switch($name)
    @case(1)
        @break

    @case(1)
        @break
    
    @default

@endswitch
```

for문도 @를 붙여서 사용하면 됨  
조금 다른 점은 출력할 떄 블레이드에서 사용하는 {{ }} 두번 감싸주면 됨
```php
@for($i = 0; $i <=10; $i++)
    <h2>The number is {{ $i }} </h2>
@endfor
```

전체 컬렉션에서 아이템 하나씩 반복하는 foreach
foreach
```php
@foreach ($collection as $item)
    <h2>The name is {{ $item }} </h2>
@endforeach
```



