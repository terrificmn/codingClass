# ac
AC: Alternating Current   

집으로 들어오는 전기는 110 - 240 VAC 정도 된다   
이 정도의 VOLTAGE는 **사람을 다치게 하거나 죽게 할 수 있다**  매우 주의 해야함    

- 직접 high-voltage를 작업하지 않는다!  high-voltage를 빵판에 연결하지 않는다!  
- I/O 핀에 직접 high-voltage를 연결하지 않는다!
- wires 만지기전에 voltage 테스트를 반드시 해야한다!
- power를 연결하기 전에 항상 더블 체크


안전하게 사용하기 위해서는 220v 의 전압을 떨어뜨려 주는 장치가 필요한 듯 하다 (transformer)   
(예를 들어 12V 로 떨어뜨려주는 장치?)   

## REALY 모듈

input Voltage를 isolation 을 해주는 것이 safety 를 위해서 중요하다   

relay 모듈에는 VCC, GND, IN 이 있고 => 아두이노의 5vcc, GND, digital PIN에 각각 연결되게 된다   
또한 realy 모듈에는 NO, NC 가 있는데    
NO: Normally Open 
NC: Normally Close   

NO 에 power supply 등에 연결하게 된다, 


[좀 더 연구해보기, 그냥 내부적으로 5v 릴레이만 사용해보는 것 시도해보기 DroneBot Workshop 참고](https://www.youtube.com/watch?v=H8FrL37Z7xE)  

20:00
