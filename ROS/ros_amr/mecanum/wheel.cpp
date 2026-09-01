// Method 1
double speed ; 
double turn;
double strafe;

기본적 공식이지만 정확하지 않다
left_front = speed + turn + strafe;
right_front = speed - turn - strafe;
left_rear = speed + turn - strafe;
right_rear = speed - turn + strafe;



theta와 power을 input으로 사용하는 방법


sin = math.sin(theta - PI/4);
cos = math.cos(theta - PI/4);


left_front = power * cos;
right_front = power * sin;
left_rear = power * cos;
right_rear = poser * sin;

이렇게 해주면 같은 속도로 움직일 수 있게 된다  

여기에서 좀 더 max 값을 구해서 max = max(abs(sin), abs(cos));
그 값으로 나눠주게 된다
cos/max 
left wheel 은 +, right wheel은 - 방향으로 움직인다면   

left_front = power * cos/max + turn;
right_front = power * sin/max - turn;
left_rear = power * cos/max + turn;
right_rear = poser * sin/max - turn;

하나의 바퀴가 max를 넘겨서 그 값이 짤려서 입력이 되면 동작을 이상하게 한다고 함
그래서 maximum을 넘지 않도록 코드를 추가 해준다 
if(power + abs(turn) > 1 ) {
    // 원래 값에서 나눠서 넣어준다 
    left_front /= power + turn;
    right_front /= power - turn;
    left_rear /= power + turn;
    left_rear /= power - turn;
}



입력되는 값은 x, y, turn 인데 조이스틱으로 받는 상황인 듯 한데, 입력값을 알아내야겠다....;;
x = left_stick_x;
y = left_stick_y;
turn = right_stick_x;

그리고 입력된 x, y를 이용해서 theta를 구해줌
/// (보통의 atan은 2 pi or 360 degree range of angles 를 사용해야한다고 함 )
theta = atan2(y, x);
power는 hypotenuse를 사용해서 구해준다 (직각삼각형 관련 공식) a2+b2 (2은 제곱) = c2  // 직각 삼각형에서 빗변의 제곱(square)는 나머지 변의 제곱의 합과 같다
power = hypot(x, y);

완성된 method 2는 아래처럼 된다 
```
x = left_stick_x;
y = left_stick_y;
turn = right_stick_x;

theta = atan2(y, x);
power = hypot(x, y);


sin = math.sin(theta - PI/4);
cos = math.cos(theta - PI/4);
max = max(abs(sin), abs(cos));


left_front = power * cos/max + turn;
right_front = power * sin/max - turn;
left_rear = power * cos/max + turn;
right_rear = poser * sin/max - turn;


if(power + abs(turn) > 1 ) {
    // 원래 값에서 나눠서 넣어준다 
    left_front /= power + abs(turn);
    right_front /= power - abs(turn);
    left_rear /= power + abs(turn);
    left_rear /= power - abs(turn);
}
```

> turn 값은 absoulte 값을 사용   
해당 함수들.. sin, cos, abs, 등은 c++ std 함수로 적절히 사용하면 될 듯하다

