# usart2
stm32 보드에서 pc로 통신을 할 때 usb serial로 통신을 
uart 을 사용할 수가 있는데  

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




두 개의 data signals를 사용 Rx(Receive), Tx(Transmit)   
연결할 두 개의 장치에는 baudrate가 필요 - (hz frequency)

stm32보드에 직접 연결할 때에는 ground 선을 연결하고,   
rx, tx 선도 연결   
+도 연결, 

usb 연결 선에는 rx, tx가 통합된 선도 있는 듯 하다

리눅스에서는 최종적으로 Usb를 pc에 연결하면 /dev/ttyACMx 또는 /dev/ttyUSBx로 잡히게 된다   

