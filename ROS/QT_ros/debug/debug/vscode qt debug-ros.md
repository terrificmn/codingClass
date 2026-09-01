먼저 ros 확장팩을 설치 한후 

왼쪽의 RUN AND DEBUG:  메뉴가 있는데 눌러서   
create a launch.json file 을 눌러 만들어 준다 

ROS 이렇게 눌러줬던 거 같은데;;  어쨋든 

```
{
    // Use IntelliSense to learn about possible attributes.
    // Hover to view descriptions of existing attributes.
    // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
    "version": "0.2.0",
    "configurations": []
}
```

이런 json 파일이 만들어지고  
왼쪽 하단에 보면 Add Configuration 이라는 버튼이 생기는데  
눌러주면 여기에서 ROS: attach 를 선택해주면 자동으로 완성 시켜준다   

이제 터미널에서 rosrun 을 실행해서 attach 하고 싶은 ROS 노드를 실행을 하면   

디버그 화면에서 초록색 세모 버튼을 눌러주면 C++을 선택해주면
command pallete 검색창이 나오는데 rosrun으로 실행하는 노드명을 검색해주면 나오는 것을 클릭해주면  
자동으로 디버거가 프로그램에 실행되서 사용할 수 있다



## 다음은 qt_creator 디버깅 정리하기
중요한 것은 CMAKE_PREFIX_PATH 이고   
이 부분은 catkin_ws/src 에서 catkin_init_workspace 를 꼭 해줘야하고   
그 다음에 .bashrc 파일에 잘 넣어주면   
ws가 많이 있더라고 차곡차곡 $CMAKE_PREFIX_PATH 환경 변수에 생긴다   

> 중요한 것은 catkin_init_workspace를 한 후 catkin build를 해준 다음에   
.bashrc 파일에 해당 ws의 devel/setup.bash를 export 해준다   

그 다음에 중요한 것은 LD_LIBRARY_PATH 인데, lib의 경로를 가지고 있다.  
위의 절차를 잘 했다면 이상없이 잘 나올 것임


qtcreator를 실행을 한 후에   
Projects 탭에서 Build & Run 부분에 해당 Desktop 을 클릭해서 Build Settings 할 수가 있는데   
(Build)부분을 클릭한다  

Build Steps 부분에서   
CMake Arguments: 에  
```
-DFORCE_DEBUG_BUILD=True
```
로 입력해준다   

그 외에 등이 있는데 (아직 사용 안해봄)
```
-DCMAKE_BUILD_TYPE:=Debug
-DCMAKE_BUILD_TYPE:=Release
```

그리고 화면의 아래쪽을 보면 Build Environment 가 있는데   
CMAKE_PREFIX_PATH, LD_LIBRARY_PATH... 등의 환경 변수도 확인할 수가 있음


이번에는 Run  을 클릭하고 (Build & Run 탭에서 (왼쪽화면) 선택된 Desktop 에 있음 )

여기에서는 executable 에 rosrun 을 넣어주고   
Command line arguments에 패키지명 노드명 을 넣어주고   
Run in terminal 을 체크를 해주고, 세모 녹색버튼(디버깅) 을 클릭해서 빌드를 하면   
디버깅 모드가 시작된다   

### 터미널을 terminator 사용,,,  안되는 경우
Run in terminal 에 체크를 하고 실행을 하는데 안되는 경우에는   
터미네이터에서 환경설정을 들어가서 (마우스 오른쪽)  

Global 탭의 Behavior 부분의 DBus server가 기본 체크되어 있는데 체크를 해제해준다  

이제 모든 터미널을 종료하고 다시 실행을 하게 되면 잘 실행이 된다!




