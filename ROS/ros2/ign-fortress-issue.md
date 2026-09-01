# gazebo fortress 문제, 느려짐 
먼저 light 플러그인 태그? 에서 cast_shadows 를 true 로 사용하게 되면 FPS가 거의 반토막이 된다.  
물론 컴퓨터가 괜찮으면 문제는 안 될 듯 하나,  

false 로 설정하면 많은 향상 된다 예()
> rz_brdige 에서 ros2 topic으로 퍼블리쉬 하는 것도 다소 느려지는 듯 하다. hz는 어느정도 유지하나   

```xml
<light name="sun" type="directional">
    <cast_shadows>false</cast_shadows>
```


physics type="ignored" 태그에서 사용하는 
max_step_size, real_time_factor, real_time_update_rate 등이 있는데 이를 조절하면 조금 향상이 된다.  

max_step_size 0.001 이 적당, 0.1 로 하면 rz_brdige가 영향을 받는다. 지정한 rate로 퍼블리쉬 되지 않는다.   
real_time_factor 1.0  (이것도 낮추면 topic rate도 느려진다. 예 0.1 로 했을 시에 rate 5).   
real_time_update_rate 1000 (500~1000)  

> 컴퓨터에 따라서 위의 설정이 잘 되는 부분도 있고  
조금 변경해서 max_step_size 0.01 에 real_time_update_rate 500 이 잘 될 경우도 있다   
3D 월드뷰? 화면에서 하단에 RTF 와 Sim Time Real Time 의 차이를 볼 수도 있다. RTF 가 100%정도가 아니고  
50%씩 떨어지면 time 갭이 생긴다.


모델들이 많이 사용되면 확실히 느려진다. 로봇 모델 외에 다른 것들을 빼고 topic rate를 확인해 보면   

예를 들어 scan 의 update_rate 를 50 로 했을 경우   
모델이 많은 경우, (벽 등..) 약 모델이 많으면 많을 수록 느려진다. 약 29hz   
없는 상태에서 로봇만 가지고 하면 45Hz 정도 까지 나온다.   

> 확실이 computing power 자원이 있으면 update_rate 지정한 만큼, 그림자 효과도 있어도 크게 상관이 없기는 하다.


## 조금 느리다 싶으면  
최대한 모델을 줄이고

그림자 효과 사용하지 않고  

사용을 하면 되는데  각 센서 플러그인들의 update_rate를 일단 최대한 높이면 그나마 조금 높게 나오는 편이다  

라이다 플러그인 같은 경우에는  
<samples>를 줄여준다. 721 resoultion은 1 ,




