opencv 설치 방법은 우분투 경우에는 apt install python3-opencv 도 있고   

```
sudo apt install libopencv-dev python3-opencv
```

python3의 패키지 매니저 pip을 이용해서 설치할 수도 있다. 


이번에는 직접 소스 코드 깃허브 다운 받은 후에 빌드를 해 본다 

먼저 깃허브 클론
```
git clone https://github.com/opencv/opencv.git
```

opencv 디렉토리로 이동 후 build 만들기
```
cd opencv
mkdir build
```

cmake를 이용해서 build script를 생성
```
cmake ../
```

그리고 build (소스파일을 make명령으로 빌드)
```
make -j4
```
역시 빌드 부분은 CPU가 많이 사용되고 시간이 꽤 걸린다  

빌드가 완료되면 install을 해주자  
```
sudo make install 
```

/usr/local/lib 등에 설치를 해준다  


이제 cpp 파일에 
```
#include <opencv2/opencv.hpp>
```
를 넣어주고 

CMakelists.txt 파일에는 find_package()에 OpenCV를 넣어준다   
그리고 include_directories()를 해서 라이브러리를 인쿠르드 시켜준다  
target_link_libraries()까지.. 모두 find_package를 해서 OpenCV_LIBS를 사용할 수 있다  
예..
```
cmake_minimum_required(VERSION 2.8)
project( DisplayImage )
find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )
add_executable( DisplayImage DisplayImage.cpp )
target_link_libraries( DisplayImage ${OpenCV_LIBS} )
```

하면 되야 하지만... 멜로딕 도커 버전기준으로 안되고 있다;;

```
  Could not find a package configuration file provided by "OpenCV" with any
  of the following names:

    OpenCVConfig.cmake
    opencv-config.cmake
```


find / -name "OpenCVConfig.cmake"

export OpenCV_DIR=/usr/local/share/OpenCV

좀 더 찾아봐야할 듯 -- 업데이트할 것


참고로 우분투 20.04 기준, ROS Noetic 에서 OpenCV는 버전 4.2 이고 find_package()을 안해도 문제가 없다  
우분투에서는 apt install python3-opencv 으로 설치됨
```
>>> print(cv2.__version__)
4.2.0
```



