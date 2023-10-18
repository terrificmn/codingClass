# include error
헤더 파일을 두 번 인쿠루드 하는 경우에 이런 경우가 있을 수 있다.

예를 들어서 각각. ExampleA.h, ExampleB.h 에 각각 파일이름과 같은 클래스가 있다고 할 때   
여기에서 서로 인쿠르드를 헤더파일에서 하고는 하는데  

```cpp
#ifndef EXAMPLE_B_H
#define NEXAMPLE_B_H
#include "ExampleA.h"

class ExampleB : public ExampleA {

};

#endif
```

이런식으로 처리를 하려고 하면 보통 문제가 없이 잘 된다. 
하지만 ExampleA.h 파일 및 클래스 ExampleA 에서도 ExampleB 클래스를 인쿠르드해서 사용을 하려고 하면  

```cpp
#ifndef EXAMPLE_A_H
#define NEXAMPLE_A_H
#include "ExampleB.h"

class ExampleA {
// 생성자
public:
    ExampleA(ExampleB* exampleB_Ptr);
};
#endif
```

대충 서로 인쿠르드 한 셈이 된다. 인쿠르드를 한번만 하게 해주는 ifndef 및 define으로 설정을 했지만  
문제는 cpp 파일에서 header 파일을 불러올 때 문제가 생기는 듯 하다.

> 즉, 각 헤더파일이 a.h, b.h 파일이 되어 있으므로 a.h 파일을 읽으면서 b.h파일을 읽고   
b.h 헤더에 보니 또 a.h 파일이 있고 뭐 이렇게 돌고 도는 ;;;;    
"foo needs bar needs foo needs bar...." 이런 느낌 (foo, bar 클래스)

생각해보면 상속 받고, 그 부모를 포인터로 사용하는 것은 좋은 구조가 아닌 듯 하기도 하다;;;   
어쨋든 두 개의 클래스를 다 제대로 사용하고 싶지만 ㅠㅠ

```
/home/sgtubunamr/catkin_ws/src/alcarto_ros/alcarto/src/service/../node_manager/node_manager.h:19:27: error: expected ‘)’ before ‘*’ token
   19 |     NodeManager(NodeStatus* nodeStatus);
      |                ~          ^


/home/sgtubunamr/catkin_ws/src/alcarto_ros/alcarto/src/service/../node_manager/node_manager.h:37:5: error: ‘NodeStatus’ does not name a type
   37 |     NodeStatus* nodeStatusPtr = nullptr;


/home/sgtubunamr/catkin_ws/src/alcarto_ros/alcarto/src/node_manager/node_manager.h:19:27: error: expected ‘)’ before ‘*’ token
   19 |     NodeManager(NodeStatus* nodeStatus);

```
> 위의 것은 우선 인쿠르드 상대경로 문제도 포함   
> 최대한 한쪽 클래스에서는 cpp 파일에서만 사용할 수 있게 extern 등을 사용하는 방식으로 변경   

약간의 편법(?) 이지만... ExampleA 클래스에서는 ExampleB 클래스를 사용해야하고   
ExampleB 클래스에서는 ExampleA 클래스를 상속 받는다고 치면, 두개의 헤더파일이 각각 필요하다. 

그래서 ExampleB 클래스 ExampleB.h 파일에서 정상적으로 ExampleA.h 를 포함시켜서 상속을 받고   
(실제 ExampleB 클래스의 정의하는 부분에서 상속받는 구문이 필요)

ExampleA 클래스에서 사용할 ExampleB 포인터는 extern으로 생성하여서(ExampleB.h 에서 정의)   
실제 ExampleA 클래스의 헤더파일에서는 정의를 안하게 하는 것 (그래서 include를 안하게 됨)   
(extern으로 선언해서 포인터로 만들면 ExampleA 헤더쪽에서는 정의를 안해도 되므로..)  

물론 ExampleA.cpp 파일쪽에서는 실제 메소드 등에서 ExampleB 포인터를 사용해야하므로   
ExampleA.cpp 파일에 ExampleB.h 헤더를 인쿠르드를 시켜주면 다행히 문제 없이 빌드가 가능했다.

> extern으로 포인터 정의 하는 것을 참고하자

위의 방법으로 다행히 해결은 가능했지만,    
**Forward Declarations** 이라는 것이 있는데, 메인함수에서 다른 함수를 먼저 선언해주는 것을 말하는데   
이를 이용해서 클래스를 미리 선언해서 사용하는 방법으로 진행을 하면 가능하다고 하는데..  
일단 *실패* 했다.. 다시 테스트 해본 후 업데이트 하기!



## include 디렉토리를 사용안 할 경우
include를 사용안하고 src 디렉토리에 cpp 파일과 같이 있는 경우에는  
그냥 `#include "myfile.h";` 이렇게 해주면 되지만   

만약 다른 경로에 있는 파일을 접근하려고 하면 "../other/my_newfile.h" 이런식으로 접근하게 됨  
이것도 해당 파일에서는 잘 되지만 상대 경로이기 때문에 문제가 발생할 수 있다.   

그래서 ros catkin 패키지 같은 경우에는 `"src/my_node/myfile.h"` 이런식으로 넣어주면 도움이 될 수 있다.  
상대 경로로 인쿠르드 하면 아래의 에러와 같이  

```
/home/myuser/catkin_ws/src/my_pkg/src/service/../manager/manager.h:19:27: error: 
```

여기에서 자세히 보면 경로를 ../ 으로 올라가서 처리하는 모습 보인다.

또 include 디렉토리가 아닌 src 디렉토리에서 사용하게 되면 vscode 의 경우 바로 헤더파일을 잘 인식해주지못한다   
그래서 .vscode 에서 파일 경로를 추가해줘야 할 듯 하다.


## 물론 include 디렉토리를 사용하면 
이 방법이 좋아보임 - 헤더파일과 cpp 파일을 분리할 수 있고   
단점은 h파일과 cpp 파일을 왔다리 갔다리 해야할 수 있으나,   

단, 이것도 중복 인쿠르드에서는 좋지 않다. 왜 include guard(?) 기능이 제대로 안되는지는 모르겠다.
