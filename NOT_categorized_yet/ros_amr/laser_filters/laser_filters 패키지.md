config 파일에 의해서 laser_fliter pkg가 실행이 된다면 레이저의 스캔의 필터가 가능함

move base등에서  subscribe하는 scan을 리맵핑을 해주면 된다 
```
<node pkg="move_base" type="move_base" respawn="false" name="move_base" output="screen">
...생략
	<remap from="scan" to="scan_filtered"/>  <!--when laser_filters uses-->
</node>
```

scan_filtered로 나오는 토픽을 move_base에서 필요한 scan 토픽을 바꿔서 subscribe한다

> 즉, move_base노드에서 필요한 것은 scan topic인데 이 scan을 scan_filtered로 바꿔서 subscribe 하는게 된다  
> 구독하는 노드에서 필요한 토픽을(from) 바꾼다라고(to) 이해하면 되는 듯 하다


또는 gmapping으로 scan 토픽을 받을 때도 마찬가지로 해주면 된다   

단, rviz에서는 scan을 구독하고 있으므로 보이는 부분에서는 다를 수 있다. 
만약 제대로 필터가 되고 있다면 특정부분이 안나오게 된다. (mapping에서 제외, 또는 장애물 표시가 안됨)



