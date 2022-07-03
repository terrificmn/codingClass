# CPP c++에서 swtich case와 enum

먼저 스위치 케이스 예제 코드를 보자

```cpp
#include <iostream>

// enum 키워드로 Color라는 데이터 타입을 정의할 수 있다 (내마음대로)
// 이 값들은 상수와 매칭이 되기 떄문에 "문자열"을 사용 안함
enum Color {black, brown, red, gray, blond};

int main() {
    // 위에서 만든 것 처럼 Color라는 데이터타입을 선언할 수 있다. 
    Color hairColor = black;

    // 스위치 케이스
    switch (hairColor) {
        case black: std::cout << "hair is Black"; break;
        case brown: std::cout << "hair is brown"; break;
        case red: std::cout << "hair is red"; break;
        case gray: std::cout << "hair is gray"; break;
        case blond: std::cout << "hair is blond"; break;

        default: std::cout << "not vaild";  
     }

     return 0;
}
```

먼저 enum이라는 데이터 타입 선언하는 것을 알아보자

> 먼저 enum 이란 것은 Enumeration declaration이라고 하는데, 열거형 이라고 함  
이것은 어떤 범위에 있는 값들을 특정해서 지정할 수 있게 해주고   
{ enumerator-list1, enumerator-list2, enumerator-list3, ...etc} 처럼 엘레먼트 값을 넣어줄 수가 있다  
그리고 그 처음 값은 상수(const) 0과 같아서 그 다음부터 1씩 증가한다    
(배열의 요소처럼 비슷하게 작동하는 듯하다)    
그리고 중요하게도 미리 정해진 값만 사용할 수 있게 해주는 선언이다.



특이점은 문자열이라도 " "를 사용안하고, 아마도 상수에 매칭이 되서 그런 듯 하다
그리고 변수처럼 깂을 넣어 줄 수도 있다. 

Foo로 예로 들면
```cpp
enum Foo { a, b, c = 10, d, e = 1, f, g = f + c };
//a = 0, b = 1, c = 10, d = 11, e = 1, f = 2, g = 12
```

이를 활용해서 스위치 케이스에서 사용할 수가 있다.  
스위치케이스문에서는 대개 숫자로 조건을 대입해서 해주는데,  
enum을 사용하게 되면 값들이 지정해서 사용할 수가 있어서 편리하고 가독성이 있게 사용할 수 있다.

```cpp
switch (hairColor) {
        case 1: std::cout << "hair is Black"; break;
        case 2: std::cout << "hair is brown"; break;
        case 3: std::cout << "hair is red"; break;
        case 4: std::cout << "hair is gray"; break;
        case 5: std::cout << "hair is blond"; break;

        default: std::cout << "not vaild";  
     }
```

> 잠깐만 🧐 아마 보통 이런식으로 사용해야할 것이다. 만약 여기에 머리색깔이 더 들어가게 되면
코드를 추가할텐데, 6번을 넣을 차례인데 6번을 yellow를 넣으려고 하는데
숫자로만 되어 있으면 yellow가 있었나? 하고 바로 알 수가 없다. (출력 되는게 없다고 가정 했을 시)  
하지만 enum을 사용해서 데이터 타입을 만들었다면 처음의 예제 처럼 
바로 어떤 것인지 알 수 있으므로 가독성에도 좋다. 

switch문에서는 중요한 것은 하나의 case마다 break를 해줘야지 
해당 케이스를 실행하고 빠져나가진다. 만약 break를 안한다면 다음 코드도 실행이 되게 된다.

```cpp
 switch (hairColor) {
        case black: std::cout << "hair is Black"; 
        case brown: std::cout << "hair is brown"; break;
```

위의 코드에서 첫 번쨰 케이스 코드에 break가 빠졌다.   
그러면 hairColor 가 Black이라고 했을 때, 실행을 해보면 break가 없으므로   
다음 줄 코드까지 실행이 되고 break를 만난게 되서 빠져나가게 됨

그래서 원치 않는 결과과 나온다
```
hair is Black
hair is brown
```
이런식으로 나오게 될 것이다.

그래서 각 case마다 break;를 넣어주면 된다.


그리고 마지막으로는 default값을 지정해 줄 수가 있는데,  
만약 enum으로 지정한 데이터 타입인 Color에 pink는 없는데 pink라는 값이 들어 왔다고 하면

```cpp
생략..

hairColor = pink; 

switch (hairColor) {
    case black: std::cout << "hair is Black"; break;
    case brown: std::cout << "hair is brown"; break;
    case red: std::cout << "hair is red"; break;
    case gray: std::cout << "hair is gray"; break;
    case blond: std::cout << "hair is blond"; break;
    }

```
이렇게 되면 pink란 값을 찾을 수가 없으므로 에러가 발생하게 된다.

이럴 때 마지막 구문에 default를 넣어주게 되면 에러를 방지해줄 수가 있다

```cpp
..생략..
hairColor = pink; 

switch (hairColor) {
    case black: std::cout << "hair is Black"; break;
    case brown: std::cout << "hair is brown"; break;
    case red: std::cout << "hair is red"; break;
    case gray: std::cout << "hair is gray"; break;
    case blond: std::cout << "hair is blond"; break;

    default: std::cout << "not valid";  
    }

```
이렇게 되면 pink라는 것이 enum으로 열거한 Color 타입에 없다고 해도 에러가 발생 안하고 
default의 "not valid"라고 나오게 된다.
