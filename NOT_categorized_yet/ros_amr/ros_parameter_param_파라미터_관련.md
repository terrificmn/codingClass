```
<arg name="publish_frame_to" value="map"/> <!-- map frame으로 publish해야함 -->
		<param name="/gps_navigation/coordinates_file" value="/waypoints/gps_coorinates.txt" type="string" />
		<param name="/publish_frame_to" value="$(arg publish_frame_to)" type="string" />
	<node ns="/gps_navigation" pkg="gps_navigation" type="gps_navigation_node" name="gps_waypoint" output="screen" />
```

런치파일에서는 param 태그가 node보다 먼저 나와줘야 한다  
> 흠.. 상관은 없다. ~~테스트를 해봤더니 상관 없다. node 태그를 안 닫고 그 안에 param태그를 넣은 후 node태그를 닫아도 상관없다   
단 아무래도 param 태그가 먼저나온 후 node 태그가 나오면 좀 더 보기에 편할 것 같다  ~~

몇 번 테스트를 해보니 param태그가 node보다 **늦게 나오면 제대로 파라미터 값을 못 받는다 (주의!)**  
**파라미터 태그가 먼저 오도록 하자**

param이 노드 태그 안에 있게 되면 계속 디폴트 값이 들어가게 된다. 그래서 계속 param값을 넣어줘도 반영이 안됨

또한 이제 이 런치파일에서 설정한 파라미터를 실제 노드에서 받아야하는데  
```cpp
std::string paramStr;
ros::param::get("/publish_frame_to", paramStr);
// "문자열" 부분인 "/publish_frame_to"가 파라미터 (런치파일에서 설정한 param name이 된다)
```

여기에서 주의할 점은 파라미터 이름인 publish_frame_to 가 ~~반드시 /로 시작을 해야하는 것 같다   
/를 빼고 빌드를 하니 파라미터 값을 받지를 못한다~~

아마 착오가 있었을 듯.. `/'를 넣는다는 것은 토픽이나 파라미터가 가장 상위단인 root 경로가 된다는 의미이다   
그러므로 namespace등을 적용할 경우에는 무조건 / 경로에 맞춰저서 적용이 안될 수 있다 

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

> std::string 식으로 타입을 지정해도 변수는 선언해줘야한다. (위에서)


## ros 클래스 말고 nh 노드 핸들러에서도 가능하다
nh 핸들러를 이용해서 바로  `nh.getParam("파라미터", 파라미터가 입력될 변수)`


```cpp
std::string frame_id = "default_frame_id";
nh.getParam("frame_id", frame_id);
```

## set 하기는 
이런식으로 할 수가 있음
```
ros::param::set("/integer_param", 5);
```


