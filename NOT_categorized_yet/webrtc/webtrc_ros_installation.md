# webrtc
기존의 http 프로토콜의 통신에서는 서버에 요청이 있고나서 응답하는 통신 방법이었다.   
request가 있어야지 서버에서 response를 해주게 되고, 그 이후 연결이 끊어진다  

> 이를 통한 프로그램이라면 계속 새로고침을 해서 request를 해야  새로운 내용을 받을 수 있게 되는것   

그래서 연결이 끊어지지 않고 계속 연결되는 open과 close로 되는   
Web socket 통신이 나오게 됨. 그래서 빠른 통신이 되게 되었다.   

하지만 연결이 서버를 통하기 때문에 많은 연결이 되어 있다면 느려지게 된다   

그래서 peer to peer가 연결되는 WebRTC가 나오게 됨   

> Real Time Communication

브라우저와 브라우저가 연결되는 방법이며 서버를 거치지 않아서 빠른 텍스트, 오디오, 비디오를 주고 받을 수 있게 된다   
단점은 많은 peer가 있을 경우, 그 사람(peer) 수 만큼 다운로드 및 업로드를 해줘야하는 문제가 있어서   
많은 연결을 확장하는 데에는 한계가 있다  

그럼에도 불구하고 브라우저와 브라우저를 연결하는 점에서 빠른 속도가 장점   

> 설치할 webrtc_ros 노드  
webrtc_ros_server_node는 web_video_server 와 비슷하게 작동을 한다고 한다   
ROS topics을 web browser에 제공을 해주게 된다  
파라미터에는 *port* 기본은 8080   
*image_transport* 기본은 raw  : ROS image tropics를 구독하는 Transport type 이 됨


## Robot Web Tools
robot web tools의 현재 홈페이지는 더 이상 운영이 안되는 듯 하다  

깃허브
```
https://github.com/RobotWebTools/webrtc_ros
```

JS와 C++로 만들어진 패키지이다  

일단 의존성 패키지를 설치한 후에 최종적으로 클론하자. 빌드하다가 실패를 많이하므로;;; 



## 먼저 의존성 패키지 설치

기본적으로 아래의 의존성 패키지가 필요
```
async_web_server_cpp
cv_bridge
image_transport
webrtc
```

image_transport가 없을 경우에는 
```
sudo apt install ros-noetic-image-transport
## 그 외에 
sudo apt install ros-noetic-rosbridge-server
```

cv_bridge 없을 경우
```
sudo apt install ros-noetic-cv-bridge
```

gtk3 설치
```
sudo apt install libgtk-3-dev
```


sudo apt install libjpeg-turbo8 libjpeg-turbo8-dev

python2 gir1.2-gmodule-2.0 libglib2.0-dev pulseaudio libasound2-dev libpulse-dev ninja-build stow

## 중요한 3rd party 프로그램 설치
중요 **의존성 jsoncpp 설치**

build 디렉토리를 만들어서 빌드를 해준다  

```
mkdir 3rd_party; cd 3rd_party
git clone https://github.com/open-source-parsers/jsoncpp.git
cd jsoncpp
mkdir build; cd build
cmake -DCMAKE_BUILD_TYPE=release -DBUILD_STATIC_LIBS=OFF -DBUILD_SHARED_LIBS=ON -DARCHIVE_INSTALL_DIR=. -G "Unix Makefiles" ..
make 
sudo make install
```


## jsocpp 빌드를 shared lib
shared lib가 되게 만들어줘야 -fPIC 를 적용되게 해준다 (정확히 모름;;)   

> f는 gcc prefix로 control the interface conventions used in code generation  
의 의미로 사용이 되며 PIC는 stands for "Position Independent Code" 라는 약자로   
dynamic linking과 global offset table 의 사이즈의 제한을 피할 때 사용    
이 옵션은 shared libraries를 만들 때 OS 한테 Global Offset Table (GOT)를 사용한다고 말해주는 의미가 되어   
모든 주소 레퍼런스등은 GOT와 관련이 되어서 해당 코드는 여러 프로세서들 간에 공유된다는 의미가 된다   
흠.. 뭔말인가? 암튼 shared ojbects (so파일)을 빌드할 때 사용된다고 한다   

cmake 할 때 `-DBUILD_STATIC_LIBS=ON -DBUILD_SHARED_LIBS=OFF` 이 부분임   

안그러면 webrtc 빌드 할 때 에러가 발생한다.  아래처럼
```
/usr/bin/ld: /usr/local/lib/objects-Release/jsoncpp_object/json_reader.cpp.o: relocation R_X86_64_PC32 against symbol `_ZTVN4Json17CharReaderBuilderE' can not be used when making a shared object; recompile with -fPIC
/usr/bin/ld: final link failed: bad value
```

> ROS2에서는 아닐 수도 있음. 왜냐하면 

## webrtc_ws 로 새로 만들기
기존의 워크스페이스를 사용해도 되나, 따로 만들어서 사용함  

```
cd
mkdir webrtc_ws/src -p
```

의존성 async_web_server_cpp 클론 및 최초 빌드
```
cd ~/webrtc_ws/src
git clone https://github.com/GT-RAIL/async_web_server_cpp.git
```
~~이건 그냥 catkin build~~ catkin 빌드 말고 catkin_make로 진행   
일단 클론으로 패키지만 받자   

## webrtc_ros 설치
~~noetic 버전은 없는 듯 하다~~  의존성 패키지만 잘 설치를 해주면 ROS1에서도 작동한다   
단, 크로미엄 Chromium 크롬 기반이어서인지 firefox에서는 안됨   ㅠㅠ    

물론 의존성 부분에서 잘 설치가 안되면   
```
cannot prepare WebRTC build system
```
에러와 함께 빌드 실패한다   

먼저 ROS noetic에서는 webrtc_ros 클론 
```
cd ~/webrtc_ws/src
git clone https://github.com/RobotWebTools/webrtc_ros
```

catkin build 말고
```
cd ~/webrtc_ws
```

`catkin_make_isolated --install` 로 해준다    

먼저 catkin build 말고  catkin_make_isolated 빌드를 해주자   
depot_tools 등, Ninja build tool, WebRtc source code 등을 fetching을 해주기 때문에   
catkin build 를 하려면 일단 catkin_make_isolated 로 해줘야 필요한 것들을 추가로 다운 (cloning)을 하고   
빌드하게 되는 듯 하다   
다행히 빌드는 webrtc/build 안에 다운들이 되는 듯 하다   

이것도 엄청 오래 걸리는데 문제가 있는 듯 하다 

```
[0:06:37] Still working on:
[0:06:37]   src/third_party
[0:06:37]   src/tools
[0:06:47] Still working on:
[0:06:47]   src/third_party
```
이렇게 계속 된다.. 대충 tool 관련해서는 다운이 된 듯 해서 

catkin build로 가능을 할 듯 한데, 일단 webrtc 부터 먼저 진행을 해주자   
```
catkin build webrtc
```
메세지는 안 나오지만, webrtc의 CMakeLists.txt 파일이 거의다가 install 관련된 내용들이다    
이래서 오래 걸리는 듯 하다.. 뭔가 잘 설치가 안되거나, 추정은 그렇고,, 한번 빌드 하다 실패하거나  
취소한 후 다시 할려고 하면 안됨  

> Desktop에서 catkin build로 성공을 했는데, 아마도 catkin_make를 한 이후 실패해서 삭제를 한 후에   
그 동안 필요한 패키지가 다운이 되서??? 잘 모르겠다.. 업데이트 필요   

```
/home/user/webrtc_ws/src/webrtc_ros/webrtc/build/webrtc/.gclient_entries missing, .gclient file in parent directory /home/user/webrtc_ws/src/webrtc_ros/webrtc/build/webrtc might not be the file you want to use.
```
이런 메세지가 나오면 빌드 쪽을 지워줘야 한다  

~/webrtc_ws/src/webrtc_ros/webrtc/build  디렉토리안의 depot_tools 등을 사용하는 듯 함  
뭔가 꼬이면 지우고 다시 클론해준다  


다시 업데이트 하자!!!!!







> ROS 브랜치 및 깃허브   
ROS2로 설치하려면 아래 깃 허브를 참고 (아마도 develop-ros2 브랜치에서 포크된 후 개발되었을 듯 하다)    
```
git clone https://github.com/polyhobbyist/webrtc_ros/tree/ros2
```



시간이 엄청 걸리기도 하는데 이것은 지켜봐야할 듯   
데스크탑에서는 문제가 있을 때는 오래걸렸지만, 의존성 해결 후 약 몇 분 안걸려서 빌드가 완료 됨   

5분 이상 빌드를 하고, cpu를 거의 사용하지 않는다. 빌드 문제가 있는 듯 하다 
'




## 에러 트러블 슈팅

GN build tool 관련 에러
```
cannot fetch GN build tool 에러 발생 시
```

python을 사용하기 때문에 설치 해준다 
```
sudo apt install python python2
```


No package 'gtk+-3.0' found 이 없다. 이 증상은 첫 번째 빌드시에 빌드가 5분이 이상 되는 경우   
원래라면 그렇게 까지 오래 걸리지 않고  
다시 빌드를 하면 에러가 발생  


*다운 그레이드 하지 말고*  sources.list 파일을 추가해줘야 한다   
먼저 `sudo apt update` 이후에 설치 libgtk-3-dev를 설치를 해보고   
의존성 문제 때문에 버전이 안 맞는다고 하는 문제가 발생한다고 하면   

apt 리스트를 추가 (물론 그냥 설치가 되면 스킵)

```
sudo vi /etc/apt/sources.list
```
기존의 있던 리스트에 추가를 해준다 `deb http://archive.ubuntu.com/ubuntu focal-updates main`   

기존 카카오로 연결되어 있던 것에 추가된 예
```
deb https://mirror.kakao.com/ubuntu/ focal main universe restricted multiverse
deb http://archive.ubuntu.com/ubuntu focal-updates main
```
복사한 후 저장해준다 

그리고 lib-gtk 3 설치
```
sudo apt update
sudo apt install libgtk-3-dev
```
이제 libgtk-3가 설치가 될 것임


### 다운 그레이드는 할 수 있다  참고만 할 것
처음에 libgtk-3를 설치하려고 하면 의존성 패키지들의 버전이 맞지 않는다면서 설치가 되지 않음   
그래서 해당 의존성 패키지들을 강제로 다운그레이드를 할 수는 있다   
예를 들어   
```
The following packages have unmet dependencies:
 libgtk-3-dev : Depends: gir1.2-gtk-3.0 (= 3.24.18-1ubuntu1) but 3.24.20-0ubuntu1.1 is to be installed
                Depends: libatk-bridge2.0-dev but it is not going to be installed

## 아래처럼 버전을 명시해 준다
sudo apt install gir1.2-gtk-3.0=3.24.18-1ubuntu1
```

어차피 이렇게 발버둥(?)을 쳐도 결국은 gtk-3.0 설치가 안되므로 그냥 **버전 명시해서 설치할 수 있다는 것만 알자**   

> dpkg: warning: downgrading gir1.2-gtk-3.0:amd64 from 3.24.20-0ubuntu1.1 to 3.24.18-1ubuntu1   
라고 나오면 설치가 다운그레이드가 됨    

위의 apt list를 업데이트를 해서 맞는 버전을 설치하자!




