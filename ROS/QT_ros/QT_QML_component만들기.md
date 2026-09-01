# QML component 만들기

먼저 사용자 컴포넌트를 만들기 위해서 자주 사용할 만한 QML Type을 가져다가 만들어주고   
파일명은 사용할 이름과 같게 해서 만들어 준다. **대문자로 시작**해야한다(파일명)   

```js
import QtQuick

Rectangle {
    border.color: "green"
    color: "white"
    radius: 4; smooth: true  
    clip: true

    TextInput {
        anchors.fill: parent
        anchors.margins: 2
        text: "Enter text..."
        color: focus ? "black" : "gray"
        font.pixelSize: parent.height - 4
    } 
}
```

> 그리고, 파일은 main.qml 이 있는 곳; 패키지의 root 디렉토리 안에 만들어 준다  

## CMakeLists.txt 파일에 등록
CMakeLists.txt 파일에 qt_add_qml_module() 함수를 이용해서 파일을 등록해줘야한다   

QT 버전 6.2 이고, cmake로 빌드하는 경우이다.  qmake 경우에는 잘 모름   

```c
qt_add_qml_module(appqtquick_hello
    URI qtquick_hello
    VERSION 1.0
    QML_FILES main.qml 
    QML_FILES LineEdit.qml
)
```

## main.qml에서 사용
해당 Component를 QML Type을 사용하듯이 사용하면 된다 

QT 6.2에서는Window를 먼저 만들어야 하나보다.  일단 5.10 예제에서는 (좀 시간이 많이 지남)   
QtQuick import 후에 하는데.. (흠.. 다른방법이 있을 수도 있다)

```js
import QtQuick

Window {
    width: 400
    height: 100
    visible: true

    Rectangle {
        width: 400; height: 100
        color: "lightblue"

        // 먼저 만들었던 Component를 사용하게 된다
        LineEdit {
            anchors.centerIn: parent
            width: 300; height: 50
        }
    }
}
```

이렇게 하면 잘 작동한다. 이렇게 응용하면 굉장할 듯 하다!

> 잘 안될 시에는, 새 프로젝트로 만들고, 거기에 이 파일들을 다시 넣어서 다시 시작하면 된다. 