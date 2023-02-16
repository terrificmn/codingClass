
qt creator 에서 application을 qt quick application으로 생성

> build 시스템은 cmake, qmake  
> 아직 cmake로 하면 어떻게 해결하는지 모르겠음;;;
> qmake로 하면 쉽게 됨

minimum required qt version은 5.15 이상 

상관없는 듯 

Kits 설정이 중요 

Qt version은 qt 6.3.0(gcc_64) 버전으로 맞춰준다 . qt_default로 설치한 qt5로 선택하게 되면   
widget application은 잘 되나, qt quick은 안됨  

> 기존의 Kits가 있으면 큰론으로 새롭게 만든 후에 버전만 6.3 이후로 선택해주면 된다   
> 나머지 cmake, g++ 등은 다 같다(기본)


> 6.3버전은 직접 빌드하는 방식으로 설치를 했었을 때 생긴 파일들임

