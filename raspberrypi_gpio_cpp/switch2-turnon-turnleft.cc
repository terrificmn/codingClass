// C++ code
// 스위치 2개를 연결하고 한쪽 스위치를 누르면 LDE가 켜지고 한쪽 스위치를 누르면 
// LDE가 꺼지게 코딩
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

int count;
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
    // 시리얼 통신 시작
    Serial.begin(9600); //통신속도를 bps로 적어준다 (bit per second)
}

void loop() // 함수자체가 loop 리턴은 값은 없음 void
{

    // 풀 업 저항이므로 data1값을 처음에 정의를 1로 함 --> 처음값에서 스위치값을 빼면 1이 되기위한 구조
    pre_data1= data1;
    data1 = digitalRead(SWT1); // data1에 SWT1로 들어온 값을 저장

    // 풀 다운 저항이므로 data2값을 처음에 정의를 0로 함 --> 처음값에서 스위치값을 빼면 -1이 되게 만들기 위한 구조
    pre_data2= data2;	
    data2 = digitalRead(SWT2);

    
    if (pre_data1 - data1 == 1) { //swt1 은 pull-up 저항이므로 떨어지는 순간을 falling edge를 검출하는 부분
        count++; //count
        value = 3;
    }

    if (pre_data2 - data2 == -1) { //swt2 은 pull-down 저항이므로 rising edge를 검출하는 부분
        //Serial.println(data2);  	
        count++; //count
        value = 5;
    }

    if (value ==3) {
        digitalWrite(LED1, HIGH);
        digitalWrite(LED2, HIGH);
        digitalWrite(LED3, HIGH);
        digitalWrite(LED4, HIGH);
        digitalWrite(LED5, HIGH);

    } else if (value ==5) {
        digitalWrite(LED1, LOW);
        digitalWrite(LED2, LOW);
        digitalWrite(LED3, LOW);
        digitalWrite(LED4, LOW);
        digitalWrite(LED5, LOW);
    }


    // if (count % 2 ==0) {
//       	digitalWrite(LED1, HIGH);
//       	digitalWrite(LED2, HIGH);
//       	digitalWrite(LED3, HIGH);
//       	digitalWrite(LED4, HIGH);
//       	digitalWrite(LED5, HIGH);
        
//     } else {
    
//       	digitalWrite(LED1, LOW);
//       	digitalWrite(LED2, LOW);
//       	digitalWrite(LED3, LOW);
//       	digitalWrite(LED4, LOW);
//       	digitalWrite(LED5, LOW);
//     }
    Serial.println(value);
    
}