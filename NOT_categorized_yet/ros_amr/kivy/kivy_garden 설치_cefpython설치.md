https://github.com/kivy-garden

kivy_garden 에 들어가서 보면 패키지들이 다양하게 있는데 . (닷) 으로 구분된 패키지명은  
레거시 패키지를 의미함
닷이 없는 패키지는 새로운 패키지로 보면 됨

가든 패키지의 안에 있는 패키지들을 flower로 칭함

예
```
python3 -m pip install kivy_garden.graph --extra-index-url https://kivy-garden.github.io/simple/
```

단, flower의 maintainer가 pypi에 올렸다면 pip install로 설치가 가능하다. 


### 일단 cefbrowser 기능을 사용하기 위해서는 파이썬 3.8 에서는 안됨 (이하 3.7)

[kivy-garden에서 cefpython 검색하기](https://github.com/kivy-garden)

위 링크에서 cefpython를 찾아도 되고 링크

https://github.com/kivy-garden/garden.cefpython

~~위의 가든 위젯을 설치를 하려면 python3를 이용해서 설치를 하게 된다  ~~


근데;;; 위의 garden에 있는 패키지들을 설치할 때랑은 조금 다르다(?);;

아무래도 python3.8 버전에서는 안되는 듯 하다

3.7 버전 이하  사용이 가능한듯 

https://github.com/allestuetsmerweh/garden.cefpython


먼저 깃 클론을 해줘야한다 
```
https://github.com/allestuetsmerweh/garden.cefpython.git
```

그리고 
```
python3 -m pip install cefpython3
```

심볼릭 링크를 만들어준다   
```
ln -s $HOME/garden.cefpython/ ~/.kivy/garden/garden.cefpython
```

그런데 일단 python 3.8을 사용하고 있으니 오류가 많이 나면서 실행이 불가  
3.7버전은 된다고 하는 듯 하니~ 될꺼 같으나.. 쓰기에는 너무 안정적인 버전이 아닌 듯 한 생각이 듬

