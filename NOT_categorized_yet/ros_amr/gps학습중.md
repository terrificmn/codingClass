1. 먼저 empty map이 필요하다   
map 디렉토리를 만들고 map.pgd, map.yaml 파일을 만들어 준다  

2. 그리고 이 맵을 실행을 해줄 런치파일을 만든다  

3. navsat 노드를 이용해서 gps 신호를 converting 해주는데 런치파일을 작성한다   
여기에는 navsat 노드에 필요한 parameter를 정의한다   
robot_localization 패키지 필요    
--> robot_localization은 geographic_msgs가 필요함   
sudo apt install ros-melodic-geographic-msgs  (의존성 추가 설치)  
apt instal libgeographic-dev 


4. config 관련해서 yaml파일을 만들고 config관련해서 패키지 만듬
robot_localization 패키지 필요    
-b melodic-devel https://github.com/cra-ros-pkg/robot_localization.git
