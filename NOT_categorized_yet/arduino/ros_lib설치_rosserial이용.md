# rosserial로 ros 관련 패키지 설치
rosrun 을 해서 필요한 ros 패키지를 ros_lib 형태로 설치해 줄 수가 있다   

먼저 `sudo apt install ros-noetic-rosserial-arduino` rosserial-arduino가 설치되어 있어야 한다  

rosserial_arduino 패키지를 이용해서 make_libraries.py 실행 한다. 파라미터로  아두이노/esp32등의 패키지 디렉토리를 지정해준다   
```
rosrun rosserial_arduino make_libraries.py /home/user/Documents/PlatformIO/Projects/esp32_mypkg/lib
```

> 현재 ros 에 설치되어 있는 패키지, msg 등을 다 가지고 와서 만들어주는 듯 하다    
PlatformIO (vscode)를 사용할 경우에는 프로젝트(패키지)의 lib 까지 경로로 만들어주면 되고   
아두이노 같은 경우에는 프로젝트(패키지) 안에 libraries 에 넣어주면 될 듯하다   

ros.h, 나 std_msgs, geometry_msgs 등과 같은 type 등을 만들어준다 

**esp32에서는 ros serial이 잘 작동을 안하는 것 같다. 좀 더 테스트를 해봐야 할 듯**

추후 다시 업데이트!

