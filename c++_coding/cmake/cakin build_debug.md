# catkin build 디버그
아마도 g++의 -g 옵션에 비슷한 방법일 듯 하다.

```
catkin build mypkg --cmake-args -DFORCE_DEBUG_BUILD=True
```

Build packages with aditional CMake args:
```
catkin build --cmake-args -DCMAKE_BUILD_TYPE=Debug
```
위 처럼도 가능하지만 워닝과 함께 DFORCE_DEBUG-BUILD 를 true로 사용하라고 하는 듯 하다. 


빌드가 완료가 되면 

`/home/myuser/catkin_ws/devel/lib/mypkg` 경로로 가면 빌드된 파일이 있다.  
이를 gdb로 실행해주면 디버깅을 할 수가 있다.  


> 또는 /home/myuser/catkin_ws/devel/.private/mypkg/lib/mypkg/mypkg 경로로 가보면   
실제 파일이 있다. 위에 devel에 있는 파일을 심링크.


예: 해당 경로로 먼저 이동 후에
```
gdb myfilename
```

물론 vscode로 하면 좀 더 쉽게 할 수 있고, 특히  ROS 같은 경우에는  ROS 확장팩을 설치한 후에 
Run and Debug 에서 조금만 설정을 하면 특히 런치파일로도 설정할 수가 있다.   

설정 후 F5를 눌르면 Debuging을 할 수가 있다. 


