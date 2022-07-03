# 로봇 시뮬레이션 gazebo
gazebo의 빌딩을 저장했다면 
~/building_editor_modelsp 에 저장이 된다

하지만 어디에 저장이 되는지 모를 때에는~ 와일드카드를 이용해서 검색을 해본다
```
$ sudo find . -name school*
```
빌딩을 저장할 때 school_4th 이라고 저장했는데 school* 까지만 해주면 school로 시작하는 파일을 -name
이름으로 찾아준다

결과는 
```
./building_editor_models/school-real-4f
./building_editor_models/school4th-floor
./building_editor_models/school-4f-open
```


# http://gazebosim.org/tutorials?tut=ros_roslaunch
투토리얼 연구해 보기

그리고 
urdf를 spawn을 이용해서 전환해줘서 launch 파일에서 작동되게 해야하는 듯 하다
