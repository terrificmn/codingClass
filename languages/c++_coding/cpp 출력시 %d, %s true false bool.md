```cpp
bool a = false;
ROS_WARN("true or false : %d", a);
ROS_WARN("true or false : %s", a ? "true" : "false");
```

%d는 정수형, %s는 string  

첫 번째는 true/ false는 1, 0으로만 표시가 된다.   
좀 더 보기 좋게, string으로 출력하려면  %s에 조건을 걸어주면 된다  

또 다른 방법으로는  iostream을 사용할 경우에

## cout의 boolalpha 사용하기

사용 예
```cpp
#include <iostream>
bool a = true;

std::cout << std::boolalpha << a << std::endl;
```

같은 결과를 얻을 수 있다 
```
true
```



