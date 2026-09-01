# class를 Pointer 만들기

이제 다이나믹으로 할당을 heap메모리에 할당 할 때에는 new 키워드가 있어야 하느데  
new 키워드가 쓰일 때는 포인터를 만들어서 memory할당을 하게 하거나, 포인터 값이 NULL 일 때에만 사용한다   

cpp
```cpp
int x;
int* ptr_int1 = new int;
int* ptr_int2 = NULL;
int* ptr_int3 = nullptr;

// delete 가능
delete ptr_int1;
delete ptr_int2;
delete ptr_int3;
```

이런식으로 사용할 수가 있다. 

하지만 malloc() 함수로 메모리 할당을 했을 때에는 delete를 사용하면 안되고, free()를 사용해야한다   
```cpp
int x;
int* ptr_int4 = (int*)malloc(sizeof(int));

## 이럴 경우에는 delete를 하면 안된다
```

일단 pointer를 new로 할당하면 dynamic memory로 할당을 한다.  
new는 constructor를 delete는 destructor를 담당한다고 생각하면 된다. 셋뚜셋뚜   


## delete 했을 경우 차이

먼저 헤더파일
```h
#ifndef POINTER_CLASS_H
#define POINTER_CLASS_H

#include <iostream>

class PointerClass {
private:
    int number = 0;

public:
    PointerClass();
    ~PointerClass();

    void testCout();
};

#endif
```

그리고 cpp 파일
```cpp
#include "pointer_class.h"

PointerClass::PointerClass() {
    std::cout << "Pointer Class Init" << std::endl;
}

PointerClass::~PointerClass() {
    std::cout << "Pointer Class Destructed" << std::endl;
}

void PointerClass::testCout() {
    std::cout << "test test test print string. ";
    std::cout << "number is: " << this->number << std::endl;
}


int main(int argc, char** argv) {

    PointerClass* ptr_class = nullptr;

    printf("First Address nullptr: %p\n", ptr_class);

    // PointerClass* ptr_class = new PointerClass; //  한번에 만들 때는 nullptr을 줄 필요없이 바로 만들어도 됨
    ptr_class = new PointerClass;
    printf("Address after new : %p\n", ptr_class);

    delete ptr_class;
    ptr_class->testCout();
    // ptr_class = nullptr;
    ptr_class->testCout();
    printf("Address after delete : %p\n", ptr_class);

    return 0;
}
```


class PointerClass 를 이용해서 만들어주고 포인터 이므로 new 키워드로 생성한 후에   
지울 때에는 delete를 이용해서 지워준다   

특이점은 delete를 하면 destructor가 실행되면서 destructor 의 내용이 출력되는데  
그래서 delete가 된 것임을 알 수 있는데... 주소를 알고 있기 때문에   
testCount()를 메소드를 호출하면 실행이 되는 것을 알 수 있음   

이유는 주소가 남아 있어서 그런 것 같다   

결과  
```
First Address nullptr: (nil)
Pointer Class Init
Address after new : 0x55638bfd22c0
Pointer Class Destructed
test test test print string. number is: 0
test test test print string. number is: 0
Address after delete : 0x55638bfd22c0
```

포인터가 주소가 알고 있어서 그런 듯 하다.   

## nullptr로 주기
delete 이후에 nullptr를 넣어준다면

```cpp
... 같음 생략
delete ptr_class;
ptr_class->testCout();
ptr_class = nullptr;
ptr_class->testCout();
printf("Address after delete : %p\n", ptr_class);
```

이번 경우에는 nullptr이 들어가서, testCount()을 실행하게 되면 세그먼트 오류가 나면서   
클래스 오브젝트를 실행할 수 없게 된다   

결과
```
First Address nullptr: (nil)
Pointer Class Init
Address after new : 0x56105e19f2c0
Pointer Class Destructed
test test test print string. number is: 0
Segmentation fault (core dumped)
```
첫번째 testCout()는 주소를 알기에 출력되지만(delete 이후)    
두번째 testCout()은 nullptr이 되기 때문에 치명적인 core dumped가 이러나면서 프로그램 종료가 됨   

> 정확한 것은 delete 이후에는 다른 object가 new키워드로 해당 메모리에 만들어 질 수도 있게 되는 상태가 되는데  
새롭게 할당 받기 전에는 그전 value를 가지고 있을 수 있다고 한다.  
하지만 프로그램이 계속 실행되면 그 delete 한 메모리의 자리에 다른 값들이 써질 수 있게 되는 것이고   
delete 이후에 오브젝트에 접근을 해서 사용한다면 당장은 실행이 되지만 결국은 문제가 발생할 수 있게 된다고 한다  
즉 운이 좋게 아직 delete된 객체(오브젝트)에 새로 overwrite가 안 되었다 정도 인 듯 하다 ㅋㅋ   
delete 이후에 nullptr을 해주고, 포인터가 있는지를 확인하려면 `if(!myObject)` 처럼 사용하면 될 듯 하다


## 정확한 방법인지는 모르겠으나... 
포인터를 delete를 했기 때문에 **nullptr**를 넣어줘서 확실하게 실행이 안되게 해야하는 것 같다

그리고 new로 다이나믹 메모리 할당할 경우도 있겠지만  
stack 메모리를 사용한 일반적 방법으로 사용하는 것이 좋다고 한다   

```cpp
{
    PointerClass ptr_class;

    ptr_class.testCout();
}
```
이런 경우에는 해당 블럭을 벗어나면 자동적으로 소멸되게 된다.   
이를 RAII 와 관련이 있는데 Resource Acquisition Is Initialization 이라고 함  

검색해보기;;


하지만 Dynamic Allocation이 필요하다면 c++에서는 smart pointer를 사용하는 것이 좋다고 한다  

> smart_pointer.md 참고하기

