// 초음파 센서를 이용해서 램프 순서대로 켜지게 하기
// C++ code
//
//pin번호 set
int LED1 = 4;
int LED2 = 5;
int LED3 = 6;
int LED4 = 7;
int LED5 = 8;

int SWT1 = 12;
int SWT2 = 13;
int delayTime = 500;
int data1=1; //초기값을 1로 셋팅 (pull up)
int data2=0; //초기값을 0로 셋팅 (pull down)

int trig = 11; //sonar의 trigger i/o 설정 ouput이 됨
int echo = 10; //sonar의 echo i/o 설정 input이 됨

int count =0;
int pre_data1, pre_data2;
int value;

void setup()
{
    pinMode(LED1, OUTPUT);
    pinMode(LED2, OUTPUT);
    pinMode(LED3, OUTPUT);
    pinMode(LED4, OUTPUT);
    pinMode(LED5, OUTPUT);
    
    pinMode(SWT1, INPUT);
    pinMode(SWT2, INPUT);
    
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);

    // 시리얼 통신 시작
    Serial.begin(9600); //통신속도를 bps로 적어준다 (bit per second)
}


// 12번 핀은 누른만큼 led의 갯수를 켤 수 있어야 한다
// 13번 핀은 확정된 (13번핀은 누른다음에는 초기화됨)

void loop() // 함수자체가 loop 리턴은 값은 없음 void
{
    long duration, distance;

    pre_data1= data1;
    data1 = digitalRead(SWT1);

    pre_data2= data2;	
    data2 = digitalRead(SWT2);

    // 초음파 센서 셋팅
    digitalWrite(trig, LOW); // 0으로 초기화 시킴 
    delayMicroseconds(2);  // 2 마이크로세컨드로 설정
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);  // 매뉴얼대로 10 마이크로세컨드로 설정
    digitalWrite(trig, LOW);

    duration = pulseIn(echo, HIGH); //여기의 HIGH 활성화 시킴- 시간이 저장됨
    distance = duration * 17/1000;

    Serial.print("distance is ");
    Serial.println(distance);

    //초음파 거리에 따른 램프 점멸하게 하기 (거리 만큼 램프 점멸하게 함)
    delayTime = 200;

    for(int i=0; i<=4; i++) {

        if (distance >=4 && distance <= 66) {
            count = 1;
        } else if (distance >=67 && distance <=133) {
            count = 2;
        } else if (distance >=133 && distance <= 199) {
            count = 3;
        } else if (distance >=200 && distance <= 256) {
            count = 4;
        } else if (distance >=257 && distance <= 331) {
            count = 5;
    }

    for (int i=LED1; i<LED1+count; i++) {
        digitalWrite(i, HIGH);
    }

    delay(delayTime * count); //램프 카운트 만큼 켠 뒤에 딜레이 시키기 (딜레이 초기값에서 카운트값을 곱해줌)

    for (int i=LED5; i>=LED1; i--) {
        digitalWrite(i, LOW);
    }
    
    delay(delayTime * count); //마찬가지로 램프가 꺼진 뒤에서 딜레이 시키기

    Serial.println(distance);

}
