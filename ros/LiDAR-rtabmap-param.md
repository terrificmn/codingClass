[참고:](http://wiki.ros.org/rtabmap_ros/Tutorials/Advanced%20Parameter%20Tuning)  
[참고:](https://github.com/introlab/rtabmap/issues/574)  
[읽어볼거리](https://www.intelrealsense.com/open3d/)  


param 데이터 보기

```
rosrun rtabmap_ros rtabmap --params
```

또는 grep 파이프 이용하기
```
rosrun rtabmap_ros rtabmap --params | grep g2o
```

launch파일 내에서 
노드 안에 적어준다 param태그를 사용. 스탠다드 방식
```
<param name="Odom/Strategy" value="0"/>
```
노드의 아큐먼트에 파라미터를 추가하기, 임시적으로 작동
```
<arg name="rtabmap_args" default="--Odom/Strategy 0"/
```



