# HDMI 모니터 소리 sound 중지 시키기
우분투 settings 에서 sound 탭을 보면  
output을 선택할 수 있는데 아마도 sound가 스피커로 나가는 상황이라면 모르겠지만  
(현재 스피커는 없음) 이어폰으로 출력을 하는데,   

HDMI / DsiplayPort 3 - High Definition Audio Controller  
Headphones - Built-in Audio

가 있는데 여기에서 Headphones를 선택해주면 된다

하지만 그럼에도 불구하고 모니터에서 소리는 계속 난다

모니터마다도 다를 수 있겠지만,  
모니터에서 소리를 끄면 헤드폰으로 소리가 안나게 되고 불륨을 줄이면 헤드폰으로 마찬가지로 소리가 안나게 된다. 🤬

보통 settings 설정에서 HDMI audio 부분을 diable 할 수 있으면 좋겠지만   
우분투 18.04 기준으로는 없는 듯하다.

그래서 프로그램을 설치해준다.

```
$ sudo apt install pavucontrol
```
아마도 우분투 19 이상부터 기본으로 깔려있다고 하는데
정확히는 모르겠음 ㅋ

일단 설치 후에 
실행을 해보자~ 슈퍼키를 누르고 (윈도우키) pav만 입력하면  
PulseAudio Volume Control 실행이 된다

<img src=0>
<br>

이제 Configuration 탭으로 이동해서    
High Definition Audio controller 와 Built-in Audio 가 있는데
아마도 스피커가 있다면 스피커가 나올 듯도 하다

어쨌든 High Definition Audio Controller의 
Profile의 드롭박스를 Off로 선택해준다

<img src=1>
<br>

그러면 모니터로 HDMI 소리가 안 나오게 된다~ 😎



