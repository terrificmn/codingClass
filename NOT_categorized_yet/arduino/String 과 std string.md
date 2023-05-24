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

