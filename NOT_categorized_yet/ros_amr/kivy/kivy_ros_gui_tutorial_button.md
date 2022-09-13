# KivyMD 

> 설치 및 py 코드는 kivy_ros_gui설치 및_hello_world.md 파일 참고

ros_gui.kv (원하는 파일명)을 만들고 메뉴얼에 따라서 참고 한다   
[https://kivymd.readthedocs mdraised button 사이트보기](https://kivymd.readthedocs.io/en/latest/components/button/#mdraisedbutton)

파이썬이므로 간격에 주의  
```
FloatLayout:

    MDLabel:
        text: "Hello World"
        halign: "center"
        size_hint: 1, 1 #(x,y 퍼센트 1이 최대치?)
        pos_hint: {"center_x": .5, "center_y": .5}  #이것도 퍼센트로 표시 (글자 위치)

    MDRaisedButton:
        text: "Press Me!"
        md_bg_color: 0, 1, 1, 1  ## 색깔 표시 (RGB)
        size_hint: 0.2, 0.1 #(x,y 퍼센트 1이 최대치? - 버튼이 전체화면으로 된다 )
        pos_hint: {"center_x": .5, "center_y": .3}  #이것도 퍼센트로 표시 (버튼 위치)
```

indent를 잘 맞춰서 써야하고  
기본 변수들 (엘리먼트?들?)이 간단한 것 같다.    
그리고 크기나 위치를 퍼센트로 해서 (1이 최대치 인듯) 지정해준다. 그래서 창이 커지거나 줄어들 때에 맞춰서 크기가 자동으로 맞춰진다 


이제 CMakeLists.txt 파일에서 py 노드가 사용될 수 있게   
catkin_install_python 부분을 찾아서 py파일이 있는 디렉토리와 파일명을 지정해준다  
```
catkin_install_python(PROGRAMS
  py/kivy_gui.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

그리고 빌드를 해준다 
cd ~/catkin_ws
catkin build

> 빌드툴을 사용하지 않는다면 catkin_make  

그리고 
```
. devel/setup.bash
```
를 해서 workstace 의 패키지를 사용할 수 있게 해준다   

```
roscore
```
를 하나의 터미널에 켜주고  다른 터미널을 열어서  
```
rosrun py_kivy_tutorial kivy_gui.py
```
를 해주면 창이 뜨고 버튼을 확인할 수가 있다






