# neo pixel led 제어

[adafruit의 공식 NeoPixel 깃허브](https://github.com/adafruit/adafruit_neopixel)

테스트용으로 산 led가 neopixel 이라고하는데  
NeoPixel은 ws2812b, sk6812 칩을 사용하느 RGB, RGBW 의 LED 브랜드  

+, -, digital pin 연결을 위한 선: 대충 이렇게 3가닥 선이 나와 있는데   
(이 신호 선 한개만으로 led를 모두 제어할 수 있는게 Neo Pixel의 장점이라고 한다)


## arduino ide를 이용해서 설치
arduino ide를 이용하면 라이브러리 추가가 쉽다  

Library manger를 클릭을 해준다음에 (화면 왼쪽에 있음)  

*adafruit neopixel* 검색을 해주면 Adafruit 에서 만든 라이브러리가 나오는데 
설치를 눌러주면 된다.  

Sketch -> Include Library 를 메뉴에서 누르면 Adafruit NeoPixel 이 나옴, 클릭해준다 

또는 
```
#include <Adafruit_NeoPixel.h>
```
입력해준다


## 예제
simple 예제를 확인해봐도 되고 

일단 중요하게 쓰이는 함수등을 정리해본다

`#define pin` 넘버를 정의하고, NeoPixels 몇개가 연결되었는지 정의  

Adafruit_NeoPixel 클래스를 인스턴스 해서 만들어 준다   
```cpp
Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
```
클래스 만들 때 3가지 인자를 넘겨주게 된다.  
1. neopixel led 갯수
2. 연결된 pin 넘버 (아두이노 디지털 핀 넘버)
3. 3번째는 NEO_GRB 는 RGB 를 사용, 또는 RGBW 를 사용할 수 있다
    각각 `NEO_GRB + NEO_KHZ800`, `NEO_GRBW + NEO_KHZ800` 

> 네오픽셀을 사용 시 제어에 실패한다면, GRB, GRBW 를 확인해본다.  
> led를 ws2812b 가 아닌 we2811을 사용할 때에는 NEO_KHZ400 으로 사용한다

그 이후 `setup()` 에서는 그 인스턴스 변수를 이용해서 `begin()` 함수사용  
: 디지털 핀을 out 으로 설정해주고, low로 출력이 될 수 있게 해주는 함수

`loop()`에서는 

```cpp
// for문 생략
pixels.clear();
pixels.setPixelColor(i, pixel.Color(150,0, 0));  // 여기서 i는 neopixel 의 해당하는 led를 의미
pixels.show(); // show()을 업데이트 된 pixel color가 전송

```
pixel.Color(255, 255, 255); 메소드는 RGB색 벨류를 받는다.  LED 순서와 색 정보를 업데이트 한후에 
show메소드를 실행하게딘다.


