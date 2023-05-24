# arduino ide 에 esp32_추가 하기

File-> Preferences

Additional boards manager URLs 에 
```
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```
추가해준다 

Tools -> Board 선택 부분에서 -> Board Manager를 선택해준다  

**esp32** 로 검색 후 Esppresif 에서 제공하는 (하나 밖에 업음)  
설치해준다


이제 보드 선택하는 부분에서 esp32 관련해서 많이 나오게 된다 

그 중 대표적으로 *DOIT ESP32 DEVKIT V1* 정도로 선택하면 무난히 잘 됨

> 사용했던 30핀 ESP32 USB-C 버전, 업로드 잘 되는 버전으로 DEVKIT V1 이라고는 되어 있음




