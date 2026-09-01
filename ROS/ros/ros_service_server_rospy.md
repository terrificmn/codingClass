# ros service server py rospy
파이썬으로 rospy를 이용해서 서비스 서버를 구성할 수가 있는데   
어찌하다보니 cpp로 안하고 서버만 파이썬으로 해보았다, 그런 김에 정리!

워낙 튜토리얼이 많아서 참고할 거리는 많지만, 그리고 파이썬 코드 자체도 꽤 짧아서 참고하는데는 좋다  

하지만...

커스텀 메세제를 인쿠르드 하거나 할 때에는 네이밍 컨벤션을 잘 알아야지 고생을 안할 듯 하다   

일단 서비스 메시지 를 만드는 것은 동일하다 

ros-service 만들기 1/2 편 참고   

srv디렉토리에 파일을 만들고, CMakeLists.txt 에 message_generation, srv 메세지 등을 등록해주는 것 

정리하면.. 결국 ;; 또 쓰네; ㅋㅋ
```c
find_package(catkin REQUIRED COMPONENTS
    rospy std_msgs message_generation
)

add_service_files(
    FILES
    my_srv_file_name.srv
)

generate_messages(
    DEPENDENCIES
    std_msgs  # Or other packages containing msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES py_service
    CATKIN_DEPENDS rospy message_runtime
#  DEPENDS system_lib
)

```

이 정도? catkin_package() 에 message_runtime 을 빼도 되는지는 확실하게 테스트를 못해봄 

어쨋든 package.xml 에도 연동을 해서 message_generation 등을 추가해야한다  
```xml
  <buildtool_depend>catkin</buildtool_depend>
  <build_depend>rospy</build_depend>
  <build_depend>message_generation</build_depend>
  <build_export_depend>rospy</build_export_depend>
  <exec_depend>rospy</exec_depend>
  <exec_depend>message_runtime</exec_depend>
```

cakin_make , catkin build 등을 해준다   


## import 및 
빌드가 잘 되었다면  

srv msg를 사용해야 하는데  

ros 패키지명은 my_service   
srv 파일 자체는 my_srv_file_name.srv 이라고 한다면, (이름이 길구먼;;) 

import를 할 때의 네이밍 컨벤션이 좀 헤깔리게 되어 있다. 

먼저 srv파일은 **패키지명.srv** 로 불러오게 되고,   
실제 import를 해서 클래스 처럼 사용할 부분에서는 **srv 파일명**을 적어주게 된다   

> 아마도 .srv 라고 해서 실제 .srv 파일이 있어서 헤깔리게 되는 것 같다.   

파이썬을 잘 이해한다면 쉽겠지만, 내 나름대로 이해한 방식은 이렇다  

먼저 from으로 패키지를 가져오는 것이 되고, 그게 my_service 패키지야~ 이런 의미에 거기의 srv를 사용하겠어   
이 정도 되는 듯 하다   

그리고 실제로 srv 메세지 타입을 인스턴스화 하듯이 사용해야하니깐 import 에서는 실제 파일명을 적어주게 된다   

> 패키지 >>> srv 파일 순으로 import 하게 되는 듯 하다. 이렇게 생각하면 쉬운 듯 하다 

```py
from my_service.srv import my_srv_file_name
```

결국 괜히 .srv 가 들어서 파일명과 다른데? 하고 생각하면 괜히 혼자 삽질을 하는 것 같다 ㅠㅠ  
하지만 큰 그림으로 생각을 해보면 결국은 cpp와 다르지 않다   
cpp에서는 `my_service::my_srv_file_name` 이렇게 사용하니깐 말이다 

이제 my_srv_file_name을 변수에 할당 시키고 콜백 함수처럼 등록을 해준다음에 사용을 한다 

srv 파일의 msg 예
```
int64 test_number
---
bool result
string info_msg
```


```py
def serviceCb(req): # req 키워드는 아니고 파라미터
    resp = my_srv_file_name()
    if(req.test_number == 100) :
        print("ok")
        resp.result = True
        resp.info_msg = "Ok"
    else :
        resp.result = False
        resp.info_msg = "not ok"
    
    # 리턴할 때에 resp 만 리턴하면 클라인트에서 응답을 받을 때 에러가 발생
    # resp 자체로 리턴이 안되는 이유는 아직 잘 모름
    return response.result, response.info_msg  


def mainFunction():
    rospy.init_node("service server node")
    serv = rospy.Service("srv_topic", my_srv_file_name, serviceCb)
    rospy.spin()

if __name__ == "__main__" :
    mainFunction()
```

대충 이렇게 된다. 

