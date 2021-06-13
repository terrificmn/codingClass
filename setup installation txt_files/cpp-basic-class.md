# cpp class정리하기

클래스 만들기. 클래스는 코드의 재사용을 위해서 사용한다고 알고 있는데 
세상의 사물을 보듯이 접근하는 방법이 Object Oriented Programming 이다

사물에는 어떤 속성과 액션이 있다고 말할 수 있는데 
예를 들어 사람이라는 물체가 있다고 하면 
사람에는 각 눈, 코, 입, 팔, 다리, 피부, 머리카락 등 다양한 속성들이 존재하게 된다

그래서 눈 색깔, 크기, 머리색깔, 생머리 곱슬머리, 키가 큰지 작은지 등의 다양한 것들이 있는데 
이를 프로그래밍에서는 속성이라고 하며 특정한 값을 넣어줘서 사용을 하게 된다.

예를 들어 hair_color = "black" 
skin = "white"
height = 200
이런식으로 말이다. 

그리고 사람이라는 것은 행동 action을 하게 되는데 
말하기, 걷기, 달리기, 뛰기, 먹기 등의 행동들을 하게 되는데 

이를 프로그래밍으로 옮기면 메소드(method)가 된다. 
항상 예제에서 많이 나오는 greeting() 메소드 그런 것 처럼 만들 수 있는게 된다. 

greeting 메소드 (함수)내에 printf("안녕하세요");
이런식으로 만들었다고 하면 
메소드를 호출하면 행동을 하게 되는 것이다. 사람이 인사를 하듯이 
프로그램으로 만든 객체인 Person도 화면에 출력을 안녕하세요라고 action을 하게 되는데 이게 메소드이다

내 나름대로 정리를 해보았는데;; 뭐 정신 없게 정리한 듯 하다 ㅋㅋ

이제 c++에서 class를 어떻게 만드는지 예제로 살펴보자

<br>

## 클래스 properties 속성 만들기, private, public

```cpp

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

먼저 Bike라는 클래스를 만들어 보고 
그안에 properties를 만들어 보자. 아마도 파이썬에서는 attributes라고 불렸던 것 같음
결국은 같은 것들 ㅋㅋ

C++ 에서는 모든게 선언하듯이 사용이 되는 것 같다는 느낌이 든다. 그래서 
class를 만든것도 객체로 사용할 때는 선언하듯이 하면 되는 것 같다

Bike MyBike; 엄청 간단하다


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

> 그냥 한번 비교해봤다. 역시 비슷하면서 다른게 재미있다 ㅋㅋㅋ 클래스는 어렵기도 하지만 재미있고 
왠지는 모르겠지만 class하면 어렵게만 느껴졌는데 요새는 조금 이해가 되서 그런가? 
class가 좋게 느껴진다


다시 본론으로 돌아와서   
기본적으로 c++에서는 클래스가 private으로 만들어 진다고 한다
그래서 외부에서 클래스의 속성(property)를 접근할 수 없다

그래서 외부에서 Mybike라고 만들어도 Mybike의 속성인 Name, Color등을 바꿀 수가 없다
즉, 클래스 내부에서만 접근이 되어서 클래스 블럭{} 안에서 접근해야지만 가능하다는 소리  

객체를 만들고 속성인 Name 에 다른 값을 줄려고하면 
예를 들어 MyBike.Name = "홍길동" 이라고 하면 에러가 발생하게 된다

이제 외부에서 접근할 수 있게 만들어주자  
**public**으로 바꿔주면 외부에서도 사용할 수 있게 된다

```cpp
#include <iostream>
using namespace std;

class Bike {
public:
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
정말 간단하게 public이라고만 적어주면 된다. public:
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


## 생성자 contructor 만들기

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
위 처럼 해당 객체의 값들을 일일이 만들어 줘야하는데 이를 편하게 하기위해서 생성자라는 것이 있다

생성자는 class명과 같아야 한다 그래서 마치 함수를 만들 듯이 만들어 주면 된다

```cpp
class Bike {
public:
    string Name;
    string Color;
    string Country;
    double Price;

    Bike(string name, string color, string country, double price) {
        Name = name;
        Color = color;
        Country = country;
        Price = price;
    }
};
```
이렇게 생성자 contructor 메소드가 만들어 졌다. 함수처럼 파라미터를 설정하고 
그 받은 값들을 속성인 Name, Color ...등에 저장해주는 방식이다

이렇게 하면 객체를 생성하면서 처음에 클래스의 속성들도 셋팅이 되게 된다
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

<br>

## 메소드
이번에는 클래스의 메소드에 대해서 알아보자

```cpp
class Bike {
public:
    //.. 생략함
    //.. 생략함

    void getInfoPrint() {
        cout << "name: " << Name << endl;
        cout << "color: " << Color << endl;
        cout << "country: " << Country << endl;
        cout << "price: " << Price << endl;
    }
```

클래스 안에서는 직접 속성 값들을 접근하는게 가능하므로 인스턴스 이름 없이 바로 Name, Color.. 등의 식으로만 적어준다 




클래스 도 정리하기

class Bicycle {
    프로퍼티
    string brandName
    string company
    string contry
    

    컨스트럭터

    메소드
}


