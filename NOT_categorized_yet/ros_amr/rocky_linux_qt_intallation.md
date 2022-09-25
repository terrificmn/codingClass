```
 sudo dnf install qt5-*-devel qwt-qt5-devel
 sudo dnf install gdb
```

이렇게 해주면 kit설정에서 debug와 desktop 버전이 제대로 나온다  
데스크탑에서 물음표 아이콘이 나온 것은 debug와 version 설정이 제대로 안되었던 것...   

opensource 버전 qt도 설치를 해보았는데  
일단 공식 홈에서 qt 설치 - 용량 꽤 많이 차지함 약 15GB이상  

결과는 qt_creator 만 있어도 되는 듯   
빌드를 하고 실행하면 윈도우 화면을 볼 수가 있고  
다만 디버깅을 하게 되면 디버그쪽 문제가 있는 듯 하다~ 빌드 관련 디렉토리가 생성이 안되서 생기는 문제로 보임  (권한 문제?)

그리고 qt는 waylands도 지원하지만    
qtcreator_ros 플러그인은 x-11 디스플레이에서만 사용이 가능한 듯 하다    
(원래 wayland에서도 잘 작동하지만, qt 정식 버전은 wayland에서 잘 실행됨 )   
그래서 디자인모드에서 버튼등을 넣을 수가 없다.  qt단 x 디스플레이로 로그인하면 잘 된다..    
하짐나 wayland를 주로 사용해서 일단 그냥 qt creator를 사용하고 ros 관련은 ubuntu에서 해결 (사용)하는게 깔끔하겠다. 

