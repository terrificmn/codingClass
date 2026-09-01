# DC Voltage

ADC analog digital convertor

Voltage Sensor  전압 센서. 저렴한 가격에 살 수 있다. 전류 센서도 있는 듯 하다  


s ---> 아두이노의 아날로그 A0 연결
- ---> 아두이노의 GND 연결
> + 는 더미 , 사용햐지 않는다

배터리 (25V 이하) 에서 ADC 모듈의 GND, VCC 부분에 각각 -, + 선을 연결해준다   


변수 셋팅
```cpp
#define ADC_PIN A0

float adc_voltage =0.0;
float in_voltage = 0.0; // actual voltage (측정할 v)

//resistor vlaues in divider (in ohms)
float R1 = 30000.0;
float R2 = 7500.0;

// reference voltage (아두이노의 v)
float ref_voltage = 5.0; 

// analog to digital convertor로 부터받을 값
int adc_value = 0;
```

먼저 analogRead로 읽어 온 값으로 계산을 해준다. loop() 함수에서 계쏙 반복
```cpp
void loop() {

    adc_value = analogRead(ADC_PIN);
    //ADC input으로 들어온 값을 계산
    adc_voltage = (adc_value * ref_voltage) / 1024.0;

    // 계산 (voltage at divider input)
    in_voltage = adc_voltage / (R2/ (R1+R2));
}

```

analogRead()로 읽은 값을 reference voltage 즉, 5.0v로 곱해주고   
아두이노가 10bit ADConverter 이기 때문에 1024.0 나눠준다    

이후 Serial을 이용해서 print를 해준다. 
> setup() 함수에서 Serial을 begin() 함수로 셋팅 먼저

```cpp
Serial.print(in_voltage, 2);  // 소수점을 2자리만 표시해 줄 수 있다
```

어쨋든 이를 이용하면 배터리의 전압을 측정해서 배터리 용량을 알 수가 있다.   



external voltage reference 를 이용하면 더 정확하게 v를 측정할 수가 있다   
adfruit LM4040 


전류+전압 측정은 Ina219 



[유투브 참고 DroneBot Workshop](https://www.youtube.com/watch?v=psNAeHoZv0A)


