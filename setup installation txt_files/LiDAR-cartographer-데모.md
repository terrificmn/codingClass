
wget -P ~/Downloads https://storage.googleapis.com/cartographer-public-data/bags/backpack_2d/cartographer_paper_deutsches_museum.bag

roslaunch cartographer_ros demo_backpack_2d.launch bag_filename:=${HOME}/Downloads/cartographer_paper_deutsches_museum.bag


___

먼저 lua 파일을 만들어야하고
cartographer_ros/configuration_files 에 보면 각종(?) .lua 파일이 있는데 
하나를 만들어 주면된다

catkin_create_pkg 를 하나 만들어 주고
```
catkin_create_pkg slam_cartographer roscpp 
```
그리고 만들어진 패키지 디렉토리로 이동

그리고 
mkdir config launch

config 디렉토리에 lua파일을 만들어 주는데 summit.lua 로 만들어 준다

기존에 cartographer_ros 안에 있는 파일을 참고해서 만들어 준다


노드가 실행되고 있을 때 트리 확인하기 pdf 파일로 만들어 준다
```
 rosrun tf view_frames 
```

https://www.youtube.com/watch?v=bXNK8VTQ4zo 참고해서 
40분 부터 다시 보기