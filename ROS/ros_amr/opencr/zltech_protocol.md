# zltech
velocity mode를 사용하려면 프로토콜 정확히 보내줘야 함   
MCU에도 이미 셋업에서 실행하지만, 실제 Bringup 패키지 등에서 모터에 데이터를 보내려면  
먼저 Velocity Mode를 해줘야 하는데   

제어 순서는 
예:   
1. Velocity Mode   
2. Acceleration time (left) to xxx ms   
3. Acceleration time (right) to xxx ms  
4. Deceleration time (left) to xxx ms   
5. Deceleration time (right) to xxx ms   
6. Enable   

> 속도는 기본은 500ms   

**Enable이 가장 중요**. Enable을 안하게 되면 velocity관련 제어를 할 수가 없다.   
Acceleration / Deceleration time 을 안하게 되면 일정한 속도로 양쪽 바퀴 제어가 안 되는 듯 하다  

