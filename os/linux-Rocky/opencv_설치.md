# opencv 설치 on Rocky Linux
일단 페도라에서는 
```
sudo dnf install opencv opencv-devel
```
로 설치가 가능하다고 하는데, 

libgdal.so.30,  의존성 패키지가 없다고 나온다.  

gdal 패키지는 CRB repository를 dnf list에 등록해줘야한다.


```
dnf repolist
```
를 해보면  Rocky Linux 9 - CRB 가 없다.

추가해준다.
```
sudo dnf config-manager --enable crb
```

이후 다시 opencv, opencv-devel 을 설치해주면 opencv 4.6 이 잘 설치 된다.

버전 확인
```
pkg-config --modversion opencv4
```


### 소스 파일 빌드
빌드로 꼭 할 필요는 없지만, 계속 설치가 안되거나 정말 문제?가 있거나 할 때 사용..  

먼저 의존성 관련 설치 해준다. 아마도 이미 거의 설치가 되어 있을 듯..

```

sudo dnf groupinstall -y "Development Tools
```

```
sudo dnf install cmake gcc gcc-c++ gtk2-devel pkgconfig
sudo dnf install python3 python3-devel numpy
```

다운 받기
```
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.7.0.zip
unzip opencv.zip
```

압축 푼 곳으로 이동 후 build 디렉토리 만들기
```
cd opencv-4.7.0
mkdir build; cd build
```

cmake 이용해서 build파일 만들기. 
```
cmake ..
make
```
여기 까지 잘 되었다면... 최종 인스톨
```
sudo make install
```

버전 확인
```
pkg-config --modversion opencv4
```
