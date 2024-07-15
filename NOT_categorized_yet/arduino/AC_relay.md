# ac
AC: Alternating Current   

집으로 들어오는 전기는 110 - 240 VAC 정도 된다   
이 정도의 VOLTAGE는 **사람을 다치게 하거나 죽게 할 수 있다**  매우 주의 해야함    

- 직접 high-voltage를 작업하지 않는다!  high-voltage를 빵판에 연결하지 않는다!  
- I/O 핀에 직접 high-voltage를 연결하지 않는다!
- wires 만지기전에 voltage 테스트를 반드시 해야한다!
- power를 연결하기 전에 항상 더블 체크


안전하게 사용하기 위해서는 220v 의 전압을 떨어뜨려 주는 장치가 필요한 듯 하다 (transformer)   
(예를 들어 28v 떨어뜨려주는 장치?)   
전압변압계 트랜스포머


## REALY 모듈
Electromagnetic switch 를 이용하는 모듈, 100년도 넘은 방식이지만 아주 잘 작동한다.  

input Voltage를 isolation 을 해주는 것이 safety 를 위해서 중요하다   

relay 모듈에는 VCC, GND, IN 이 있고 => 아두이노의 5vcc, GND, digital PIN에 각각 연결되게 된다   

또한 realy 모듈에는 NO, NC 가 있는데    
NO: Normally Open 
NC: Normally Close   
NO 에 power supply 등에 연결하게 된다, 
COM: 그라운드   
그라운드에 장치를 연결해준다.  예: 전구, 연결된 선은 다시 파워서플라이의 그라운드로 연결해주면 된다.


## arudino 등 MCU
에서는 pinMode는 OUTPUT으로 설정해서 사용하면 된다.

```cpp
setup() {
    pinMode(RELAY_PIN, OUTPUT);
}
loop() {
    /// relay가 NO로 되어 있다면 low를 주면 전원이 연결이 되게 된다.
    digitalWrite(RELAY_PIN, LOW);
    delay(2000);

    /// HIGH를 주면 OFF의 효과가 있다.
    digitalWrite(RELAY_PIN, HIGH);
    delayo(2000);
}
```

## solid state switches
무접점 릴레이



[좀 더 연구해보기, 그냥 내부적으로 5v 릴레이만 사용해보는 것 시도해보기 DroneBot Workshop 참고](https://www.youtube.com/watch?v=H8FrL37Z7xE)  

20:00
