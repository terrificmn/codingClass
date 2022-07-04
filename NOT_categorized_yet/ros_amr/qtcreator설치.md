qtcreator 설치하기 (qtcreator-ros)

snap을 이용해서 설치한다  
```
snap install qtcreator-ros --classic
```


Create Project > Other Project > ROS Workspace 를 선택해준다  
Project 이름은 catkin_ws의 이름과 같은 것으로 설정  
Build system은 Catkin Tools를 사용할 것이므로 선택   
Workspace는 선택해주거나 직접 입력 /home/{userid}/catkin_fund_ws/


Debug 메뉴에서 Start Debugging을 선택해서 attach to running application을 선택해주면  
이제 process로 돌아가고 있는 프로그램 목록이 뜨는데  
여기에서 실행하고 있는 노드를 선택해주면 된다
