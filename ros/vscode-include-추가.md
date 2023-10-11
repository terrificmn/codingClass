# .vscode 에 include 관련 파일 추가하기
include 의 헤더 파일을 잘 인식하지 못하고, CMakeLists.txt 말고(빌드와는 관계 없음)   

참고로 빌드는 
```c
include_directories(
    include
    ${catkin_INCLUDE_DIRS}
)
```

부분에 include를 포함시켜준다.  

빌드와는 관계 없이 헤더파일 관련해서 intelligence가 잘 작동하지 않을 경우, 지렁이 표시될 때..  

해당 패키지를 열어서 .vscode 디렉토리를 열어준다. (vscode로 열면 됨;)   

c_cpp_properties.json 파일에   
```json
"includePath": [
                "/home/username/catkin_ws/devel/include/**",
                "/home/username/other_ws/devel/include/**",
                "/opt/ros/noetic/include/**",
                "${workspaceFolder}/include"
            ],
```
위의 형식에 맞춰서 넣어주면 된다. 그러면 include 의 헤더파일을 잘 인식해준다.

> ROS 패키지 특성상 include 디렉토리 이하에 다시 프로젝트 명으로 되어 있어서 바로 인식이 안될 수가 있으므로..   
예) myPackage/inlcude/myPackage/myClass.h  이런식으로 구성이 되어 있음..

그래도 잘 인식이 안 될 경우에는 .vscode의 c_cpp_properties.json 파일을 지운 후에 vscode를 다시 실행해주면 인식이 될 수 있음

