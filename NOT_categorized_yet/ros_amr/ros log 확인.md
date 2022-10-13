각종 ROS_INFO(), ROS_WARN(), ROS_ERROR() 으로 출력이 나온 것은 rosout.log 파일에서 확인을 할 수가 있는데   

저장 장소는 $HOME/.ros/log 디렉토리 임

하지만, log 파일 경로는 임시 디렉토리가 생성되서 만들어지는데   
현재 노드에서 어느 경로에 저장하고 있는지 확인할 수가 있다

```
roscd log
```

현재 노드 관련 log 파일이 저장되는 곳을 살펴보면  

예를 들어서 
```
/home/myuser/.ros/log/37b0a630-4acb-11ed-9464-25ba8ea93797
```

이동 후 

rosout.log 파일을 살펴보면 된다 
