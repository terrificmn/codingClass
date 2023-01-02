c/c++에서는 functions 이 extern 으로 declare가 되어 있는데  
그래서 extern으로 되어 있다는 것은 다른 소스파일에서 작성되어 있는 함수들도 사용할 수가 있다는 것이 된다  (한 프로그램 내에서)


declare는 변수를 선언하지만 메모리에 할당은 안 한 상태로 컴파일러는 어떤 변수가 있는지만 알게 된다  
```cpp
double x;
```
x라는 double 형 변수가 code에 있다는 것을 의미하고   

define은 메모리에 할당하는 것
```cpp
double x = 0.1;
```

이렇게 되면 변수 x가 있다고 declaring을 하면서 메모리에 할당을 한다

declare는 여러번 할 수 있지만..  
define은 한번 밖에 할 수가 없다. 왜냐하면 메모리에 같은 변수를 여러번 할당할 수는 없기 때문이다  

> x= 0.2;  이런식으로 하는 것과는 다르다 (변수를 선언하면서 할당할 때)



이제 변수를 declare를 할 때 extern을 붙이면 다른 소스코드에서도 불러서 (접근)사용할 수 있게 된다     
test_x.h 파일에서   
```cpp
extern double x;
```

test_x.cpp 파일에서 x를 define 해줘야한다  
```cpp
double x = 0.1;
```

> 헤더파일에서는 변수만 declare를  해주고, cpp 파일에서 define을 해서 사용할 수 있게 한다 



main.cpp 파일에서 x를 불러다가 사용할 수가 있다  
```cpp
#include <iostream>
#include "test_x.h"

int main() {
	std::cout << "x: " << x << std::endl;

	return 0;
}
```


이렇게 해서 외부파일인 test_x.h 파일의 x 변수를 사용할 수 가 있다.   

> 만약 헤더파일에서 declare만 했을 경우에는 빌드시 에러가 발생한다.   
왜냐하면 x는 declare만 되어 있는 상태이기 때문이다 . 즉, 컴파일러는 변수 x는 알고 있지만 메모리 할당이 안되어 있는 상태이므로 define을 해서 메모리 할당까지 해야지 잘 작동하게 된다   



이런식으로 클래스나 함수들도 extern으로 선언해서 사용할 수가 있다   


ExampleA 클래스가 있다고 할 때, 이를 ExampleB 클래스에서 사용하려면 클래스를 instance 해서 사용할 수도 있지만, block 등에서만 사용이 가능하거나, 소멸되는 등의 문제가 발생할 수가 있다   

이제 extern으로 선언 후  main함수 등에서 클래스를 생성하고 ExampleB 클래스에사용할 수가 있게 된다   

main.cpp, ExampleA.h, ExampleA.cpp, ExampleB.cpp 등이 있다고 할 경우   

변수 x를 만든 방식처럼 h파일에서는 declare를 해주고, cpp파일에서 define을 해준다  

```cpp

class ExampleA {
public:
	ExampleA();
	
};
extern PtrExampleA* ExampleA; 
```


cpp에서는 define을 해줌
```cpp
#include "ExampleA.h"

PtrExampleA = nullptr;

// 생성자에서 바로 할당
ExampleA::ExampleA() {
	PtrExampleA = this;
}

ExampleA::printHello() {
	std::cout << "hello";
}
```
처음에서는 포인터에 값이 null로 넣어준다  그 후 클래스가 생성이 되게 되면 주소값을 가질 수 있게   
this자체가 현재 클래스의 주소 이므로..  포인터 주소가 잘 할당되게 된다 

이제 다른 소스 파일에서 ExampleA 포인터를 사용하려면 어느 순간에 (프로그램이 종료되지 않는 선에서)  
객체로 만들어져야하고 대충 main.cpp 에서 만든다고 치면,  
ExampleB 같은 클래스에서 사용할 수 있게 된다   (ExmapleA 클래스를 include만 하면 된다)

main.cpp
```cpp
#include "ExampleA.h"
#include "ExampleB.h"

int main () {
	ExampleA A_class_object;

	ExampleB B_class_object;
	B_class_object.doSomething();
	
}
```

이제 extern으로 선언된 PtrExampleA를 사용하면 된다   

ExampleB라는 클래스에는 예를 들어 아래처럼 되어 있다. extern으로 정의된 PtrExampleA를 사용해서   
ExampleA 클래스의 메소드를 호출하고 있다

ExampleB.cpp 파일
```cpp
#include "ExampleA.h"

ExampleB::ExampleB() {
}

ExampleB::doSomething() {
	PtrExampleA->printHello();
}
```



--- update필요! 및 디버깅 필요