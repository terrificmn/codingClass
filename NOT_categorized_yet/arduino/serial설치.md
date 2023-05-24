# serial 설치

serial 관련 패키지도 꽤 많다..

먼저 ros 에서 사용하는 패키지는 *serial* 이다   

```
 Could not find a package configuration file provided by "serial" with any
  of the following names:
```

빌드 시 못 찾으면   
ROS distro에 맞춰서 설치해준다 
```
sudo apt install ros-noetic-serial
```

그리고 CMakeLists.txt 파일에 find_package()를 통해서 패키지를 찾을 수 있게 등록  
 예
```
find_package(catkin REQUIRED COMPONENTS
    roscpp serial
)
```

## 아두이노
참고로 아두이노에서는 Serial 로 대문자 시작하는 놈으로 사용한다   



## rosserial 설치
```
sudo apt install ros-noetic-rosserial-arduino
```
파이썬으로 되어 있는 패키지   





