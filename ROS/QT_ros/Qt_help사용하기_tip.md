# QT QML Quick tip 메뉴얼 보기

## F1
qml등에서 모르는게 있거나 알아볼려고 할 때   
웹사이트를 사용할 수도 있겠지만 IDE에서도 어느정도 볼 수 있게 구현이 되어 있다.   

원하는 QML Type에 커서를 위치 시키거나 마우스를 가져간 다음에 F1 키를 눌러주면 안내 화면이 나온다   

예를 들어 이런 `TextInput`, `Window`, `Rectangle` 등 것들..  

> QML Type 아니면 Element라고 하는게 맞는지 모르겠지만, 비슷한 개념들인 것 같기는 하다..  

예를 들어서 Window 로 가서 확인해보면   
Properties, Attached Properties, Signals, Methods, 등을 확인할 수가 있고 

자세히 보면 Window는 QQuickWindow에서 생성이 된 객체이고, QQuickWindow는 c++ 클래스 이고  
QWindow로 부터 상속받은 객체가 되겠다 (QWindows는 또 QObject로부터 상속(base class임))

## 안나오는 것들 확인하기
자동으로 연결되는 것들은 F1으로 확인이 되지만 안되는 경우도 많다   

이런경우에는 왼쪽 하단에 검색을 할 수 있는 입력 창이 있는데 (단축키: **Ctrl + k**)  
입력은 `?(스페이스바)<키워드>` 이런식으로 검색하면   

예를 들어 (대소문자 구별함)
```
? Key
```

엔터를 눌러서 자세한 내용을 볼 수 있고, 이는 꽤 유용하다

> ?는 help index를 보는 기능 



