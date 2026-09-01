# ROS 패키지 만들기 - 2

## 패키지(yh_tutorial) 의 CMakeLists 파일 수정하기

패키지의 CMakeLists.txt 파일을 보면
이것도 편한 에디터로 보자 

패키지 상위로 디렉토리를 변경하자
```
$ cd ..
# 또는 
$ cd ~/catkin_ws/src/yh_tutorial
```

아래 내용을 찾아준다

```
find_package(catkin REQUIRED COMPONENTS
  message_generation
  roscpp
  std_msgs
)
```
위의 내용은 처음에 패키지를 만들 때 catkin_create_pkg 를 할 때 적어준
의존성 패키지들이 들어가 있는데, 이를 통해 빌드를 하면 필요한 패키지를 먼저 찾게 된다

그 다음으로 아래 내용을 찿는다. msg 관련 내용이다
```
## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msgoscpp_generate_messages_eus
```

위의 코드를 아래처럼 바꿔준다. 필요한 파일은 yh_msg_tutorial.msg 이므로 이것만 적어주면 된다

```
 add_message_files(
   FILES
   yh_msg_tutorial.msg
 )
```

그 다음은 아래 부분을 찾아보자~ 마찬가지로 주석을 풀어준다음에 파일 이름을 바꿔준다
```
## Generate added messages and services with any dependencies listed here
# generate_messages(
#   DEPENDENCIES
#   std_msgs
# )
```

위의 주석 처리가 되어 있는 부분은 주석만 풀어주면 된다
```
  generate_messages(
    DEPENDENCIES
    std_msgs
  )
```

그리고 다음은.. catkin_package의 라이브러리와 (패키지명) 과 의존성 관련 패키지를 적어준다 (이 또한 역시 처음에 만들 때 적어뒀던 의존성패키지임)

```
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES yh_tutorial
#  CATKIN_DEPENDS message_generation roscpp std_msgs
#  DEPENDS system_lib
)
```

다른 주석은 남겨두고 라이브러리 (패키지) 부분만 주석을 풀어준다
```
catkin_package(
  LIBRARIES yh_tutorial
  CATKIN_DEPENDS roscpp std_msgs
```
그리고 message_generation은 이미 사용이 되기 때문에 불필요하므로 지워준다.


여기 까지는 빌드 하기 전에 필요한 패키지나 이름 등을 정해주는 설정에 가까운 부분이 었고 
이제 부터는 빌드를 하기 위해서 실행되는 코드라고 한다


build 빌드 부분 이후에 아래 코드를 찾는다

```
# add_executable(${PROJECT_NAME}_node src/yh_tutorial_node.cpp)
```
주석을 해제하고 실행 가능하게 추가해주는 것인데 
########
일단 기본적으로 프로젝트 이름만 알기 때문에 PROJECT_NAME 이후에는 자동으로 생성이 된 것이므로 
이름을 맞게 다시 바꿔준다. publisher와 subscribe가 2개를 만들었으므로 2개를 추가해준다
```
add_executable(pub_test src/pub_test.cpp)
add_executable(sub_test src/sub_test.cpp)
```

그리고 아래에 있는 부분을 또 바꿔준다
```
# add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
```

${PROJECT_NAME}_node 부분을 node 파일이름으로 바꿔준다 (pub_test.cpp/ sub_test.cpp 파일명이 node명 이다)
```
add_dependencies(pub_test ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(sub_test ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
```

이번에는 또 아래를 찾는다... 아고
```
## Specify libraries to link a library or executable target against
# target_link_libraries(${PROJECT_NAME}_node
#   ${catkin_LIBRARIES}
# )
```

이번에는 라이브러리 링크를 수정해준다 ${PROJECT_NAME}_node 부분을 노드 파일 이름으로 수정해준다

주석을 풀고 아래처럼 바꾸면 된다
```
target_link_libraries(pub_test
   ${catkin_LIBRARIES}
)

target_link_libraries(sub_test
   ${catkin_LIBRARIES}
)
```

<br>

# 실행하기

먼저 다시 빌드를 해줘야한다
```
$ cd ~/catkin_ws
$ catkin_make
```
> 팁  빌드과정에서   
[ 00%] 가 나오기 전에 즉, 퍼센트로 빌드가 되는 과정이 아직 안 나오는 상태에서 에러가 설정 부분에서 에러가 발생할 가능성이 크다    
[ 00%] 나온 후, 즉, 빌드가 되면서 에러가 발생했으므로 코드의 문법 에러 발생 등이 발생했을 가능성이 크다

<br>


첫번째 터미널에서 
```
source devel/setup.bash 
```
을 해 준후에

```
$ rospack profile 
```
을 해준다


master를 켜준다
```
$ roscore
```

<img src=0>
<br>

그리고 다른 터미널을 연 후에 

노드를 실행해준다 
publish를 실행 해 준다
rosrun [패키지이름] [노드이름] 순으로 실행을 해주면 된다

```
$ rosrun yh_toturial pub_test
```
그러면 출력이 되는데 subcribe 에는 상관이 없이 계속 출력이 되면서 발행을 하게 된다
```
[ INFO] [1623126939.237065305]: send msg = 236924393
[ INFO] [1623126939.237098127]: send msg = 2300
```


이제 
서브스크라이브를 켤 차례

다른 터미널을 열어 준 후에 rosrun으로 열어 준다 
마찬가지로 [패키지명] [노드이름] 식으로 실행을 해준다. 대신 이번에는 sub_test 로 열어준다
```
$ rosrun yh_tutorial sub_test
```
그러면 sub_test 가 실행이 되면서 subscribe가 실행이 되면서 
publisher가 보낸 내용을 받아서 출력을 하게 된다

```
[ INFO] [1623126939.237612144]: received msg = 236924393
[ INFO] [1623126939.237647490]: received msg = 2300
```

<img src=1>
<br>


이 때 roscore가 실행되고 있는 것을 꺼도 (master가 꺼진다) 두 개의 노드는 이상없이 통신을 계속 한다

