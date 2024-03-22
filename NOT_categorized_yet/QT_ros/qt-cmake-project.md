# qt5 이용해서 cmake 빌드로 만들기
기존 qtcreator 를 이용하게 되면 버전 6.2 이상 이다.  
qt quick 을 이용해서 개발을 할 때 기존의 만들어진 Release 버전 실행 버전으로는   
단독 실행이 안되는 것을 확인했다. qtcreator 를 설치를 해서 다시 빌드를 해줘야지 해당 프로그램을 사용할 수가 있었다.  

아직 테스트 해보지는 못했지만, cmake 빌드 시스템 및 qt버전을 낮춰서 진행하면 실행 파일만으로  
우분투, 페도라 등의 시스템에 배포를 할 수 있게 하는 게 목표다!

> 물론 이게 되는지는 모르겠다. 아직 테스트 못 해봄. 
페도라, 우분투 등에서는 qt5.15 버전을 쉽게 설치할 수 있다.(dnf, apt 이용)  

## Qt Quick Application (compat)
New Project를 열어서 진행  

*Qt Quick Application (compat)*   
주요 기능은 qmake 외에 CMake 빌드 시스템을 사용할 수가 있고, QT6 버전 이하를 사용할 수가 있다.   

qt_creator_kits인식_qt5.md 파일을 참고해서 Kit를 추가

minimum required Qt version 은 Qt 5.15 로 지정 한다.

Kit은 qt5가 적용된 kit을 선택해준다.

