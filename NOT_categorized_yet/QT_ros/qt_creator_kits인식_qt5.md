snap stable 버전으로 설치한 Qt Creator 8.0.1 버전, Qt 6.2.4 버전 기준
Rocky Linux 기준

Project를 새로 만들려고 할 때
Kits 섹션에서 Kit Selection 에서 인식되는 kits 가 나오는게 없다. 비활성화되어 있음


## Rocky linux 에서 kits / desktop / version 설정 
먼저 qt 공식 홈에서 받은 open source 버전은 지움 (용량이 너무 큼 15.5GB)

qtcreator_ros (snap으로 설치한 것도 지움)   

> 버전은 qt creator 4.12.4, Qt 5.15.2

dnf로 설치 qt5 및 디버거 설치
```
sudo dnf install qt5-*-devel qwt-qt5-devel
sudo dnf install gdb
```

>  qt5 관련 패키지를 설치를 해야지 qmake 파일등을 설정할 수 있는 듯 하다

qt-creator 설치
```
sudo dnf install qt-creator
```

qt-creator 버전은 4점 대, 기존에 비해 버전은 느리지만 qt은 5를 사용한다 

Tool -> Options 클릭  
Qt  Versions 탭으로 가서 Add 버튼으로 지정을 해준다  
경로는 `/usr/bin/qmake-qt5`  
그리고 Kits 탭으로 돌아가면 Desktop을 선택해주고   
Qtd version을 Qt 5.12.2 를 선택해준다  

/usr/lib64/qt5/bin/qmake  경로에도 있음


이제 새로운 프로젝트를 실행하면 Design 폼에서 버튼 등을 만드는 것도 잘 되고  

빌드를 (망치 아이콘 - 왼쪽 하단) 한 후에 녹색 세모 버튼을 누르면 실행도 잘 된다  


___
### ubuntu 에서 qtcreator Kits 설정
우분투에서는 snap 또는 run파일을 다운 후 qtcreator_ros를 사용함

qtcreator설치 참고 

ubuntu에서도 마찬가지로 데스크탑에 ! 아이콘이 떠있거나하면 먼저 version을 제대로 설정 (path)를 잘 지정해줘야 한다   

만약 우분투에서는 qmake 파일이 없다면
```
sudo apt install qt5-default
```

Edit > Preferences 를 누르면 처음 Kits 라는 섹션이 보이고   
Qt Versions 탭에서 Add를 눌러준다  

/usr/lib/x86_64-linux-gnu/qt5/bin/qmake   

경로로 잘 지정해준다  

만약 경로가 없거나 틀리면  

```
find / -name qmake >  res
cat res
```
qmake 파일을 찾아보자

버전을 확인 되었다면   
Apply를 눌러준 후에 처음의 Kits 탭으로 이동  
Manual에 추가가 되어 있는 Desktop (default)를 클릭 후에   
Qt version을 선택해준다. 앞서 qt version을 선택 안 했을 시에는 선택이 안됨   
Qt 5.15.2 (qt5) 를 선택해준다  

이제 마지막으로 Apply를 눌러주고 다시 New Project를 만들어 보자  


## New Project
New Project 에서 Application (Qt) 로 만들고 Qt Widgets Application 으로 만들어 준다   

qt에서의 Project는 ros의 패키지와 비슷한 것 같다.   
패키지의 이름과 Location을 정해주는데 여기에서의 이름이 패키지처럼 만들어진다   
> 예를 들어서 프로젝트의 네임은 myproject,  dir위치를 
 /home/myuser/Workspace/qt_ws  처럼 만들었다면    
 해당위치에 하위에 myproject 디렉토리로 만들어진다  
 이런식으로 프로젝트(패키지) 하나씩 만들면 될 듯

이제 Kits 섹션에서 Desktop를 선택할 수 있다 




___

## qt quick 프로젝트 할 때
kit을 지정할 때 버전을 6.2 이상으로 변경해준다   

처음 프로젝트 만들 때 최소 버전은 5. 혹은 6.2 상관없으나, kit 자체를 버전 6.2를 사용할 수 있게 해줘야한다  

안 그러면 No kits found 식으로 나오게 된다   


처음 만들 때 빌드 시스템을 cmake로 만들면   
문제발생: No CMake configuration found!  아직 문제 해결은 못함  

대신  
qmake로 하면 런까지 하는데 문제가 없다  



