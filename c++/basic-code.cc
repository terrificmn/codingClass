// C++ code
//
//pin번호 set
int LED1 = 5;
int LED2 = 6;
int LED3 = 7;
int LED4 = 8;
int LED5 = 9;
int delayTime = 100;

void setup()
{
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  
}

void loop() // 함수자체가 loop 리턴은 값은 없음 void
{
  digitalWrite(LED1, HIGH);  // 디지털 신호에 첫번째 파라미터에 적어준다. HIGH 는 대개 5v를 의미
  delay(delayTime); // Wait for 1000 millisecond(s) == 1초
  digitalWrite(LED1, LOW);
  delay(delayTime); // Wait for 1000 millisecond(s)
  
  digitalWrite(LED2, HIGH);  // 디지털 신호에 첫번째 파라미터에 적어준다. HIGH 는 대개 5v를 의미
  delay(delayTime); // Wait for 1000 millisecond(s) == 1초
  digitalWrite(LED2, LOW);
  delay(delayTime); // Wait for 1000 millisecond(s)
  
  digitalWrite(LED3, HIGH);  // 디지털 신호에 첫번째 파라미터에 적어준다. HIGH 는 대개 5v를 의미
  delay(delayTime); // Wait for 1000 millisecond(s) == 1초
  digitalWrite(LED3, LOW);
  delay(delayTime); // Wait for 1000 millisecond(s)
  
  digitalWrite(LED4, HIGH);  // 디지털 신호에 첫번째 파라미터에 적어준다. HIGH 는 대개 5v를 의미
  delay(delayTime); // Wait for 1000 millisecond(s) == 1초
  digitalWrite(LED4, LOW);
  delay(delayTime); // Wait for 1000 millisecond(s)
  
  digitalWrite(LED5, HIGH);  // 디지털 신호에 첫번째 파라미터에 적어준다. HIGH 는 대개 5v를 의미
  delay(delayTime); // Wait for 1000 millisecond(s) == 1초
  digitalWrite(LED5, LOW);
  delay(delayTime); // Wait for 1000 millisecond(s)
}
