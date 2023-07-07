## usb serial 예제
ROS를 사용하면서 std::vector를 사용해서 serial 패키지를 사용하는 경우  

```cpp
void setup() {
  // put your setup code here, to run once:
  Serial1.begin(19200);
}


void loop() {
  // put your main code here, to run repeatedly:
  static bool led_state;
  static uint32_t t_time = 0;

  if(Serial.available())
  {
    Serial1.print(Serial.read());
  }

  if(Serial1.available())
  {
    Serial.print(Serial1.read());
  }

  if(millis() - t_time > 500)
  {
    t_time = millis();
    digitalWrite(LED_BUILTIN, led_state);
    led_state = !led_state;
  }

}
```

Serial, Serial1을 이용해서 양쪽 데이터를 번갈아 테스트 

## 시리얼 통신시 문자열은 ascii로

프로토콜이 어떻게 정의가 되었는지에 따라 달라질 수도 있겠지만  

```cpp
    std::vector<int> data;
    data.push_back('$'); //&  36
    data.push_back('C');
    data.push_back('S');
    data.push_back(','); //,
    data.push_back('1');
    data.push_back(','); //,
    data.push_back('1');
    data.push_back('0');
    data.push_back(0x0D); // \r
    data.push_back(0x0A); // \n
```

시리얼은 통신으로 보내기 위한 데이터를 만든다고 하면, (vector로 만들었을 경우)   
캐릭터 한자한자 입력을 해주는 방식으로 하게 되고   
또는 맨아래 `0x`형태로 hex 방식으로 직접 넣어줘도 된다.   

> 주의 할점은 그냥 숫자를 넣어주게 되면 이는 아스키코드의 숫자가 되므로 원하는 숫자가 아닐 수 있으므로   
실제 숫자를 만들어야 한다면 실제 숫자에 해당하는 ascii를 확인한다   


