# std string을 char c-style로 사용

문자열을 받아서 각 요소로 사용하고 싶을 경우가 있다    
하지만 c++에서 std::string 상태에서는 배열로 접근을 할 수가 없다. 물론 배열로 접근할 일이 많이 없기는 하지만...   

어쨋든, std::string을 c_str()메소드로 변환 하면 쉽게 배열로 접근해서 사용할 수가 있다

```cpp
std::string str = "0.12345";

const char *converted_char = str.c_str();
```

> 여기에서 주의할 점은 그냥 char로 변환은 안 된다. const char 포인터로 선언을 해줘야 std::string 방식을  
변환을 해 줄 수가 있다 . **const char \***

이제 각 배열로 인덱스로 접근해서 원하는 데이터를 사용하거나 출력할 수가 있다 

```cpp
int first = (int)converted_char[0];
std::cout << converted_char[3];
```
