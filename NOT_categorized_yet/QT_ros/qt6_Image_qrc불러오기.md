# QT 5 QtQuick Image 불러오기 

Qt5 에서는 qml.qrc 파일에 추가를 해서 사용할 수 있다.  
cmake 빌드를 할 경우에도 CMakeLists.txt 따로 넣어줄 필요는 없다

> qt6 를 이용 && cmake 를 사용하는 경우에는 조금 복잡하다. qt6_Image_qrc불러오기.md 를 참고하자

## qml.qrc 파일에 추가하기
처음 프로젝트를 만들면 기본으로 qml.qrc 파일이 프로젝트의 root(최상단) 에 생긴다.

여기에 file 태그를 사용해서 넣어주면 된다. 이미지 파일 경로를 넣어주면 된다.

```
<RCC>
    <qresource prefix="/">
        <file>qml/main.qml</file>
        <file>images/test.png</file>
    </qresource>
</RCC>
```

상위 디렉토리 안에 images 디렉토리를 만들어 주고 원하는 이미지를 넣어준다.

> 물론 qml 파일 지정도 해준다

## qml Image
qml 에서 Image 를 사용해서 source 로 지정해서 사용해준다.

```qml
Image {
    id: image1
    x: 10
    y: 10
    width: 200
    height: 200
    source: "qrc:/images/test.png"
}
```

## cpp
cpp 에서 활용하려면 아래 처럼 사용할 수 있음. 해보지는 않음
```
QImage *test_image = new QImage(":/images/test.png");
```

