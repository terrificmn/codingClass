# iostream 의 cout과 cin

c++언어를 시작할 때 처음에 당황했던 코드 중 하나여서 정리해본다.   
솔직히 << 가 너무 많이 나와서 당황함 ㅋㅋ 😭

> 잠깐만! 사실 std에는 문자열 관련된 기능도 들어가 있다. 

cout 포스팅을 하기에 앞서서 이 부분 (문자열 관련)을 잠깐 보면   
(사실 이 부분도 처음에는 몰라서 당황 😱 이게 뭔가 했다?! 그래서 정리해보았다.)

먼저 C언어에서는 char로 선언하고 [] 배열로 넣어줘야했던 것 같은데, 끝에는 0이 들어가야 했었던가? 🙄
```c
char str[5] = "hello";
```
하지만 c++에서는 **string** 타입을 지원한다. 그냥 string 으로 선언하고 변수에 문자열을 넣어주면 되는 것  
이것을 가능하게 해주는 게 std 이다. 이것을 사용하려면 아래 처럼 입력
```cpp
std::string str = "hello";
```
라고 해주면 된다. 

좀 더 편하게 할 수 있는데 std::를 사용한다고 선언해주면 쉽게 사용이 된다  
using std::string 이라고 선언해준다  
```cpp
#include <iostream>
using std::string;

main (){
    string str;
    str = "hello";
}
```

<br/>

## 이제 cout를 본격적으로 살펴보자~
cout은 standard output stream 이며  C++ stream object를 사용햘 때 cout을 사용해서 출력을 한다

#include <iostream>을 사용해서 헤더 파일을 선언을 해서 include로 가져와야한다
```cpp
#include <iostream>
```

기능은 출력을 해주는 printf 함수와 비슷한 기능을 한다

기본적으로 사용법은 std::cout 처럼 사용을 한다. 위에서 std::string으로 선언한 것과 비슷한 원리이다.  

사용예:
```cpp
std::cout << "hello world" << "from C++";
```
2개의 <<는 왼쪽방향으로만 써주면 되고 그 사이에 원하는 문자열, 변수를 넣어주면 된다. 

하지만 std::string도 using 키워드를 사용한 것 처럼  
네임스페이스라는 기능을 사용해서 std를 사용하겠다고 해주면
```cpp
using namespace std;
```
std를 사용하겠다고 선언을 해서 이제는 std를 빼고 cout만 사용을 할 수 있게 된다.

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
using namespace std;

int number = 10;
cout << "hello world\n" << "숫자는 " << number << "입니다." << endl;
cout << "hello world";
```
아 그리고 endl 은 '\n'과 같은 기능이면, 줄바꿈을 해준다
```
hello world
숫자는 10입니다.
hello world
```

<br/>

## 이번에는 cin 살펴보자~

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
