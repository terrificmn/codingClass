https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md
여기에 나온방식대로 안됨

gpg: keyserver receive failed: No keyserver available

이렇게 나옴

```
sudo apt-update
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
```

```
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo $(lsb_release -cs) main" -u
```

이제 apt-key가 설치되었으므로 위의 명령어가 실행이 됨


이제 리포지터리 등록 후 인스톨

sudo apt-get install librealsense2-dkms
sudo apt-get install librealsense2-utils


시간관계 상 이거는 나중에 해보자

Optionally install the developer and debug packages:
sudo apt-get install librealsense2-dev
sudo apt-get install librealsense2-dbg

usb-c 타입을 컴퓨터와 라이다 카메라와 연결 후 

이제 실행은 터미널에서 
realsense-viewer 

그러면 viewer가 실행되고 
Intel RealSense L515 를 발견했다며 Version 업데이트를 하라고 한다. 눌러준다

시간이 좀 걸림


