# debug 
cakin build --help를 통해서 알아보자   

> catkin tools가 필요함

이 중에서 cmake-args ARG를 사용
```
--cmake-args ARG [ARG ...]
Arbitrary arguments which are passed to CMake. It
collects all of following arguments until a "--" is
read.
```

빌드 타입  
1. Release: high optimization level, no debug info, code or asserts.  
실행 속도를 위해서 높은 최적화, 디버깅 정보가 없다. 최종적 SW Release를 위해서 사용    
2. Debug: No optimization, asserts enabled, [custom debug (output) code enabled],  
   debug info included in executable (so you can step through the code with a  
   debugger and have address to source-file:line-number translation).  
   최적화를 사용하지 않음, debug 정보를 기록
3. RelWithDebInfo: optimized, *with* debug info, but no debug (output) code or asserts.  
Debug 도 가능하면서 Release에 가까운 성능으로 최적화
4. MinSizeRel: same as Release but optimizing for size rather than speed.  



아규먼트를 넣어서 빌드를 할 수 가 있다  
```
catkin build --cmake-args -DCMAKE_BUILD_TYPE=RelWithDebInfo
```

> RelWithDebInfo는 디버깅이 가능한 바이너리를 만들어준다  

[여기참고하기 https://junstar92.tistory.com/217](https://junstar92.tistory.com/217)



## vscode debug configure c++
일반 c++ 프로그램 디버깅   

vscode에서 debuging을 하려고 하면  cpp 관련 디버깅을 하려고 하면  
Run and Debug 탭에서 상단의 리스트 콤보(?) Add Configuration... 를 클릭하면  
자동으로 launch.json 파일이 열리면서, 리스트를 추가할 수 선택 창이 뜨는데 여기에서 launch 또는 attach를 선택해 준다

C/C++ (gdb) launch   
C/C++ (gdb) attach   
(Pipe launch/attach 도 있는데.. 잘 모름)   

이렇게 선택을 해주게되면 자동으로 필요한 요소들이 추가가 된다   
또는  
configuration의 value를 bracket를 클릭하면 항목이 나오는데 gdb launch 또는 gbd attach를 선택해준다   

이 중에서 키, 벨류를 몇개를 수정한다면   
- "name" 은 콤보 리스트에서 선택할 수 있는 이름이 된다 (딱 알아 볼 수 있는 이름으로 해준다)   
- "request" 은 일단 launch 또는 attach
- "program" 은 실행 파일 주소  

> 자동으로 완성 되므로 바꿔줘야할 것은 제한적이다   

이제 이 중에서 *"program":* 의 value는 꼭 지정을 해줘야하는데, full path를 입력해준다   
예를 들어
```json
"configuration": [
    {
    "name": "c++ my socket test",
    "type": "cppdbg",
    "request": "launch",
    "program": "${workspaceFolder}/socket/c++_socket/socket_web/build/socket_web",
    ...생략
}]
```
여기서 프로그램은 실행파일을 의미, 컴파일이 된 실행 가능한 파일을 지정해 준다  


### 디버깅 시작
- launch 의 경우   
json파일에서 *name* value로 등록한 것이 콤보리스트에 뜨는데, 이를 선택하고   
상단의 재생버튼(녹색 삼각형)을 누르면 해당 프로그램이 시작되게 된다    

- attach 의 경우   
마찬가지로 등록된 콤보 리스트에서 (왼쪽 상단) 를 선택하고 초록색 삼각형(start버튼) 을 눌러주면   
Process를 선택하는 창이 나오는데, 자신의 프로그램을 검색하면 c++ 실행 프로세스가 나오는데 이를 선택해주면   
디버깅이 프로세스에 붙게 된다

> start 버튼은 F5를 누르면 된다



## vscode에 debug ROS
ROS C++ 패키지 디버깅 경우   

ros catkin package를 vscode로 열어준 다음에   

Run and Debug 탭을 선택해주고 상단의 콤보리스트를 눌러서 add configuration...  을 선택해준다   

여기에서 ROS: Launch 와 ROS: Attach 가 있는데 둘 중 하나를 선택한다.  

> launch는 바로 해당 프로그램을 실행   
attach는 프로그램을 따로 rosrun, roslaunch로 실행한 후에 추후 debug를 붙이는 방법  

또는 이미 launch.json 파일이 만들어져 있다면   
특정 패키지를 열면 .vscode 숨김 디렉토리가 있는데 여기에서 launch.json 파일을 열어서 보면   
그 중에 program 변수가 있는데 이를 디버거를 통해서 볼려고 하는 경로 및 파일명(노드)를 입력해준다

여기에서 중요한 것은 *"program"* 키의 해당하는 value를 지정해주는 것인데, 프로그램의 패스를 지정해준다

> ROS 같은 경우는 워크스페이스에/devel/lib/패키지명/실행노드  요렇게 있다

예
```json
생략..
..
"request": "attach",
            "program": "/home/sgtubunamr/catkin_ws/devel/lib/cartographer_ros/cartographer_node",
            "processId": "${command:pickProcess}",
```

"request"를 attach로 지정을 했다면   
먼저 노드를 실행해준다 cartographer의 예제 bag파일을 열어서 실행  

이제 왼쪽 탭에서 디버거 화면을 눌러서 Run and Debug를 눌러서  
상단의 (gdb) Attach 를 선택한 다음에 실행버튼(녹색 삼각형) 또는 F5를 눌러준다   
Attach to process 창이 뜨면서 검색을 하게 되어 있는데 cartographer 노드 (자신의 실행된 노드)를 찾아준다음에 클릭해주면 된다   


stackoverflow 답변

RelWithDebInfo is the same as Release, allowing you to have symbol files for debugging.

For example in Visual Studio, you'll have .pdb files and without them, it'll be hard to debug because all the signatures in the binary files are not going to be human readable and there's no way to map them to the source code.

MinSizeRel is the same as Release, with its optimization configuration just set to Minimize Size instead of Maximize Speed as illustrated in this link in Visual Studio, for example.

    If I want to generate a production build, should I choose Release?

Yes, that should do the right job for you. Debug/Release are the most commonly used options.
