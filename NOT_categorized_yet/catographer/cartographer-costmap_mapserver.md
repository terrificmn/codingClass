# cartographer - costmap

일반적으로 cartographer로 만들어서 OccupancyGrid 형식으로 사용하려고 하면 일반적으로는 작동이 안됨  

이유는 move_base 패키지에서 쓰이는 OccupancyGrid는   
occupied, free and unknown   
즉 Free 는 0,  occupied는 100, unknown은 -1 로 되는데 

Cartographer's states are about 100 based on certainty    
셀의 벨류를 
-1 부터 100까지 value 로 생성이 되어서 처음에 디텍션 때 ~40까지 측정이 되고   
많은 데이터가 더 측정되면 value은 0으로 되거나, 100이 된다 (free일 경우는 0, obstacles는 100)




##  map_server
맵 만들 때, occupied 영역 지정하기, free 영역 지정하기 

```
rosrun map_server map_saver -f gridmap --occ 65 --free 20 
```

단, 카토그래퍼에서는 직접 map을 사용 안 함..;;








