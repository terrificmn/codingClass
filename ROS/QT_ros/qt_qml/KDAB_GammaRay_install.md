# GammaRay 설치 
KDAB 의 GammaRay 설치 및 빌드

[GammaRay README INSTALL](https://github.com/KDAB/GammaRay/blob/master/INSTALL.md)

깃클론
```
git clone https://github.com/KDAB/GammaRay.git
```

build
```
cd ~/GammaRay
cmake -G Ninja -DCMAKE_PREFIX_PATH=$HOME/Qt/6.3.0/gcc_64 -DCMAKE_INSTALL_PREFIX=$HOME/qt_ws/gammaray
```

Qt 6.3버전 사용 중인데 계속 시스템의 qt5를 계속 찾는 듯하다.. 계속 qt5 CMake Error가 발생하면   
CMakeCache.txt 파일을 열어보면 QT6_BUILD가 OFF로 되어 있는데 이를 바꿔준다 
```
GAMMARAY_QT6_BUILD:BOOL=ON
```
이후 다시 빌드를 하면 잘 된다 

*CMAKE_PREFIX_PATH* 를 자신의 Qt 버전 경로로 지정해준다.  
현재 커스텀으로 빌드로 해서 설치를 했기 때문에 위의 경로로 되어 있다 

*CMAKE_INSTALL_PREFIX* 은 GammaRay가 최종적으로 설치될 경로이고, 원하는 경로로 설정을 해준다   
필요한 파일이 다 최종 경로에 설치되는 것은 아니고, 최종적으로는 위의 경로에  bin/ 이하에 gammaray 실행파일 하나가 만들어진다  
아예 옵션을 빼버리면 /usr/local 에 설치가 되므로 이왕이면 바꿔주자. 

> CMAKE_INSTALL_PREFIX 시 해당 경로가 없다고 하는지는 정확하지 않다. 없다고 하면 만들어준다  
마지막 설치되는 **경로가 꽤 중요!**. 실행 파일을 다른 곳으로 옮기면 실행에 필요한 shared libraries를 찾지 못할 수가 있다   
sub directory가 많이 생성 되므로, 처음에 gammayray가 설치될 디렉토리를 꼭 확인하자 (깃 클론한 곳이랑 다른 경로)



이후 
```
cmake --build .
cmake --build . --target install
```

## 설치 이후 
이동 후 실행
```
cd ~/qt_ws/gammaray/bin
./gammaray
```

필요시 PATH 환경 변수, symlink 등을 만들어서 활용하면 될 듯


## qt5 관련해서 에러
현재 qt6를 사용하고 있는데  
```
CMake Error in plugins/qmlsupport/CMakeLists.txt:
  Imported target "Qt::QmlPrivate" includes non-existent path

    "/usr/include/x86_64-linux-gnu/qt5/QtQml/5.12.8"


블라블라...

CMake Error in plugins/guisupport/CMakeLists.txt:
  Imported target "Qt::GuiPrivate" includes non-existent path

    "/usr/include/x86_64-linux-gnu/qt5/QtGui/5.12.8"
...

CMake Error in plugins/quickinspector/CMakeLists.txt:
  Imported target "Qt::QuickPrivate" includes non-existent path

    "/usr/include/x86_64-linux-gnu/qt5/QtQuick/5.12.8"
...

```
이런 비슷한 에러가 계속 발생

원인은 일단 `qmake -v` 를 하면 기존 리눅스에 설치되어 있는 qmake 버전을 알려주는데 이번 경우에는   
5.12.8 인데  그래서 해당 디렉토리에 5.12.8이 붙어서 계속 찾는 듯 하다   

그래서 기존의 Qt6.3 으로 진행하기 위해서  
CMakeCache.txt 파일에서 아래를 OFF에서 ON으로 변경
```
GAMMARAY_QT6_BUILD:BOOL=ON
```

몇가지 optional 프로그램이 없다는 것 빼고는 build 및 인스톨까지 잘 됨
