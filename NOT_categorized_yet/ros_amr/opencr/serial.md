serial은 "하나 다음에 또 다른 하나" 처럼 연속적으로 되는 통신을 하는데,   (직렬통신 이라고도 함)
하나의 bit을 transfer 하고 또 하게 된다 

다행이도 아두이노의 Serial 라이브러리를 사용하면 된다

```
Serial.begin(9600);
```

begin() 함수로 시작을 하는데, 여기에서 숫자는 bps 속도를 의미 (bits-per-second)   
여기에 들어가는 파라미터는 braud rate 이다, 즉 초당 9600 bit를 전송





