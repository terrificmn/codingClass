# RealSense™ SDK 2.0 설치

[참고 공식 깃허브](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md)

gpg: keyserver receive failed: No keyserver available
이렇게 나올 시에는 아래처럼

```
sudo apt-get update
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
```

```
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u
```

이제 apt-key가 설치되었으므로 위의 명령어가 실행이 됨


이제 리포지터리 등록 후 인스톨
```
sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils
```

시간관계 상 이거는 나중에 해보자

Optionally install the developer and debug packages:
```
sudo apt-get install librealsense2-dev
sudo apt-get install librealsense2-dbg
```

usb-c 타입을 컴퓨터와 라이다 카메라와 연결 후 

이제 실행은 터미널에서   
realsense-viewer 

그러면 viewer가 실행되고 
Intel RealSense L515 를 발견했다며 Version 업데이트를 하라고 한다. 눌러준다

시간이 좀 걸림

## D435i
D435i를 설치할 때에
sudo apt-get install librealsense2-dkms    
있어도 된다  

꼭 util은 없어도 될 듯 하고 


secure boot가 활성화 되어 있다고 하면  
비밀번호를 잘 입력해준다. 8자 이상  (꼭 기억해두자)



## 빌드 하기
앞서 apt-get으로 설치했다면 지워주기
 1997  sudo apt-get remove librealsense2-dkms
 1998  sudo apt-get remove librealsense2-utils
 1999  sudo apt-get remove librealsense2-dev
 2000  sudo apt-get remove librealsense2-dbg
 2001  sudo apt-get remove ros-melodic-realsense2-camera


[공식 깃허브](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md)

```
git clone https://github.com/IntelRealSense/librealsense.git
```

usb제거 후 , 핵심 패키지 설치
```
sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
```

우분투 18
```
sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev
```

realsense permission script실행 (librealsense 루트 리렉토리에서 실행)
```
./scripts/setup_udev_rules.sh
```

build 디렉토리 생성
```
mkdir build && cd build
```

cmake하기
cmake ../ - The default build is set to produce the core shared object and unit-tests binaries in Debug 
mode. Use -DCMAKE_BUILD_TYPE=Release to build with optimizations.
```
cmake ../ -DBUILD_EXAMPLES=true


```
참고 옵션 들..
cmake ../ -DBUILD_EXAMPLES=true - Builds librealsense along with the demos and tutorials
cmake ../ -DBUILD_EXAMPLES=true -DBUILD_GRAPHICAL_EXAMPLES=false - For systems without OpenGL or X11 build only textual examples

Recompile and install librealsense binaries:
```
sudo make uninstall && make clean && make -j4 && sudo make install
```

Tip: Use make -jX for parallel compilation, where X stands for the number of CPU cores available:
sudo make uninstall && make clean && make **-j8** && sudo make install


# realsense2-camera 설치
[공식 깃허브](https://github.com/IntelRealSense/realsense-ros)

이동
```
cd ~/catkin_ws/src/
```

```
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/
git checkout `git tag | sort -V | grep -P "^2.\d+\.\d+" | tail -1`
```
ddynamic_reconfigure가 필요한데 설치가 안되어 있다면

꼭 빌드를 할 필요는 없다 
```
sudo apt install ros-melodic-ddynamic-reconfigure
```

빌드는 참고만..   
```
git clone https://github.com/pal-robotics/ddynamic_reconfigure.git
```

빌드
```
cd ../..
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
```



## 빌드가 딱히 소용없다면 지우기
먼저 librealsense 설치하는 build로 이동 후 지우기
```
cd ~/librealsense/build
sudo make uninstall && make clean
cd 
rm -rf librealsense/
```

