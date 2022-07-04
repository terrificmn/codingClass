cakin build --help를 통해서 알아보자   

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


## vscode에 debug 
특정 패키지를 열면 .vscode 숨김 디렉토리가 있는데 여기에서 launch.json 파일을 열어서 보면  
(또는 톱니바퀴 아이콘)    
그 중에 program 변수가 있는데 이를 디버거를 통해서 볼려고 하는 경로 및 파일명(노드)를 입력해준다

예
```json
생략..
..
"request": "attach",
            "program": "/home/sgtubunamr/catkin_fund_ws/devel/lib/cartographer_ros/cartographer_node",
            "processId": "${command:pickProcess}",
```

먼저 노드를 실행해준다 cartographer의 예제 bag파일을 열어서 실행  


이제 왼쪽 탭에서 디버거 화면을 눌러서 Run and Debug를 눌러서  
상단의 (gdb) Attach 를 선택해준다   

그러면 실행버튼 또는 F5를 눌러준다   
Attach to process 에서 cartographer 노드를 찾아준다음에 클릭해주면 된다



stackoverflow 답변

RelWithDebInfo is the same as Release, allowing you to have symbol files for debugging.

For example in Visual Studio, you'll have .pdb files and without them, it'll be hard to debug because all the signatures in the binary files are not going to be human readable and there's no way to map them to the source code.

MinSizeRel is the same as Release, with its optimization configuration just set to Minimize Size instead of Maximize Speed as illustrated in this link in Visual Studio, for example.

    If I want to generate a production build, should I choose Release?

Yes, that should do the right job for you. Debug/Release are the most commonly used options.

Reading this CMAKE FAQ will actually help you a lot.


