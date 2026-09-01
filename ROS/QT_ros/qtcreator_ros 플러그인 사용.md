# catkin workspace 등록
먼저 맨 처음으로 Create Project를 눌러서 catkin_ws를 선택해준다  

Create Project 버튼을 눌러서 New Project 만들기에서 template를 골라주는데  
Other Project 의 ROS Workspace를 선택  Next를 누른 후에  
Name은 catkin_ws 정도로 해주고    
Build System은 Catkin Tools 가 설치되어 있으면 선택, 없다면 catkin_make로 선택

~~Workspace Path는 Browse검색이 잘 안되면 직접 타이핑을 해준다 (버그인가?) ~~ 

> qmake 지정이 (qt version이 지정이 안되서 발생)


## New file 만들기 - qt designer form class

새로운 파일을 만들 때에는 
File -> New File 선택 후  
Qt -> Qt Designer Form Class 를 선택해준다  (C++ header파일을 만들어준다 )   

이제 Template를 선택할 수 있는데 Widget으로 선택  
> Main Window는 File메뉴가 있는 window창

Class Name을 선택해 주는데 원하는 클래스명을 정해준다  (카멜케이스)
그리고 자동으로 header파일등의 이름이 들어가지는데 ros의 네이밍 컨벤션에 따라 스네이크케이스로 만들어준다   
path에는 해당 만들려고 하는 패키지의 include안의 패키지명까지 지정해준다  

예  
Class name:  HelloGui  
Header File: hello_gui.h  
Source file: hello_gui.cpp  
Form file: hello_gui.ui  
Path: /home/sgtubunamr/catkin_ws/src/template_gui_package/include/template_gui_package


마지막으로 나오는 화면에서 최종적으로 확인하면 QT화면 화면이 나오게 된다  


https://www.youtube.com/watch?v=Cg1DaNFnZyY&t=24s  
이후 7:20 부터 


