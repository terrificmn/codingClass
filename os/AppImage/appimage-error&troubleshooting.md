# AppImage qt 만들기
아마도 appimagetool-x86_64.AppImage 를 사용해서 만든 것 같으나,  
적용 방법을 정리하는데 실패한 듯 하다.  

linuxdeploy 를 이용해서 AppImage 만드는데 성공했으므로  
[!appimage-linuxdeploy-완성버전.md](appimage-linuxdeploy-완성버전.md) 파일을 참고하자


## 이하는 참고

appimage 가 성공적으로 빌드가 되더라도  실행을 하게 되면  
QtQuick 등 이.. load가 안되었다며 에러가 발생  
"QtQuick.controls" 가 못찾는 에러 발생  

sdk에서 qml 관련 디렉토리를 AppDir/usr/lib 에 복사해준다.   
그리고 LD_LIBRARY_PATH 환경변수 셋팅 및 AppRun 스크립트에 export 환경 변수를 셋팅   


이 경우에도 LD_LIBRARY_PATH 경로를 추가로 넣어준다.   
에러는 아래와 같다..

```shell
ERROR: ldd outputLine: "libQt6ShaderTools.so.6 => not found"
ERROR: for binary: "/home/myuser/Workspace/appimage-build/AppDir/usr/lib/qml/Qt5Compat/GraphicalEffects/private/libqtgraphicaleffectsprivateplugin.so"
ERROR: Please ensure that all libraries can be found by ldd. Aborting.
```

위를 종합하면 ~/.bashrc 파일에   
```shell
export QT_DIR=${HOME}/qtc-sdk/6.6.0/gcc_64
export PATH=$QT_DIR/bin:$PATH
QT_TOOL=${HOME}/qtc-sdk/Tools/QtCreator/lib/Qt/lib
export LD_LIBRARY_PATH=$QT_DIR/lib:$QT_TOOL:$LD_LIBRARY_PATH
```

마지막으로 플러그인을 못 찾을 때 에러  
```shell
ERROR: ldd outputLine: "libmimerapi.so => not found"
ERROR: for binary: "/home/myuser/qtc-sdk/6.6.0/gcc_64/plugins/sqldrivers/libqsqlmimer.so"
```
pulgins 에 있는 libqsqlmimer.so 파일을 복사해서 빌드 하는 중에 에러가 발생하는데 말 그대로 libmimerapi.so 못 찾는다..    
일단 libmimerapi.so 는 설치되어 있지 않고, libqsqpmimer를 사용하지도 않는다.  
이럴 경우에는 /home/myuser/qtc-sdk/6.6.0/gcc_64/plugins/sqldrivers 이하의 디렉토리 들어가서 잠깐 파일을 다른 곳으로  
예를 /home 이하로 이동 시켜 준다.  (이름 바꾸는 것으로는 효과가 없음)   

이렇게 하면 빌드가 잘 된다.  
여태껏 빌드가 대충 되었을 경우에는 금방 끝나고, 실행을 하면 허무하게 안되는 경우였는데   
확실히 카피 및 appimage 빌드가 시간이 꽤 걸린다. 약 30초 이상 거리는 듯 하며    
마지막으로 아래와 같은 메세지가 나와야 성공이다.
```
Marking the AppImage as executable...
Embedding MD5 digest
Success
```
> 실패할 때 굉장히 빨리 되는 것은 확실히 문제가 있었던 것 같다. 빌드 할 때 작은 프로그램이어도 수 초가 소요 된다.  

## ubuntu 에서 빌드
확실한 것은 ubuntu 20 버전에서 해주는 것이 가장 좋다.   
fedora 에서 해보고, ubuntu 에서도 해봤지만, fedora는 너무 업스트림이라 버전이 높다. 호환성이 안 좋다.   
> fedora 에서 실행하는 것은 libgcc? 관련 가장 높은 버전에서 하기 때문에 호환성 때문에 appimage를 만들기 어려운 것 같다.  

그래서 ubuntu 20 버전에서 빌드를 하게 되면, fedora, ubuntu 20, 22에서도 호환이 좋다. 

## 프로그램에서 config 등을 사용할 경우  
추가로 고려해야할 것은 내 프로그램에서 yaml 파일 등을 읽어서 실행 한다면, 인식이 잘 될 수 있게 스크립트에 추가해야 한다.   

$APPDIR 을 이용해서 External files 를 읽을 수 있게 해주는 것
AppRun 스크립트에 추가  
```shell
CONFIG_FILE="$APPDIR/config.yaml"
```

추가로 사용해보기
일단 다행인 것은 appimage 파일에서 symlink도 잘 인식한다. 



