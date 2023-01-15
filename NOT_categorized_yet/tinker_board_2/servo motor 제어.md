
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



mg995
| 종류               | 내용             |     
| ------------------ | ---------------- |     
| Limit angle        | 180 +- 5         |     
| Bearing            | Dual bb          |     
| Motor              | Dc motor         |     
| Operating voltage  | 4.8V             |     
| Pluse with range   | 500-2500 us      |     
| Rotating direction | Counterclockwise |     
| Puse Cycle         | 20 ms            |     


 Position "0" (1.5ms pulse) is middle, "90" (~2ms pulse) is all the way to the right, "-90" (~1ms pulse) is all the way to the left.   
 
 The default servo pulse widths (usually 1ms to 2ms) may not give you a full 180 degrees of motion. In that case, check if you can set your servo controller to custom pulse lengths and try 0.75ms to 2.25ms. You can try shorter/longer pulses but be aware that if you go too far you could break your servo!


gpio readlall 명령어로 확인 했을 때  wPi로 할당되는 부분을 사용하면 되고   
PWM을 지원하는 핀은 PWM0 을 사용해서 26번 핀을 할당해서 사용했다. 실제 물리적핀 번호는 32번이다   


빌드는 
gcc -o  [실파일이름.cpp]  [실행파일이름]  -l [라이브러리이름(-l과 붙여서 사용해도 무방)]

```
g++ servo_test.cpp -o motor_test -l wiringpi
```


```

 +-----+-----+---------+------+---+--Tinker--+---+------+---------+-----+-----+
 | CPU | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | CPU |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | 126 |  21 | GPIO3D6 |   IN | 0 | 29 || 30 |   |      | 0v      |     |     |
 | 125 |  22 | GPIO3D5 |   IN | 0 | 31 || 32 | 0 | IN   | GPIO4C2 | 26  | 146 |
 | 150 |  23 | GPIO4C6 |  OUT | 1 | 33 || 34 |   |      | 0v      |     |     |
 +-----+-----+---------+------+---+----++----+---+------+---------+-----+-----+
 | CPU | wPi |   Name  | Mode | V | Physical | V | Mode | Name    | wPi | CPU |
 +-----+-----+---------+------+---+--Tinker--+---+------+---------+-----+-----+
```
일부분만 가져옴 ..(readall 했을 때)

예를 들어 PWM0 인 32번 핀(Physical)을 사용한다고 하면   
_wiringPiSetupGpio()_  146 
gpio 방식으로 셋하면 맨 끝에 있는 값으로 설정이 된다  tinker 보드 기준시 CPU 라고 나오는 부분

_wiringPiSetup()_ then it work with 26.
그냥  setup은 wPi 로 되어 있는 부분의 pin 번호: 26 할당

*라즈베리파이랑 비교?해 볼것


하드웨어 pwm 방식
```cpp
#include <wiringPi.h>
int main() {

	wiringPiSetupGpio();
	pinMode(18, PMM_OUTPUT);
	pwmSetMode(PWM_MODE_MS);
	pwmSetRange(2000);
	pwmSetClock(192);
	
	while(1) {
		pwmWrite(18, 150) // neutral
		delay(1000);
		pwmWrite(18, 190) // neutral + 45 
		delay(1000);
		pwmWrite(18, 150) // neutral + 45 
		delay(1000);
		pwmWrite(18, 110) // neutral - 45 
		delay(1000);
	}
}

```


소프트웨어 pwm 방식
```cpp
#include <wiringpi.h>
#include <softPwm.h>

int main() {
	wiringPiSetup();
	softPwmCreate(1, 0, 200); // this creates 50hz PWM signal 
	
	while(1) {
		softPwmWrite(1, 15); // this produces 1500 micro seconds pulse width
		delay(1000);
		softPwmWrite(1, 19); // neutral + 45
		delay(1000);
		softPwmWrite(1, 15); // neutral 
		delay(1000);
		softPwmWrite(1, 11); // neutral - 45
		delay(1000);
	}
return 0;
}
```

빌드는 
```
g++ 파일이름.cpp -o servo_test -l wiringPi 
```

[참고 블로그 aleksandarhaber.com](https://aleksandarhaber.com/controlling-servo-motors-using-raspberry-pi-2/)

