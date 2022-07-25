```
<arg name="publish_frame_to" value="map"/> <!-- map frame으로 publish해야함 -->
		<param name="/gps_navigation/coordinates_file" value="/waypoints/gps_coorinates.txt" type="string" />
		<param name="/publish_frame_to" value="$(arg publish_frame_to)" type="string" />
	<node ns="/gps_navigation" pkg="gps_navigation" type="gps_navigation_node" name="gps_waypoint" output="screen" />
```

런치파일에서는 param 태그가 node보다 먼저 나와줘야 한다  
> 흠.. 상관은 없다. 테스트를 해봤더니 상관 없다. node 태그를 안 닫고 그 안에 param태그를 넣은 후 node태그를 닫아도 상관없다   
단 아무래도 param 태그가 먼저나온 후 node 태그가 나오면 좀 더 보기에 편할 것 같다  


또한 이제 이 런치파일에서 설정한 파라미터를 실제 노드에서 받아야하는데  
```cpp
std::string paramStr;
ros::param::get("/publish_frame_to", paramStr);
// "문자열" 부분인 "/publish_frame_to"가 파라미터 (런치파일에서 설정한 param name이 된다)
```

여기에서 주의할 점은 파라미터 이름인 publish_frame_to 가 반드시 /로 시작을 해야하는 것 같다   
/를 빼고 빌드를 하니 파라미터 값을 받지를 못한다  

그리고 물론 string 말고도 , int, double 등으로 타입으로 보낼 수 있다.    
런치파일에서
```
<param name="param1" type="int" value="7"/>
<param name="param2" type="double" value="10.5"/>
```

## 또는 이런식도 됨. default 값을 설정할 수가 있다 
```
ros::param::param<std::string>("/param1", paramStr, "odom"); //default set 
```
런치파일에서
```
<arg name="publish_frame_to" default="" /> 
```
이렇게 비워두면 위에서 지정한 (cpp)에서 odom을 기본값으로 가져간다 


## set 하기는 
이런식으로 할 수가 있음
```
ros::param::set("/integer_param", 5);
```


