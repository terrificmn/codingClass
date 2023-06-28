## String , std::string, 그리고 char
아두이노에서는 std::string을 사용할 수 가 없다.  자세한 내용은 아래 내용을 보자

`String` and `std::string` both dynamically allocate memory, and will both cause heap fragmentation.

They are just different implementations of the same principle. `std::string` is the most commonly used version, as it is part of the official C++ standard. However, on AVR Arduinos, you cannot use the C++ Standard Template Library (STL), so you cannot use `std::string`. That's why Arduino created its own `String` class, and this is the most widely used version in the Arduino ecosystem.

While both string classes use dynamic memory, most implementations of `std::string` have Small String Optimizations (SSO), where small strings are allocated on the stack instead of the heap. This can slightly reduce the amount of fragmentation caused by the strings.

The best string implementation to use on microcontrollers with limited RAM is null-terminated character arrays, allocated on the stack. The stack data structure ensures that memory is deallocated in the reverse order of the allocations, which makes fragmentation impossible. These strings are often referred to as "c-strings".

Pieter   --  아두이노 포럼에서 복사


그리고 String으로 만들고 ,

```cpp
String stringOne =  String(13);                           // using a constant integer
String stringOne =  String(analogRead(0), DEC);           // using an int and a base
String stringOne =  String(45, HEX);                      // using an int and a base (hexadecimal)
String stringOne =  String(255, BIN);                     // using an int and a base (binary)
String stringOne =  String(millis(), DEC);                // using a long and a base
String stringOne =  String(5.698, 3);                     // using a float and the decimal places
```

String으로 만든 객체에 toDouble(), toInt(), toFloat() 등도 사용가능


하지만.. c style 로 사용하는 것이 추천이라고 함;;;; 흠... 

역시 퍼온 내용 중... 

Here we would not recommend using that class though and stick to c-strings and associated C functions in [stdlib.h 53](http://www.cplusplus.com/reference/cstdlib/) and [string.h 98](http://www.cplusplus.com/reference/cstring/)

Converting an int to a cString could be done with [itoa() 680](http://www.cplusplus.com/reference/cstdlib/itoa/) for example and if you have enough flash memory (because it adds a heavy piece of code) sprintf() could help too


[출처: 더 참고... ](https://forum.arduino.cc/t/how-to-convert-a-int-number-to-a-string-text/573255/5)


## char를 넘겨줄 때
함수를 만들어서 char를 넘겨주려고 하면 참 힘든것 같다... 아직까지 정확하게 정리가 안됨 ㅠ   

일단 String으로 만들어서 넘겨주는 방식이 편한듯 하다   

String으로 바로 넘겨주거나 아니면, 포인터로 넘겨주는 방식

```cpp
void myFuntion(String *str_ptr);

/// 생략
void loop() {

    char data_chars[4] = "abc";
    String str = data_chars;

    myFuntion(&str);
}

void myFuntion(String *str_ptr) {
    ///생략
    // str_ptr을 가지고 뭔가 처리
}
```

char 배열이 만들어져 있어서 뭔가 처리해야할 때 char 형태로 함수에 넘겨주고 싶은데   
이게 배열의 크기가 달라지는 경우도 있고   
그냥 char로 넘겨주면 * 관련 에러가 발생   

그래서 그냥 String으로 처리했지만   
위의 방법도 잘 통하지만, 뭐가 char로도 잘 정리를 해봐야겠다.  

언제나 char 배열이 어려운 듯 싶다 ㅠ



### const char 로 변환
String을 char 방식 c style로 사용하는 것에는 

const char 포인터를 사용해서 만들어 줄 수가 있다 

```cpp
String my_str = "hello";
const char* my_char = my_str.c_str();
```

`char *` , `const char`, `const *char[]`, `char []` 이런 걸로는 String 을 변환해서 넣어줄 수가 없고,  
**contst char*\** 이어야만 하는 듯 하다

물론 바로 `my_str.c_str();` 처럼 바로 사용해서 어떤 값으로 넘겨줄 수도 있지만   


이유를 좀 더 학습해봐야겠다   

