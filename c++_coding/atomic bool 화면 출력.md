atomic 관련으로 선언된 것을 출력할 때는 %d로 출력이 안됨

간단하게 출력할 때에는 %u 와 함께 load() 메소드를 사용하면 된다   

```cpp

std::atomic_bool atomic_bool_test{false};

ROS_WARN("False or True: %u", atomic_bool_test.load());
```


