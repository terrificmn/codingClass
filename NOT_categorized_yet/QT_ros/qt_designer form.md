File > New file 선택 후

template 중에서 Qt를 선택해준다  
Qt Designer Form Class를 선택하면 헤더파일도 만들어주게 된다  
Widget를 선택해준다  

이제 Class name, Header file, Source file, Form file, Path 등을 선택해주는데   

Ros의 네이밍 컨벤션을 따라준다면  
class는 카멜 케이스로 만들어주고  
나머지 Header file, Source file, Form file 은  스네이크 케이스로 만들어준다   

예를 들어   
MyQtTest 로 클래스 명을 만든다면  
나머지 파일들은 my_qt_test.h, my_qt_test.cpp, my_qt_test.ui 등으로 만들어주면 좋다  

> 버그일지도 모르겠으나 path 설정에서 파일 열기로 진행이 안된다  
> 일단 path에 직접 경로를 입력해준다 
> 예:) $HOME/catkin_ws/src/my_package/include/my_package

그리고 특히 snap 버전은 경로 설정이 잘 안되는 문제가 발생하는 것 같음  
(kits에서 desktop을 설정하게 되면 잘 되기도 하나 다른 qrc 파일등을 불러올 때 경로 설정이 잘 안됨)

결론: qtcreator설치 를 확인하자

일단 파일들이 만들어지고 design 폼이 열리게 되는데 먼저 cpp파일을 현재 패키지의 src 디렉토리로 이동을 시켜준다   

그리고 scr 디렉토리에 ros cpp 파일을 추가해서 사용하면 된다.  

왼쪽의 파일 디렉토리 화면에서 마우스 오른쪽 버튼을 눌러서 Add file

