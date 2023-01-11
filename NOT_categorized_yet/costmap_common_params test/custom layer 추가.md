#### other_layer 기본 메소드 설명

1. updateBounds()  메소드를 이용해서  update를 시켜줄 지역을 정의해준다. 당장 costmap이 업데이트 되는 것은 아니다.   

	변화시킬 mark_x, mark_y를 지정하고, 계산 한 후 min/max 영역을 확장해서 새로운 point에 포함될 수 있게 해주게 하는 메소드 이다   

2. 실제로 업데이트가 되는 것은 updateCosts() 메소드를 통해서..
	worldToMap을 통해서 grid cell 의 point를 계산 후,  cell의 cost를 지정하게 된다  



#### grid_layer 설명
other_layer와 grid_layer 의 차이점은   
클래스 상속을 Costmap2D까지 extend해서 받음  

grid_layer의 cpp 파일에서는  
intialization에서 default_value를 셋팅, matchSize()메소드를 호출.   
matchSize()는 마스터 grid의 사이즈를 default_value로 채운다. 여기에서 default는 0임

updateCosts() 의 값을 셋팅하는 대신에 setCost() 메소드를 이용해서 layer의 costmap을 이용해서 값을 셋팅해주게 된다   

updateCosts() 메소드에서 전의 master costmap 값에 mark를 포함해서 덮어 씌운다.   
만약 layer's costmap 값이 NO_INFORMATION이면 덮어쓰지 않는다.  



이 other_layer나 grid_layer 클래스를 실행시키려면 costmap2d 패키지에   

> navigation 패키지를 깃 클론한 후 빌드해야함  


costmap_plugins.xml이 있는데   (grid_layer 패키지안에 costmap_plugins.xml에 추가해도 됨)

```
<library path="lib/libsimple_layer">
	<class type="other_layer_namespace::OtherLayer" base_class_type="costmap_2d::Layer">
	<description>Demo Layer that adds a point 1 meter in front of the robot</description>
	</class>
</library>
  

<library path="lib/libgrid_layer">
	<class type="other_layer_namespace::GridLayer" base_class_type="costmap_2d::Layer">
	<description>Demo Layer that marks all points that were ever one meter in front of the robot</description>
	</class>
</library>
```

해당 클래스들을 넣어주면 된다   

> 사실  costmap2D 패키지의 안에 있는 costmap_plugins.xml이 추가해도 되지만  예제에서 GridLayer 클래스 및 패키지를 만들 때에도 costmap_plugins.xml이 있었는데 그곳에 넣어줘도 플러그인이 잘 등록되어서 실행은 잘 되는 듯 하다  


move_base를 작동시킬 런치파일에서 param관련 config yaml 파일을 등록시키고   
실제 파일인 common_costmap.yaml 파일등에서  layer를 사용할 수 있게 등록해준다   

예를 들어서   costmap_common_param.yaml 파일이 있다고 하면 
```
grid_layer:
test_param: "void_test"
```
grid_layer를 등록시키고 (여기에서 test_param 같은 파라미터는 실제 GridLayer 클래스에서 파라미터를 받아서 동작하게 된다)

> common costmap 설정하는 yaml파일 

그리고 global_costmap_params.yaml 에서는 plugins를 추가해준다
예
```
global_costmap:
	global_frame: map
	... 생략..
	plugins:
		- {name: static, type: "costmap_2d::StaticLayer"}
		- {name: obstacles_layer, type: "costmap_2d::ObstacleLayer"}
		- {name: inflation_layer, type: "costmap_2d::InflationLayer"}
		- {name: grid_layer, type: "costmap_2d::GridLayer"}
```

> 기본 플러그인인 StaticLayer, ObstacleLayer, InflationLayer  외에 추가한 GridLayer를 추가하게 된다


