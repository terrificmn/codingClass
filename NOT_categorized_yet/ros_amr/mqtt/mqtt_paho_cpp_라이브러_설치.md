# Eclipse Paho MQTT C++ 라이브러리

## 디펜던시 설치
먼저 필요한 패키지 설치  우분투 기준
c++11, MQTT 브러커 연결 및 퍼블리싱 메세지, 토픽 구독

기본적으로 필요한 패키지
```
sudo apt-get install build-essential gcc make cmake cmake-gui
```

secure sockets 이용
```
sudo apt-get install libssl-dev 
```

doxygen도 필요할 수 있음
```
sudo apt-get install doxygen
```


### 먼저 Paho C 라이브러리를 먼저 빌드
먼저 디렉토리 하나 만들고 그 안에 클론 후에 하나씩 실행하면 된다   
```
mkdir lib_paho
cd lib_paho

git clone https://github.com/eclipse/paho.mqtt.c.git
cd paho.mqtt.c
git checkout v1.3.8

cmake -Bbuild -H. -DPAHO_ENABLE_TESTING=OFF -DPAHO_BUILD_STATIC=ON \
    -DPAHO_WITH_SSL=ON -DPAHO_HIGH_PERFORMANCE=ON
sudo cmake --build build/ --target install
sudo ldconfig
```
SSL/TLS 가능하게 빌드가 된다. disable하려면  cmake 할 때 -DPAHO_WITH_SSL=ON 을 해준다  

install 자체를 다른곳에 하려면  
CMAKE_INSTALL_PREFIX 를 다른 곳으로 지정
예
```
camke -Bbuild -H . ... 생략  \
-DCMAKE_INSTALL_PREFIX=./build/_install
```

### 이제 Paho C++ library  빌드
이전에 만든 lib_pho_c 디렉토리로 다시 이동
```
cd ~/lib_pho
```

paho C++ 클론 및 빌드
```
git clone https://github.com/eclipse/paho.mqtt.cpp
cd paho.mqtt.cpp
cmake -Bbuild -H. -DPAHO_BUILD_STATIC=ON \
    -DPAHO_BUILD_DOCUMENTATION=TRUE -DPAHO_BUILD_SAMPLES=TRUE
sudo cmake --build build/ --target install
sudo ldconfig
```

참고  
만약 Paho C 라이브러리를 기본 location에 설치를 안했다면, 또는 다른 버전을 설치하려면 cmake에 옵션을 다르게 준다  
예  
```
cmake -Bbuild -H. -DPAHO_BUILD_DOCUMENTATION=ON -DPAHO_BUILD_SAMPLES=ON \
    -DPAHO_BUILD_STATIC=ON \
    -DCMAKE_PREFIX_PATH=$HOME/mqtt/paho.mqtt.c/build/_install
```

컴파일러 지정도 가능 (mac)
```
cmake -DCMAKE_CXX_COMPILER=clang++
```


샘플 코드
https://github.com/eclipse/paho.mqtt.cpp/tree/master/src/samples


