// C++ code
//
//pin번호 set
int LED1 = 5;
int SWT = 12;
int delayTime = 100;
int data;

void setup()
{
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);
  pinMode(LED5, OUTPUT);
  
  pinMode(SWT, INPUT);
  // 시리얼 통신 시작
  Serial.begin(9600); //통신속도를 bps로 적어준다 (bit per second)

}

void loop() // 함수자체가 loop 리턴은 값은 없음 void
{
	data = digitalRead(SWT); // INPUT으로 읽어올 때에는 핀번호만 넘겨주면 된다
  	Serial.print("button data: ");
  	Serial.println(data);
}


