qt sytle sheets는 CSS와 비슷하다 
거의 CSS와 같은 방식으로 작동

```css
h1 { color: red, background-color: white;}
```

qt style sheets
```
QLineEdit { color: red; background-color: white; }
```

property와 value로 되어 있고 ;세미콜론으로 구분

Qt에서 style sheet를 함수를 호출해서 지정할 수 있다 
```
myPushButton->setStyleSheet("color: blue");
```


### style sheet 지정

버튼, Horizontal Slider, radio buttion, check box등을 넣은 다음에  

오른쪽의 Object 패널에서 마우스 오른쪽 버튼, 
또는 디자인 폼의 창에서 마우스 오른쪽 버튼을 누른 후에  
Change Stylesheet를 눌러준다   

```
QPushButton {
	border: 2px solid gray;
	border-radius: 10px;
	padding: 0 8px;
	background: yellow;
}
```

QPushButton 을 지정하지 않고 그냥 블럭으로만 해서 지정한다면 전체에 style이 지정 된다   
QPushButton은 class 이름이고, 이것을 지정하면 된다.  

> 디자인폼에서 Push Button을 추가하게 되면 Object이름은 pushButton 클래스명은 QPushButton이 된다. 이 class를 style sheet에 지정해준다   
> (오른쪽 화면의 Object/Class 패널을 보면 된다)

버튼을 눌러서 오른쪽 Object, Class 패널을 보면  
pushButton 은 QPushButton 클래스 인 것을 알 수 있음.   
**style을 클래스 명으로 지정해주면 된다**

단, 모든 버튼이나, 라벨이나 모두 같은 클래스를 사용하므로 스타일을 지정할 때 다 같은 값이 지정이 된다  

그래서 특정 object에만 사용을 하려고 한다면  특정 오브젝트의 (버튼 등)  의 property 창에서  
objectName을 변경해준다. 그러면 그 고유의 이름이 되게 되는데  
스타일을 지정할 때 # 기호를 붙여서 사용하면 된다   

아래 내용을 참고

widget의 특정 Object를 클릭하고 QObject의 objectName 찾아서 사용을 하면 된다  

예를 들어 3번째로 만든 pubhButton은 objectName이 pushButton_3


### 한개의 버튼에만 지정하기 
```
QPushButton#pushButton_2 {
	border: 2px solid gray;
	border-radius: 10px;
	padding: 0 8px;
	background: yellow;
}
```
2번째 버튼만 지정이 된다  

```
QPushButton {
	color: red;
	border: 0px;
	padding: 0 8 px;
	background: white;
}
QPushButton#pushButton_2 {
	border: 2px solid gray;
	border-radius: 10px;
}
```

> 대소문자 구별하므로 주의!

또는 클래스명은 생략하고 object이름으로만 # 을 넣어서 지정한다  
```
#pushButton_2 {
  ...내용
}
```

qt style sheet 에서는 QPushButton에 지정했던 것의 property가 계속 유지가 된다. 다른 버튼에 다른 값을 주지 않으면 버튼에 지정했던 것으로 지정됨  

그래서 pushButton_2 에는 색깔을 지정 안했지만, QPushButton 자체에 색을 red로 했으므로 pushButton_2 도 red가 된다 



### universal selector
별* 표시로 지정하면 위젯 전체에 적용시킬 수 있다  
color 등을 rgb()로 지정

```
*
{
	background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);
	color: rgb(255, 255, 255);
	border: 1px solid #ffffff;
}
```

pushButton에는 이미 스타일을 지정했기 때문에 별 표시로 지정한 것이 적용되지는 않는다 

> 괄호는 붙여서 사용

특정 오브젝트만 지정해서 사용할 경우에는 # 표시를 붙여준다 
```
#loginForm {
border: 1px solid; 
}
```

> 여기에서 # 뒤에 스페이스를 주면 안됨. 붙여서 사용한다 


