# DC Voltage

ADC analog digital convertor

Voltage Sensor  전압 센서. 저렴한 가격에 살 수 있다. 전류 센서도 있는 듯 하다  


s ---> 아두이노의 아날로그 A0 연결
- ---> 아두이노의 GND 연결
> + 는 더미 

배터리 등에서 +, - 선을 연결해준다   

analogRead()로 읽은 값을 reference voltage 즉, 5.0v로 나눠주게 된다   
아두이노가 10bit ADConverter 이기 때문에 1024.0 나눠준다    

이런식으로 된다 
```cpp
adc_voltage = (analogRead(ANALOG_IN_PIN) * 5.0) / 1024.0
```


어쨋든 이를 이용하면 배터리의 전압을 측정해서 배터리 용량을 알 수가 있다.   



external voltage reference 를 이용하면 더 정확하게 v를 측정할 수가 있다   
adfruit LM4040 


전류+전압 측정은 Ina219 



[유투브 참고 DroneBot Workshop](https://www.youtube.com/watch?v=psNAeHoZv0A)


