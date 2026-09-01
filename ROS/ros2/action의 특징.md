action의 특징
action client는 action server가 response를 보내기 전까지 계속해서 기다리지 않고, 다른일을 할 수 있다   
action client는 request를 보낸 뒤에도 지속적으로 feedback을 받을 수 있다   
피드백을 받고 있다가, 뭔가 잘못되었을 (감지가 되었을 때) 때에는 cancel이 가능   

하지만 여러 request를 동시에 작업하는 것은 본질적으로 불가능하다고 한다. 
즉 service 처럼 순차적으로 실행이 되게 된다   
이것을 프로그래밍적으로 해결이 가능하는데 MultithreadedExecutor가 사용된다고 한다   

네비게이션과 비슷하다
목적지 request를 하고 경로검색을 마치면 안내를 시작
운전 중간 계속해서 피드백을 줌
목적지에 도착했다면 경로 안내를 종료, 다음 request를 기다리게 된다

> 실제 ROS2 Nav2 에서 action를 적극 사용하고 있다
자율주행에서는 꼭 필요한 기능이며, Nav2 에서는 action을 사용하기 위한 헤더파일인  
rclcpp_action.hpp 파일을 include를 하고 있는 것을 알 수 있다


서비스에서 request, response가 있었다면  
action에서는 Goal(Request), Feedback, Result가 있다고 볼 수 있다

데이터 타입은 .action을 사용(파일명)
```
# Goal
int32 order
---
# Result
int32[] sequence
---
# Feedback
int32[] partial_sequence
```

> 벡터 (파이썬의 리스트와 비슷한) 자료형을 사용
마찬가지로 custom action 파일도 만들 수 있다


## 터미널에서 action 커맨드

```
ros2 action list
```

action명을 넣어서 info로 볼 수도 있다
```
ros2 action info /fibonacci
```

action타입의 상세 정보 자료형 보기
```
ros2 interface show /custom_interfaces/action/Fibonacci
```

goal request를 커맨드로 하기
ros2 action send_goal action이름 action타입 "{name: value}"
```
ros2 action send_goal fibonacci custom_interfaces/action/Fibonacci "{order: 5}"
```

feedback 여부를 옵션으로 넣어주기
```
ros2 action send_goal --feedback fibonacci custom_interfaces/action/Fibonacci "{order: 5}"
```




먼저 include를 시켜야함
```
#include "rclcpp_action/rclcpp_action.hpp"  
```


rclcpp_action::create_server 만들 때 타입을 다 적어줘야하는데 이 부분의 Fibonacci는 using을 사용해서 
미리 축약으로 만들어서 길게 복잡하지 않고 가독성이 좋게 만들 수 있다

```
using Fibonacci = custom_interfaces::action::Fibonacci;

// 위에서 using을 사용했기에 Fibonacci 만 사용하면 된다
rclcpp_action::create_server<Fibonacci>
```

액션 서버를 만들 때에는 매개변수가 들어가는데 처음에 this가 들어가는 이유는  
rclcpp::Node로 부터 상속받아서 subcriber, publish 등을 사용했지만
액션서버는 다른 곳으로부터 (rclcpp_action.hpp) 받아오기때문에 다른 파라미터들이 많이 필요하게 되고
그래서 처음에는 this 키워드를 사용하게 된다

매개변수에는 callback 함수들을 지정하게 되는데 마지막 handle_accepted는 바로 bind로 묶지 않고 
thread로 멀티트레딩이 될 수 있게 한다



handle_goal에서의 uudi는 개별로 들어오는 request로 생각하면 되나  
이번 예제에서는 사용하지 않는다



handle_accepted 에서는 execute함수와 bind가 되어 있게 된다 그리고 이게 thread로 묶여 있게된다

만약 멀티스레딩을 사용하지 않는다면 처음에 액션서버를 create할 때 마지막 매개변수에서 handle_accepted 부분에서
바로 execute 로 바인드를 해주게 되겠지만 


goal_handle을 다양하게 사용하게 되는데 메소드인 ->is_canceling(), ->canceled(result), ->succeed(result) 등 
->publish_feedback() 많이 사용이 되게 되고 

피보나치 수열을 저장하기 위해서 파이썬에는 리스트를 사용했지만  
cpp에서는 스탠다드 벡터형식을 이용하게 된다

