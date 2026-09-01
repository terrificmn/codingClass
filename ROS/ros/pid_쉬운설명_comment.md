# pid 쉬운 설명
공식 말고 P, I, D 에 대한 쉬운 개념인 듯 하다 

PID 에서  Proportional, Integrator, Derivative   
P, D가 좀 더 중요한 듯 하다  

P는 원하는 목표 타겟에 도달 할 수 있게 하는 파라미터 쯤으로 생각하면 된다  

그래서 P가 High 값이 라면  
목표치에 금방 도달해버리고, 이렇게 되면 overshoot가 되어서 목표치를 벗어나서 다시 내려왔다 올라갔다 하는 게 되어버리고  

P가 너무 low라면  
목표치에 도달하는데 꽤 시간이 걸리게 되어, overshoot는 적게 발생하겠지만  
poor 컨트롤 및 빠른 리액션을 할 수가 없게 된다   
(P가 너무 너무 낮다면 목표치에 도달 못 할 수도 있다)


여기에 D는 P의 움직임을 보상, 상쇄해주는 역할을 한다   
그래서 P에서 목표치에 올라갈려고 할 때 많이 근접하게 되면 D에 속도를 낮춰야 한다 신호를 주게 되고   
이는 마치 break force를 발생시키는 것 처럼 P의 움직임을 상쇄해서 overshoot를 발생을 낮춰주게 되어   
목표치에 부드럽게 접근하는 모습을 보일 수가 있다  


I는 P가 목표치에 도달해서 목표치에 근접했을 경우 더 이상 acceleration을 하지 않는 경우에   
I의 좀 더 목표치 도달 할 수 있게 해주는 역할


## 나름 센스 있는 comment
공식보다는 개념을 이해할 수 있게 도움이 되는 말인 듯 하다   

D is watching sudden change of position within the fraction time to give feedback.   
It does’t matter where the target is.
So ..
1. Set P for the smooth and sluggish curve.   
2. Set I to help add power to P if it is taking too much time to get to the target.   
3. Set D to push the power back if  I  is doing too much work and excessive acceleration.  

P I’ll try to get to the target.   
I   I’ll give you extra power because you are taking too much time.   
D I’ll slow you down because I is giving too much power and detected sudden movement in short period of time.