맵을 먼저 저장한 후에  
map.yaml 파일을 이용해서 map_server를 실행할 수 있다 

먼저 맵 파일이 있는 곳으로 이동  

예:  
rosrun map_server map_server my_map.yaml  


그리고 네비게이션을 할 수 있는 launch 파일을 열어준다   
이 부분은 좀 더 찾아봐야할 듯


## 수동으로 rviz 연 후에 rviz config 파일 만들기
rviz를 열어준 후에  
add를 눌러서 map을 추가해주고 topic은 /map 으로 지정해준다 

robot도 추가해준다 

PoseArray 추가해줌  
Topic은 /particlecloud 로 선택

TF 추가해주기  

Path 추가  
topic은 move_base_ local


이제 file->Save config
를 해주면 .rviz 파일을 만들어 준다 0


rviz에서 열어서 TF를 확인해보면 각각의 프레임을 알 수가 있다 





move_base 노드는 path를 따라 갈 수 있게 해주고 회피를 할 수 있게 해주는 노드  



## turtlebot3_navigation 패키지의 move_base.launch 파일을 참고  

base_footprint 프레임은 로봇의 중심  



