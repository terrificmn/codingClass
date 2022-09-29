# TWIN_ALARM_ON 으로 설정
md motor 드라이버를 사용할 때에   
한쪽 모터가 스탑되는 경우에 다른 한쪽 모터도 정지될 수 있게 셋팅   

> 이유는 한쪽이 마비되면 제대로 동작을 안하기 때문에 위험할 수 있어서 아예 모터 둘 다 정지해준다

먼저 coms3 드라이버 인식이 되어야하기 때문에  
구글에서 coms-485 usb 드라이버를 다운 & 설치를 한다   

md robot  홈페이지에서 mbas 프로그램을 다운로드 한다. (Windows 전용)

### 프로그램 사용법
1.  command  에서 MER_ATER_ACTION_ON
2. Data Request를 눌러주는데 (PID4)
3. select PID to write 에서 도 TWIN_ALARM_ON을 해준다  
4. send를 눌러준다   
