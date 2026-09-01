# QT 6 QtQuick Image 불러오기 cmake

아고 이미지 하나 불러와서 표시하는데 qml 기준으로는 쉽게 되어 있지만...  
하지만 파일 패스를 입력하는 게 그냥 경로를 입력한다고 되는게 아니게 되어있다;;;; 
그냥 상대경로를 입력해줬으면 좋겠는데 그게 안됨   

어쨋든 **Qt 6.2 버전 및 cmake로 빌드하는 방법임**

qml 의 QtQuick을 인쿠르드 하면서 사용하면서 image를 불러와서 display를 할 수가 있는데   
- cmake 의 rcc를 이용해서 qt_add_resources() 호출하는 방법과,   
- cmake의 CMAKE_AUTORCC 기능을 이용해서 .qrc 파일을 사용하는 방법,   
- 절대 경로를 사용하는 방법이 대충 있다.  

## cmake의 qt_add_resources
먼저 images 디렉토리를 현 패키지의 root 아래에 만들어 준다. 또는 이동 복사  

CMakeLists.txt 파일에 `qt_add_resources(<TARGET> <RESOURCE_NAME> )`  를 추가해준다  

예
```c
qt_add_resources(appmy_pkg "app_images"
    PREFIX "/"
    FILES
        images/my_image_file.png
        images/my_image_file2.png
        images/my_image_file3.png
        // 파일이 더 있으면 추가
)
```

> my_pkg가 프로젝트명이고 app 은 prefix로 붙는다.   
resource 네임은 어딘가에서 쓰이겠지만, 정확히 어디에서 사용되는지는 모르겠다. 일단 (메뉴얼대로 함 "app_images")     
중요한 파일 경로는 프로젝트의 root 기준으로 만들어 준다   


이 qt_add_resourece() 는 qt6Core의 CMake 함수라고 하는데, qrc파일을 쓸 필요 없이 해당 내용을 resources로 추가해준다   

이제 main.qml 에 가서 Image로 사용하면 된다 
```js
Window {
// ... 생략..

    Image {
        id: image1
        x: 50
        y: 50
        width: 100
        height: 100
        source: "qrc:/images/my_image_file.png"

    }
}
```

qrc 파일이 없지만 `qrc:...` 로 해주면 이미지가 잘 로드가 된다 (qrc를 빼면 제대로 읽지 못한다)

> QT creator IDE에서 Projects 패널에 Resources에 my_image_file.png 파일이 나온다

## CMAKE_AUTORCC On 으로 .qrc 파일 사용
먼저 CMakeLists.txt 파일에서  CMAKE_AUTORCC ON으로 셋 해준다   
그리고 qt_add_executable()에 qrc파일을 추가해준다
```c
set(CMAKE_AUTORCC ON)

... 생략

qt_add_executable(appmy_pkg
    main.cpp
    image_resources.qrc
)
```

이제 image_resources.qrc 를 만들어 준다. 해당 패키지의 최상단에서 만들어 주면 된다.   
내용은 이렇게
```xml
<RCC>
    <qresource prefix="/">
        <file>images/my_image_file.png</file>
    </qresource>
</RCC>
```

> image 파일은 마찬가지로 images 디렉토리에 있음


이제 main.qml 에 가서 Image로 사용하면 된다 
```js
Window {
// ... 생략..

    Image {
        id: image1
        x: 50
        y: 50
        width: 100
        height: 100
        source: "qrc:/images/my_image_file.png"
    }
}
```


## 마지막으로는 절대경로 사용
CMakelists.txt와 qrc파일을 사용 안하고, 둘 다 필요없다. 그냥 qml에서 다이렉트로 사용할 때 가능   

qrc 대신에 `file:/....` 이렇게 사용하면 absolute path 를 사용 가능  

```js
Window {
// ... 생략..

    Image {
        id: image1
        x: 50
        y: 50
        width: 100
        height: 100
        source: "file://home/my_user/qt_ws/my_pkg/images/my_image_file.png" 
    }
}
```


