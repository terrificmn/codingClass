# encoder 정보 계산 
encoder에서 나오는 pulse 값이 몇 인지 확인해야함   

16 pulses / 1 rotation   
gear ratio  /  1 output shaft rotation   

> 해당 모터가 한 바퀴를 돌 때 몇 펄스가 나오는지,   
그리고 기어 ratio는 몇인지 데이터시트를 확인해야 한다   

그래서 펄스 * 기어 ratio 가 된다   

그래서 예를 들어서 16 pulses 에 기어 ratio는 18.75 라고 하면 

```cpp
float pulses_per_turn = 16 * 18.75
```

> 또 다른 예로는 11 pulse를 발생시키는 (한 바퀴) encoder에   
gear비는 34:1 이라고 하면   ( 11 * 34 = 374 )  374   
34번의 모터 안쪽 축이 회전을 하게 되면 바깥쪽의 모터 (바퀴 연결부분)의 축이 한 바퀴 돌게 되고   
1 바퀴를 돌면 374번의 pulse가 발생하게 된다


이제 바퀴의 길이를 재서 예를 들어 28cm 이라고 한다면 0.28(m) (100나눠서)    
wheel's circumference 원주, 원둘레 *(C = 2 PI r)*

한 바퀴를 돌때의 길이로 나눠준다. 1 / 0.28 그러면 3.5714가 나오는데    

이를 pulses_per_turn 과 곱해준다  
```cpp
float pulses_per_meter = pulses_per_turn * 3.5714
```

velocity가 1 일 때, ( 1 rotation per second )  

Position change in encoder pulses는   
1 rotation / 1 second x t seconds x 16 * 18.75 pulses / 1 rotation    
이 된다 

그래서 
position_chnage = velocity * delta_t * pulses_per_turn;

모터 수 만큼 반복을 해서 
```cpp
t = fmod(t, 12)  // time in seconds
float position_change[4] = {0.0, 0.0, 0.0, 0.0};
float velocity = 1;  //  일단 1초당 한바퀴

for(int k=0; k < 4; i++) {
    position_change[k] = velocity * delta_t * pulses_per_turn;
}

```
delta_t 값을 알아내야함


Curio Res 채널 다시 확인하기. 일단 tt 모터가 와야 함 ㅜ


## 홀 센서 
홀 센서 A, B 에 따라서 어떤 것이 뭔저 pulse가  High가 되느냐에 따라서 방향을 알 수가 있다   

만약 11 pulse를 발생 시키는 encoder가 있다면   
rpm에 따라서 모터 기어비에 따라서 만약 515 의 모터라면  11 * 515 가 되어야 축이 한 바퀴가 돌게 된다  

## encoder interupt
attachInterupt() 함수를 사용하게 되는데, 이때 콜백 함수 처럼 함수를 불러줄 수가 있고   
RISING, 또는 CHANGE 상수를 파라미터로 넘겨주게 되어 있는데   
이는 마그네틱 홀센서 (encoder의) 펄스가 rising, falling 일 경우 둘 다에도 인터럽트가 발생하게 된다   

인터럽트가 발생했을 때 해당 모터드라이브에 연결된 A, B 의 펄스값을  
digitalRead() 로 호출해서 받는다   



## PID 예제

// PID parameters 
// pid 파라미터는 기계, 모터에 따라서 response가 다 다르므로, 더 좋은 response를 얻으려면 좋은 파라미터 값을 찾아야 한다   
float proportional = 1.35;   // k_p = 0.5
float integral = 0.0005;    // k_i = 3
float derivative = 0.01;    // k_d = 1

// pid-related variables   
float previous_time = 0;     // for calculating dela t
float previous_error  = 0;  // for calculating the derivative (edot)
float error_integral = 0;   
float current_time = 0;     // time in the moment of calculation
float delta_time = 0;   // time difference
float error_value = 0;
float edot = 0;      // derivative ( de/dt)
flost control_signal = 0;

calculatePID();

void calculatePID() {
    // Determining the elasped time
    current_time = micros(); // current_time
    delta_time = (current_time - previous_time) / 1000000.0;  // time difference in seconds  (micro second 이므로 1 밀리언을 나눠준다 )
    previous_time = current_time; // save the current time for the next iteration to get the itme difference

    error_value = motor_position - target_position; // current position - target position(or setpoint)

    edot = (error_value - previous_error) /  delta_time;  // edot = de/dt - derivative term

    error_intergral = error_integral + (error_value * delta_time); // integral term 

    control_signal = (proportionl * erro_value) + (derivative * edot) + (integral * error_integral); // final sum, proportional term also calculated 

    previous_error = erro_value; // save the error for the next iteration to get the difference
}

위에서 계산된 pid 즉, control_signal 값을 가지고 
int pwm_value = (int)fabs(control_signal); // PWM values cannot be negative and have to be integer
// float를 절대값으로 만들어주는 함수 fabs(), 그리고 바로 int로 캐스트 바꿔버림

if(pwm_value > 255) {
    pwm_value = 255;  // 8bit 최대치
}

if(pwm_value < 30 && error_value != 0) {
    pwm_value = 30; // minimum 설정
    // 일정 이하의 PWM에서는 모터를 돌릴 수 있는 전류량이 충분치 않을 수가 있으므로 
    // PWM 수치가 있어도 모터가 움직이지 않을 수도 있다  
    // 그래서 mimimum 수치를 정해줌 --  모터 마다 다를 수 있다고 함
}

// control_signal   pid 계산으로 나온 벨류로 전진 , 후진 등을 알 수가 있다   
if(control_signal < 0) {
    motor_direction = -1; // CCW 로 negative라면 (Counter Clock Wise)
} else if(control_signal > 0) {
    motor_direction = 1; // positive라면 CW (Clock Wise)
} else {
    motor_direcion = 0;
}

// 위에서 결정된 방향으로 모터 드라이브 핀의 값을 결정해준다 
if(motor_direction == -1) {
    digitalWrite(DIR_PIN_1, LOW);
    digitalWrite(DIR_PIN_2, HIGH);

} else if (motor_direction == 1) {
    digitalWrite(DIR_PIN_1, HIGH);
    digitalWrite(DIR_PIN_2, LOW);

} else {   // stop or break -- break 기능이 모터 드라이브 마다 조금씩 다르다 
    digitalWrite(DIR_PIN_1, LOW);
    digitalWrite(DIR_PIN_2, LOW);
}
// 위의 방식으로 define한 digital pin 값으로 넣어줘서 모터드라이브에서 작동할 수 있게 해준다  
// 방향 값을 encoder에서 받을 수 도 있으니 그것을 사용할 수도 있을 듯 하다   

//이제 motor speed를 pwm 값으로 지정해준다 
analogWrite(PWM_PIN, pwm_value);


[참고 Curious Scientis 채널](https://www.youtube.com/watch?v=jTIRUXJKMX4)
