acc_lim_x
acc_lim_theta  
acc_lim_y  
이렇게 있는데  acc_lim_y를  diff drive robot 같은 경우에는 같은 값을 넣어주는 것이 좋은 듯 하다

turtlebot 예제에는 아예 y는 0.0 으로 셋팅되어 있는데   
x, y를 같은 값으로 주면 똑바로 나가는 듯 y를 2배 정도 주면 벽쪽으로 치우쳐진다.. y쪽으로 
y값을 주면 장애물 사이를 똑바로 지나가는 듯 하다;;

x,y를 같은 값으로 설정해주는것이 좋은 듯 하다. 1.0 으로 각각 셋팅함

___

max_vel_x: 0.6  # 0.55
min_vel_x: -0.2

최소 x값에 마이너스 값을 주면 패스를 만들때 회전을 해야하는 구간에서 그냥 후진을 할 수도 있다   

다만 뒤쪽에는 라이다가 없으므로(?) 뒤쪽도 감지하기는 함  
적당히 잘 사용하면 좋을 듯 하다 
___

occdist_scale: 0.02 는 회피율인데..  0.01로 함 (0.02로 하면 return 실패할 수도 있는 듯 함)

이유는  
  max_vel_y: 0.0  # diff drive robot      
  min_vel_y: 0.0 # diff drive robot   
단 y를 0.0 주면 회전을 해야하는 웨이포인트 부분에서 회전을 못함

단, 0.0을 주면 정가운데로 이동함. 단 회전은 못함

그래서 max_vel_x, min_vel_x와 같은 값으로 지정해준다  



___

## common_cost_map 관련 

map_type은 따로 지정하지 않는 것이 낫다











