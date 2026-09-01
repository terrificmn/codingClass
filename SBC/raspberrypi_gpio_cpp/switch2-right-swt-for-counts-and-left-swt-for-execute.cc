//////// falling edge와 rising edge만으로 간결하게 가능
/////// 오른쪽 스위치는 카운트를 하고 왼쪽 스위치는 그 카운트 만큼 led를 켜는 코드

// if (pre_data1 - data1 == 1) { //swt1 은 pull-up 저항이므로 떨어지는 순간을 falling edge를 검출하는 부분
//     cnt++;
//     led_pcs = cnt;   
    
//     if (cnt >=5) {
//       cnt = 5; //5로 고정
//     }
//   }

//   if (pre_data2 - data2 == -1) { //swt2 은 pull-down 저항이므로 rising edge를 검출하는 부분
//     for (int i=LED1; i<LED1+count; i++) {
//       digitalWrite(i, HIGH);
//     }

//     for (int i=LED5; i>=LED1+count; i--) {
//       digitalWrite(i, LOW);
//     }

//     count = 0; //초기화
//   } 

//// 아래 코드 같은 기능
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
  // 시리얼 통신 시작
  Serial.begin(9600); //통신속도를 bps로 적어준다 (bit per second)
}


// 12번 핀은 누른만큼 led의 갯수를 켤 수 있어야 한다
// 13번 핀은 확정된 (13번핀은 누른다음에는 초기화됨)

void loop() // 함수자체가 loop 리턴은 값은 없음 void
{
  
  	pre_data1= data1;
  	data1 = digitalRead(SWT1);
  
  	pre_data2= data2;	
  	data2 = digitalRead(SWT2);
  
  	
  	if (pre_data1 - data1 == 1) { //swt1 은 pull-up 저항이므로 떨어지는 순간을 falling edge를 검출하는 부분
      	value = 3;
  	}
  
  	if (pre_data2 - data2 == -1) { //swt2 은 pull-down 저항이므로 rising edge를 검출하는 부분
		//Serial.println(data2);  	
      	value = 5;
  	}
  	
  	// SWT1 눌렸을 때
  	if (value == 3) {
      if (count >= 5) { // 카운트가 뒤에서 ++ 되는 것에 주의~ 
        //즉, 5번 누른상태일 때 이미 count는 5이고 6번째 눌러야 현재 if문에 도달
      	count = 1;  //5 이상이면 초기화
        value = 0; //다시 반복 안하도록 value도 초기화
        
      } else {
      		count++;
        	value = 0; //다시 반복 안하도록 value도 초기화
    	}
      
    } 
  	
  	// SWT2 눌렸을 때
  	if (value == 5) {
      	// count가 있을 때 실행
      	if (count != 0) {
      		for(int i=LED1; i<=LED1+count-1 ; i++) { 
    			digitalWrite(i, HIGH); //카운트 만큼만 켬
      		}
          count = 0; //다시 초기화: count 0이면 불 켜는 거 실행 안함
          value = 0; //다시 반복 안하도록 value도 초기화
          
        } else { //아니면 불 끄기: 즉 count가 0일 때

          	for(int i=LED1; i<=LED1+5 ; i++) { //하드코딩: 5개
				digitalWrite(i, LOW);  //다 끔
      		}
          
          	value = 0; //다시 반복 안하도록 value도 초기화
        }
    }
  
  	// 확인용
  	Serial.println(count);
  	
}
