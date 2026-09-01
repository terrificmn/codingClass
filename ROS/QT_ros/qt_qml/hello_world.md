
## function 사용
function 사용하기  JavaScript와 비슷한 문법이지만, 완전히 같은 문법은 아닌듯 하다   
예를 들어 `() => {  }` 이런식은 안되는 듯 하다
```js
import QtQuick

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Rectangle {
        x: 100; y: 100
        height: 100
        width: funcExample()
        color: "lightblue"

        function funcExample() {
            console.log("Hello World");
            return height * 2;
        }
    }
   // set order is important. because it will be layered . overlapped
    // Property  over F1
    Rectangle {
        x: 100; y: 170; z: -1  // z -1 current Rectangle will be forward  z coordinate라고 생각하면 된다. 
        height: 100
        width: 200
        color: "green"
    }

    Text {
        text: "hello world"
    }
}

```

##  declarative programming language  
TextInput의 propety 인 id를 textElement를 해서 다른 Property에서 사용을 하는데   
여기에서는 Rectangle의 width가 TextInput의 width의 값을 사용한다고 되어 있다. 즉, property가 서로 연결(?)이 되어 있다  
이를 Propety Binding라고 하는데   
QML에서는 그래서 TextInput 는 입력을 할 수가 있는데 창에서 입력을 하면 width가 변경이 되고   
이게 바로 Rectangle 의 width에 연결이 되어서 Rectangle도 길이가 변경하는 것을 볼 수가 있다

```js
import QtQuick

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    TextInput {
        id: textElement
        x: 50; y: 25
        text: "Qt Quick"
        font.pixelSize: 50
    }

    Rectangle {
        x: 50; y: 75
        height: 5
        width: textElement.width
        color: "lightblue"
    }

}

```

QML은 declarative programming language  

바로 Rectangle의 사이즈가 TextInput 사이즈랑 같게 하고 하려고 하는 것을 Declarative라고 하는 듯 하다 

`width = 400`  이것은 assignment 할당이 되는데, 

QML에서는 Property Binding 이므로 할당이 아니다.
`width: 400`

