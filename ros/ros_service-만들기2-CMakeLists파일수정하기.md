# service 통신 만들기 튜토리얼 2
이전 과정이 궁금하다면 아래 링크를 확인해주세요

[ROS topic 통신 튜토리얼 보러가기](/tag/catkin_create_pkg)

[ROS topics, services and actions 알아보기](http://54.180.113.157/blog/ROS-topics-services-and-actions-%EC%97%90-%EB%8C%80%ED%95%B4%EC%84%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90)


🤖   
이제 service 만들기의 패키지가 만들어졌다면  
package.xml 파일을 열어서 
간단하게 description이나 maintainer의 이름, 이메일 주소 등을 수정해보자  
필요시 author email 도 등록

튜토리얼에서는 사실 별거 아니여서 정확히 넣어줄 필요는 없겠지만(?),

> package.xml 파일이 있는 이유는   
오픈소스이기 때문에 메인테이너등을 입력해줘서 오픈소스라는 생태계에 기여를 할 수 있게 되는 것 같다  
예를 프로젝트를 만들었다면 maintainer 등을 입력을 해서 피드백을 받을 수도 있고, 
또 author email 같은 부분은 혼자 프로젝트를 할 수 없기 때문에
공동 작업한 사람들의 이메일 주소를 넣어 주는 것이라고 한다

아직은 잘 모르겠지만 뭐 그렇다 ㅋㅋㅋ

<br>

## 빌드전에 CMakeLists.txt 파일 수정하기 
topic 통신을 할 때와 패키지의 CMakeLists.txt를 수정하는 것은 거의 비슷하다

먼저 yh_tuto_service의 CMakeLists.txt를 열어 준다. 편한 에디터로 열어주자
그리고 나서 아래 내용을 확인한다 (경로는 ~/catkin_ws/src/yh_tuto_service 가 된다)

msg 즉, topic을 했을 때랑은 다르게 
이번에는 service 부분을 찾아준다

윗 부분의 주석을 풀고 내용을 srv 디렉토리에 만든 yh_srv.srv 파일을 넣어준다
.srv 파일을 넣어준다
```
add_service_files(
  FILES
  yh_srv.srv
)
```

generate_messages 부분을 찾아서 주석이 되어 있는 것을 풀어준다
```
generate_messages(
  DEPENDENCIES
  std_msgs
)
```

catkin_package의 LIBRARIES, CATKIN_DEPENDS 주석을 풀고 message_generation 지워준다

아래처럼 된다
```
catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES yh_tuto_service
  CATKIN_DEPENDS roscpp std_msgs
#  DEPENDS system_lib
)
```

요렇게 생긴 놈 아래 부분을 작업할 차례
```
###########
## Build ##
###########
```
빌드 부분 이후를 찾아서 바꿔준다

```
# add_executable(${PROJECT_NAME}_node src/yh_tuto_service_node.cpp)
```
를 찾아서 노드이름을 을 지정해준다. 

${PROJECT_NAME}_node 부분을 노드 이름을 써주고 이하는 파일.cpp로 적어준다
아래처럼
```
add_executable(srv_server src/srv_server.cpp)
add_executable(srv_client src/srv_client.cpp)
```

그리고
```
add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
```
도 찾아서 ${PROJECT_NAME} 부분에 서비스 서버와 클라이언트 이름을 넣어준다
아래처럼 바꿈
```
add_dependencies(srv_server ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
add_dependencies(srv_client ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
```

이제 마지막으로 target_link_libraries 부분의 서비스 이름을 바꿔준다
```
target_link_libraries(srv_server
  ${catkin_LIBRARIES}
)
target_link_libraries(srv_client
  ${catkin_LIBRARIES}
)

```

<br>

# 이제 빌드를 한 후에 실행을 해보자~
빌드를 할 때 주의점은 위의 서버나 클라이언트 이름이 겹치면 안 된다는 것에 주의하자

```
$ cd ~/catkin_ws
```
로 이동을 한 후에 catkin_make를 실행하자

```
$ catkin_make
```

> 빌드가 에러가 발생했다면.. 어쩔 수 없게도 ㅠ 디버깅을 해보자~    
(다 맞는 건 아니지만.. 교수님께 알려주신 팁!)  
빌드를 시작하고 %가 올라가지다가 에러가 발생했으면 문법, 또는 cpp상에서 잘못했을 경우가 높아짐을 참고하자  
아예 퍼센트가 시작도 안 된 상태라면 CMakeLists.txt 파일에서 경로, 파일명 등을 다시 한번 살펴보자  

<br>

## 이제 실행을 해 볼 차례

빌드가 무사히 잘 되었다면!😛 

터미널에 roscore, rosrun 등으로 명령어를 입력해야하는데

추천1은 터미널 분활이 잘 되는 terminator라는 터미널 프로그램을 사용하는 것이다.
화면을 분힐해서 쓸 수 있어서 매우 유용한 방법이다.

[terminator 설치 및 간단한 사용법 보러가기](/blog/terminator-설치하기-터미널-설치-화면-분할-하기)

<br>

그것도 아니면 ㅋㅋ vscode를 사용하는 방법이다.  
(솔직히 이 방법, 저 방법 다 써보는 것을 추천😎 ㅋㅋㅋ )  

vscode를 열어서 오픈 폴더를 해서 현재 yh_tuto_service 를 통채로 열어주자

혹시 만약 터미널이 친숙하다면 ㅋㅋ 
```
$ cd ~/catkin_ws/src/yh_tuto_service
$ code .
```
이렇게 하면 현재의 디렉토리를 기준으로 vscode가 실행되게 된다. 매우편리👍👍 ㅋㅋ 

<br>

## 이제 vscode 메뉴를 이용해서 터미널을 열어보자~   
터미널 메뉴에서 새 터미널을 선택

<img src=0>


터미널이 열리면 차례차례
```
$ rospack profile 
$ roscore
```
차례차례 입력을 해주면 된다.

<img src=1>

이제 roscore 를 해서 마스터가 열렸고  (계속 실행이 되고 있는 상태임)

이제 새로운 터미널을 열어서 이제는 서버와 클라이언트 노드를 실행해줄 차례이다  
아래 처럼 터미널의 아래의 오른쪽 부분의 **+** 버튼을 눌러 주면 된다

<img src=2>


이제 새로운 터미널이 열렸는데 이제는 +버튼 바로 옆의 아이콘을 클릭해서 터미널을 2개로 분할을 해주자

<img src=3>


이제 한쪽에는 
```
$ rosrun yh_tuto_service srv_rver 
```
또 다른 한쪽에는 클라이언트를 실행하는데 숫자 2개의 파라미터를 넘겨준다
```
$ rosrun yh_tuto_service srv_client 10 20
```

<img src=4>

먼저 왼쪽 터미널의 서버 노드를 먼저 실행을 해준다. 
```
ready srv server!!
```
라고 나오면 바로 오른쪽 터미널의 클라이언트 노드를 실행을 시켜주면 된다

그러면 아래와 같이 클라이언트에서 10 20으로 서버에 요청을 하면 
30이란 값을 넘겨주는 Service 통신이 되게 된다

<img src=5>

<br>

끝!