# ign fortress axis 변경하기
기존 완성되어 있는 모델에서 (meshes 관련 dea / sdl 파일등에서 )   
기존 앞뒤를 바꾸려고 할 경우에는  

blender로 파일을 import 한 다음에   

참고로 뷰 시점에서는 x(빨강), y(연두), z(파랑)로 ros 축과 비슷해 보이는데  

이제 export 에서 dae 또는 sdl로 선택을 한 뒤에  
저장하기위한 창이 뜨면, Transform 부분에서 Forward와 Up을 지정해준다.  
현재 모델 기준으로는 Y Forward가 기준으로 되어 있어서 -Y Forword로 지정해주면 앞뒤가 바뀐다.
UP은 Z UP으로 해준다   

> 단, X가 아닌 Y축 인지는 잘 모르겠다. 원래 파일 자제에서 그렇게 설정되어 있는 건지  
blender 쪽이 그런지? 공부가 필요.  

> 그리고 한번 저장을 하게 되면 해당 Transform이 마지막에 했던 값으로 되어 있기 때문에  
원하는 방향으로 바꿔서 저장을 해줘야 한다. 꼭 원래 방향을 표시하지 않는 듯 하다.




# ign fortress sdf 에서 axis 변경하기 
sdf 파일 또는 urdf 파일에서 wheel link joint 부분에서   
axis 태그의 z축을 변경한다. 1 또는 -1, 모델의 meshes 의 상태에 따라서 변경해봐야 할 수 있다.

예
```xml
    <joint name="my_right_wheel_link_joint" type="revolute">
      <parent>base_link</parent>
      <child>my_right_wheel_Link</child>
      <axis>
        <xyz>0 0 1</xyz>
        <!-- <xyz>0 0 -1</xyz> -->
        <limit>
          <lower>-1.79769e+308</lower>
          <upper>1.79769e+308</upper>
        </limit>
      </axis>
    </joint>
```

> rviz나 gazebo 등에서 joint를 봐가면서 하면 도움이 된다.  

또는 아예 link의 pose를 특히 roll 부분을 회전을 시켜야 한다면 이 부분을 변경해야 할 수 도 있다.
예
```xml
<link name="my_left_wheel_Link">
    <pose>0.0 0.225 0.0 -1.5707 0 0</pose>
    <!-- 또는 <pose>0.0 0.225 0.0 1.5707 0 0</pose> -->
    <inertial>
    <!--이하 생략 -->
```
> 역시 meshes 또는 shere 등의 모델 형태에 따라서 roll 부분을 수정해준다. 


