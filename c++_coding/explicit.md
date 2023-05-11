# explicit

class를 생성할 때 constructor 앞에 explicit 키워드를 넣어주게 되면   

constructor가 type을 변환하지 않게 할 때 사용한다   
implicitly (직접적인 방법이 아닌 방법)으로 생성자가 자동으로 type 변환을 해주는데   

```cpp
class Foo {
public:
    Foo(int n); // allocates n bytes to the Foo object
    Foo(const char *p); // initialize object with char *p
};
```
Foo class가 있고, 인스턴스를 하면 

Foo myString = 'x';

char 로 받아서 생성되기를 기대하지만, 컨스트럭터는 int로 type을 변환해서  
이를 implicitly 변환된다고 한다. 어쨋든 그래서 int로 변환받은 상태로 생성이 된다   

그래서 이런것을 못하게 막는 것이 **explicit** 키워드 이다 

그래서 
```cpp
class Foo {
public:
    explicit Foo(int n); // allocates n bytes to the Foo object
    Foo(const char *p); // initialize object with char *p
};
```

라고 만들어 주고   

다시 한번 클래스를 인스턴스로 만들어 주면

Foo myString = 'x';
이때 int로 받아지는 것이 아니 원했던 char로 받아서 만들어진다  

뭔가 원하지 않는 에러가 또는 변환을 막기 위해서 사용하는 것이라고 보면 된다 

