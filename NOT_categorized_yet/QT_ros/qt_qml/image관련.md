# image 관련 
아주 큰 용량의 파일을 로드할 때  아래쪽 사각형 바를 보여주는 예제
```js
import QtQuick
Window {
    width: 1000
    height: 1000
    visible: true

    Image {
        id: image
        width: 1000
        height: 1000
        source: "qrc:/images/rocket.jpg"
//        Component.onCompleted: console.log(width, height);
        fillMode: Image.PreserveAspectFit

        Rectangle {
            color: "red"
            x: 0; y: 950
            height: 50
            width: 1000 * image.progress
            visible: image.progress !== 1
        }

        onStateChanged: console.log(sourceSize)
    }
}
```
단 `image.progress !== 1` 에서 워닝이 있다;; 버전 업 되면서 아마 호환성이;;;  
추후 알아보기



## 이미지 
크게 3가지 방법이 있다
Stretch: Scale the image to fit to the available area
Repeat: Tile the image until there is no more space
Round: Like Repeat, but scales the images down to ensure that the last image is not cropped