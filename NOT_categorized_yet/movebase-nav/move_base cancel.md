/move_base/cancel 토픽을 이용해서 취소를 할 수가 있다 

먼저 goal 지정되어 수행을 하고 있는 경우에 
goal_id 를 지정해서 취소를 하거나, 아니면 actionlib의 msg type 이용해서 {} (중괄호)를 사용해서 일괄 취소 시킬 수 있다  


cmd 로 할 경우에는 rostopic pub 을 이용한다 
```
rostopic pub -1 /move_base/cancel actionlib_msgs/GoalID {}
```

> -1 을 빼면 publishing을 계속 해주고, -1을 사용하면 3초만 publishing 한다


그 외에 
- /move_base/status 토픽을 통해 goal id 포함한 status를 알 수가 있고   
- /move_base/result 토픽을 통해 도착여부를 알 수 있다. 단, subscribe 하고 있는 상태에서 도착을 하면 알려준다 


