# Serial 연동 esp32 rx tx
MCU 장치끼리 서로 연동을 할 수가 있는데, 기본적으로 rx0, tx0 핀들을 사용한다  

일단 하드웨어 끼리 연결하는 것이라 시리얼 모니터를 사용할 수가 없으나, (방법은 있다)   

OpenCR에서 아두이노 핀 맵을 사용해서 rx, tx를 연결 하고  
ESP32 rx0, tx0 를 사용한다. 서로 반대로 연결을 해주면 된다   

opencr rx ---- esp32 tx   
opencr tx ---- esp32 rx
그리고 그라운드를 서로 연결해준다  


## OpenCR 핀
핀은 기본 gpio 핀 말고, arduino 핀으로 (중앙)에 있는 것을 사용해서   
0, 1 핀인 각각 RX, TX (UART6_RX, UART6_TX ) 로 사용


## ESP32 핀
핀은 RX는 16, TX는 17번을 사용한다  


## Serial 통신

`Serial1.begin(115200)` **Serial1** 을 사용해서 서로 통신을 할 수 있다   

하드웨어로만 연결을 했기 때문에 시리얼 모니터를 볼 수 없으나,   

받는 쪽에서  
`Serial.begin(115200)` 그냥 Serial 으로도 연결을 한 후,    
Serial1 으로 read()해서 그 값을 Serial.print(시러얼1로 받은 데이터) 로 출력을 하면 시리얼 모니터로 확인할 수가 있다  

> 보내는 쪽에서는 Serial1 으로만 그냥 write()해주면 된다  



