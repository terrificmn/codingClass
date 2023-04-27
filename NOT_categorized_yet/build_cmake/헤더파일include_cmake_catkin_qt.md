# include 포함 시키기 
cmake, caktin, qt를 사용할 때 공통적으로 CMakeLists.txt 파일을 이용하는데  

> 참고, 사실 QT로 처음 프로젝트를 만들면 프로젝트 root 안에 다 만들게 되는데  
이때에는 header파일이 같은 디렉토리에 있기 때문에 CMakeLists.txt 파일에 특별히 지정을 안 해도   
excutable에 cpp파일만 등록해줘도 헤더파일을 잘 찾는다.   

하지만 뭔가 디렉토리로 구조를 src, include 이런식으로 만들면 (ROS는 아예 구조가 처음부터 그러하다)   
이게... 참 include에 있는 헤더 파일을 인식시키는데 참;; 한번에 안된다.. ㅠ

## 파일들
```
my_pkg/
├── include/
│   └── classA.hpp
└── src/
    ├── classA.cpp
    └── main.cpp
```
일반적인 요런 구성으로 src 안에 cpp파일, include 디렉토리 안에 h, hpp파일이 위치한 경우!

## cmake 사용
가장 순수하게 하는 방법.. 너무 좋다;;; 쉽고 심플하다

`include_directories( include )` 라고 하는 방법이 있는데 이렇게만 해줘도 include 디렉토리를 잘 찾아준다  
하지만 모든 include 디렉토리를 검색하는 것인지는 확실하지가 않다. (정확하지 않음)

그래서 좀 더 확실하게 해주면
```c
include_directories(
    ${PROJECT_SOURCE_DIR}/include
)
```

classA.cpp 파일 내부에서도 그냥 `#include "class_a.hpp"` 라고 만 해주면 알아서 잘 찾는다 

> add_executable() 에서는 cpp 파일 경로만 적어준다


## catkin ROS
ROS를 사용할 경우에는 디렉토리 구조가 조금 달라진다. 일단 ROS 기준으로 보면  

```
my_pkg/
├── include/
        └── my_pkg    
               └── classA.hpp
└── src/
    ├── classA.cpp
    └── main.cpp
```
include 디렉토리 안에 패키지명과 동일한 이름으로 디렉토리가 있고 그안에 헤더파일 위치  
즉 my_pkg/include/my_pkg/classA.hpp  

CMakeLists.txt 파일에는 
```c
catkin_package(
 INCLUDE_DIRS include
 CATKIN_DEPENDS roscpp
)

include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)
```

그리고 ClassA.cpp 파일에서 인쿠르드 할 때에는 패키지명을 한번 입력해서 해주면 된다   
```cpp
#include "my_pkg/classA.hpp"
```

> add_executable() 에서는 cpp 파일 경로만 적어준다


## 문제의 QT6
일단 qt6 버전인데... qmake가 아닌 cmake를 사용하는 방법임.  
~~분명히 방법이 있는데 지금 확실하게는 못 찾음~~

파일 디렉토리는 구조는 처음의 상태와 같다. (이 부분도 아래에서 추가로 다룸)  
일단 위에서 나온 방법 처럼 include_directories()를 바로하면 제대로 헤더파일을 못찾는다.. 그게 문제  

현실적으로 쉬운 방법은 CMakeLists.txt 에서 qt_add_executable() 기능에 헤더파일 위치 등록해 주는 것

```
qt_add_executable(appmy_pkg
    src/main.cpp
    src/classA.cpp
    include/classA.hpp
)
```
> add_executable() cmake의 기본 함수? 말고 qt 자체 것 사용


그리고 classA.cpp, main.cpp 에서 인쿠르드 할 때에는   
```cpp
#include "include/classA.hpp"
```

이렇게 하면 빌드가 잘 되고 클래스를 사용하는데 전혀 문제가 없지만, cpp파일에서 **"include/...cpp파일"** 처럼   
include를 포함시켜야 한다    


### 문제의 QT6 업데이트 최종 정리!
(사실 QT가 문제가 있는 건 아니다 ㅋㅋ)

기존의 cmake 의 include_directories() 방법 처럼 include를 포함시켜서 하지 않는 이유는   
include_directories는 -I flag를 사용하는 것 처럼 인쿠르드 디렉토리가 채워지는 것인데  
header file들을 executable 하게 지정을 해준 다음에   
그 실행 가능하게 지정된 include 디렉토리만 -I flag로 지정할 수 있게 하는게 추천 방법인 듯 하다   

그래서 위의 hpp, h 파일들을 set 으로 변수 지정한 다음에 add_executable()에 넣어준다  
단, 여기에서는 qt의 함수(?) qt_add_executable() 를 사용한다   

```c
set(HPP_FILES include/classA.hpp)

qt_add_executable(appmy_pkg
    src/main.cpp
    src/classA.cpp
    ${HPP_FILES}
)
```

여기 까지 해주면 빌드가 문제 없이 되지만, cpp파일에서 include 할 때 include 경로까지 포함해야지 파일을 정확히 찾는다.  
`#include "include/classA.hpp"`   

하지만 위에서 말한대로 executable()로 가능한 include로 지정이 된 후에 사용하면   
target_include_directories()를 추가하고 사용하면
```c
set(HPP_FILES include/classA.hpp)

qt_add_executable(appmy_pkg
    src/main.cpp
    src/classA.cpp
    ${HPP_FILES}
)

target_include_directories(appmy_pkg PUBLIC include)
```

이렇게 해서 빌드를 하게 되면 include 디렉토리를 잘 찾아가므로   
cpp파일에서 include 할 경우에 실제 경로인 include를 빼도 헤더파일을 잘 찾는다  
classA.cpp, main.cpp 에서 헤더파일을 인쿠르드 하면 (실제 include 경로는 빼도 잘 인식한다, 물론 해도 됨)   
```c
#include "classA.hpp"
또는 
#include "include/classA.hpp"
```

> target_include_directories()를 마지막으로 추가해주면 cpp파일에서 "include/..." 경로로 적을 수도,   
생략할 수도 있다는 점이 차이점 중 하나이고,   
target_include_directories()를 할 때에는 executable(), 즉 qt_add_executable()로 헤더파일이 지정이 되어야 한다   

