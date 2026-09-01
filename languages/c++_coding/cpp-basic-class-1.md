# OPP Object Oriented Programming

먼저 클래스를 이야기 하기 전에 OOP를 살짝 정리해보자

> 약간 개인적으로 정리한 것이라, 내용이 다소 틀릴 수 있습니다.


먼저 세상의 사물을 보듯이 접근해서 프로그래밍 하는 방법이 Object Oriented Programming 이다

사물에는 어떤 속성과 액션이 있다고 말할 수 있는데   

예를 들어 사람이라는 물체(?)가 있다고 하면   
사람에는 각 눈, 코, 입, 팔, 다리, 피부, 머리카락 등 다양한 속성들이 존재하게 된다

그래서 눈 색깔, 크기, 머리색깔, 생머리 곱슬머리, 키가 큰지 작은지 등의 다양한 것들이 있는데   
이를 프로그래밍에서는 속성이라고 하며 특정한 값을 넣어줘서 사용을 하게 된다.

예를 들어 
```
hair_color = "black" 
skin = "white"
height = 200
```
이런식으로 말이다. 

그리고 현실세계의 사람이라는 물체(?)는 행동 action을 하게 되는데   
말하기, 걷기, 달리기, 뛰기, 먹기 등의 행동들을 할 수 있는데 

이를 프로그래밍으로 옮기면 메소드(method)가 된다.   
항상 예제에서 많이 나오는 greeting() 메소드 그런 것 처럼 만들 수 있게 된다. 

greeting 메소드(함수)에서 printf("안녕하세요"); 가 출력되게 했다면

greeting 메소드를 호출하면 행동을 하게 되는 것이다.

그래서 이런것을 가능하게 해주는 기본이 class이다

위의 사람을 물체에 비유했듯이, 그것을 틀로 만들어 찍어내야한다
그것이 바로 클래스 이다~ 붕어빵 기계 같은 것

그래서 class Person 을 만든다면 이게 붕어빵 기계틀(?)이 되어서
대량생산 🤩    
(표현이 적절치 않을 수도 있지만 감안하고 들어주세요)

Person 클래스를 이용해서 Alice, Mark, Mike등 만들어 낼 수 있게 된다

<br/>

내 나름대로 정리를 해보았는데;; 뭐 정신 없게 정리한 듯 하다 ㅋㅋ

이제 c++에서 class를 어떻게 만드는지 예제로 살펴보자

<br>

## 클래스 properties 속성 만들기, private, public
클래스 만들기. 처음에 OOP니 뭐니 거창하게 떠들었는데  
클래스를 사용하는 큰 이유 중 하나는 코드를 재사용하기 위해서 클래스를 사용한다.   

그러기 위해서 먼저 클래스를 생성하는 법 부터 배워보자~  

Bike라는 클래스를 만들어보자

```cpp
using std::string

class Bike {
    string Name;
    string Color;
    string Country;
    double Price;
};

int main() {
    Bike MyBike; // 객체 생성하기

    return 0;
}
```

클래스 안에 선언된 변수 Naem, Color, Country, Price 는 attributes 또는 properties라고 한다. 클래스의 속성이라고 보면 된다. 

C++ 에서는 모든게 선언하듯이 사용이 되는 것 같다는 느낌이 든다.   
아무래도 데이터 타입을 선언해야하고 엄격하게 지켜야 해서 그런 것 같다   
class를 만든것도 객체로 사용할 때는 선언하듯이 하면 되는 것 같다

만들어진 class 를 메인함수에서 사용하려면 , 즉 붕어빵 기계 Bike로 새로운 Mybike를 만들려면
그냥 선언만 해주면 된다 Bike MyBike; 엄청 간단하다

이렇게 새로운 변수에 저장을 하는 것을 인스턴스, 객체라고 한다   
MyBike가 이렇게 만들어졌다.

<br/>

쓰잘때없이 구지 비교를 해보자~ 파이썬에서는 어떻게 사용할꺄?
```py
class Bike :
    #...생략

# 인스턴스 생성
MyBike = Bike()
```

구지 비교를 하면 php에서는 
```php
class Bike {
    private Name = "bicycle";
    
    //생략..
}
# 인스턴스 생성
$MyBike = new Bike();
```

> 그냥 한번 비교해봤다. 역시 비슷하면서 다른게 재미있다 ㅋㅋㅋ  
클래스는 어렵기도 하지만 재미있고 왠지는 모르겠지만 class하면 어렵게만 느껴졌는데   
요새는 조금 이해가 되서 그런가? 😛 class 를 잘 사용하고 싶은 마음이 든다


다시 본론으로 돌아와서   
기본적으로 c++에서는 클래스가 **private**으로 만들어 진다고 한다    
그래서 외부에서 클래스의 속성(property)를 접근할 수 없다

그래서 외부에서 Mybike라고 만들어도 Mybike의 속성인 Name, Color등을 바꿀 수가 없다  
즉, 클래스 내부에서만 접근이 되어서 클래스 블럭{ } 안에서 접근해야지만 가능하다는 소리  

객체를 만들고 속성인 Name 에 다른 값을 줄려고하면
```cpp
int main() {
    Bike MyBike; // 객체 생성하기

    MyBike.Name = "홍길동"; 
    return 0;
}

```
private이므로 (비공개) 에러가 발생하게 된다

> cpp 에서는 크게 3가지가 있다. private, protected, public  
이 중 protected는 말 그대로 보호되고 있는 것이어서, 일반적으로는 접근을 할 수가 없다  
대신 public은 말 그대로 공개가 되어 있으므로 접근이 가능하다


이제 외부에서 접근할 수 있게 만들어주자  
**public**으로 바꿔주면 외부에서도 사용할 수 있게 된다

이제 외부에서 즉, 클래스 {} 블럭 안이 아닌, 메인 함수등에서 접근해서 내용을 입력해 주자

(클래스의 속성값들을 바꿔주고 출력해보는 코드 입니다.)
```cpp
#include <iostream>
using std::string;
using namespace std;

class Bike {
public:  // 이제 이하는 다 public이라는 의미가 된다
    string Name;
    string Color;
    string Country;
    double Price;
};

int main() {
    Bike MyBike; // 객체 생성하기

    MyBike.Name = "삼천리자전거";
    MyBike.Color = "black";
    MyBike.Country = "korea";
    MyBike.Price = 1000000;

    cout << "name: " << MyBike.Name << endl;
    cout << "color: " << MyBike.Color << endl;
    cout << "country: " << MyBike.Country << endl;
    cout << "price: " << MyBike.Price << endl;

    return 0;
}
```
정말 간단하게 public이라고만 적어주면 된다. public:  (콜론)

> private: 또는 protected:  식으로도 만들 수 있음

이렇게 해주면 클래스 외부에서도 접근이 되어서 위의 코드처럼 클래스의 속성값들을 바꿔주거나 넣어줄 수 있다

Bike 클래스로 생성한 MyBike의 속성(property)를 접근하려면 . (dot) 을 이용하면 된다

클래스 (설계도면 같은 것)로 찍어낸 MyBike의 Name 바꾸고 싶으면 MyBike.Name = "자전거이름"; 로 사용할 수 있다

```
name: 삼천리자전거
color: black
country: korea
price: 1000000
```
처럼 출력이 되게 된다.

<br/>

## 생성자 Constructor 만들기

이제 속성 값들을 넣어주는 것은 알았는데 다른 객체를 만들고 새로운 값들로 넣어주고 싶을 때면
일일이 속성을 만들어 줘야할 텐데 
예를 들면 아래와 같다

``` cpp
int main() {
    Bike MyBike; // 객체 생성하기

    MyBike.Name = "삼천리자전거";
    MyBike.Color = "black";
    MyBike.Country = "korea";
    MyBike.Price = 1000000;


    Bike MyBike2; // MyBike2 객체 생성하기
    MyBike2.Name = "알톤자전거";
    MyBike2.Color = "yellow";
    MyBike2.Country = "korea";
    MyBike2.Price = 500000;
}
```
MyBike 와 다른 MyBike2를 만들었다.    
위 처럼 해당 객체의 값들을 넣어 주면 된다. 

만약 이런 것들이 MyBike3, MyBike4, MyBike5 ...처럼 엄청 많아 진다면 일일이 다 넣어주기가 힘들다

그래서 클래스에는 생성자 Constructor 라는 메소드가 있어서 처음 생성시   
입력을 할 수가 있다

이제 하는 예시를 보자~
먼저 생성자는 class명과 같아야 한다 그래서 마치 함수를 만들 듯이 만들어 주면 된다

```cpp
class Bike {
public:
    string Name;
    string Color;
    string Country;
    double Price;

    // 생성자
    Bike(string name, string color, string country, double price) {
        Name = name;
        Color = color;
        Country = country;
        Price = price;
    }
};
```
이렇게 생성자 constructor 메소드가 만들어 졌다. 함수처럼 파라미터를 설정하고 
그 받은 값들을 속성인 Name, Color ...등에 저장해주는 방식이다

이렇게 하면 객체를 생성하면서 처음에 클래스의 속성들도 셋팅이 되게 된다

처음에는 그냥 단순하게 Bike MyBike; 로만 했지만, 
이제 생성자를 발동시키기 위해서는 생성자에서 만든 파라미터 값들 (변수들)을 넣어서 만들어야한다  

이어서 코드를 보자, 이번에는 main 함수내에서 인스턴스 (객체) 생성부분이다

``` cpp
int main() {
    Bike MyBike("삼천리자전거", "black", "korea", 1000000);
    Bike MyBike2("알톤자전거", "yellow", "korea", 500000);

    // 이제 속성값을 직접 넣어주는 것은 필요없게 됨
    // MyBike.Name = "삼천리자전거";
    // MyBike.Color = "black";
    // MyBike.Country = "korea";
    // MyBike.Price = 1000000;
}
```

전체 코드로 보면..
```cpp
#include <iostream>
using namespace std;

class Bike {
public:
    //속성들
    string Name;
    string Color;
    string Country;
    double Price;

    //생성자
    Bike(string name, string color, string country, double price) {
        Name = name;
        Color = color;
        Country = country;
        Price = price;
    }
};

int main() {
    Bike MyBike("삼천리자전거", "black", "korea", 1000000);
    Bike MyBike2("알톤자전거", "yellow", "korea", 500000);

    cout << "name: " << MyBike.Name << endl;
    cout << "color: " << MyBike.Color << endl;
    cout << "country: " << MyBike.Country << endl;
    cout << "price: " << MyBike.Price << endl;

    return 0;
}
```

이렇게 하면 MyBike가 만들어 지면서 매개 변수로(arguments) 값들이 넘어가면서 Bike 클래스에서 
생성자 메소드가 실행이 되게 되고 코드에 의해서 properties 속성값들이 바뀌게 된다


[다음은 cpp class 2편 더 이어서 보기](/blog) NOT UPDATED 링크수정해야함