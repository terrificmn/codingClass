사용할 때에는 

CMakeLists.txt 파일에   
find_pakcage()에 추가를 해줘야 한다 

안해주면 빌드시  undefined reference to  에러가 발생한다 

```
find_package(catkin REQUIRED COMPONENTS
	roscpp
	actionlib
	actionlib_msgs
)
```

> 단, action server일 경우에는 actionlib_msgs 이면 되고   
 action client 일 경우에는 actionlib_msgs와 actionlib 도 필요하다
 그리고 catkin_package()에는 추가를 안해도 상관 없는 듯 하다






