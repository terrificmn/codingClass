## footprint_padding 파라미터가 
기존 costmap common 관련 파라미터에 볼 수 있는   
기존 footprint에 조금 더 clearance를 주는 것 (footprint_padding) 

그래서 로봇과 장애물 사이에 조금 더 간격을 두는 것 (extra distance)

여기에서 footprint는 실제 로봇의 물리적 크기가 되어야 한다 
그리고 footprint_padding은 조금 더 여유를 줘서 실제 장애물 등과 부딪히지 않게 해준다   

이와 유사하게 topic 도 있다 /footprint   
geometry_msgs/Polygon 의 메세지 타입이고, 여기로 정보가 들어오면 footprint 파라미터의 값을 대체하게 됨



