# sleep 을 thread, chrono 이용하기
```cpp
#include <chrono>
#include <thread>

std::this_thread::sleep_for(std::chrono::milliseconds(1000));
```

1초 멈춤