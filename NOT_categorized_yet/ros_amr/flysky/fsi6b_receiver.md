# F-si6b
FLY SKY 의 무선 transmiter 및 receiver 사용

## Fail Safe 
receiver에서는 무선 신호가 끊기면, 무선 조종기가 전원이 꺼졌거나 수신이 안 되는 경우에   
리시버에서는 그 이전 pulse 값을 계속 보내온다.   
만약 1500 정도의 수치를 받아오다가 수신이 안되면 그 전의 데이터가 계속 받아지는데  
정확히 예전 데이터 값이 아닐 수도 있지만, (조금씩 펄스값이 바뀜)   
어쨋든 수신 쪽에서는 언제 더 이상 수신이 안되는지 알 수가 없다.   

응답이 없어서 pulseIn()함수에서 0을 리턴해주면 좋겠지만 그렇지는 않다.   

이때 사용할 수 있는게 Fail Safe 기능이다. 무선 조종기에서 선택 후 설정할 수가 있는데   
설정을 하면 초기 설정한 값을 기본값으로 가지고 있고, 수신이 더 이상 안되는 상황에서   
기본값을 넘겨주게 된다   

무선 조종을 하다가 갑자기 수신이 안되는 경우에 조종이 안되는걸 막기 위한 것인데   
예를 들어서 무선 자동차가 더 이상 조종 불가인데 계속 가면 안되고, 드론인데 계속 날라가거나 추락하면 안되니  
어떤 기본값을 설정을 해서 멈추거나 호버 기능을 할 수 있게 하는 것이라고 한다

> 처음에는 어차피 근거리에서 조종을 하는데 갑자기 무선이 끊길 이유는 없다고 생각을 했는데  
좀 더 생각을 해보니, 무선 조종기가 꺼져있을 경우에도 해당하는 것이였다.  

서론이 길었지만..  
1. FS-i6 같은 경우에는 무선 조종기의 OK 버튼을 2~3초 누르면 메뉴가 나오는데    
2. System 셋팅 메뉴에서 ok 누른 후 UP DOWN 버튼을 눌러서 RX 셋팅을 눌러준다   
Failsafe 메뉴를 on을 시켜준다   
2. 사용하고나 하는 채널을 선택을 한 후에 해당 채널에 해당하는 조이스틱을 움직여서 원하는 값을 설정   
(바가 움직인다. 채널1, 2 같은 경우에는 중간 값으로 설정했다)   
3. 저장은 cancel 버튼을 잠깐 누르고 있으면 약 1초?2초 후에 저장되면서 나가진다   
4. 다른 채널도 on 을 시켜주고 같은 작업을 해주면 된다   
5. 최종 전체 save는 다시 failsafe 메뉴에서 cancel키를 또 press and hold 를 해준다   


## binding 하기
처음에 receiver와 transmiter를 연결할 경우에는   
1. fs-i6b 의 수신기 단말에 오른쪽에 신호 단자(top)와 ground 단자 (bottom) 를 연결 해주면 된다  
(보통 점프선으로 맨아래와 맨위를 연결해주면 된다(female용으로만) 중간의 +는 연결하지 않는다)    
2. receiver에 전원을 연결해준다. GND, 5v 를 연결해준다  (하단이 GND, 중간이 +)   
(맨 왼쪽 채널쪽에 연결해주면 된다)   
3. 무선 조종기(transmiter)의 왼쪽 하단의 동그란 binding 버튼을 눌러준다   
4. binding 버튼을 누르고 있는 상태에서 조종기의 전원을 켜주면 거의 바로 binding이 완료가 된다   

> +가 중간에 있는 이유는 신호선과 GND를 잘 못 거꾸로 껴도 +는 중간에 있어서 합선을 방지해 준다고 한다   



