# fa-duino, faduino
산업용으로 나와있는 arduino 기반 보드  

Board는 arduino mega or mega 2560 ATmega2560 (mega2560) 을 선택해준다

## 전원
24V 로 연결

## 시리얼 upload
upload 포트를 사용하며 Rs232 to USB 변환 어댑터가 필요   
(예를 들어 next-340pl 같은 제품)

rate는 57600 사용


## upload 포트
`/dev/ttyUSB0` 를 사용한다.  
포트가 많은 경우, 심링크를 이용해서 변경해서 사용해도 좋다 (예: ttyFaduino)

