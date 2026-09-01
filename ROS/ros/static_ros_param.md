# ros static parameters
클래스에서 static 함수로 만들면 클래스로 인스턴스로 만들지 않고도 접근이 가능하다.  

예를 들어서 class StaticExample 이라고 있다면    
`static void setTest();` 만들었다면   

StaticExample::setTest() 로 호출해서 사용할 수가 있다.

단, static 함수는 class의 member가 아닌 것처럼(?) 취급되어서   
해당 함수에서 어떤 값들을 저장하거나 할 때에는   

변수를 클래스 내에서 static으로 만들어서 사용할 수 가 있다.   

이를 한번 더 클래스 밖에서 사용하려면 전역으로 main() 함수가 시작되기 전에  
해당 static 변수를 **초기화를 시켜야**지만 사용이 가능하다.  


예 header 파일
```cpp

class StaticExample {
public:
    StaticExample();

    static void setTest();
    static int test_num;
    static bool is_true;
};
```

cpp 파일
```cpp
#include "static_exmaple.h"

StaticExample::StaticExample() {}

void StaticExample::setTest() {
    // 여기에서 사용할 변수 값들 처리
    test_num = 10;
    is_true = true;
}

```

메인.cpp
```cpp
#include <iostream>
#include "static_exmaple.h"

// 초기화를 시켜야 한다. 클래스 내에서는 초기화를 할 수가 없다. 
int StaticExample::test_num = 0;
bool StaticExample::is_true = false;

int main() {

    // 사용
    StaticExample::setTest();

    // 뭐 대충 이런식으로 사용.
    int new_numb = StaticExample::test_num;

    // 인스턴스를 만들었다면..보통 접근하는 방식처럼 사용도 가능
    StaticExample staticEx;
    std::cout << staticEx.is_true << std::endl;

    return 0;
}
```

이제 static으로 선언된 함수 및 변수 들은 어디에서든 접근이 가능하므로   
파라미터 설정이나, 공통된 데이터를 사용할 때 유용하게 사용할 수 있을 듯 하다.

> static이 아니면 기존 메인에서만 사용이 가능하거나, 다른 인스턴스로 값을 넘겨주거나 해야해서  
다른 인스턴스에서 해당 공통 값을 받아서 사용하기가 불편(?) 했는데      
static 변수에 저장해놓고 사용하면 다른 클래스에서 접근하기 쉬워서 좋은 듯 하다.  


