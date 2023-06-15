# MessageDialog
일단은 6.4- QT 6.3
[MessageDialog](https://doc.qt.io/qt-6.4/qml-qtquick-dialogs-messagedialog.html#icon-prop)

MessageDialog 를 통해서 버튼이 포함된 다이얼로그 메세지 창을 띄울 수가 있음  

예제를 통해서 buttons 을 property에 `buttons: MessageDialog.Ok | MessageDialog.Cancel` 처럼 쉽게 버튼을 표시 할 수가 있고   

이를 `OnAccepted: {}` property를 통해서 뭔가 처리하게 해줄 수가 있다. 

그리고 프로그램을 꺼야 할 경우에 창의 X 버튼을 누르면 MessageDialog가 뜨기도 전에 꺼져 버리는데  
이는 onClosing 메소드를 사용해서 `close.accepted = false` 로 줘서 일단 꺼지지 않게 해줄 수가 있다.  
이유는 기본으로 true로 되어 있기 때문에 X 버튼을 누르면 꺼지게 되는 것   

예
```
onClosing: {
    close.accepted = false  // 일단 꺼지지 않게 막아줌
    messageDialog.open()  
}

MessageDialog {
    id: messageDialog
    ...// 생략

}
```


