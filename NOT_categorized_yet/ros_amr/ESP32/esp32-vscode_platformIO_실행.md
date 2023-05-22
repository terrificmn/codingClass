# ESP32 vscode

Board 종류가 많다. 그래서 *esp32 dev* 정도로 검색을 하면   
그 중 Espressif ESP32 Dev Module 이 나오는데 이를 선택해주고 새로운 프로젝트를 해주면 된다.   
framework는 Arduino로 선택  

(프로젝트를 만들게 되면... )   
platformio.ini 파일은 아래와 같이 생성이 된다 
```
[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

아직 테스트는 안해봤지만 usb 로 컴퓨터로 연결을 했을 경우에   
`/dev/ttyS0` 로 device가 나오는 것 까지는 확인   


추후 테스트 및 좀 더 해본 후 업데이트하기!


