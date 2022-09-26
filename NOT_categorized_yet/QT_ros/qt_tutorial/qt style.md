qt sytle sheets는 CSS와 비슷하다 

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

버튼을 눌러서 오른쪽 Object, Class 패널을 보면  
pushButton 은 QPushButton 클래스 인 것을 알 수 있음. style을 클래스 명으로 지정해주면 되는 듯 하다 



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


qt style sheet 에서는 QPushButton에 지정했던 것의 property가 계속 유지가 된다. 다른 버튼에 다른 값을 주지 않으면 버튼에 지정했던 것으로 지정됨  

그래서 pushButton_2 에는 색깔을 지정 안했지만, QPushButton 자체에 색을 red로 했으므로 pushButton_2 도 red가 된다 



### universal selector
별* 표시로 지정하면 

chapter basic 1- 6
