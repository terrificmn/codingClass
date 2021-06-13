ros
그렇게 잘 사용은 안하지만

스위치문

```cpp
#include <iostream>

enum HairColor {black, brown, red, gray, blond};

int main() {
    HairColor haircolor = black;

    switch (haircolor) {
        case black: std::cout << "hair is Black"; break;
        case brown: std::cout << "hair is brown"; break;
        case red: std::cout << "hair is red"; break;
        case gray: std::cout << "hair is gray"; break;
        case blond: std::cout << "hair is blond"; break;

        default: std::cout << "not vaild";  
     }
}

    return 0;

```
switch문에서는 하나의 case마다 break를 해줘야지 
해당 케이스를 실행하고 빠져나가진다. 만약 break를 안한다면 다음 코드도 실행이 되게 된다.

Haircolor로 선언한 것이 black, brown, red, gray, blond 이 아닌 다른 문자열이 오면
예를 들어서 switch (white) 이런식으로 넣으면 에러가 발생하게 된다
그래서 switch case에 default를 넣어줄 수가 있다.



보너스 데이터타입

그래서 스위치 이프 베이직 하나

포인터 하나

클래스 하나 

이렇게 포스팅하기


포인터도 들어감- 다시 한번 보면서 정리하기


클래스 도 정리하기

class Bicycle {
    프로퍼티
    string brandName
    string company
    string contry
    

    컨스트럭터

    메소드
}


