# qt deployment
다른 컴퓨터에서 실행 파일을 실행하려면  
shared library 파일들이 필요한데  

리눅스에서는 **ldd** 명령어로 실행파일을 확인하면 어떤 라이브러리를 사용하는지 알 수 있다. 

```
ldd my_app
```

예..

```
linux-vdso.so.1 (0x00007fd7846ee000)
	libQt6Quick.so.6 => /home/myuser/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Quick.so.6 (0x00007fd784000000)
	libyaml-cpp.so.0.7 => /lib64/libyaml-cpp.so.0.7 (0x00007fd783faf000)
	libQt6QmlModels.so.6 => /home/myuser/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6QmlModels.so.6 (0x00007fd783ee6000)
	libQt6Qml.so.6 => /home/myuser/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Qml.so.6 (0x00007fd783800000)
	libQt6Network.so.6 => /home/myuser/qt-sdks/qtc_sdk/6.4.0/gcc_64/lib/libQt6Network.so.6 (0x00007fd783657000)
```

이후 실제 so 파일들을 복사해서 하나의 디렉토리 안에 넣어준다. 예를 lib



## office qt-installer-framework 
[다운로드는 여기에서](https://download.qt.io/official_releases/qt-installer-framework)

4.8.0 버전으로 다운로드 - linux x64 버전으로 다운로드 한다. 


이제 해당 프로그램으로 binary 프로그램을 만들 수가 있다.

먼저 해당 프로그램으로 자신의 데스크탑에 설치를 해준다.

기본으로 다음다음 눌러서 설치를 한다면 
`QT/QtIFW-4.8.0` 에 설치가 되고, 해당 경로에 uninstall 등이 있다.   
bin 이하 디렉토리에 binarycreator 프로그램이 있다.


### 자신의 프로젝트 셋팅 
구조는 vnc_connector 테스트 압축 파일의 구조를 참고

config.xml, package.xml 등의 파일을 다 만들었다면 다시 위의 qt-installer-framework 를 이용해서 installer를 만들어 주는데  

package.xml 에서 Licenses 태그와 Script 태그를 주석처리해서 사용함   



해당 디렉토리로 이동 후 명령 실행   
```
cd ~/Qt/QtIFW-4.8.0/bin
./binarycreator -c ~/자신의프로젝트-디렉토리/config/config.xml -p ~/자신의프로젝트-디렉토리/packages/ installerTest
```

일단 해당 디렉토리에서 installerTest 라는 실행파일이 생긴다.   
> 물론 installerTest 는 실행파일 installer프로그램 이름이다. 아무거나 상관 없음

이제 installerTest 파일만 있으면 되는 셈인데,   
이를 다른 컴퓨터에 복사한 후에 실행을 하게 되면  

어디에 설치할 지 묻는 화면부터 해서 next next로 설치를 할 수가 있다. 


일단 첫 번째 도전은 실패.   libgc 버전이 달라서 실패한 듯 한데... 

TODO: 좀 더 연구해보자


```
./appvnc_connector: libc.so.6: version `GLIBC_2.34' not found (required by /lib/x86_64-linux-gnu/libGLdispatch.so.0)
./appvnc_connector: libc.so.6: version `GLIBC_2.33' not found (required by /lib/x86_64-linux-gnu/libkrb5.so.3)
./appvnc_connector: libc.so.6: version `GLIBC_2.34' not found (required by /lib/x86_64-linux-gnu/libkrb5.so.3)
./appvnc_connector: libc.so.6: version `GLIBC_2.33' not found (required by /lib/x86_64-linux-gnu/libk5crypto.so.3)
...생략
```
