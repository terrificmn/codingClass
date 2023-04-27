# FileDialog
버전 5점 대랑 호환이 안되는 경우도 있으니 적극적으로 메뉴얼 보기 권장

[FileDialog--메뉴얼 보기 권장](https://doc.qt.io/qt-6.2/qml-qtquick-dialogs-filedialog.html)

예를 들어 QML로 FileDialog 기능을 사용하려고 하는데   
QT 5점대에 있는 fileUrl 이 QT6.2 에서는 없다. 없는 Property라고 나온다   
filUrl(s)는 없어지고, *currentFile(s)*로 바뀜. 

> 참고로 selectedFile(s) 는 마지막 선택을 하고 확인을 눌렀을 때 결정되는 property


