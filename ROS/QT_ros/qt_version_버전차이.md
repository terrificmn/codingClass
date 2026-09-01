현재 Rocky Linux에서 사용하는 Qt Creator 버전이 좀 낮다 

Qt Creator 4.12.4  
Qt 5.15.2

여기에서 만든 것을 상위 버전에서 적용하면 kits의 Desktop이 변경이 되는데  
이렇게 되면 이제 하위 버전에서는 에러가 발생하는 듯 하다.  

좀 더 확인해 볼 것

QT 정식버전은  
Qt Creator 8.0.1  
Qt 6.3.1

(우분투 기준)
Qt creator ros 버전
Qt Creator 8.0.1  
Qt 5.12.8 또는 Qt 6.2.4 (현재 5.12버전 사용)



## No valid settings file could be found.  
디렉토리가 다르므로 CMakeLists.txt.user 파일에서 경로와 버전등이 맞지 않아서 나오는 문제   
Kit 을 재설정

qt 버전 5.12 / 5.15 를 사용했을 경우 ubuntu에서도 잘 된다  
단, kit 버전을 5로 다시 설정해주고, cmake 등 초기화가 안될 경우에는 초기화를 시켜주면 잘 됨

우분투에 설치한 QtQuick 같은 경우 2.15 버전은 설치가 안되어 있을 경우는 안됨. (2.12버전이 설치되어 있음)  
Rocky Linux에는 2.12, 2.15 다 되는 듯..   

qt 버전 6.3은 ubuntu에서 다시 실행할 때 kit버전 6으로 설정 후에 하면 역시 실행에는 문제 없음
> 프로젝트를 만들 때 최소 버전 선택한 것



QT 5.15 LTS
QT 6.2 LTS
나머지 버전은 short term 인 듯 하다   

라이센스는 LGPL 및 상업용 둘 중에 하나 사용가능  
qt 라이브러리를 다이나믹 라이브러리로(리눅스 so)사용시에는 공개 필요가 없다고 하는 데   
자세한 룰은 복잡한 듯 하다;;;

