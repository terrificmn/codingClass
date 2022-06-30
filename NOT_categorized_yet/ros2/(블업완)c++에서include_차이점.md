# cpp에서 include를 할 때에 <>와 ""의 차이점
<> 는 Angled brackets 이라고 하고 "" 쌍따옴표는 double quotes 라고 한다

그런데 c++ 프로그램에서 처음에 include를 할 때에 보면 어떤 것은 쌍따옴표로 하고 
또 어떤 것은 꺽쇠(?)로 해서 한다

예를 들면   
```cpp
#include <functional>
#include <memory>
#include <iostream>
#include <cmath>
#include <vector>

#include "rclcpp/rclcpp.hpp"
#include "rclcpp_action/rclcpp_action.hpp"
#include "nav_msgs/msg/odometry.hpp"
```

무슨 차이가 있어서 그럴까하고 찾아보았다 ㅋㅋ

모두 다 header files를 찾는 것과 관계가 있다.

1. 먼저 angled brackets 경우  
우리가 직접 만든 header files이 아니라는 것을 말해주고 있다. 그래서 컴파일러는 특정한 파일위치를 검색하게 된다.   
컴파일러는 프로젝트 소스 코드의 디렉토리를 직접 찾지 않게 된다.   
예를 들면 vector는 /usr/incldue/c++/8/vector 이런식으로 위치를 컴파일러가 
또는 OS에서 기본값으로 header파일들이 있는 위치가 지정되어 있다고 보면 될 듯  

2. 두 번째 double-quotes를 사용하는 경우  
컴파일러한테 헤더파일은 직접 만들어진 것이라고 하는 경우라고 한다. 그래서 컴파일러는 먼저 현재 디렉토리를 헤더파일을 찾기 위해서 검색을 한다.   
그래도 찾지 못하는 경우에는 include 디렉토리를 검색하게 된다.

<br/>

## 결론
하지만 언제나 예외는 있을 것 같고  
아마 따옴표와 꺽쇠를 바꿔쓰더라도 컴파일을 할 때 에러가 나지는 않았다.   
(상황에 따라 다를 수도 있음)

- 컴파일러가 이미 헤더파일이 지정되어 있는 경우에는 <> (꺽쇠)를 사용. 현재 프로젝트 디렉토리는 검색을 안 함

- 내가 직접 만든 헤더파일이라면 "" (쌍다옴표)로 그래서 현재 프로젝트 디렉토리를 검색할 수 있게 해준다.  

아마 이런식으로 구분지어 생각하면 될 듯 하다. 

> 물론 예외도 있고, 컴파일러가 스마트하게 잘 찾아주는 것 같다. 일단 이런 컨셉이라는 것은 알게 된 것 같다

