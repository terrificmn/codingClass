# include 포함 시키기 
cmake, caktin, qt를 사용할 때 공통적으로 CMakeLists.txt 파일을 이용하는데  
이게... 참 include에 있는 헤더 파일을 인식시키는데 참;; 그렇다;


## 파일들
```
my_pkg/
├── include/
│   └── classA.hpp
└── src/
    ├── classA.cpp
    └── main.cpp
```

요런 구성이라고 했을 경우 

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
분명히 방법이 있는데 지금 확실하게는 못 찾음  

파일 디렉토리는 구조는 처음의 상태와 같다. (이 부분도 아래에서 추가로 다룸)

일단 위에서 나온 방법으로 하면 제대로 헤더파일을 못찾아준다.. 그게 문제  

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

이렇게 하면 빌드가 잘 되고 클래스를 사용하는데 전혀 문제가 없다   

하지만, include 디렉토리만 인식시키려고 하면 꽤 어려움(?) 있다.  
먼저 처음에 qt6의 파일 구조는 src, include 이런식이 아니고 (ROS는 아예 구조가 처음부터 그러하다)   
그냥 프로젝트 root아래에 main.cpp가 있는 구조   

업데이트 하기!
