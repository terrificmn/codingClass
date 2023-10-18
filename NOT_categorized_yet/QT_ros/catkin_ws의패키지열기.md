# qtcreator에서 ros 패키지를 열때 

Open project를 해서 특정 패키지의 CMakeLists.txt 파일을 지정해준다  

예) catkin_ws/src/my_test_project/CMakelists.txt

Configure Project가 나오는데  
Kits를 선택을 해주는데  

먼저 Desktop를 선택한 후에  Details를 눌러서 자세히 보기를 한다   

Debug 를 기존의 qt 방식대로 project가 있는 디렉토리에   
예)qt_ws/build-my_test_project-Desktop-Debug

이런식으로 생기는 게 qt 방식인데 이것을 catkin_ws의 build 디렉토리로 바꿔준다  
예)/home/myuser/catkin_ws/build/my_test_project

Release 등은 체크 해제를 해준다  

> catkin_make나 catkin build 없이 build 디렉토리에서 make 명령어로 컴파일을 진행할 수가 있다.  이유는 build디렉토리에 makefile 이 있기 때문


패키지(프로젝트(가 열리면   
왼쪽의 Build Settings를 클릭해서  

CMake 부분을 설정하는데 CMAKE_BUILD_TYPE 부분에 Debug라고 입력한다  

> 아무것도 들어가 있지 않다면 release 모드



## catkin_ws 열기
catkin_ws 를 통채로 열려고 할 때에는 catkin_ws 안의 catkin_ws.workspace 라는 파일을 지정해서 열어주면 된다   

만약 없다면 create 프로젝트를 해서 ROS Workspace 를 열어줘서 catkin_ws 이름으로 만들고  
catkin_ws의 디렉토리 지정해주면 된다. (Build System은 CatkinTools 있을 경우)


## catkin_ws 빌드
catkin_ws 빌드를 할 경우에 특히 cartographer 관련 패키지를 빌드해야할 경우에는   

```
  Building in Debug mode, expect very slow performance.
Call Stack (most recent call first):
  CMakeLists.txt:40 (google_initialize_cartographer_project)
```

Projecs 의 Build & Run 부분에서 Build Steps 를 지정해주는데   
CatkinTools Step 에서  
CMake Arguments: 를 `-DFORCE_DEBUG_BUILD=True` 로 지정해 준다. 

디버깅 빌드로 셋팅해준다. 디버깅을 할 수 있게되지만, 퍼포먼스가 느려진다. 특히 카토그래퍼는 영향이 있음

