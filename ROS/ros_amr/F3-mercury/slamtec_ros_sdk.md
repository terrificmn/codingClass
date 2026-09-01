# slamtec sdk 사용하기
먼저 아래에서 다운로드  / (*또는 FTP 사용)   

[다운로드 부분에서 SDK and Firmware 부분-> Slamware ROS SDK](https://www.slamtec.ai/home/support/#sdk-and-firmware)

> Linux SDK 도 있으나, ROS SDK 만 있으면 될 듯 하다.

## 다운 후 

압축을 풀게 되면, slamware_ros_sdk 와 slamware_sdk 가 있는데 이 중 slamware_ros_sdk 패키지만 사용하려고 한다  

`~/catkin_ws/src` 에 해당 패키지들을 옮겨준다. 단 slamware_sdk 패키지에 있는 include 파일들과 lib의 static 라이브러리들이 필요하므로   
복사를 해준다  

드래그로 복사를 하던가  
```
cd ~/slamware_sdk/include
cp -r ./* ~/catkin_ws/src/slamware_ros_sdk/include/
cd ~/slamware_sdk
cp -r ./lib ~/catkin_ws/src/slamware_ros_sdk/
```

## CMakeLists.txt 파일 수정

include 및 lib 의 파일들을 찾아주기 위해서 경로를 현재 패키지의 경로로 수정한다   
```
find_path(slamware_sdk_INCLUDE_DIR rpos/rpos.h ${PROJECT_SOURCE_DIR}/include)
find_path(slamware_sdk_LIBRARY librpos_framework.a ${PROJECT_SOURCE_DIR}/lib)
```

이렇게 해주면 target_link, install 등을 잘 찾아서 연결해주게 된다   

> 참고로 패키지 명은 그대로 사용하자, include로 사용을 많이 하고 있기 때문에 일만 복잡해진다   
> slamware_sdk 의 include와 lib의 static 라이브러리를 포함하고 있음   

이후 빌드를 해준다
```
cd ~/catkin_ws
catkin build slamware_rosk_sdk
```


## 런치파일 실행
먼저 무선 wifi를 이용해서 F3 로봇 같은 경우에는 태블릿의 핫스팟을 켜주고 (최초 로봇과 태블릿은 wifi로 연결이 먼저 되어 있어야 함)   
데스크탑에서 핫스팟으로 접속을 한 후에 런치파일을 실행해 주면 된다 

`ip_address:=` 파라미터를 이용해서 ip를 지정해준다. 로봇 자체의 ip 192.168.11.1 (기본값) 으로 정해준다  
```
roslaunch slamware_ros_sdk slamware_ros_sdk_server_node.launch ip_address:=192.168.11.1
```

TF를 잡지 못한다면  
런치파일을 열어서 토픽 들 중에 절대경로로 지정되어 있는 것을 바꿔준다   

예: 파라미터 중에 `<param anme="/cmd_vel" 의 기본값을 value="cmd_vel"` 처럼 바꿔준다  (전부 바꿔주자!)

> ip_address 아규먼트의 default 값을 바꾸면 런치파일 실행할 때 좀 더 수월


## 문제점
rviz 화면으로 관련 토픽 내용을 볼 수가 있지만  

~~API 요청이 전혀 안되고, rviz에서 맵, 레이저, 오도메트리등은 잘 나오나~~   
~~movebase/simplegoal 을 통한 goal 지정은 작동하지 않는다.(토픽은 발행된다)~~   
뭔가 enable 등을 먼저 해주고 시작이 되어야 하는지는 모르겠다   

slam부분의 mapping, localization을 enable 시켜야하는데 api를 통해서 제공한다


## 아직까지 문제점
런치파일에서 토픽들은 절대경로로 되어 있다면 `/` 를 빼주면 TF가 잘 발행 됨

예
```xml
  <param name = "/cmd_vel"                 value = "cmd_vel"/>
  <param name = "/move_base_simple/goal"   value = "move_base_simple/goal"/>
```


