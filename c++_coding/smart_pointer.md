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

단, return 등으로 스코프를 벗어날 경우에도 그러한지는 더 공부가 필요할 듯 


# 스마트 포인터 스터디 및 업데이트하기

