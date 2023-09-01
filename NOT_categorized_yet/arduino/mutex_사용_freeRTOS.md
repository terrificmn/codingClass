# freeRTOS 라이브러리 - mutex 

std::mutex 와 비슷한 기능을 하는 freeRTOS 라이브러리로 구현할 수 있다   

```cpp
// Create a mutex:
std::mutex mutex;  

// 특정 블럭에서...
{
    // Use the mutex in a task:
    std::lock_guard<std::mutex> lck(mutex); // enter critical section
    /* access shared resources */
    
} // automatically exit critical section
```


이를 arduino 에서는...   

```cpp
// Create a mutex:
SemaphoreHandle_t mutex = xSemaphoreCreateMutex();
assert(mutex);

// 특정 블럭 (아마도 function을 지정해야할 것이다..)
// Use the mutex in a task:
{
    xSemaphoreTake(mutex, portMAX_DELAY); // enter critical section
    /* access shared resources */
    xSemaphoreGive(mutex); // exit critical section
}
    // Must manually destroy the mutex when no longer needed:
    vSemaphoreDelete(mutex);

```

위에서 xSemaphoreTake() 함수는 unique_lock() 함수와 비슷해서 Take, Give를 통해서   
lock, unlock을 해줘야 한다   


> 물론 테스트에서는 성공하지 못함  

