## auto_ptr
스마트 포인터에는 auto_ptr, shared_ptr, unique_ptr, weak_ptr 이 있는데  

그 중에 auto_ptr은 가장 오래된 스마트 포인터   

사용하지 않는 것이 좋다.   

포인트의 얕은 복사가 문제가 될 수 있다고 한다   

skip..


## shared_ptr
인스턴스를 만들 때마다 포인팅 횟수를 늘리고,   
해당 인스턴스가 블럭이나, 함수등을 벗어나서 소멸한다면, (자동으로 소멸된다)   

포인팅 횟수를 마이너스를 해주고, 최종적으로 0이 되게 되면 자동 소멸된다   

> 처음 생성하면 카운터는 1이 된다  


```cpp
#include <memory>
```
memory를 인쿠르드 하고 `std::shared_ptr<클래스>` 로 사용할 수가 있다. 

dynamic allocation을 하게 되면 new 로 pointer에 클래스 등을 할당해주고   
**delete 키워드**로 없애야 하는데   

smart pointer를 사용하면 동적으로 heap 메모리를 할당하면서도 자동으로 destruct 해주게 된다   

std::shared_ptr 이나 std::unique_ptr 을 사용  

```cpp
{
    // heap 메모리에 오브젝트 sptr_x 를 만들어준다
    std::shared_ptr<MyClass> sptr_x = std::make_shared<MyClass>();

    // 이제 sptr_x를 이용해서 메소드등 호출하면서 사용
    sptr_x->testCout();  // 이런 함수가 있다고 가정
}
```

sptr_x 오브젝트는 블럭을 벗어나게 되면 자동으로 소멸하게 된다.   
new 키워드로 만들게 되면 delete를 해서 해줘야하는데, 
스마트 포인터는 heap 메모리에 할당이 되어도 블럭을 벗어나면 자동으로 std::shared_ptr 에서   
소멸시켜준다  

return 등으로 스코프를 벗어날 경우에도 자동으로 소멸한다   

[예제는 cpp_practice_playground 깃허브으 smart 디렉토리를 확인하자]()   



