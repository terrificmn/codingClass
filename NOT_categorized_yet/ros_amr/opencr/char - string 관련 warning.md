
```
warning: ISO C++ forbids converting a string constant to 'char*'
```

아두이노 관련 IDE에 실행할 때 위와 같은 warning이 발생하면  
c++ 11 이후로 char *  point 로 허용이 되지 않는다고 함.   
string 문자열이 const char[] 배열로 만들어 지는데 const 데이터를 가리키는 non-const 포인터는 생성할 수가 없다고 한다 . 그래서 포인터로 만들 때에는 const char*  식으로 포인터로 만들어야 한다고 한다   

> string constant 이면 수정되면 안 된다

char* msg로 만들어 놓고 사용하려고 하면 문자열 상수는 char* 로 변환할 수 없다고 나온다 
예를 들면 이런 식

```
char* msg = "hello";
strlen(msg);
```

워닝 발생
```
src/main.cpp: In function 'void loop()':
src/main.cpp:14:17: warning: ISO C++ forbids converting a string constant to 'char*' [-Wwrite-strings]
     char* msg = "Hello";
```

이런 경우에는 아예 포인터가 아닌 배열로 만들어서 접근할 수 있게 하거나,  
char 포인터로 생성을 안 하고, char array로 생성을 해주거나  
String으로 만들어서 사용하면 편하다. strlen() 함수 등이 필요할 때는 .c_str()함수로 변환해서 사용하면 된다. 
std:string 과는 다른것 같으나, 문제 없이 작동 된다.  

```cpp
char msg1[] = "hello";
String msg2 = "world";

strlen(msg1);
strlen(msg2.c_str());
```






