## qt 다른 버전 빌드하기
먼저 qt5.15 는 apt, dnf 로 설치 참고


지금은 Qt 6.6까지 나왔는데   
6.2 kit으로 설정하고 싶을 경우에는 ros_qtc_plugin (깃허브) 로 설치할 수 있다.

먼저 클론 해주고
```
git clone https://github.com/ros-industrial/ros_qtc_plugin.git -b devel
```

해당 디렉토리로 들어가면 `cd ~/ros_qtc_plugin`
root 디렉토리 내에 version.yaml 파일이 있다. 여기에서 qtc_version, qt_version 을 변경 할 수 있는데  

qtc_version 은 qt creator 버전을 말하는 것이고  한단계 아래 버전을 하려면 변경  
> 버전이 원래 13이였는데 13로 12로 낮췄더니 qt 6.2 에서 ros플러그인 생생에서는 실패했다.  
하지만 6.2 빌드 자체는 잘 됨. qt 6.2 버전만 필요했으므로 추후 버전은 13으로 다시 시도?? 

qt_version 만 변경해주면 될 듯 하다. 
```
qt_version: "6.2"
qt_modules: ['qtbase', 'qtdeclarative', 'icu', 'qttools', 'qt5compat']
```

이후 qtcreator 직접 빌드 설치하기 ubuntu qtcreator_ros build install.md   
또는 rocky linux 에서 직접 build-qtcreator.md 등 참고


만약 그 전에 빌드를 이미 진행했다면 컴파일 에러 발생하는데 이미 빌드를 해서 파일들이 남아있어서 그렇다 
build 디렉토리를 백업해두자

```
mv build build_6-6-backup
```

> 추후 필요할 경우 사용.   

이후 빌드를 진행하면 /tmp/qtc-sdk 디렉토리가 생기는데, 이것을 원하는 장소로 이동 시켜준다.  
tmp에 생긴것이라 컴터 끄면 지워질 수 있음  
```
mv /tmp/qtc-sdk/6.2.0 ~/qtc_sdk/qtc-sdk/
```

이제 qtcreator 를 실행해서 Preferences 에서 Kits 설정을 추가로 만들어서 진행한다.   
Kits 에서 Qt Versions 탭에서 Add. 를 눌러서 추가를 하고  
이동 시켰던 디렉토리 6.2.0 에서 이하 bin 디렉토리에 있는 qmake6 파일을 선택해주고   
다시 Kits 탭으로 넘어와서 Kit을 추가한 후에 스크롤을 내려서 Qt version 에서   
Qt 6.2.0 (gcc_64) 를 선택해주면 된다. 

## qt 버전 고르기

프로젝트에서(디렉토리) CMakelist.txt 을 열어서 프로젝트를 여는 방식으로 주로 사용하는데  (qmake 빌드 대신)   
6.2 빌드로 진행하려면 한번 열었던 프로젝트라면   
CMakeLists.txt.user314 이런 파일을 지워준다.  
그러면 설정이 안되어 있다면서 qt kit 버전을 고르는 화면이 나오는데   

여기에서 원하는 버전을 골라서 진행해주면 된다. 예를 들어 Debug, Release 등의 디렉토리 설정을 할 수도 있다.  

결과적으로는 문제 없이 잘 빌드 된다.


## TODO
추후 빌드된 파일을 복사해서 사용해보기   
아마도 다른 컴퓨터에서 사용이 가능할지 모르겠다. 안될 가능성이 높다.  예를 들어 페도라 에서 우분투로   
아마도 다른 리눅스 디스트로 시스템이라면 빌드를 다시 해야할 수 있다.




