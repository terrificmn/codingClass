# 함수의 parameter 디폴트 value 주기

헤더파일에서 정의 되는 부분하고, 실제 cpp 파일에서 내용이라 조금 다르다

헤더파일에서 디폴트 value를 정의한다
```cpp
#ifndef FUNCTION_EXAMPLE_H
#define FUNCTION_EXAMPLE_H

class MyClass {
public:
    MyClass();
    void myFunctionA(int a = 0);
};

#endif
```

그리고 이제 cpp에서는 디폴트 값이 아닌 그냥 변수만 정의한다  
```cpp
MyClass::MyClass() {}

MyClass::myFunctionA(int a) {
    if(a != 0) {
        ....
    }
}
```

간단하다. 하지만 cpp에도 정의한 것 마냥 함수의 파라미터 부분에 `int a =0` 이라고 헤더파일과 똑같이 하게 되면   
에러가 발생한다  

```
default argument given for parameter 1 of
```

이제 main() 함수, 다른 곳에서 호출만 해서 파라미터 없이 넘겨주면 기본값 a에 0이 할당되고  
특별히 값을 넘겨줘서 처리하려면 다른 값을 매개변수로 넘겨준다
```cpp
MyClass myClass;
myClass.myFunctionA();

// or
myClass.myFunctionA(10);
```

> 나중에 까먹어서 또 왜 안되지 할까봐 남겨봄!ㅋ   
