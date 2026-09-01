# ESP32 vscode

Board 종류가 많다. 그래서 *esp32 dev* 정도로 검색을 하면   

doit-devkit-v1 으로 시작하는 것이 있는데, esp32doit-devkit-v1 를 선택해주면 된다. 

> 30핀짜리 ESP32로 했을 경우에는 잘 됨

또는 Espressif ESP32 Dev Module 이 나오는데 이를 선택해주고 새로운 프로젝트를 해주면 된다.    
framework는 Arduino로 선택  

(프로젝트를 만들게 되면... )   
platformio.ini 파일은 아래와 같이 생성이 된다 
```
[env:esp32doit-devkit-v1]
platform = espressif32
board = esp32doit-devkit-v1
framework = arduino

//// 또는 
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

usb 로 컴퓨터로 연결을 했을 경우에   
`/dev/ttyS0` 와, `/dev/ttyUSB0` 로 2개의 device가 나오는 것 까지는 확인  

## 핀 주의 사항
디지털 핀을 사용할 경우에 사용이 안되는 것들이 있다. 그래서 그 핀을 연결하고 계속 업로드를 하면 업로드가 실패하게 된다   

일단, **GPIO 12번** 핀은 OUTPUT 전용인데, 내부적으로 사용이 되는 것 같다. 외부에서 연결해서 사용할 수 없는 듯 하다   
(ESP32 보드에는 D12 로 프린트 되어 있다.)

그리고 **GPIO 35**, **34**, **39**, **36** 은 INPUT only 로 작동하게 된다   
(ESP32 보드에는 각, D35, D43, VN, VP 로 프린트 되어 있다.)



![esp32-pinout](img/esp32-pinout.png)   
[참고사이트 lastminuteengineers.com](https://lastminuteengineers.com/esp32-pinout-reference/)

