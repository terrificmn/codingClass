# rs485 Serial3  
rs-485.md 파일의 예제 처럼 작동에는 잘 된다.   

기본적으로 OpenCR은 Dynamixel 관련 rs485 라이브러리는 제공하나  
다른 프로토콜에 해당하는 라이브러리, 프로토콜은 제공하지 않는다.   

하지만 rs485 통신이 안되는 것은 아니다. 잘 된다!

## Class로 사용 시 주의사항
Class를 만들어서 전역 변수로 instance를 만들어서 사용할 경우   
클래스의 constructor 부분에 Serial3.begin() 등으로 시작해도 빌드 시 문제가 없지만   

아두이노 스타일의 setup() 함수에 정의를 해주지 않으면 제대로 작동하지 않는다   
그래서 setup() 함수에 정의를 해주고, 클래스에서는 따로 정의를 안 해도 된다   

> Serial 같은 경우에는 어디에서나 사용할 수 있으므로 클래스 내에서도 선언을 안해도 사용이 가능하다    
(setup에서 begin이 되었다면.. )   


```cpp
// 이런식으로 define을 해서 rs485를 Serial3 처럼 사용할 수도 있고 
#define rs485 Serial3

// 아니면 
void setup() {
    pinMode(84, OUTPUT);
    rs485.begin(9600): 
    Serial3.begin(9600); // 이런식으로 사용도 가능 (둘 중에 편한 방식으로..)
}

```

## Serial3.write() 할 때 
opencr에서 시리얼로 통신을 하려면  해당핀을 HIGH 신호로 변경해줘야 하는데   

신호를 HIGH를 주게되면 transmit할 때 사용된다   
신호를 LOW를 주게되면 receive를 할 때 사용이 된다   

그래서 시리얼로 데이터를 write을 해서 보낼 때에는 반드시 HIGH를 주게된다   
그리고 송신이 끝나면 LOW를 줘서 데이터를 받을 수 있게 해준다   

> HIGH로만 하면 수신이 안 되고 송신만 된다   

```cpp
digitalWrite(84, HIGH);

Serial3.write(data);
Serial3.flush();

digitalWrite(84, LOW);
```

송신이 잘 안된다면 digitalWrite() 후에 delay(10) 정도 필요할 수 있다   
통신하는 모듈과도 관련이 있겠지만..(예: 모터 드라이브 등..)   
digitalWrite(핀, HIGH/LOW) 는 반드시 필요하고, delay()를 5 또는 10 정도가 필요할 수가 있다. HIGH, LOW 처리 후 사용

> flush() 정말 중요. 끝까지 잘 보내게 된다 (기다림)  





