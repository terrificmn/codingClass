qtcreator에서 ros 패키지를 열때 

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


