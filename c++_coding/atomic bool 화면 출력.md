atomic 관련으로 선언된 것을 출력할 때는 %d로 출력이 안됨

간단하게 출력할 때에는 %u 와 함께 load() 메소드를 사용하면 된다   

```cpp

std::atomic_bool atomic_bool_test{false};

ROS_WARN("False or True: %u", atomic_bool_test.load());
```
결과: 0

또는 typecast를 이용해서 변환해서 출력한다
```cpp
std::atomic_bool atomic_bool_test{true};
ROS_WARN("False or True: %u", unsigned(atomic_bool_test));
```

결과는 1이라고 나옴


근데 
```cpp
std::cout << "False or True: " << atomic_bool_test << std::endl;
```

cout으로 출력을 하면 typecast를 할 필요도 없이 잘 출력된다 

