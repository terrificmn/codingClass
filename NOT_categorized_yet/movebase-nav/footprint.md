common costmap 의 footprint는 로봇의 실제 크기를 나타내주는데  
2차원 배열로 지정해준다   

```
footprint: [[-0.48, -0.31], [-0.48, 0.31], [0.13, 0.31], [0.13, -0.31]]
```

footprint가 장애물의 inflation으로 들어가면 충돌이 발생한 것이기 때문에    
정확히는 로봇의 풋프린트가 inscribed circle 영역이라고 하는 부분 풋프린트의 안쪽 서클     
으로 침범하면 안되기 때문에 footprint는 약간 여유를 줘서 하는 것이 좋다고 한다   


## footprint 지정하기
먼저 로봇 상태를 먼저 확인해 주는게 좋은데   rviz로 해서 tf 트리를 보면서 하면 더 편하고   

아니면 [x0, y0], [x1, y1], [x2, y2], [x3, y3] 이런식으로 되어 있는 것이기 때문에   
하나의 배열 당 좌표 포인트가 된다    

				 ↑
[ x는+, y는 -]	x방향		[ x는 +, y는 +]				
				↓
			로봇 + 센터 기준
					
[ x는-, y는 -]			               [ x는 -, y는 +]				
			← y뱡향 →

ros 좌표계는 이와 같은 방향   
(오른손 법칙? 앞으로 총 모양(?)을 만들면  검지가 가리키는 방향이 x,  중지가 y, 엄지가 z)   

그래서 좌표도 대충 위와 같은 방식이다  (아마도 맞을...;;;)

로봇 기준으로 왼쪽 뒤쪽 부터 반 시계 방향으로 배열이 만들어 지는 것 같은데   
순서가 상관 있는지는 모르겠지만   
(어차피 로봇이 사각형 모형이라면 x,y의 +,- 는 딱 정해져 있기 때문에)

> husky, turtlebot3 등의 런치파일을 찾아봤더니, 일단 위의 형식 그대로 사용을 하고 있다   
> 그냥 +, - 를 위의 순서대로 하면 될 듯 하다 



#### 그 밖에.. footprint 파라미터 
footprint_padding: 0.01  추가적으로 패딩을 넣어줄 때 사용
robot_radius  :로봇이 circular 일 경우에 사용한다   



