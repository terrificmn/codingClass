// C++ code
//
//pin번호 set
int LED1 = 4;
int LED2 = 5;
int LED3 = 6;
int LED4 = 7;
int LED5 = 8;

int SWT = 12;
int delayTime = 1000;
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
  int i;
  	

    if (data==0) {
      //Serial.print("button data: ");
      //Serial.println(data);
      	for(i=LED1; i<=LED5; i++) {
          //digitalWrite(i, HIGH);
          //delay(delayTime); 
          //digitalWrite(i, LOW);
          Serial.println(i);
        }

    } else if (data==1){
      	//Serial.print("button data: ");
      	//Serial.println(data);
      	for(i=LED5;i>=LED1;i--) {
          //digitalWrite(i, HIGH);
          //delay(delayTime); 
          //digitalWrite(i, LOW);
          Serial.print(i);
        }
    }
  
}