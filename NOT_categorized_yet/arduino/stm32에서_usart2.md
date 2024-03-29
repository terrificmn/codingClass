# usart2
stm32 보드에서 pc로 통신을 할 때 usb serial로 통신을 
uart 을 사용할 수가 있는데  

> UART는 프로토콜은 아니고 아두이노에 포함된 circuitry (서킷)라고 생각하면 된다

UART  
Universal Asynchronous Receiver / Transmitter

micro controller에서 incoming/outgoing 데이터를 (bytes)를 serial bit stream 변환해준다  

Start bit로 시작을 해서 Stop bit 으로 끝나게 되어 있는데  
여기서 Stop bit(s)는 1bit이나 2bit가 될 수가 있다   

거기에 UART에는 옵션으로 parity bit를 추가할 수가 있어서 전송할때 에러를 잡는 용도로 사용한다   

| start bit | | | | | | | | parity bit(option) | stop bit | 또는 stop bits |
| --- | --- | --- |  --- |  --- | --- | --- | --- | --- | --- | --- |
| | 0 | 1 |  2 |  3 | 4 | 5 | 6 |  |  |  |


USART 는 Universal Synchronous/ Asynchronous Receiver / Transmitter

UART와 같지만 Synchronous가 추가되어 있다. 

UART에서는 serial data를 시간으로 잴 수 있는 기능이 있는데. 이를 이용해서  
USART에서는 synchronous 모드로 작동을 하게 할 수 있다고 한다   

A USART는 다양한 포맷, 프로토콜을 지원 (UART에 비해 많음)   
IrDa, LIN, Smart Card, rs-485 interface 드라이버, Modbus 등...   
물론 UART처럼 asynchronous로도 작동을 할 수 있다. (start bit -- data -- stop bit)


[참고 geeksforgeeks: USART](https://www.geeksforgeeks.org/difference-between-usart-and-uart/)

[또한 정리가 잘되어 있는 사이트 littelbirdelectronics.com](https://littlebirdelectronics.com.au/guides/147/uart-and-arduino)


두 개의 data signals를 사용 Rx(Receive), Tx(Transmit)   
연결할 두 개의 장치에는 baudrate가 필요 - (hz frequency)

stm32보드에 직접 연결할 때에는 ground 선을 연결하고,   
rx, tx 선도 연결   
+도 연결, 

usb 연결 선에는 rx, tx가 통합된 선도 있는 듯 하다

리눅스에서는 최종적으로 Usb를 pc에 연결하면 /dev/ttyACMx 또는 /dev/ttyUSBx로 잡히게 된다   


## baudrate
두개의 device에서, 이를 테면 PC와 arduino가 연결된다고 하면   
baudrate는 서로 약속이 된 상태에서 통신을 하게 된다   

아두이노에서 자주 사용되는 rate는 9600, 14400, 19200, 또는 115200   

아두이노 uno에는 하나의 serial port 밖에 없지만, 다른 디바이스 같은 경우에는 UART devices가 더 있음 (아두이노 메가)    

그럴 경우 아두이노에서 `Serial1`, `Serial2`, `Serial3` 처럼 사용할 수가 있다    

Uno 기준 64바이트의 버퍼로 RX, TX 두 개의 방향으로 통신을 하게 되는데, 데이터는 손실되지 않음 (overflow 되지 않으면!)   
**overflow** 는 읽는 데이터 보다 받아지는 데이터가 빠를 경우 발생한다


## 시리얼 통신
```cpp
Serial.print("Hello World");
```
이 처럼 print() 함수를 사용하게 되면 ASCII text 케릭터로 표시가 되는데, 이는 serial monitor로 볼 수가 있다     
그냥 숫자를 보내게 되면 아스키코드로 인식을 해서 

예를 들어서 65를 보내게 되면 `Serial.print(65);` 숫자 65가 보내지는 것이 아닌 아스키코드로써 65가 보내지므로   
실제 serial 모니터에서는 'a' 가 찍히게 된다   

> 테스트를 한번 해봐야할 듯 하다 

binary 데이터를 보내려고 하면 Serial.write()함수를 사용하면 된다   

```
Serial.write(0x48); 
```
위의 0x48은 헥사코드로 
H에 해당하는 아스키코드 72를 보내게 되는데, 이때 binary로 0100 1000 을 보내게 된다 











