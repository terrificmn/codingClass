ubuntu에서 qtcreator_ros 버전이 안된느 경우.md 지울
# qt / qtcreator 설치

우분투 기준 
- Qt 공홈에서 opensource버전 다운 후 설치
- qtcreator-ros 버전으로 snap으로 설치
- qtcreator-ros 버전 깃클론 후 빌드하기
- apt 패키지를 이용해서 설치

이중에서 가장 추천 방법은 **qtcreator-ros 버전 깃클론 후 빌드하기**  
아니면 qt 공홈에서 다운 후 설치  

왜냐하면 다른 방법들은 결국 자잘한 문제가 발생해서 잘 안됨 

*Rock Linux에서는 qt공홈에서 받아서 사용(qt_creatro만으로 잘 안되는 듯 하다.)    
또는 dnf 패키지매니저로 설치한다


### ROS qt creator ubuntu18.04 버전으로도 설치가 가능

현재 우분투 20.04 이나 설치 가능 

[https://ros-qtc-plugin.readthedocs.io/en/latest/_source/How-to-Install-Users.html여기에서 다운로드](https://ros-qtc-plugin.readthedocs.io/en/latest/_source/How-to-Install-Users.html)

[Bionic Online Installer](https://qtcreator-ros.datasys.swri.edu/downloads/installers/bionic/qtcreator-ros-bionic-latest-online-installer.run) (Recommended) 이 권장이지만  
무슨 문제인지는 몰라도 실패

[그래서 Bionic Offline Installer 로 용량이 좀 더 크지만 다운 후 설치 잘 됨 ](https://qtcreator-ros.datasys.swri.edu/downloads/installers/bionic/qtcreator-ros-bionic-latest-offline-installer.run)


New file or Project > other project > Ros workspace 추가 
그리고 catkin_ws를 추가해주고  Workspace path 등을 설정해준다   

패키지는 catkin_create_pkg 로 만든 후에  
새로 파일들이 추가가 된다면  Projects 창에서 마우스 오른쪽 버튼을 눌러 Rebuild를 해준다 


빌드 할 때 에러 발생 하면 
```
no such file or directory #include QWidget
```

CMakeLists.txt 파일에  
```
find_package(catkin REQUIRED COMPONENTS
  roscpp std_msgs Qt5Widgets
)
```

Qt5Widgets 추가해준다 

[cmke와 qt5관련 읽어보기](https://www.kdab.com/using-cmake-with-qt-5/)

> 처음에는 cmake로만 해서 발생한 문제 인 듯 하다  qmake를 지정하고 qmake로 컴파일을 진행해도 된다  


찾아보면 
/usr/include/x86_64-linux-gnu/qt5/QtWidgets/QWidget   
여기에 설치가 되어 있는데 ...


#### 지우려면 
QtCreator 디렉토리에 가면 MaintenanceTool 파일이 있는데 실행을 해주면 된다   




##  snap으로 qtcreator 설치하기 (qtcreator-ros) 
Kits를 못 찾는 문제가 있지만 처음에 옵션에서 해결할 수 있는 듯 하다  
qt_creator_kits 인식 참고

snap을 이용해서 설치한다  
```
snap install qtcreator-ros --classic
```

지울 경우
```
snap remove  qtcreator-ros
```

Create Project > Other Project > ROS Workspace 를 선택해준다  
Project 이름은 catkin_ws의 이름과 같은 것으로 설정  
Build system은 Catkin Tools를 사용할 것이므로 선택   
Workspace는 선택해주거나 직접 입력 /home/{userid}/catkin_fund_ws/


Debug 메뉴에서 Start Debugging을 선택해서 attach to running application을 선택해주면  
이제 process로 돌아가고 있는 프로그램 목록이 뜨는데  
여기에서 실행하고 있는 노드를 선택해주면 된다



## QT 공식 홈에서 다운로드 후 설치하기 

[https://www.qt.io/download 공식 홈에서 다운로드/ 단 회원가입을 해야한다](https://www.qt.io/download)

아예 설치를 해주면 시간이 엄청 오래걸리지만~ 잘 됨   

최소 14GB 용량이 필요하고,  

opensource 버전으로 설치한다 


