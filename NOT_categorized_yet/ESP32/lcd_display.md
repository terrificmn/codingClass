# lcd 1602
label: meaning   
vss GND   
vdd 5VDC   
VO Bright   
RS register selection  
RW read write  
EN enable pin  
D0 pareller  
D1  
D2  
D3  
D4  
D5  
D6  
D7  
A  Anode (backligt led)  
K Cathode (backlight led)   


원래는 모든 핀들을 다 연결해줘야하는데 digital I/O를 너무 많이 사용하게 된다  


## I2C
- I2C 를 사용하면 I2C Bus (inter integrated Circuit Bus)   
- 여러 디바이스와 컨트롤러를 연결할 때 사용   
- short distances 에 사용됨   

그래서 기존의 LCD에 이미 I2C 가 연결이 되어 있고 I2C의 4개의 핀 만 사용하면 된다  

I2C의 4-pin   
Vcc -3.3 or 5volts   
GND ground  
SDA serila DATA  
SCL serial clock   

참고 속도  
origin clock speed는 100 KHz 와 400 Khz  
fast mode plus - 1Mhz  
high speed mode - 3.4 mhz
ultra fast mode - 5 mhz

SDA and SCL 은 pull-up resistor를 사용 (사용하지 않을 때 시그널이 HIGH)    
마스터와 여러개의 슬레이브로 구성이 될 수 있다.  각 device의 bus는 unique한 address를 갖는다   

ESP32에서 SDA는 D21 핀 이고, SCL 은  D22 pin     
Arduino 에서는 SDA 또는 A4, SCL 또는 A5   

GND VCC 는 각각 esp32의 GND, VIN 물려주면 된다 


## 라이브러리 
라이브러리는 liquid crystal 로 검색하게 되면 LiquidCrystal_I2C 가 나오는데 install 을 해주면 된다.   


만약 깃 클론으로 직접 설치하려고 하는 경우라면, PlatformIO의 프로젝트 디렉토리 안에 lib 디렉토리에 깃 클론하게 되면   
자동으로 .pio/libdeps/ 안에 디렉토리에 복사가 되면서 설치가 된다   


라이브러리 사용 시에 현재 버전은 3개의 파라미터를 받는 것이 일반적임  
예전 방식으로는 d1, d2.. 등 많은 파라미터를 생성자에 넘겼는데~ 이제는 그렇게는 안 됨  

그리고 **begin() 함수도 사용 못함** 

**init() 함수로 대체**해서 사용. 그리고 처음에 setup 함수내에서 backlight() 함수를 실행해야지 화면이 볼 수가 있다 

> 단, lcd 뽑기에 따라 다를 것 같기는 하지만, 현재 가지고 있는 LCD 는 밝기를 최대한으로 낮춰준다. 그래야 조금 볼 수가 있다  
최대 밝기로 되어 있는면 print() 함수를 써서 프린트를 해도 text가 전혀 안보이게 된다    
빌드 시에 문제도 없고 업로드도 잘 되었는데 글자가 전혀 안나온다면 밝기를 낮춰보자;  





