gps를 사용하는 경우에는 맵을 사용하지 않고  
global costmap을 static map을 사용하지 않는다면 맵 사이즈와 origin을 잘 선택해줘야한다.  

맵은 사용안하지만 empty map은 필요  
laser로 costmap을 만드는 경우에만 사용하는 것이 좋다 (Slam을 안 하는 경우)

1. 맵을 크게 만든다   

2. global_costmap이 width 50, height 50 이라면  
시작위치를 25, 25 이런식으로 하면 가장 오른쪽 상단(?)에 위치하게 된다  
스캔은 해당 사이즈 밖으로 나가버리고 plan도 맵 밖으로 나가게 됨   
그래서 origin 가운데 (0, 0) 으로 해줘야하는데 이럴 때에는 -25, -25 로 해주면 됨  

예
```
global_costmap:
    static_map: false
    global_frame: /map
    width: 50
    height: 50
    resolution: 0.05
    origin_x: -25.0
    origin_y: -25.0
```
