# ros2 webrtc
ros 버전도 거의 비슷하다.  webrtc_ros가 아닌 webrtc 자체를 따로 설치하려면  
cpp_practice_playground/ repo 참고

워크스페이스는 따로 만들어서 진행하는게 좋다.  
> 아무래도 webrtc는 한번 빌드하면 할 필요가 없고, 게다가 오래걸림




의존성 설치
```
sudo apt install ros-humble-image-transport ros-humble-rosbridge-server ninja-build libgtk-3-dev
```

python 은 따로 obselted 프로그램이어서 python 자체 설치가 안되는 듯 함.   
python은 필요하므로 python-is-python3 로 설치해준다.  
```
sudo apt install python-is-python3
```

> python2는 설치할 필요가 없다.

async-web-server도 빌드를 하거나 쉽게 pre-build 버전으로 설치 가능   
```
sudo apt install ros-humble-async-web-server-cpp
```

original GT-RAIL 의 asycn 패키지에서 ros2 버전(원 리포에도 있기는 함)   
소스 코드가 변경이 필요할 경우에는 클론 후 빌드  
```
git clone https://github.com/fkie/async_web_server_cpp.git -b ros2-develop
```


아래 에러는 libgtk-3-dev 없을 경우 webrtc 를 빌드하다가 에러가 발생하므로 미리 설치 해준다.
```
CMake Error at CMakeLists.txt:56 (message):
  cannot prepare WebRTC build system

webrtc/build$ ./prepare_webrtc_build ~/docker_ros2_cg_ws/build/webrtc/ninja

Package gtk+-3.0 was not found in the pkg-config search path.
Perhaps you should add the directory containing `gtk+-3.0.pc'
to the PKG_CONFIG_PATH environment variable
No package 'gtk+-3.0' found
Could not run pkg-config.

See //examples/BUILD.gn:666:5: whence it was called.
    pkg_config("gtk_config") {
    ^-------------------------
See //BUILD.gn:57:9: which caused the file to be included.
        "examples:examples_unittests",
        ^----------------------------
```

`sudo apt install libgtk-3-dev`



## webrtc 빌드
[webrtc-ros2브랜치](https://github.com/RobotWebTools/webrtc_ros/tree/develop-ros2)

```
git clone -b develop-ros2 https://github.com/RobotWebTools/webrtc_ros.git
```

참고로 ros2 관련 webrtc_ros가 완벽하게 업데이트가 되어 있지가 않아서  
특히 webrtc 를 depot_tools 등이 cmake 에서 받아서 할 경우에 버전이 (커밋)이 최신인 듯하다.   
그래서 webrtc_ros 패키쪽에서 사용해야할 내용이 많이 변경이 되어 있다.   
예를 들어서 특정 헤더파일이 없거나 (bind.h) 그래서 webrtc_ros 빌드가 안됨   


`/Workspace/docker-ros2-swork/docker_ros2_cg_ws/src/webrtc_ros/webrtc/build/webrtc/src$`  
webrtc_ros 이하가 중요, 해당 submoudle 브랜치의 webrtc 버전이 93081d594f 인데  
checkout 으로 f183d1d996 으로 변경 해주자. 단 git checkout을 안하고 스크립트에서 수정한다.  

~~git checkout f183d1~~  좀 더 확실한 방법은    
`get_webrtc_source` 쉘 스크립트에서 revision 변수의 값을 아래 처럼 변경   
`revision="src@f183d1d9966b312006e395dc4c270639b35d26de"`   


그리고 나서 build 디렉토리 이하의 webrtc 와 depot_tools 를 지워주고 (빌드를 한번 해본 경우라면)   
colcon 워크 스페이스에 build, install 등을 지운 후에    
다시 colcon 빌드를 해주면 webrtc가 잘 빌드가 된다.   
확실히 이번에는 rtc_base/bind.h 가 있다.    

이를 이용하는 webrtc_ros 도 변경 없이 잘 빌드가 된다.   


> 참고로.. 최초 cmake 및 webrtc 소스 코드를 가져올 때에는 최신으로 가져왔다가   
webrtc 가 빌드하기 전에 커밋 변경 후 빌드하게 되는 듯 하다.

> 또한, 추후 RobotWebTools에서 develop-ros2 브랜치 업데이트가 변경 되면   
위의 과정이 필요 없을 수도 있다. Oct.11, 2024 기준


처음에는 webrtc 를 먼저 빌드하게 되는데  
중간에 꼬이면 webrtc/build 이하의 depot_tools와 webrtc를 지우고  
workspace의 최상위에 위치한 build install log 등을 지우고  
다시 빌드를 시도해 준다.

정상적이라면 최초에는   
[시간.s] [0/1 complete] [webrtc:cmake - 1min 0.0s] 로 나온다   
이때 depot_tools, webrtc 소스 코드등을 다운 하는 것 같다. 처음에는 시간이 오래걸려도 빌드되기를 기다려야 한다   

이후  
[시간.s] [0/1 complete] [webrtc:build 35% - 1min 15.0s] 이런식으로   
build % 가 나와야 한다. build %가 안나오고 3분이상 계속 빌드가 되면   
cmake에서 execute_process() 로 script 파일 실행이 실패했을 수 있다.  

> 정상적이라면 2~3분이면 빌드완료

### colcon 빌드 
```
colcon build --packages-select webrtc
colcon build --symlink-install --packages-select webrtc_ros_msgs
colcon build --symlink-install --packages-select async_web_server_cpp 
colcon build --symlink-install --packages-select webrtc_ros
```

### 빌드 실패할 경우- 
```
/home/docker_humble/docker_ros2_cg_ws/src/webrtc_ros/webrtc
/usr/bin/env: ‘python’: No such file or directory
depot_tools/ninja.py: Could not find Ninja in the third_party of the current project, nor in your PATH.
Please take one of the following actions to install Ninja:
- If your project has DEPS, add a CIPD Ninja dependency to DEPS.
- Otherwise, add Ninja to your PATH *after* depot_tools.
```
파이썬이 없는 경우, python, python2 를 설치하지 말고  python-is-python3 해주면 된다   
또한 ninja 는 cmake로 빌드를 하면서 따로 받아서 사용하는 듯 하다.  
아니면 apt로  ninja-build 설치


### webrtc_ros 의 web 및 src 의 cpp파일 수정   
web은 webrtc_web_removed_js_html_version.tar.xz 파일 참고   
depth topic 및 필요 없는 태그 h1 태그 등이 삭제된 버전임   

src는 webrtc_ros_server.cpp 의 파라미터 port 를 불러오는 부분을 하드코딩으로 원하는 포트로 바꿔 줄 것   
> launch 파일에 port 를 지정하게 되어 있는데, 파라미터를 제대로 못 불러오는 듯 하다. 디버깅이 필요하나 귀찮으므로 포트를 고정 ㅋ

webrtc_client.cpp 의 iceClient->wait_for_service() 부분이 있는데 10초 되어 있는데  
10초 동안 blocking이 되므로 브라우저에서 이미지가 바로 안 나오므로 시간을 줄여준다. 
```cpp
if (iceClient->wait_for_service(10s)) {
  ///
}
```

