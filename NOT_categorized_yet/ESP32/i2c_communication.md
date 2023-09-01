# I2C 
I2C 마스터와 슬레이브를 설정해서 통신을 할 수 있는 프로토콜

## 마스터
마스터로 설정을 하면 master가 slave를 통제하게 되어 있어서,   
슬레이브쪽으로 데이터를 보낼 수도 있고, 슬레이브로부터 데이터를 받을 수 있다.   
단, slave쪽에서는 데이터 transmission을 시작할 수가 없고 오직 마스터만이 slave에게 data를 보내게 할 수 있다.  

## Wire
`Wire.h` 파일을 인쿠루드 해서 사용  

setup() 함수에서 begin() 함수로 사용하게 된다. 이때 파라미터로 SDA, SCL 핀넘버를 넘겨준다  

```cpp
#include <Wire.h>
#define SDA 21
#define SCL 22

int SLAVE_ID = 0x02;   

setup() {
    Wire.begin(SDA, SCL);
}
```
이때 슬레이브로 사용할 ID를 위 SLAVE_ID 처럼 지정해 준다. 임의로 숫자로 지정하면 된다   


## write 과 requestFrom
마스터에서 전송을 시작할 때에는 write 함수를 사용할 수 있고   
위에서 언급한 것 처럼 slave 장치로 부터 데이터를 수신 받고 싶을 때에는 requestFrom 함수를 통해서 요청 한다

write함수 예
```cpp
uint8_t data = 1;
Wire.beginTransmission(SLAVE_ID);
Wire.write(data);
Wire.endTransmission();
```

requestFrom() 사용 예
```cpp
byte how_many = 1;
Wire.requestFrom(SLAVE_ID, how_many);
```

## read 
읽을 경우에는 read(), readBytes() 함수를 통해서 읽는다.  

예
```cpp
uint8_t buf[1];
Wire.readBytes(buf, 1);
Serial.print("buffer: ");
Serial.println(buf[0]);
```
> 한 개의 바이트(데이터) 만 읽는다.   


read() 함수 등도 한번에 하나씩만 받아지는 것 같다. 여러개의 바이트 줘서 한번에 그 바이트 수 만큼 반복 시키는게 안되었던 것 같다   
> read() , readBytes() 를 사용한 다음에 for loop 등을 이용해서 안의 데이터를 배열에 저장시키는게 안 된다  
read 했을 때 한번씩만 읽어지는 것 같다. 그래서 loop 자체에서 한번 돌면 비로소 그 다음 데이터가 읽어지는 데 아마도 clock과도 관계가?  
정확히는 모르겠다. 어쨋든 loop 이 돌면 다음 데이터가 들어오므로 10개를 보냈다면 10번 loop이 돌면 추가로 배열에 쌓을 수가 있다   

Serial 처럼 for문으로 한번에 받아지지는 않는듯 하다   


## loop() 함수 내에서 처리

```cpp
loop() {
    uint8_t data = 1;
    Wire.beginTransmission(SLAVE_ID);
    Wire.write(data);
    Wire.endTransmission();

    byte how_many = 1;
    Wire.requestFrom(SLAVE_ID, how_many);

    uint8_t buf[1];
    Wire.readBytes(buf, 1);
    Serial.print("buffer: ");
    Serial.println(buf[0]);

}
```
위에서는 한 개의 데이터만 보냈지만 여러 바이트를 보낼 경우에는   
for문으로 감싸서 array형식으로 만들어 준 다음에 byte(데이터 수) 만큼 반복해서 write() 함수를 사용하면 되겠다.  

```cpp
uint8_t how_many_array_count = 5; 
uint8_t data[5] = { 0, 1, 2, 3, 4 };

for(unsigned int i=0; i < how_many_array_count; i++) {
    Wire.beginTransmission(SLAVE_ID);
    Wire.write(data[i]);
    Wire.endTransmission();
}
```

마스터에서 데이터를 받기 위해서는 slave 쪽에 요청을 해야하는데, 이때 byte 수를 파라미터로 넘겨줘야 하는데  
정확한 수를 보내줘야 하는데, 어떻게 유연하게 보낼 수 있을 지 고민해봐야한다  

**물론 Slave 장치**에서는 requestFrom() 함수에 대한 응답으로 보내는 코드를 작성해 줘야하고   

> 만약 master에서 requestFrom()을 통해 10개 데이터를 요청했는데 슬레이브쪽에서 5개만 보낸다면  
나머지 5개의 데이터는 255 식으로 채워지게 된다.  필요 없는 데이터는 버리거나 아예 buf 배열에 저장시키지 않는 방식도 있을 듯 하다.    
일단, 주고 받는 데이터가 일정하면 문제가 안되지만, 데이터 길이가 변경되는 경우에는 생각을 해봐야할 듯 하다

Wire.avaliable() 함수 같은 경우에는 실제 들어온 byte 수를 리턴 하지 않고   
마스터에서 requestFrom() 함수에서 요청한 byte 수만큼 읽어 지는 것 같다.   




## Slave 쪽 통신
slave쪽 mcu에서 먼저 Wire.h 인쿠르드가 필요하고  
마스터에서 설정한 slave id를 같이 적용해준다.  

```cpp
#include <Wire.h>

int SLAVE_ID = 0x02;  
```

마스터와는 다르게 transmission을 할 수가 없기 때문에 SDA, SCL 핀 넘버를 셋팅을 할 필요는 없다   

> 물론 SDA , SCL 선에는 연결


## I2c interupt로 연결
마치 interupt로 연결하듯 callback 함수처럼 함수를 만들어준다   

```cpp
// 선언부
void receiveEvent(int how_many);
void requestEvent();
```

setup() 함수 부분에서 Wire.begin()을 시작

```cpp
void setup() {
    Wire.begin(SLAVE_ID); 
    Wire.onReceive(receiveEvent); //위의 함수를 넘겨준다
    Wire.onRequest(requestEvent); // only master can request data to slave

}

```

이제 실제 receiveEvent(), requestEvent() 에서 각각 데이터 처리 및 통신을 하면 되겠다  

```cpp
void receiveEvent(int how_many) {
    int result = Wire.available();
    uint8_t read_value = Wire.read();
}

void requestEvent() {
    Wire.write(1);
}
```

주의 해야할 점은 아마도.. interupt 이기 때문에 loop함수 내에서 같은 변수를 사용하거나 할 때   
주의가 필요할 듯 한데..  

std::mutex 처럼 lock을 걸 수 있는 것을 테스트 해보면 좋을 듯 하다   

arduino 에서는 Arduino_FreeRTOS.h, semphr.h 을 이용해서 할 수가 있는 듯 하다.    
> 라이브러리는 feilipu/FreeRTOS@^10.5.1-1  

먼저 thread를 만들 듯이 먼저 함수 정의를 해줘야하는 듯 한데... 

FreeRTOS 를 사용해서 함수를 지정할 때, Wire.onReceive(), Wire.onRequest()로 지정을 해야하므로   
이를 함수 포인터로 넘기는 식으로(?) 하면 되지 않을 까 생각... ㅠ  

많은 테스트가 필요할 듯 하다  




