# libneopixel 라이브러리 테스트 
opencr에서 neopixel 라이브러리가 잘 안되서 테스트 해봄   

빌드 및 업로드 잘 되지만,  이것도 반응이 없다   
최대 단점은 소스코드의 example 등이 없고, 주석는 잘 되어 있으니 분석을 해봐야한다  

## 깃 클론
플랫폼io 기준으로 패키지를 만들고 직접 깃 클론을 해준다  

```
cd ~/Platformio/my_pkg/lib
git clone https://github.com/berndoJ/libneopixel32.git
```

깃 클론을 받아보면 include 디렉토리가 inc 로 되어 있다   
include로 변경해준다 (원활한 인식을 위해서)   

그리고 빌드할 경우에 src/neopixel32.c 을 인식을 잘 못한다   
그래서 cpp 파일로 확장자를 변경해준다 (neopixel32.cpp)

이제 빌드를 하면 잘 인식을 한다   

여태 것 해본 example 코드인데 아직 작동은 안한다  
```cpp
#include <Arduino.h>
#include <neopixel32.h>

#define NEO_PIN 53

NP32_Instance_t neo_32;
NP32_RGB_t rgb;

void setup() {
    Serial.begin(115200);
    neo_32.LED_Count = 4;

    rgb.R = 200;
    rgb.G = 100;
    rgb.B = 50;
    neo_32.LED_Col_Buffer = &rgb;

    int8_t result = NP32_Init(&neo_32);

    NP32_SetLED_RGB(&neo_32, 4, rgb);

    if(result == -1) {
        Serial.print("error");
    }

}

void loop() {

    NP32_Update(&neo_32);
    delay(2000);
    
    NP32_ClearAllLEDs(&neo_32);
    delay(2000);
}

```


## static 라이브러리도 make 파일로 지원
libneopixel32 로 이동해보면   
Makefile 있는데 여기에서 inc를 바꿔줬기 때문에 여기도 바꿔준다. 동시에 cpp 파일로도 지정해주면 되겠다   

```c
# --- SOURCE FILES ---
C_SRC = neopixel32.cpp

# --- INCLUDE DIRECTORIES ---
INC  = -I ./include
```

빌드를 하려면 Makefile 이 있는 libneopixel32 디렉토리 내에서 
```
make all
```
해주면 bin 디렉토리에 스태틱 라이브러리가 만들어진다.   

.a 파일을 사용하려면 find_package() 따위를 해줘야 할 것 같은데, platformio 에서는 어떻게 하는지   
아직 잘 모르겠다.  

추후 업데이트!
