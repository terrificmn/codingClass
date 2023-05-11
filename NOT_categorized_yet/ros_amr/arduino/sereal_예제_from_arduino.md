## usb serial 예제

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

Serial, Serail1을 이용해서 양쪽 데이터를 번갈아 테스트 