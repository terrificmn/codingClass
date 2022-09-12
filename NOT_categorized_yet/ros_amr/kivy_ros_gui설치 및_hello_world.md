kivy 설치 - 파이썬 pip으로 설치하게 됨


```
sudo apt install python3-pip   
python3 -m pip install --upgrate pip
```

https://kivy.org/#download    
소스로 빌드하려면 다운로드 홈피 확인  

> python2 일 경우에 pip이 없는 경우
```
sudo apt install python-pip

```

그리고 kivy 로 만들어져 있는 kivyMD를 다운 

> KivyMD is a collection of Material Design compliant widgets for use with,   
Kivy cross-platform graphical framework a framework for cross-platform,   
touch-enabled graphical applications. The project’s goal is   
to approximate Google’s Material Design spec as close as possible   
without sacrificing ease of use or application performance.

```
python3 -m pip install kivymd
```
(kivyMD는 kivy 의존성이 필요하므로 kivy를 먼저 설치해줘야 한다 )

역시  python 2 버전일 경우에는  
```
python -m pip install kivymd
```



## 튜토리얼 hello world

패키지를 하나 만들어 준다. catkin_ws으로 이동 후 
```
cd ~/catkin_ws
catkin_create_pkg py_kivy_tutorial rospy
```

py 디렉토리를 만들어서 그 안에 python 파일을 하나 만들어서 저장 (파일명은 kivy_gui.py 정도로 해주고) 

내용은 
```py
#!/usr/bin/env python3

import rospy
from kivymd.app import MDApp  ## 거의 모든 위젯(kivyMD) 사용가능
from kivy.lang import Builder

""" MDApp class로 상속 받는 클래스를 만들어서 사용하면 된다 """
class TutorialApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        ## ros_gui.kv 파일을 불러오게 됨
        self.screen = Builder.load_file('/home/sgtubunamr/catkin_ws/src/py_kivy_tutorial/ros_gui.kv')

    def build(self):
        return self.screen        


if __name__ == '__main__':
    rospy.init_node('simple_gui', anonymous=True)
    TutorialApp().run()
```


이제 kv파일을 작성할 차례  
kv파일을 ros_gui.kv라고 해서 위의 경로에 만들어 준다  
내용은 kivyMD 메뉴얼에 나와있는 components를 참고해서 원하는 기능을 복사 붙여넣기해서 사용  

파이썬이므로 간격에 주의  
```
FloatLayout:

    MDLabel:
        text: "Hello World"
        halign: "center"
```


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
를 해주면 창이 뜨는 것을 확인할 수가 있다






