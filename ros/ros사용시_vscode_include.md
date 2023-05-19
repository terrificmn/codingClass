# vscode에서 include 
vscode에서 ros 패키지로 c++ 프로그램을 만들다보면 include 경로의 헤더파일을 못 찾는 경우가 있다   

실제 경로는 사실 catkin_ws 안에 `my_new_pkg/include/my_new_pkg/my_header.hpp`   

위 처럼 include 디렉토리가 자신의 패키지안에 있는데, 그 안에 다시 같은 이름으로 된 패키지 디렉토리가 또 있고 그 안에   
header파일이 있게 된다   

보통 c++ 프로그램을 하면 include 디렉토리 안에 바로 헤더파일이 있는 경우가 일단 기본적인 케이스 인 듯 하지만,   
ROS 컨벤션이 원래 이렇게 만들어지므로 참고한다. 

일단 vscode 내에서는 이미 잘 설치가 되어 있는(?) 라이브러리는 자동으로 잘 인식이 되는데   
ROS 패키지는 잘 못 찾을 때가 있는 듯 하다.   


## vscode 에서 includePath에 추가하기

같은 패키지 안에 *.vscode* 디렉토리가 생기는데 이곳의 `c_cpp_properties.json` 파일을 열어서 json 형식으로 추가를 해주자  

```json
// 생략...
"includePath": [
    "/home/user/catkin_ws/devel/include/**",
    "/opt/ros/noetic/include/**",
    
    //// 생략
    
    "/home/user/catkin_ws/src/my_new_pkg/include/**",
    "/usr/include/**"
],
/// 생략
```

이런식으로 마지막에 두 번째 줄에 추가한 것 처럼, 자신의 패키지 경로를 입력해주면 된다   


또는 `#include 헤더파일.hpp` 부분에 에러표시인 지렁이가 표시되면 그곳을 클릭하면 ? 아이콘을 눌러서 진행할 수도 있는데   
이 경우에도 include 패스를 입력하는 부분에 위의 json으로 입력했던 것 처럼 경로를 입력해주면 된다   






> 물론 vscode 설정에서는 패키지 다이렉트의 include 디렉토리 이하 /** 로 포함해서 딱 include/**까지만 해주면 된다

