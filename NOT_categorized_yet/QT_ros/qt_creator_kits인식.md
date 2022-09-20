snap stable 버전으로 설치한 Qt Creator 8.0.1 버전, Qt 6.2.4 버전 기준
Rocky Linux 기준

Project를 새로 만들려고 할 때
Kits 섹션에서 Kit Selection 에서 인식되는 kits 가 나오는게 없다. 비활성화되어 있음


Edit > Preferences 를 누르면 처음 Kits 라는 섹션이 보이고   
Qt Versions 탭에서 Add를 눌러준다  

그리고 qmake 파일은 연결해줘야하는데  
/usr/lib64/qt5/bin/qmake  경로에 있다 . 파일을 선택해준다 

> 아마도 우분투 기준에서는 /usr/lib/x86_64-linux-gnu/qt5/bin/qmake   
> qmake파일은 컴파일 하는데 사용이 된다

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

