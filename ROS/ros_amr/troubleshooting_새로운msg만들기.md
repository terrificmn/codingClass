Errors     << md:make /home/r1d2/catkin_ws/logs/md/build.make.010.log          
/home/r1d2/catkin_ws/src/md/src/main.cpp:10:10: fatal error: md/vel_msg.h: No such file or directory
 #include "md/vel_msg.h"
          ^~~~~~~~~~~~~~
compilation terminated.

파일이 있는데 에러가 발생;

md 패키지 안에 있는 msg가 빌드가 완료가 되지 못해서 에러가 발생  


그래서 외부로 msg를 빼내서 패키지를 만든다  
customs_msgs 패키지로 만든다면  

catkin_create_pkg customs_msgs

그리고 msg 디렉토리를 복사 시키거나 만들어준다 

customs_msgs의 root 디렉토리 안에 msg 디렉토리를 만들고 그 안에 vel.msg 파일을 넣어준다  

그리고 CMakelists.txt 파일은 아래처럼  
```
find_package(catkin REQUIRED COMPONENTS
    message_generation
)

add_message_files(
    FILES
    vel.msg
)

generate_messages(
    DEPENDENCIES
    customs_msgs
)


```
를 추가해준다 

여기에서 generate_messages() 부분을 해주면 include에 헤더파일로 만들어준다 (generate_messages를 생략하면 안 만들어짐)  
devel/include 에 customs_msgs.h 파일이 만들어 진다 

이렇게 해서 빌드를 하면 커스텀 메세지가 패키지가 만들어 짐  

이제 위의 customs_msgs.h 파일을 사용하려고 하는 메인 패키지의 include 디렉토리에 customs_msgs.h 파일을 복사해준다  

> 복사를 안해도 의존성 추가해주면 잘 되는 것 확인. 테스트 완료



그리고 메인 패키지에서 할 일은  
CMakelists.txt 파일에서   
customs_msgs 패키지를 find_package(catkin REQUIRED COMPONENTS) 넣어줘야 한다

```
find_package(catkin REQUIRED COMPONENTS
    roscpp
    customs_msgs
)

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES main_package
    CATKIN_DEPENDS roscpp customs_msgs

)
```

이제 의존성을 추가해줬으니 package.xml 에도 추가해줘야한다   
```
<build_depend>customs_msgs</build_depend>

<exec_depend>customs_msgs</exec_depend>
```
2개 모두 추가해 줘야함

그리고 이제 src/ 의 cpp 파일에서 customs_msgs 메세지는 아래처럼 인쿠르드
```
#include "customs_msgs/vel.msg
```
