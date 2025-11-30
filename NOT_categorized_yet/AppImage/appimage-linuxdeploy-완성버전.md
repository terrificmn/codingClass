## 환경
물론 Fedora, 우분투 22.04 등에서는 좀 더 쉽게 sdk 따로 설치 필요 없이 apt 나 dnf 등으로 쉽게 설치해서 사용 가능  
> 좀 더 버전이 높은 stable 버전 가능  

대신 appimage 로 만들 경우에는 우분투에서도 20.04 버전으로 시작하는게 좋을 듯 하다. 
gcc 버전(?) 등이 하위 호환이 잘 되게 된다. 물론 상위 버전에서도 잘 되고 된다.  
단, docker 나 우분투 20.04 native 로 사용할 경우에는 qt6 관련 apt 패키지를 받지 못할 수 있으므로  
sdk 를 따로 설치해서 진행해야 한다. (snap 등도 가능하나 qt6 등을 사용할 경우)  
docker 에서도 우분투 20에 sdk를 받아서 진행

qtcreator 직접 빌드 설치하기 ubuntu qtcreator_ros build install.md 참고

## 최초 실행
처음 new_app 이하의 create_appdir.sh 실행하면 AppDir 관련 디렉토리를 만들어준다. 
AppRun, 데스크탑.desktop, 아이콘파일.png 파일을 AppDir 안에 복사.

각 파일은 프로젝트에 맞게 수정하기  

## qt 실행파일
qt app 실행파일은 AppDir/usr/bin 디렉토리 복사해준다. 


## AppRun 파일
AppDir 바로 아래 root 디렉토리에 복사  
exec 의 실제 실행되는 파일명으로 변경
```
exec "$APPDIR/usr/bin/실행프로그램명" "$@"
```

완성된 AppRun 파일
```
#!/bin/bash
## cpp 라이브러리 인식
export LD_LIBRARY_PATH="$APPDIR/usr/lib:$LD_LIBRARY_PATH"
## qml 인식
# export QML2_IMPORT_PATH="$(dirname "$0")/usr/lib/qml"
export QML2_IMPORT_PATH="$APPDIR/usr/qml:$QML2_IMPORT_PATH"
export MY_APP_QML_PATH="$APPDIR/qml"
exec "$APPDIR/usr/bin/appauto_udevrule_app" "$@"
```


## desktop 파일 및 icon 파일
Desktop 파일은 실제 실행할 파일 및 icon 파일이름 등으로 변경

예)
```
[Desktop Entry]
Name=vnc_connector
Exec=appvnc_connector
Icon=vnc-connector
Type=Application
Categories=Utility;
```

예)
```
[Desktop Entry]
Name=auto_udevrule_app
Exec=auto_udevrule_app
Icon=auto_udevrule_app
Type=Application
Categories=Utility;
```

모든 이름을 다 통일하면 더 쉽다. 
icon 파일은 256X256 사이즈에 png 파일이면 된다. (파일명에 png 확장자는 입력하지 않음.)

여기에서 주의할 점은 desktop 파일 및 icon 파일을 직접 AppDir/usr/share 이하에 복사해줘야 한다.  
**desktop 파일: AppDir/usr/share/applications/**  
**icon 파일: AppDir/usr/share/icons/hicolor/256x256/apps/**


## 빌드 준비
먼저 linuxdeploy-x86_64.AppImage 파일을 new_app 디렉토리에 복사를 해준다. 
qt 플러그인을 복사하기 위해서는 추가로 linuxdeploy-plugin-qt-x86_64.AppImage 파일도 같이 복사해준다. 

> 생성된 AppDir 디렉토리 상위에 위치 하면 된다. 


## 실제 실행 파일 준비
먼저 준비된 qt 패키지를 깃클론 등을 해서 빌드를 해준다.  
qtcreator 등 사용  

우분투 20 및 lua5.3 버전을 사용할 경우에는 빌드시 lua 5.3 을 라이브러리 및 헤더파일 인쿠루드를 잘 명시해줘야 한다.  

이후 빌드된 실행 파일을 AppDir/usr/bin 이하로 복사해준다. 


qrc를 사용 안하고 qt_add_qml_module() qml 파일들을 빌드했다면  
해당 프로젝트의 qml 파일들을 수동으로 카피해줘야 한다.  
실제 qml 파일들이 있는 디렉토리 통으로 복사해준다.   
예)
```
cp -r ~/qt_ws/auto_udevrule_app/qml/ AppDir/
```
이제 AppDir 이하에도 qml 디렉토리 및 파일들이 복사 된 것을 AppRun 에서 환경 변수를 셋팅해서 잘 사용될 수 있게 해준다. 

AppRun 에서 
```
export QML2_IMPORT_PATH="$APPDIR/usr/qml:$QML2_IMPORT_PATH"
export MY_APP_QML_PATH="$APPDIR/qml"
```
이 추가됨. QML2_IMPORT_PATH 가 지정되면 qml 파일들을 AppDir/usr/qml 로 복사해주게 되고   
MY_APP_QML_PATH 는 위에서 직접 수동으로 복사해서 위치하고 있는 디렉토리 및 파일

> 위의 작업을 안하게 되면 qml 관련 module 찾을 수 없다는 에러가 발생함

### 빌드 
실행 커맨드시에 plugin 옵션을 사용할 수가 있다. 
`cd ~/new_app`  

```
./linuxdeploy-x86_64.AppImage --appdir AppDir/ --plugin qt --output appimage
```
> linuxdeploy-plugin-qt-x86_64.AppImage 같은 디렉토리에 있으면 된다.



## Quick Step
오류가 있어서 다시 시작할 경우에는 (실제 AppDir/usr/bin 에 복사한 qt app 자체가 실행이 안되는 현상이 발생할 경우)  
AppDir 을 삭제 후 다시 시작  
```
cd ~/Workspace/new_app
rm -rf AppDir
./create_appdir.sh
```

실제 실행할 파일과(qt app) 과 실제 qml 디렉토리 이하의 qml파일들을 실제 프로젝트로 부터 복사해준다.
> docker 라면 컨테이너 안에서 qtcreator 등을 통해서 미리 release 버전 등으로 빌드 
```
cp ~/qt_ws/auto_udevrule_app/build/Desktop-Release/appauto_udevrule_app AppDir/usr/bin/
cp -r ~/qt_ws/auto_udevrule_app/qml/ AppDir/
```
> 가장 중요한 실행파일과, qml 파일들은 실제 위치를 참고해서 복사해준다.

```
cp ./AppRun AppDir/
cp ./auto_udevrule_app.desktop AppDir/usr/share/applications/
cp ./auto_udevrule_app.png AppDir/usr/share/icons/hicolor/256x256/apps/
```

> 데스크탑 파일과 아이콘 파일명은 그리고 데스크탑에 들어가는 파일명은 다 똑같이 통일해주자  
예 vnc_connector 로 했을 경우,  
데크스탑 파일명: vnc_connector.desktop,  
이미지: vnc_connector.png   
desktop의 파일내용의 Name, Exec, Icon 모두 vnc_connector  
실제 usr/bin 에 들어가는 파일명과는 달라도 된다. 예: 실제 실행파일은 appvnc_connector  
아이콘 파일도 구하기 귀찮으면 그냥 파일명만 바꿔서 사용해도 무방 (어차피 이미지가 표시 안됨)  

```
./linuxdeploy-x86_64.AppImage --appdir AppDir/ --plugin qt --output appimage
```

아래 까지 나온다면 성공! 물론 중간에 qml 및 shared lib 가 모두 찾아져야 한다. 
```
 Marking the AppImage as executable...
[appimage/stdout] /home/sgtubunamr/Workspace/appimage-build/new_app/AppDir should be packaged as auto_udevrule_app-x86_64.AppImage
[appimage/stderr] Embedding MD5 digest
[appimage/stderr] Success
```

현재 디렉토리에 auto_udevrule_app-x86_64.AppImage 가 생기는데   
파일을 실행 했을 때 기존의 실행파일 처럼 실행되면 최종 성공!


만약 Qt module 을 못찾을 때
```
[qt/stdout] Found Qt modules:
[qt/stdout] Extra Qt modules:
[qt/stdout] ERROR: Could not find Qt modules to deploy
```

환경 변수를 다시 한번 셋팅, AppRun 파일이 아닌 터미널에서 사용  
```
export PATH=~/qtc-sdk/6.6.0/gcc_64/bin:$PATH
export LD_LIBRARY_PATH=~/qtc-sdk/6.6.0/gcc_64/lib:$LD_LIBRARY_PATH
export QML2_IMPORT_PATH=~/qtc-sdk/6.6.0/gcc_64/qml
```
터미널 일회용이므로 계속 사용하려면 `/.bashrc` 에 넣어준다.


## 참고  
auto_udevrul_app 의 helper write 는 우분투 20에서 다시 빌드해서  
현재는 일단 수동으로 helper writer도 복사해줘야한다. AppImage 파일을 복사할 pc 에 카피해준다. 



