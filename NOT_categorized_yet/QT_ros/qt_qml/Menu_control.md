# Menu Controls
일단 4종류   
Menu   
MenuBar  
MenuBarItem   
MenuItem


[Menu컨트롤 메뉴얼](https://doc.qt.io/qt-6.2/qtquickcontrols2-menus.html)


예제
```js
Button {
    id: button1
    text: "button"
    x: 200
    y: 500
    onClicked: menu.open()

    Menu {
        id: menu
        y : button1.height
        MenuItem
        {
            text: "Menu1"
        }
        MenuItem
        {
            text: "Menu2"
        }
        MenuItem
        {
            text: "Menu3"

        }
        MenuItem
        {
            text: "Menu4"

        }

    }
}
```