# char* 사용 시 주의

```
warning: ISO C++ forbids converting a string constant to ‘char*’ [-Wwrite-strings]
[-Wwrite-strings]
    9 |     param("hello", 10);
      |           ^~~~~~~
```
이런식으로 char를 변환하려고 할 때 에러가 발생  

```cpp
// 이런 함수가 있고, c style로 파라미터를 받는다고 할 때
void param(char* str, int) {
    std::cout << str << std::endl;
}

int main() {
    ...
    param("hello", 1);
}

```

재연해보면 이런식의 프로그램 인 듯 하다.  

위의 string을 complier러는 constant로 인식을 한다고 한다  
그래서 char* 포인터로 변환이 안된다고 하는 것

대신에 위의 char를 const char* 로 하는 것은 변환이 되고, 허용이 된다   

그래서 위의 내용을
```cpp
void param(const char* str, .....)
... 생략
```
이런식으로 하면 빌드 시에 문제없이 warning 없이 빌드가 된다 

## string
STL 라이브러리를 이용한 `string`을 이용해서 하는 방법이 좋다.  
char* 대신에, std::string 으로 사용하기 
애초에 파라미터와 주고 받을 때 std::string 을 사용하면 c++ 스타일이 되는 것 같다 