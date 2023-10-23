# vscode c_cpp_properties.json 설정
cpp 파일을 만들면 현재의 디렉토리에 .vscode 디렉토리가 생기는데 

헤더파일을 잘 못 찾는 경우에는 .vscode 내의 `c_cpp_properties.json` 파일을 삭제한 후에  
다시 vscode를 열어주면 잘 인식을 하는 편이고   

## include 패스 
그래도 헤더파일을 잘 인식이 안되면   
json안의 includePath 부분에 해당 패키지의 (ros의 경우) include 패스를 지정해준다.  
```json
// ...생략
"includePath": [
        "/home/myuser/catkin_ws/devel/include/**",
        "/opt/ros/noetic/include/**",
        "/home/myuser/catkin_ws/src/my_pkg/include/**",
        "/usr/include/**"
      ],
```

> 여기에서 include 이하 **은 reclusive의 의미, 해당 이하의 디렉토리를 게속 찾아준다.   


## src 디렉토리에 header 파일이 있는 경우
include 디렉토리에 넣지 않는 경우에는 vscode에서 잘 인식이 안된다.   
물론 현재 src 디렉토리에 같은 경로에 있으면 예를 들어 src/my_cpp.cpp , my_cpp.h 파일이 있다면,  

include를 할 때 `#include "my_cpp.h"` 만 해도 잘 되지만   
만약 src 이하에 이하 디렉토리로 되어 있거나, 또는 다른 경로에 있을 경우에는   
`src/new_part/my_cpp1.h` 이런식이라면 인쿠르드 해서 빌드하는 것에는 크게 문제가 되지는 않는다.   

하지만, vscode에서 잘 인식이 안되서 자동완성 이라던가, 함수간 이동이 굉장히 불편해진다;;;;;

어쨋든 그럴때에는 위의 json includePath 부분에   
```json
// ... 생략
"includePath": [
    //...생략
    "${workspaceFolder}/**",
]
```

위에 처럼 해주면 src/ 경로에 들어있어서 (include 디렉토리에 들어 있지 않아도)   
vscode에서 잘 찾아줘서 빨강 지렁이 없고 ㅋㅋ, 함수 및 자동완성 잘 되게 된다. 