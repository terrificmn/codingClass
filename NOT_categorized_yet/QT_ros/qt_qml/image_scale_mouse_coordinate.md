# image scale

이미지를 띄우고 source property를 통해서 파일 위치를 지정해준다.  

> CMakeLists.txt 를 사용하는 경우에는 image 위치를 지정해줘야 한다   

마우스 버튼을 눌르면 특정 이미지가 커지게 하려면  

Image의 id는 image1 이라고 할 때   
mouse 이벤트가 발생했을 경우에 `image1.scale += 0.2` 식으로 키워주게 되면 이미지를 크게 해줄 수가 있다 

예:   
```
Rectangle {
    id: rect1
    width: 100; height: 100
    // 생략
    Image {
        id: image1
        width: parent.width; height: parent.height
        source: "qrc:/my_image.png"
    }
    MouseArea {
        id: mouseArea
        onClicked: (mouse) => {
            image1.scale += 0.2
        }
    }
}
```
Image의 scale 속성을 사용하게 되면 이미지의 크기는 아주 잘 확대가 되지만,  
해당 부모나 Image 자체의 width, height 는 무시(?)가 되는 것 같다.   

그래서 좌표를 사용하거나 할 경우에 이미지와 맞지가 않거나 아예 클릭해서 좌표를 받아오지 못할 경우도 있다   
그래서 그런 경우를 감안하고 사용하면 되겠다   


## 마우스 좌표와 이미지 크기 맞추려면  
가장 상단에서 qml에서 사용할 property를 사용자 정의로 만들어준다 (root 또는 부모에서 정의)   
```
Window {
    width: 500
    height: 500
    property real my_scale: 1.0

    Rectangle {
        id: rect1
        // 최초 크기 지정 및 마우스 이벤트 발생했을 경우에도 크기가 조정될 수 있게 해줌 
        // my_scale을 곱하지 않으면 마우스 이벤트 발생 시 아무일도 안 일어난다
        implicitWidth: 100 * my_scale; implicitHeight: 100 * my_scale
        // 생략

        // 이미지의 크기는 부모 rectangle을 그대로 받아서 사용
        Image {
            id: image1
            width: parent.width; height: parent.height
            source: "qrc:/my_image.png"
        }
        MouseArea {
            id: mouseArea
            onClicked: (mouse) => {
                my_scale += 0.2;  // Image의 scale 이 속성이 아닌, 새로 만든 property를 사용
                image1.width = 100 * my_scale;
                image2.height = 100 * my_scale;

                //좌표출력은 mouseX, Y 이용
                console.log(`x: ${mouseX}, y: ${mouseY}`);
            }
        }
    }
}

```

## mouse 좌표 얻기 방법2
이런식으로 만들면 이미지 확대도 되고, 마우스 좌표도 정확히 맞아 떨어진다  
mouseX, mouseY는 mouse에 있는 property 정도 되겠다  (좌표 정보를 가지고 있음)  

또는 `mapToItem()` 같은 함수를 사용할 수도 있다  
```
onClicked: {
    console.log("mouse coordinate: ", mapToItem(rect1, mouseX, mouseY));
}
```





