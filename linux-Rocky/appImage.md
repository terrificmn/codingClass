# AppImage Tool
Fedora 에서는 linuxdeploy-x86_64.AppImage 등의 패키지는 사용이 불가 하다.  
fedora 버전이 너무 높기 때문에 그러하다..

대신 AppImage Tool을 사용하면 메뉴얼로 만들어 줄 수는 있는데..  이것도 쉽지는 않은 듯 하다.   
> 계속 테스트 중.. 아무래도 최신 버전 보다는 ubuntu 20 정도 기준으로 하는 게 나을 듯 하다.  
> 따로 우분투를 안 깔았다면 도커를 사용하는게 정신 건강에 나을 지도 모르겠지만 일단 테스트 중...

https://github.com/AppImage/AppImageKit

여기의 AppImage Tool 이다.  `appimagetool-x86_64.AppImage` 


appimage-builder 도 있는데 문서는 이쪽에 있으며 
https://appimage-builder.readthedocs.io/en/latest/intro/install.html#intro-install
위의 프로그램과는 다른 프로그램. 파라미터 등도 다르다.



## appimagetool
먼저 프로젝트를 구성해준다. 실행할 디렉토리를 만들고 필요한 파일을 복사 시키고, 물론 실행 파일도 이동(복사) 해준다.  

다큐먼트

https://docs.appimage.org/packaging-guide/from-source/linuxdeploy-user-guide.html



AppRun -- shell script 파일
```sh
#!/bin/bash
CUR_PATH=$(readlink -f "$0")
HERE=${CUR_PATH%/*}
EXEC="${HERE}/usr/bin/appimage-vnc_connector"
exec "${EXEC}"
```

usr/bin 에 실행파일 넣어주기,  --- AppRun 파일에서 실행시키는 파일명이랑 동일하면 되겠다.

desktop 파일
```
[Desktop Entry]
Name=vnc_connector
Exec=appimage-vnc_connector
Icon=vnc-connector
Type=Application
Categories=Utility
```

아이콘 파일은 png 파일로 크기는 256*256 






## 실패

빌드는 해서 성공했지만, 역시 
```
/tmp/.mount_vnc_co8d4UkU/usr/bin/appimage-vnc_connector: error while loading shared libraries: libQt6Quick.so.6: cannot open shared object file: No such file or directory
```

에러 발생.. 역시 shared library 까지 알아서 만들어 주지는 않는 듯 하다. 다시 시도해보자.

ldd 후 카피해주는 명령어 
```
cp $(ldd `pwd`/usr/bin/appimage-vnc_connector | awk '$2 == "=>" { print $3 }') `pwd`/testlib
```
> `pwd` 현재 위치이므로 일단 cd로 이동 후 적절히 명령 수행  

> `awk` 명령어는 특정 패턴을 찾아서 출력 등을 할 수 있다.  awk 프로그래밍이 있을 정도로 꽤 많은 기능을 제공 (키워드, 변수 등..)   
예를 들어 아래는 ldd 로 나온 출력   
```
libQt6Quick.so.6 => /home/myuser/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Quick.so.6 (0x00007f1f5be00000)
libyaml-cpp.so.0.7 => /lib64/libyaml-cpp.so.0.7 (0x00007f1f5bdaf000)
libQt6QmlModels.so.6 => /home/myuser/qtc_sdk/6.4.0/gcc_64/lib/libQt6QmlModels.so.6 (0x00007f1f5bce6000)
```
ldd 를 통해 나온 결과를 awk 로 넘겨줘서 사용할 수 있게 하고    
$2 는 패턴의 2번째를 의미 "=>" 스트링이 있다면 $3 인 3번째의 내용을 출력하라는 내용. 이제 cp 명령어와 결합이 되면  마지막 경로로 copy가 된다    
> 심볼링 링크의 so 파일들을 복사하게 된다.  


심볼릭 링크 확인. 참고만 하자.. 위의 명령어 사용법과 같다.  
대신 **실제 파일들을** 복사하면 **안 되는 듯** 하다. shared object file 을 찾지 못한다.  
```
ls -li $(ldd `pwd`/my_app | awk '$2 == "=>" { print $3 }')
```

appimage 파일에서 압축을 풀어준다. 
`./your-app.AppImage --appimage-extract`

잘 만들어졌는지 확인할 경우에 쓰일 수 있을 듯 하다.

아직까지는 파일도 잘 만들지만, lib 파일도 포함해서 이제는 36MB 정도 되는데, 압축을 반대로 풀어봐도 해당 라이브러리 등이 잘 있다.   

단 ubuntu 에서 실행했을 경우에 아직도 
```
/tmp/.mount_vnc_coANvYaw/usr/bin/appimage-vnc_connector: error while loading shared libraries: libQt6Quick.so.6: cannot open shared object file: No such file or directory
```

해당 디렉토리를 찾지는 못한다.;;



linux-vdso.so.1 (0x00007fca92fc2000)
	libQt6Quick.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Quick.so.6 (0x00007fca92800000)
	libyaml-cpp.so.0.7 => /lib64/libyaml-cpp.so.0.7 (0x00007fca92f4e000)
	libQt6QmlModels.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6QmlModels.so.6 (0x00007fca92737000)
	libQt6Qml.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Qml.so.6 (0x00007fca92000000)
	libQt6Network.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Network.so.6 (0x00007fca9258e000)
	libQt6OpenGL.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6OpenGL.so.6 (0x00007fca92eac000)
	libQt6Gui.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Gui.so.6 (0x00007fca91600000)
	libQt6Core.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Core.so.6 (0x00007fca90e00000)
	libGLX.so.0 => /lib64/libGLX.so.0 (0x00007fca91fcf000)
	libOpenGL.so.0 => /lib64/libOpenGL.so.0 (0x00007fca92569000)
	libstdc++.so.6 => /lib64/libstdc++.so.6 (0x00007fca90a00000)
	libm.so.6 => /lib64/libm.so.6 (0x00007fca9151c000)
	libgcc_s.so.1 => /lib64/libgcc_s.so.1 (0x00007fca91fa1000)
	libc.so.6 => /lib64/libc.so.6 (0x00007fca9080f000)
	libxkbcommon.so.0 => /lib64/libxkbcommon.so.0 (0x00007fca914d5000)
	libGL.so.1 => /lib64/libGL.so.1 (0x00007fca90d8c000)
	libpthread.so.0 => /lib64/libpthread.so.0 (0x00007fca92ea5000)
	/lib64/ld-linux-x86-64.so.2 (0x00007fca92fc4000)
	libdl.so.2 => /lib64/libdl.so.2 (0x00007fca92e9e000)
	libgssapi_krb5.so.2 => /lib64/libgssapi_krb5.so.2 (0x00007fca91480000)
	libz.so.1 => /lib64/libz.so.1 (0x00007fca90d6b000)
	libEGL.so.1 => /lib64/libEGL.so.1 (0x00007fca90d5a000)
	libfontconfig.so.1 => /lib64/libfontconfig.so.1 (0x00007fca90d0a000)
	libX11.so.6 => /lib64/libX11.so.6 (0x00007fca906ca000)
	libglib-2.0.so.0 => /lib64/libglib-2.0.so.0 (0x00007fca9057c000)
	libQt6DBus.so.6 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6DBus.so.6 (0x00007fca904b8000)
	libfreetype.so.6 => /lib64/libfreetype.so.6 (0x00007fca903ef000)
	libgthread-2.0.so.0 => /lib64/libgthread-2.0.so.0 (0x00007fca92e97000)
	libicui18n.so.56 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libicui18n.so.56 (0x00007fca8fc00000)
	libicuuc.so.56 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libicuuc.so.56 (0x00007fca8f600000)
	libicudata.so.56 => /home/sgtfedmsi/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libicudata.so.56 (0x00007fca8da00000)
	librt.so.1 => /lib64/librt.so.1 (0x00007fca92e90000)
	libXext.so.6 => /lib64/libXext.so.6 (0x00007fca90cf6000)
	libGLdispatch.so.0 => /lib64/libGLdispatch.so.0 (0x00007fca90c7d000)
	libkrb5.so.3 => /lib64/libkrb5.so.3 (0x00007fca90327000)
	libk5crypto.so.3 => /lib64/libk5crypto.so.3 (0x00007fca90c66000)
	libcom_err.so.2 => /lib64/libcom_err.so.2 (0x00007fca90320000)
	libkrb5support.so.0 => /lib64/libkrb5support.so.0 (0x00007fca90310000)
	libkeyutils.so.1 => /lib64/libkeyutils.so.1 (0x00007fca90309000)
	libcrypto.so.3 => /lib64/libcrypto.so.3 (0x00007fca8d400000)
	libresolv.so.2 => /lib64/libresolv.so.2 (0x00007fca902f7000)
	libxml2.so.2 => /lib64/libxml2.so.2 (0x00007fca90199000)
	libxcb.so.1 => /lib64/libxcb.so.1 (0x00007fca9016e000)
	libpcre2-8.so.0 => /lib64/libpcre2-8.so.0 (0x00007fca900ce000)
	libdbus-1.so.3 => /lib64/libdbus-1.so.3 (0x00007fca8fbac000)
	libbz2.so.1 => /lib64/libbz2.so.1 (0x00007fca900ba000)
	libpng16.so.16 => /lib64/libpng16.so.16 (0x00007fca8fb72000)
	libharfbuzz.so.0 => /lib64/libharfbuzz.so.0 (0x00007fca8fa56000)
	libbrotlidec.so.1 => /lib64/libbrotlidec.so.1 (0x00007fca900ac000)
	libselinux.so.1 => /lib64/libselinux.so.1 (0x00007fca8fa29000)
	liblzma.so.5 => /lib64/liblzma.so.5 (0x00007fca8f9f6000)
	libXau.so.6 => /lib64/libXau.so.6 (0x00007fca900a4000)
	libsystemd.so.0 => /lib64/libsystemd.so.0 (0x00007fca8f512000)
	libgraphite2.so.3 => /lib64/libgraphite2.so.3 (0x00007fca8f9d6000)
	libbrotlicommon.so.1 => /lib64/libbrotlicommon.so.1 (0x00007fca8f4ef000)
	libcap.so.2 => /lib64/libcap.so.2 (0x00007fca8f9c9000)
	liblz4.so.1 => /lib64/liblz4.so.1 (0x00007fca8f4ce000)
	libzstd.so.1 => /lib64/libzstd.so.1 (0x00007fca8f40f000)





우분투에서는 일단 linuxdeploy-x86_64.AppImage 프로그램으로는 빌드는 성공, 물론 실행은 안 되지만, shared lib 못 찾는다는 에러는 없어졌다.  

> 참고로 fedora40 에서는 버전이 너무 높아서 인지, appimage로 빌드가 될 때 shared libs 를 가져오는데 이때 실패한다. 


실행은 --appdir 로 디렉토리 넣어주고, --output 넣어주기  
usr/lib 디렉토리를 만들 필요는 없다. (shared libs 를 일일이 복사할 필요 없음)   
만약 만들다가 실패하게 되면 usr/bin에 있는 파일 자체가 이상해진다. 이후 실행도 안되서 다시 실행파일을 복사해서 사용해야 한다. 

거의 appimagetool 과 마찬가지로 디렉토리 구조는 비슷 하다.

Icon에 png 확장자 넣지 않음. 역시 Exec 에서 실행파일명도 맞춰준다.


다른점은 appimagetool 에서는 icon, desktop 파일은 AppDir 의 최상위 경로에 넣어주면 되었는데, 여기에서는 찾지를 못함. 단 파일은 만들어짐
usr/lib 디렉토리도 잘 만들어 준다.
```
./linuxdeploy-x86_64.AppImage --appdir vnc-connector.AppDir/ --output appimage
```
이렇게 하면 실행 파일이 만들어진다.  


단, 에러 발생
```
qt.qpa.plugin: Could not find the Qt platform plugin "xcb" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
```

세그먼트 폴트 에러 발생하면서 프로그램이 바로 죽는다.  
LD_LIBRARY_PATH 를 추가해주면 되기는 하지만, 이것도 qt creator 및 qt sdk가 있기 때문에 가능   
```
export LD_LIBRARY_PATH=/home/myuser/qtc-sdk/6.6.0/gcc_64/lib:$LD_LIBRARY_PATH
```
추가해주면 잘 실행이 되지만, 실제 qt가 없는 곳에 배포를 하면 당연히 안 될 듯 하다..(아마도..)


dlopen(): error loading libfuse.so.2

AppImages require FUSE to run. 
일 경우에 
```
sudo apt install libfuse2
```

페도라 경우 
```
sudo dnf install fuse fuse-libs
```
그래도 안 될 경우 지웠다가 다시 설치해본다.  


fuse: failed to exec fusermount: No such file or directory

```
sudo apt install fuse
```

LD_LIBRARY 환경 변수를 설정하지 않으면 usr/lib 에 있는 파일을 사용하지를 못한다.
```
/tmp/.mount_vnc_cowDAUWU/usr/bin/appvnc_connector: error while loading shared libraries: libQt6Quick.so.6: cannot open shared object file: No such file or directory
```

```
#export LD_LIBRARY_PATH="$APPDIR/usr/lib:$LD_LIBRARY_PATH"
```
이런식으로 넣어줘야 함. 스크립트 파일에 넣어주기 (AppRun파일)

단 이렇게 해주면 qt 관련 so 파일은 찾지만 새로운 에러 발생함

++.so.6: version `GLIBCXX_3.4.32' not found (required by /tmp/.mount_vnc_coBidr43/usr/lib/libyaml-cpp.so.0.7)


새로운 에러 일단, libstdc++ 버전이 달라서 그러는 듯 하다. 
```
/tmp/.mount_vnc_coNEReOF/usr/bin/appvnc_connector: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by /tmp/.mount_vnc_coNEReOF/usr/bin/appvnc_connector)
/tmp/.mount_vnc_coNEReOF/usr/bin/appvnc_connector: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_ABI_DT_RELR' not found (required by /tmp/.mount_vnc_coNEReOF/usr/lib/libyaml-cpp.so.0.7)
/tmp/.mount_vnc_coNEReOF/usr/bin/appvnc_connector: /lib/x86_64-linux-gnu/libstdc++.so.6: version `GLIBCXX_3.4.32' not found (required by /tmp/.mount_vnc_coNEReOF/usr/lib/libyaml-cpp.so.0.7)
/tmp/.mount_vnc_coNEReOF/usr/bin/appvnc_connector: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_ABI_DT_RELR' not found (required by /tmp/.mount_vnc_coNEReOF/usr/lib/libglib-2.0.so.0)
/tmp/.mount_vnc_coNEReOF/usr/bin/appvnc_connector: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by /tmp/.mount_vnc_coNEReOF/usr/lib/libglib-2.0.so.0)

```

아래를 명령어를 ubuntu22 에서 해보면
```
strings /usr/lib/x86_64-linux-gnu/libstdc++.so.6 | grep GLIBCXX
```
GLIBCXX_3.4.30  .. 아마도 Fedora 버전이 너무 높은 듯 하다.   


### qt plugin
깃허브  
https://github.com/linuxdeploy/linuxdeploy-plugin-qt   

qt plugin 을 이용할 수 있다고 하는데, 사용법은 간단하지만 플러그인을 못 찾으면서 에러가 발생,   
(위의 LD_LIBRARY_PATH 와는 상관없이)    

https://github.com/linuxdeploy/linuxdeploy-plugin-qt/releases/tag/1-alpha-20240109-1


사용법은 간단하다. linuxdeploy-plugin-qt 파일을 실행가능하게 해주고, (이 파일로 실행하지는 않음;)  
실제로는 linuxdeploy 프로그램을 이용한다. 파라미터로 --plugin qt 이렇게만 해주면 된다 

예
```
/linuxdeploy-x86_64.AppImage --appdir vnc-connector.AppDir/ --plugin qt --output appimage
```
아직까지는 실패, 잘 모르겠다.


qt plugin은 /usr/bin/qmake 에서 찾는 듯 하다.;;;  
일단 내 버전은 거기가 아니긴 하고, qmake도 안 사용하지만 어쨋든.. 

```
[qt/stdout] Found Qt modules:  
[qt/stdout] Extra Qt modules:  
[qt/stdout] ERROR: Could not find Qt modules to deploy 
```
이거를 경로? 수정 할 수 있는 방법은 아직 모르겠다. extra-plugin 을 해봤지만 안 되는 듯 하다.



linuxdeployqt 로 만든 후에 execv error: Permission denied 가 발생하는 경우에는  
AppRun 스크립트 파일의 실행 권한이 없을 경우일 수 있다. 


