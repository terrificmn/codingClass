
소스코드 내에 최소/ 최대 pulse값을 넣어주는 것이 있는데 이것으로 PWM 된
다   

> Pulse-width modulation



c코드는 아직 다 못 보았지만, 
`min_pulse_width=0.0005, max_pulse_width=0.0025` 라고  정의해 줘야한다면    
이 정보를 어떻게 알 수 있냐하면 서보 모터의 데이터 시트를 참고해야한다  

예를 들어 아래와 같은 스펙을 가지고 있다면..  
| item              | Control Specification |
| ----------------- | --------------------- |
| Pulse width range | 500 - 2500 us                      |

여기 데이터 시트에서 나온 us 라는 수치에서 1,000,000 을 나눠주면 된다 

그래서 최소는 0.0005,  최대는 0.0025 가 된다

> us 는 마이크로 세컨드(second) 인 듯 하다. 이를 초(second)로 바꾸면 위 처럼 되는 듯 함 (1 million을 나눠준다)
> 참고로 ms 는 밀리 세컨드. 1000 (1 thousand)을 나눠준다 


wiringPi build에 대해서 알아보기   
softServo.h 파일이 없음



