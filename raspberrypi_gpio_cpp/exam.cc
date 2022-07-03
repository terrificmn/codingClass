// C++ code

// LED
int LED_GREEN = 3;
int LED_BLUE1 = 4;
int LED_BLUE2 = 5;

int LED_RED1 = 8;
int LED_RED2 = 9;
int LED_RED3 = 10;

// 초음파 
int trig = 11;
int echo = 12;

// 스위치 
int SWT_POWER = 6; 
int SWT_MODE = 7;

// 변수 
int swtDataPower = 0;
int preDataPower;
int onCount = 0;
int swtDataMode = 0;
int preDataMode;
int modeCount = 0;
int dist;

void setup()
{
    pinMode(LED_GREEN, OUTPUT);
    pinMode(LED_BLUE1, OUTPUT);
    pinMode(LED_BLUE2, OUTPUT);
    pinMode(LED_RED1, OUTPUT);
    pinMode(LED_RED2, OUTPUT);
    pinMode(LED_RED3, OUTPUT);
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
    pinMode(SWT_POWER, INPUT);
    pinMode(SWT_MODE, INPUT);
    
    // 시리얼 통신 시작
    Serial.begin(9600);

}

// 초음파 거리별 5단계별 LED on off 함수
int modeDistance5(int delayTime) {

    long duration, distance;
    int distCount;

    // 초음파 센서 셋팅
    digitalWrite(trig, LOW); // 0으로 초기화 시킴 
    delayMicroseconds(2);  // 2 마이크로세컨드로 설정
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);  // 매뉴얼대로 10 마이크로세컨드로 설정
    digitalWrite(trig, LOW);

    duration = pulseIn(echo, HIGH); //여기의 HIGH 활성화 시킴- 시간이 저장됨
    distance = duration * 17/1000;

    for(int i=0; i<=4; i++) {
        if (distance >=4 && distance <= 66) {
            distCount = 1;
        } else if (distance >=67 && distance <=133) {
            distCount = 2;
        } else if (distance >=133 && distance <= 199) {
            distCount = 3;
        } else if (distance >=200 && distance <= 256) {
            distCount = 4;
        } else if (distance >=257 && distance <= 331) {
            distCount = 5;
        }
    }

    
    if (distCount == 1) { 
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, LOW);
        }

    } else if (distCount == 2) {
        digitalWrite(LED_RED1, HIGH);
        delay(delayTime);
        digitalWrite(LED_RED1, LOW);
        delay(delayTime);

    } else if (distCount == 3) {
        // 처음에 초기화 해주기 다 끔 // 꺼야지 빨리 반응 (딜레이 미포함)
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, LOW);
        }

        for (int i=LED_RED1; i<=LED_RED2; i++) {
            digitalWrite(i, HIGH);
            delay(delayTime);
            digitalWrite(i, LOW);
            delay(delayTime);
        }
        
    } else if (distCount == 4) {
        //처음에 초기화 해주기 다 끔; 꺼야지 빨리 반응 (딜레이 미포함)
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, LOW);
        }

        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, HIGH);
            delay(delayTime);
            digitalWrite(i, LOW);
            delay(delayTime);
        }

    } else if (distCount == 5) {  
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, HIGH);
        }
    }

    return distance;
}


// 초음파 거리별 3단계별 LED on off 함수
int modeDistance3() {

    long duration, distance;
    int distCount=0; //초기값

    // 초음파 센서 셋팅
    digitalWrite(trig, LOW); // 0으로 초기화 시킴 
    delayMicroseconds(2);  // 2 마이크로세컨드로 설정
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);  // 매뉴얼대로 10 마이크로세컨드로 설정
    digitalWrite(trig, LOW);

    duration = pulseIn(echo, HIGH); //여기의 HIGH 활성화 시킴- 시간이 저장됨
    distance = duration * 17/1000;

    for(int i=0; i<=4; i++) {
        if (distance >=4 && distance <= 113) {
            distCount = 1;
        } else if (distance >=114 && distance <=222) {
            distCount = 2;
        } else if (distance >=223 && distance <= 331) {
            distCount = 3;
        } 
    }

    if (distCount == 1) { 
        digitalWrite(LED_RED1, HIGH);
        digitalWrite(LED_RED2, LOW);
        digitalWrite(LED_RED3, LOW);

    } else if (distCount == 2) {
        digitalWrite(LED_RED1, HIGH);
        digitalWrite(LED_RED2, HIGH);
        digitalWrite(LED_RED3, LOW);
        
    } else if (distCount == 3) {
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, HIGH);
        }

    } else { // 아니면 다 끔 (초기값 0일때)
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, LOW);
        }
    }

    return distance;

}



void loop()
{
    int delayTime;
    // 메뉴 전원 스위치 버튼 데이터 저장 // 1이면 5V
    preDataPower = swtDataPower;
    swtDataPower = digitalRead(SWT_POWER);

    // 메뉴 스위치 버튼 데이터 저장
    preDataMode = swtDataMode;
    swtDataMode = digitalRead(SWT_MODE);

    if (preDataPower - swtDataPower == -1) {  // 전원 켜짐
        onCount++;
    }

    if (preDataMode - swtDataMode == -1) { //모드 변경
        modeCount++;
    }

    // 전원 버튼 입력 부분 
    if (onCount % 2 != 0) { //홀수는 전원 on  
        digitalWrite(LED_GREEN, HIGH);

        // 모드 버튼 입력 부분
        if (modeCount == 0) { //초기값일 때는 불 끔
            digitalWrite(LED_BLUE1, LOW);
            digitalWrite(LED_BLUE2, LOW);

        } else if (modeCount % 2 != 0) {  //홀수는 첫번째 모드 on
            digitalWrite(LED_BLUE2, LOW);
            digitalWrite(LED_BLUE1, HIGH);
            // 호출- 거리별 초음파 5단계
            Serial.print("distance: ");
            dist = modeDistance5(delayTime=200); 
            Serial.println(dist);

        } else {
            digitalWrite(LED_BLUE1, LOW);
            digitalWrite(LED_BLUE2, HIGH);
            //호출- 거리별 초음파 3단계
            dist = modeDistance3(); 
            Serial.print("distance: ");
            Serial.println(dist);
        }

    // 전원 OFF // 짝수 일 때 전원 off
    } else { 
        digitalWrite(LED_GREEN, LOW);
        
        // 혹시 남아 있을 LED 끄기
        for (int i=LED_RED1; i<=LED_RED3; i++) {
            digitalWrite(i, LOW);
        }
        digitalWrite(LED_BLUE1, LOW);
        digitalWrite(LED_BLUE2, LOW);
    }


}