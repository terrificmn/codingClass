
## property  
property 를 정의한느 것에 대해서는 
[여기를 메뉴얼을 참고하자](https://doc.qt.io/qt-6.2/qtqml-syntax-objectattributes.html)

[default] [required] [readonly] property <propertyType> <propertyName> 요렇게 정의하게 되는데   

propertyType에는 int, color string, url 등이 있고   

Item {
    property int someNumber
    property string someString
    property url someUrl
}


var로 선언하게 되면 placeholder type이 되어서 어떤 타입이든 가질 수가 있다 (리스트, 오브젝트 포함)

```js
property var someNumber: 1.5
property var someString: "abc"
property var someBool: true
property var someList: [1, 2, "three", "four"]
property var someObject: Rectangle { width: 100; height: 100; color: "red" }
```

> 특정 타입이 명확할 경우에는 int, string 등 확실하게 정의해주는게 좋다   

**TODO 일단** 한 { } 블럭안에서만 property로 인식이 되고 블럭을 벗어나면, 또는 부모에서 정의해도   
자식이나, 블럭을 벗어나서는 `ReferenceError is not defined` 라고 나오게 되는데     
CPP에서 Q_PROPERTY 로 등록을 할 수가 있는지 그걸 꼭 해야하는지 테스트를 해봐야겠다 


```js
import QtQuick
Window {
    width: 400
    height: 400
    color: grey
    visible: true

    Rectangle {
        id: root
        x: 50; y: 50
        height: 150
        width: 300
        color: "orange"

        Rectangle {  // parent-oriented
            x: 50
            y: 50
            width: 50
            height:50
            color: "white"
        }
    }

    Rectangle {
        x: 50
//        y: 200  /// y를 직접 적어줄 수도 있지만, 상위 Property의 id를 이용해서 property를 지정해주는 것이 더 좋을 수도 있다
        y: root.y + root.height
        height: 150
        width: 300
        color: "yellow"
        clip: true   //child can't be off the position  
        //  clip은 원래 false 인데, 자식 element가 범위를 벗어날 수 없게 한다 
        // 기본설정에서는 마음껏 벗어나는게 가능하다 

        Rectangle {
            x: -50; y:50
            width: 150; height: 50
            color: "lightblue"
        }
    }
}

```

