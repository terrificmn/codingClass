# gazebo plugin h와 cpp
클래스 head파일과 cpp로 분리한 버전은 spawn_other_robots pkg를 참고 

주의할점은 헤더파일에서 클래스 정의가 끝난 다음에는  

`GZ_REGISTER_WORLD_PLUGIN(custom클래스명)` 또는   
`GZ_REGISTER_MODEL_PLUGIN(custom클래스명)` 처럼 월드 플러그인, 모델 플러그인으로 macro를 해줘야한다

그리고 월드 파일안에 플러그인 태그로 shared library 인 so파일을 넣어줘야하고    
예
```xml
<plugin name="amr_model_push" filename="libamr_model_push.so" />
```

## export
플러그인 so파일의 위치도 export를 해줘야함   
모델 sdf 파일이 필요하다면 export를 해줘야 한다 

> export를 할 경우에 so파일 위치에 맞춰서 해준다

gazebo_plugin_tutorial 패키지는 자체 cmake로 빌드를 해서 build 디렉토리에 so 파일이 생성,   
- gazebo_plugin_tutorial 패키지를 참고하려면 경로가 다름에 주의   
(아이러니 하게 같은 catkin/src에 만듬;;;)  
예: ~/catkin_ws/src/gazebo_plugin_tutorial/build

- 반면 catkin 패키지로 만든 spawn_other_robots 는 catkin build로   
devel/lib에 shared lib이 생성되므로 참고  
예: ~/catkin_ws/devel/lib 



## 참고로 publish 하는 방식을 이용해서 다시 또 msg를 전송하면?
원래는 최초 Load()함수를 이용해서 gazebo에서 모델을 띄우고나서   
특정 위치로 이동시키고 싶었는데...  LinearVel()같이 움직이는 것 말고, 특정 pose로 이동   

OnUpdate() 함수를 연동해서 콜백 방식으로 10초 마다 다시 msg::Factory 를 다시 만들어서   
재 전송을 했더니, 작동은 된다. 그러나 새로운 모델이 계속 생긴다;;;   
Factory 자체는 처음에 모델을 불러들일 때 사용하는 것 같다. 모델을 어느 지점으로 이동시키려면 다른 방식을 사용해야겠다..  

다음에 삽질을 방지하기 위해;;;

아마도 ros topic  
**/gazebo/set_model_state** 토픽을 이용해서 pose를 publish하면 될 듯 하다

## 참고  /gazebo/set_model_state
```
rostopic pub /gazebo/set_model_state gazebo_msgs/ModelState "model_name: 'cylinder'
pose:
    position:
        x: -10.0
        y: -5.0
        z: 0.0
    orientation:
        x: 0.0
        y: 0.0
        z: 0.0
        w: 0.0
twist:
    linear:
        x: 0.0
        y: 0.0
        z: 0.0
    angular:
        x: 0.0
        y: 0.0
        z: 0.0
reference_frame: ''" 
```

