# footprint - move_base cost_map
footprint x, y 좌표로 한 포인트씩 4곳을 지정  시계방향?   

```yaml
footprint: [ [], [], [], [] ]
footprint_padding: 0.01
```
위와 같은 방식으로 지정하게 되는데  

footprint는 충돌관련 planner에서 사용되기 때문에 중요하다  
footprint_padding은 풋프린트와 장애물과의 쿠션같은 역활을 해준다  






