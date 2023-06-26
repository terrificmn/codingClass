# adafruit neopixel
OpenCR 을 이용해서 ws2018b 를 이용한 LED를 사용하려고 할 때의 문제 발생  

## 일단 platformIO 에서
platformIO 에서는 adafruit neopixel 라이브러리를 받아서 사용하려고 하면  
빌드 시에 에러가 발생한다  

일단 F_CPU 가 define 이 안 되었다는 에러가 발생한다   
에러를 해결하려고 했지만 쉽지 않은 듯 하다. OpenCR 보드는 ARM STM32F746ZGT6 을 사용하는데  

같은 보드는 아니지만 stm32 보드인 NUCLEO 에서는 해당 라이브러리가 잘 빌드되고   
led도 잘 켜진다   

> 비교해서 에러를 해결해 보려고 했지만 실패  

일단, opencr에서는 Neopixel을 사용하기가 쉽지 않은 듯 하고, 자료도 거의 없다.   
사실 사용하는 사람이 많이 없는 것 같다; 로봇용으로 나왔는데 왜 이렇게 자료가 없는지는 좀 의문   

## arduino IDE 
아두이노 IDE를 사용했을 경우에는 빌드 상에서 에러가 없다   

> 아마도 platformIO에서는 공식으로 지원하고 있지 않기 때문에 그런 듯 하다.   
고수가 platformio에서 가능하게 한 것을 사용하고 있을 뿐.. ㅠㅠ   

하지만 업로드 이후 전혀 LDE에서 반응이 없다. 빌드 후 업로드 시에 에러도 발생하지 않고   
OpenCR이 켜져 있어도 전혀 에러도 발생 안하고 전혀 안됨   

보통  LED를 GPIO 와 arduino 핀에 연결해서 테스트 해보면 digital pin은 이상이 없다   

ws2018b led 도 다른 esp32, stm32 nucleo 보드에서 사용하면 잘만 된다;;;

결론.. 현재 on Jun26 2023 기준으로는 일단 실패다;; OpenCR에서는 쉽지 않다.  
