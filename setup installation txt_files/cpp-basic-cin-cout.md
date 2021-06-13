## cout

c++언어를 시작할 때 처음에 당황했던 코드 중 하나여서 정리해본다

cout은 standard output stream 이며  C++ stream object를 사용햘 때 cout을 사용해서 출력을 한다

#include <iostream>을 사용해서 사용할 수 있으며
출력을 해주는 printf 함수와 비슷한 기능을 한다

원래는 std::cout 처럼 사용을 해야하나 
네임스페이스라는 기능을 사용해서 std를 사용하겠다고 해주면
```cpp
using namespace std;
```
그러면 cout 만 사용을 할 수 있게 된다.

사용법은 cout 처음에 써주고 << 넣어주고 원하는 문자열 변수를 차례차례 넣어주면 된다.

사실은 << (2개의 less than sign)이 표시 때문에 이게 무슨 의미인가 했다.
이것도 이름이 있다 insertion operator 삽입연산자 정도이다

```cpp
int number = 10;
cout << "hello world ";
cout << number;
```

```
hello world 10
```
이런식으로 나오게 된다.

쓰고 싶은 것은 insertion operator을 이용해서 << 
쓰고 싶은 것을 쭉쭉 적어주면 된다. 참고로 줄 바꿈은 endl 로 해주게 된다
(문자열 끝에 \n으로도 가능하다 "hello world\n")

```cpp
int number = 10;

cout << "hello world\n" << "숫자는 " << number << "입니다." << endl;
cout << "hello world";
```

```
hello world
숫자는 10입니다.
hello world
```


## cin

cin은 반대로 입력을 받을 때 사용하며 마찬가지로 C++ stream object에서 키보드로 입력을 받을 때 사용

반대로 >> 표시를 사용한다 (two "greater than" sign)

```cpp
int num;
cout << "숫자를 입력하세요 : ";
cin >> num;
cout << "입력한 숫자는 " << num << " 입니다";
```

이런식으로 변수를 선언하고 키보드를 입력을 받아서 num변수에 넣어줄 수 있다

cin도 마찬가지로 2개 이상을 받을 때 >>을 여러번 넣어서 사용할 수 있다

```cpp
cin >> a >> b;
```

끝

[참고한 매뉴얼-튜토리얼 사이트](https://www.cplusplus.com/doc/tutorial/basic_io/)