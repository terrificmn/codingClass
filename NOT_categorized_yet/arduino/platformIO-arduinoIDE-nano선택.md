## Arduino Nano 업로드 문제 시 
일단 해당 프로세서를 (부트로더)를 잘 선택해줘야 한다  

- 예전 버전일 경우
PlatformIO 에서 예전 버전일 경우에는 nano ATmega328 를 선택해준다. (old라고 안 나옴- 반대로 new가 있음)     

아두이노IDE를 통해서 업로드를 할 경우에는 Processor에서 (old bootloader) 버전을 선택해준다  

그래야지 업로드가 된다 

- 최신(?) 버전일 경우   
최신 버전 일 경우에는 PlatformIO 에서 (new bootloader) 를 선택해줘야 한다   
마찬가지로 아두이노IDE에서는 AtMega328P 를 선택   


겉으로는 구분할 수가 어려운 것 같다. 직접 번갈아보면 업로드를 해서 되는지 안되는지 확인해야함  


### rx tx 핀으로 Serial 통신 중
다른 MCU와 하드웨어 시리얼 통신을 하고 있다면 업로드가 안 된다.   
```
avrdude: ser_recv(): programmer is not responding
```
이런식의 에러가 발생  

잠깐 rx, tx 핀을 뽑고 업로드를 진행한다   

> esp32 는 rx tx로 다른 mcu와 연결해도 업로드 상관 없다




