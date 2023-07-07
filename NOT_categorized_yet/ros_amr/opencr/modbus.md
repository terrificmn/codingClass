# modbus

패킷구조 

Device Address (driver address)   1 byte  
Function Code   1 byte   
Data    n byte  
CRC     2 byte

요청 시  
Slave Id 1 byte  
Function Code 1byte
data...  시작 주소   2byte
        data 개수 2byte
CRC    2 byte

시작 주소는 0부터 시작 (2Byte 이므로 65535 의 크기를 갖지만)   
데이터개수도 2byte   


응답 ( slave)
Slave Id 1 byte  
Function Code 1byte, 길이 1byte  
Data 첫 번째 2byte  
Data n 번째 2 byte * n
CRC 2 byte


