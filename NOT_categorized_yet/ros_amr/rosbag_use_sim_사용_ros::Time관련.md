시뮬레이션이나 rosbag을 사용해서 play를 하고 있을 때에는  

cpp로 프로그램을   
ros::Time::now() 값이 0 값이 리턴이 된다  

그래서  rosparam을 이용해서    
rosparam get /use_sim_time   
확인을 해보면   
true / false 가 나옴  

```
rosparam set /use_sim_time false
```
그러면 false로 바꿔주면  시간이 0이 아닌 제대로 나오게 된다 


터미널 한쪽에서만 실행해주면 다 반영됨
