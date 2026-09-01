# battery protocol
배터리 관련 메뉴얼 (A3)의 4.2 관련 부분을 참고

## Request  
rs485 통신 (modbus 의 프로토콜 형식은 아님)   

- monitoring 2 기능으로 요청

| type | Hex | Meaning |
| --- | --- | --- |  
| SOI | 0x7F | start flag |
| ADD | 0x10 | device address |
| VER | 0x02 | version |
| LEN | 0x06 | length for writing |
| FUN | 0x11 | function code (command) |
| CKS | 0x58 | checksum |


- 또는 monitoring 1 기능으로 요청  

| type | Hex | Meaning |
| --- | --- | --- |  
| SOI | 0x7F | start flag |
| ADD | 0x10 | device address |
| VER | 0x02 | version |
| LEN | 0x06 | length for writing |
| FUN | 0x10 | function code (command) |
| CKS | 0x59 | checksum |


## Response (return 데이터)

monitoring 2 request 했을 때의 응답 프로토콜   

| type | Hex | Meaning |
| --- | --- | --- |  
| SOI | 0x7F | start flag |
| ADD | 0x10 | device address |
| VER | 0x02 | version |
| LEN | 0x1B | length for response |
| FUN | 0x11 | function code |
|  | 0x01 | battery pack status flags |
|  | 0x00 | battery pack status flags |
|  | 0x00 | battery pack status flags |
|  | 0x00 | battery pack status flags |
|  | 0x14 | charging current |
|  | 0x00 | charging current |
|  | 0x45 | highest cell voltage, LOW bit, 10 mV |
|  | 0x10 | highest cell voltage, HIGH bit, 10mv|
|  | 0x33 | lowest cell voltage, LOW bit, 10 mV |
|  | 0x10 | lowest cell voltage, HIGH bit, 10mv|
|  | 0x1D | total voltage of battery pack, LOW bit, 10 mV |
|  | 0x15 | total voltage of battery pack,   HIGH bit, 10mv|
| | 이하 | 생략 자세한 것은 메뉴얼 참고 |
| | 이하 | 총 27개의 byte, 마지막은 CKS checksum |

> 전압만 알기 위한 목적이므로 다른 data는 현 시점에서는 별 필요 없다    
> LEN을 통해서 처음부터 checksum 까지의 데이터 갯수를 알 수 있다   


High값은 256을 곱하고, low 과 더해준다. 단위는 10mV 이므로 곱해서 계산 하면되나...   
더해진 값에서 생략하고 100 나눠서 그냥 V 로 파악해도 됨   
*처음 들어오는 데이터가 LOW 부분이고, 뒷에 들어오는 데이터들이 High

각 위의 예제에서 Highest cell v는 4165 mV * 10mv = 41650 mv / 1000 = 41.65V     
lowest cell v는 41.47V   
totla voltage는 5376 + 29 = 5405 mv * 10mV  = 54050 / 1000 = 54.05V

> monitor1 관련 프로토콜은 메뉴얼 참고


## 우리 프로토콜
위의 프로토콜은 battery에서 자체적으로 BMS 로 rs485 통신으로 알 수 있는 것이고   

BMS 포토콜톨로 전압 파악이 되었으면, AMR Labs에 맞춰서 다시 만들어서 보내게 된다

| Hex | Meaning |
| --- | --- |  
| 0x10 | Device ID |
| 0x13 | Function Code |
| 0x03 | Start Address |
| 0x03 | End Address (length) |
| 0x00 | data - 남은용량 |
| 0x00 | data - 전압 high |
| 0x00 | data - 전압 low |
| 0xFF | crc high |
| 0xFF | crc low |

End Address는 몇개의 데이터를 보낼지 결정 (자기자신 제외)   - 0x03 이므로 3개의 데이터(byte) 보낼 예정

> 남은 용량 계산 등은 프로그램 코드 참고




