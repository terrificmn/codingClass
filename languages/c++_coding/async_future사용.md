# async 사용

std::thread 를 사용하는 것 처럼 std::async 를 사용할 수가 있는데  

std::cin.get(); 함수를 사용하는데, 이때 사용자 입력이 있기 전까지 block이 된다  
그래서 만약 while loop안에서 사용 중이라면 다른 기능들은 사용할 수가 없다.  

그래서 이를 thread로 처리해서 할려고 했으나, async 기능으로 구현하면 더 적합한 것 같아서 진행

> 아마도 std::thread로도 같은 기능으로 구현이 가능할 듯 한데.. 테스트 코드를 만들어 봐야할 듯 


async를 사용하려면 future를 include 한다
```cpp
#include <future>
```

클래스를 많이 사용하므로 클래스의 어느 특정 메소드를 연결하는 방법이다.  

먼저 클래스를 인스턴스화 해준 후에, std::future로 만들어준다
```cpp
MyClass myClass;

std::future<void> myFuture = std::async(std::launch::async, &MyClass::myMethod, &myClass);
```

이때 연결해줄 클래스 및 메소드(펑션)을 연결해주고, 마지막 인자로 인스턴스로 만든 변수를 참조로 넘겨준다   
std::future로 만들어주는 type에는 연결할 메소드에서 리턴하는 타입을 넣어준다. 즉 myMethod에서 리턴하는 type   


이제 main 함수에서 while문이 돌아가고 있거나, 어느 특정 구간을 지난 다음에  
```cpp
myFuture.wait();
```
을 넣어준다   

이렇게 해주면 thread 와 비슷하게 blocking 하는 것 없이 서로 따로 작업을 수행할 수 있게 된다   


## async 연결 한 함수
async 연결 한 함수 myMethod 에서는 계속 반복이 되어야 할 것이기 때문에   
thread인데 한 번만 하고 끝내면 안되기 때문에  
`while(ture)`, `for(;;)` 등으로 감싸서 코드를 구성하면 될 듯 하다.   

앞서 말했던 std::cin.get() 을 사용하면서 게속 입력을 받을 수 있게 무한 루프로 구성을 하고   

> 확실이 thread 나 async 로 구성을 할 때 while 등으로 무한으로 구성을 안 해주면   
한번 내용을 수행하고 끝나버리게 되므로 주의

다른 main 함수 등에서는 동시에 다른 작업을 수행할 수 있게 한다.

