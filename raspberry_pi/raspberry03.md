https://www.tinkercad.com


SoNAR - Sound navigation & Ranging
RaDAR - Radio Detection & Ranging
LiDAR - Light Detection & Ranging
(* 적외선도 라이다의 일부)

빛의 특징은 가장 빠르고, 직진성이 있다. 
포인트 클라우드. 빛은 어느 포인트에 무조건 맺히는 특징


```
거리 = 속력 * 시간
distance = verocity * time
```

음파는 직진성이 없고 퍼져나감
초음파센서 340m/s , 속도를 알 수 있고, 물체 부딪혀서 다시 오는 시간만 구한다면
거리를 구할 수 있다.

y = 340m/s * x (us)(마이크로세컨드)
y = 340x (m/s * us)

1 s = 1000 ms
1ms = 1000 us 임
여기서 중요한 것은 단위환산이 중요하다

그래서 1s 는 10 6제곱

y = 340 / 10 6제곱
y(m미터) = 17 / 10 5제곱  (m미터)


17/1000 이 나옴



아날로그 In 부분은 입력만 받을 수 있다

각 제품을 보면 제품번호가 써 있는데 
제품번호 datasheet를 확인해보면 해당 제품의 매뉴얼을 볼 수 있다
예를 들어 
초음파 거리센서 HC-SR04 라는 제품을 검색해보면 HC-SR04 datasheet 를 검색 시 
많은 정보를 알 수 있다.

먼저 pinMode로 셋팅, 트리거는(초음파 발생) output이고 에코는 input이다
```
void setup() {
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
}
```

10uS (마이크로세컨즈) trigger을 발생시킨다
이를 프로그래밍하면
```
digitalWrite(trig, LOW);
delayMicroseconds(2);
digitalWrite(trig, HIGH);
delayMicroseconds(10);
digitalWrite(trig, LOW);
```
처음에 0V로 초기화~ 2 마이크로 세컨드 동안 유지시킨다음에 10마이크로 초 동안 5V로 발생시킨다.
그 이후에 다시 0V로 꺼준다.

그 다음에 
거리 구하는 공식을 이용해서 (초음파 속도는 340/m)로 구한 속도를 넣어준다
```
duration = pulseIn(echo, HIGH);
distance = duration * 17 / 1000;
```



삼각함수 
d sin세타
로 초음파 센서에 잡힌 것의 높이도 파악할 수 있다
