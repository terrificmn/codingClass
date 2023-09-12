# opencr

> OpenCR1.0 (Open-source Control module for ROS) 는 아두이노 같은 MCU 이며  
오픈소스이고, ARM Cortex-M7 line-up의 강력한 MCU로 로봇 컨트롤러에 사용된다

opencr의 r은 ros를 의미! 

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
mkdir platforms; cd platforms
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

> 안 나온다면 vscode를 종료 후 다시 시도, 또는 로그오프

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



## 아두이노 ide에서 복사시켜서 업데이트   
또 다른 방법으로는  
arduino IDE와 같게 맞춰주는 방법이 있다  

아두이노 IDE로 opencr 보드를 추가시킨다음에 보면  

다음 경로에  
`/home/myuser/.arduino15/packages/OpenCR/hardware/OpenCR/1.5.2`

부트로더, cores, libraries, variant, 나머지 txt 파일이 있는데   

즉 전체 디렉토리 1.5.2 디렉토리의 내용을 복사해서   
`/home/sgtubunamr/.platformio/packages/framework-arduinoststm32-opencr` 에 복사 덮어쓰기를 해준다   

모두 파일을 merge를 해주면 된다   



## opencr core 업데이트?
> 위에 아두이노IDE에서 동일하게 복사했다면 구지 할 필요 없다

platformio의 opencr 보드는 ROBOTIS-GIT/OpenCR 에서 fork를 해온 것이므로 참고를 할 수 있으나   
현재 업데이트된 내용은 별로 없어보이고 라이브러리 정도만 업데이트가 된 듯 하다   

[opencr 깃허브](https://github.com/ROBOTIS-GIT/OpenCR)   

여기에서 다시 클론을 해준다음에  

`https://github.com/ROBOTIS-GIT/OpenCR/tree/master/arduino/opencr_arduino/opencr/libraries` 여기 경로를 보면   

라이브러리에서 OLLO, turtlebot3, turtlebot3_ros2, OpenCR (example 코드 등) 업데이트 됨  

이 디렉토리들을 복사 후  아래의 경로에 복사해준다  
`/home/myuser/.platformio/packages/framework-arduinoststm32-opencr/libraries`

