# my mecanum project
mecanum project 언제 시작??

## bitRead()
먼저 bitRead()함수를 이해하고 넘어가자~

arduino의 bitRead() 를 사용한 예제  
파라미터는 2개를 받게 되어 있다. 각각 bit, last_bit  
: 이 함수는 bit의 요청된(파라미터) 하나의 비트를 리턴해준다(0 or 1)

`bitRead(5, 0);` 로 하게 되면 10진수 5는 바이트로 101이 된다   
이제 1바이트(8비트)로 표현해줘서 앞에서 0을 붙여주면 0000 0101 이 되는데  
2번째 파라미터 0 은 비트의 가장 작은 수를 의미, 그러므로 우리 입장에서 제일 마지막이 되겠지만,  
제일 작은 비트라고 해야하는 것이 맞는 것 같다. 

어쨋든 0에(the least) 해당하는 비트는 1 이므로 1을 리턴!  
`bitRead(5, 1);` 이렇게 하게 되면 2번째 비트는 0 이니깐 0을 리턴


## 스케치 코드에서..
메카넘 휠로 움직일 수 있는 움직임이 총 18개 이다. (아마 최소?)  

그래서 그 해당하는 것을 움직임에 대한 코드를 byte로 지정을 해놓았는데  
코드에서  
```cpp
#define MOTOR_FRONT_AI1 32
#define MOTOR_FRONT_AI2 23
// 생략...그 밖에 모터 드라이브에 연결될 output 들.. 총 8개

void setup() {
    const byte STRAIGHT_FORWARD = B10101010;
    //...생략... 이런 움직임 정의가 18개나 있다 -- mecanum이면 가능
    
    pwm_speed1 = 100;
    pwm_speed2 = 100;
    //..생략..
}

void moveMotors(speed1, speed2, speed3, speed4, move_control) {
    //....생략...
    digitalWrite(MOTOR_FRONT_AI1, bitRead(move_control, 7) );
    digitalWrite(MOTOR_FRONT_AI2, bitRead(move_control, 6) );

    digitalWrite(MOTOR_FRONT_BI1, bitRead(move_control, 5) );
    //.. 생략  .. bitRead()의 2번째 파라미터가 순차적으로 줄어든다
}

void loop() {

    // 실제로 moveMotors()를 loop()함수에서 call
    moveMotors(pwm_speed1, pwm_speed2, pwm_speed3, pwm_speed4, STRAIGHT_FORWARD);
}
```

대충 재연하자면 이런 느낌인데.. 처음에 pin 셋팅하고 각 속도 셋팅 후 moveMotors()로 넘기는 것을 알겠으나   
bitRead()에서 왜 2번째 파라미터가 자꾸 줄어들까?  

왜 그런지 고민 이였는데, 처음에 움직임에 대해서 정의를 했을 때   

STRAIGHT_FORWARD 같이 정의 된 부분이 byte로 정의했는데 이게 모터 드라이브와 하나씩 매칭이 되는 byte였다  


즉,  
첫 번째 1 0 --> MOTOR_FRONT_AI1 에 매칭,  
두 번째 1 0 --> MOTOR_FRONT_AI2 에 매칭,  
세 번째 1 0 --> MOTOR_FRONT_BI1 에 매칭,   
네 번째 1 0 --> MOTOR_FRONT_BI2 에 매칭  

마지막으로 digitalWrite에서는 HIGH, LOW 밖에 없으니, 그 값이 bitRead()한 값이 정확이 2개씩 떨어지게 된다.  
파라미터로 넘어간 7, 6 은 가장 큰 bit 수, 8번째 7번째 이므로 (0부터 시작) , 리턴된 값은 각각 1, 0  
이렇게 되면 첫 번째 모터 드라이버에게는 HIGH가 , 두 번째 모터 드라이버에게는  LOW가 들어가게 되는 것   

지금까지 이해한 바로는 그렇다. 신기하군~

아직 프로젝트는 시작 안했지만, 코드 분석하면서 배우는게 많다!

추후 계속 업데이트!

