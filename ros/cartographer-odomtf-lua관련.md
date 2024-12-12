# 슬램 관련 lua 파일에서 odom tf
transform odom 데이터를 받아서 사용하는 경우에는 

lua 파일에서 frame 등이 odom 를 사용할 수 있게 한다. 
```lua
-- 생략

map_frame = "map",
tracking_frame = "base_link",
published_frame = "odom",
odom_frame = "odom",
provide_odom_frame = false
```

카토그래퍼 외에 다른 프로그램에서 odom transform 데이터를 제공해줘야 한다.   
> 실제 로봇이나, *gazebo 시뮬레이션*을  사용할 경우에는 위 처럼 사용해야 할 듯. 

만약 `"odom" passed to lookiupTransform argument source frame does not exist.` 라고 나온다면   
Tf에서 odom frame이 없을 경우에 해당한다 .  



반대로 카토그래퍼에서 odom frame을 제공하려면,   
```lua
map_frame = "map",
tracking_frame = "base_link",
published_frame = "base_link",
odom_frame = "odom",
provide_odom_frame = true
```
lua 파일에서의 provide_odom_frame 은 카토그래퍼에서 제공하는 것을 의미  

카토그래퍼에서 odom tf 를 만들어주므로 다른 프로그램에서 odom 관련 tf를 publish를 할 필요가 없음.     
odom 토픽은 제외

> gazebo와 연동을 odom_frame 주는 것을 빼는 식으로? 테스트를 해봐야 할 듯 하다. 안 해봄;;;   
TODO: 추후 업데이트 하기
