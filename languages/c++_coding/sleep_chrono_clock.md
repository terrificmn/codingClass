# sleep 을 thread, chrono 이용하기
```cpp
#include <chrono>
#include <thread>

std::this_thread::sleep_for(std::chrono::milliseconds(1000));
```

1초 멈춤

## chrono steady_clock 사용하기
먼저 system_clock 과 steady_clock 이 있는데 자세한 것은 아직 공부를 아직 못함   

ros의 duration 처럼 steady_clock 도 현재 시간을 할당 한 다음에  
같은 steady_clock 형식으로 빼 주면 duration으로 만들 수가 있다.

```cpp
std::chrono::steady_clock::duration duration_t;
std::chrono::steady_clock::time_point current_t;

current_t = std::chrono::steady_clock::now();
//ex
duration_t = std::chrono::steady_clock::now() - current_t;
```

여기에서 나온 duration형식을 일단 int등과 비교하려면  
`std::chrono::seconds{10}` 으로 해서 바로 비교할 수가 있다.

```cpp
if(duration_t < std::chrono::seconds{10} ) {
    std::cout << "shorter than 10 seconds" << std::endl;
}
```

다른 예제도 더 공부해서 업데이트하기!

