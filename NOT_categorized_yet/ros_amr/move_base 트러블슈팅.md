# The robot's start position is off the global costmap

맵 파일의 yaml 파일을 위치를 중간으로 바꿔본다 
예: -100, -100

답은 아니다;;; 테스트 해봐야함

그리고 move_base에서 config 파일이 param 정의해놓은 파일에서  
resolution 을 맵 파일이랑 일치되게 적어야 하는 듯 하다?



odom 토픽을 받을 수 있도록 한다   
기존의amr에서 받는다면 /odom  
ekf 노드에서 받는다면 /odometry/filtered

```xml
<remap from="odom" to="/odometry/filtered"/>
<!-- <remap from="odom" to="/md_odom"/> -->
```


네비게이션 스택  
https://github.com/husky/husky/tree/melodic-devel/husky_navigation


Warnings like Map update loop missed its desired rate of *.*Hz ... are because of not enough computing power and are almost unavoidable. You can ignore them because it doesn’t affect system efficiency.


레이져 관련 읽어보기
https://community.husarion.com/t/solved-timed-out-waiting-for-transform-from-base-link-to-map-during-map-navigation/1004/9
