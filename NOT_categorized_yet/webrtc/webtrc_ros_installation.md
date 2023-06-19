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


## Robot Web Tools
robot web tools의 현재 홈페이지는 더 이상 운영이 안되는 듯 하다  

깃허브
```
https://github.com/RobotWebTools/webrtc_ros
```

JS와 C++로 만들어진 패키지이다  


## webrtc_ros 설치
noetic 버전은 없는 듯 하다   
~~`git clone https://github.com/RobotWebTools/webrtc_ros.git`~~ 일반적으로 클론을 하게 되면  
빌드 실패를 하게 된다   
 cannot prepare WebRTC build system

좀 더 연구가 필요할 듯 하다 

ROS2로 설치하려면 아래 깃 허브를 참고 (아마도 develop-ros2 브랜치에서 포크된 후 개발되었을 듯 하다)    
```
git clone https://github.com/polyhobbyist/webrtc_ros/tree/ros2
```

의존성 패키지
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


의존성 jsoncpp
```
git clone https://github.com/open-source-parsers/jsoncpp.git
```
build 디렉토리를 만들어서 빌드를 해준다  

```
cd jsoncpp
mkdir build; cd build
cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_STATIC_LIBS=ON -DBUILD_SHARED_LIBS=OFF -DARCHIVE_INSTALL_DIR=. -G "Unix Makefiles" ..
make 
sudo make install
```

의존성  
```
git clone https://github.com/GT-RAIL/async_web_server_cpp.git
```
이건 그냥 catkin build   
```
catkin build
```


좀 더 연구해보기!!! 업데이트 필요!! onJun19


webrtc_ros_server_node는 web_video_server 와 비슷하게 작동을 한다고 한다   
ROS topics을 web browser에 제공을 해주게 된다  

파라미터에는 *port* 기본은 8080   
*image_transport* 기본은 raw  : ROS image tropics를 구독하는 Transport type 이 됨


