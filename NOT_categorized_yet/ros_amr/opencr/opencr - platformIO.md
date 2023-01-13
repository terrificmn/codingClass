# opencr

> OpenCR1.0 (Open-source Control module for ROS) 는 아두이노 같은 MCU 이며  
오픈소스이고, ARM Cortex-M7 line-up의 강력한 MCU로 로봇 컨트롤러에 사용된다

arduino IDE인  sketch 프로그램을 사용해도 되지만,  vscode의 platformIO 확장팩이 사용하기 좋다   
하지만 opencr이 바로 인식이 되지 않으므로 깃허브에서 깃클론을 해줘야한다  


자신의 /home 디렉토리에 .platformio 라는 숨겨진 디렉토리가 있는데 이동한다   
```
cd ~/.platformio
```

이제 platforms, packages 디렉토리에 각각 깃클론을 해줘야한다  


## platforms 디렉토리

먼저 platforms로 이동후 깃 클론을 한다 (opencr-support 브랜치를 클론)
```
cd platforms
git clone https://github.com/cguimaraes/platform-ststm32.git -b opencr-support
```

그리고 나서 새로 생긴 (클론)  디렉토리로 다시 이동 후 .piopm 이라는 숨김 파일을 만들어준다
```
cd platform-ststm32
touch .piopm
```

이제, 에디터로 vi, code 등등으로 열어서 json 스트링을 입력 후 저장해 준다 

```json
{"type": "platform", "name": "ststm32", "version": "15.2.0", "spec": {"owner": "platformio", "id": 8020, "name": "ststm32", "requirements": null, "url": null}}
```

> .piopm을 만들어 주는 이유는 매뉴얼로 package를 설치하고 있기 때문에 PlatformIO Package Manager files을 직접 만들어줘야 한다 


## packages 디렉토릭

이번에는 다시 상위의 packages 디렉토리로 이동한다 
```
cd ~/.platformio/packages
```

여기에서 아두이노 ststm32-opencr 패키지를 받아야한다. 깃클론 해준다 
```
git clone https://github.com/cguimaraes/framework-arduinoststm32-opencr.git
```

깃클론이 되면 해당 디렉토리로 이동해서 다시 한번 .piopm 파일을 만들어준다 
```
cd framework-arduinoststm32-opencr
touch .piopm
```

에디터로 .piopm 파일에 아래 내용을 넣어준 후 저장
```json
{"type": "tool", "name": "framework-arduinoststm32-opencr", "version": "1.4.18", "spec": {"owner": "platformio", "id": 8080, "name": "framework-arduinoststm32-opencr", "requirements": null, "url": null}}
```

이제 마지막 설정만이 남았다 


## New Project

vscode 왼쪽 탭에서 PIO home을 클릭해서 New Project를 만들어 준다   

프로젝트 이름은 아무거나 설정하고, 중요한 Board 칸에서 opencr 이라고 검색을 하면   
OpenCr 1.0(ROBOTIS) 라고 board가 나온다. 이제 선택 후  Finish를 눌러서 프로젝트를 만들어준다   

자신의 프로젝트가 만들어졌다면, 예를 들어 프로젝트가 new_opencr 이라면  
new_opencr 이라는 디렉토리가 생기고 그 안에 보면   
platformio.ini 이라는 파일도 있다. 이 파일에 내용을 추가해주자   

```
[env:opencr]
platform = ststm32
board = opencr
framework = arduino
upload_command = ${platformio.packages_dir}/framework-arduinoststm32-opencr/tools/linux/opencr_ld /dev/ttyACM* 115200 $SOURCE 1
```

> monitor_speed = 115200, upload_port = /dev/ttyACM0 으로 따로 설정을 해보았지만 업로드를 해봐도 opencr에서는 전혀 작동하지 않음!
>  upload_command 로 framework 디렉토리와 장치명, braudrate도 설정해준다 

이제 간단한 예제 프로그램을 작성 후 업로드를 하면 opencr이 잘 된다  

```cpp
#include <Arduino.h>

void setup() {

// Set up the built-in LED pin as an output:
	pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
	digitalWrite(LED_BUILTIN, HIGH); // set to as HIGH LED is turn-off
	delay(1000); // Wait for 1 second
	digitalWrite(LED_BUILTIN, LOW); // set to as LOW LED is turn-on
	delay(2000); // Wait for 1 second
}
```


[깃허브 참고 이슈-- 아래 블로그로 이어진다](https://github.com/platformio/platform-ststm32/issues/140)

[참고 블로그 ](https://zenoh.io/blog/2022-02-08-dragonbot/)

[opencr1.0 로보티즈 메뉴얼](https://emanual.robotis.com/docs/en/parts/controller/opencr10/)
