# Tinker board 2
Tinker board 2 와  2S 는 같은 사양이고, 다른점이라고 하면 S2는 Micro Sd 카드 대신에 
내장된 메모리를 사용한다는 것 이다.   

SD카드가 저렴하기도 하고,  팅커보드 2 가 더 가성비가 좋은 것 같아서 선택했다. 

[팅커보드2에 대한 많은 것을 알려준다. 리눅스 포함, GPIO 등.. cam 많은 자료가 있다. 좋은 자료! https://www.waveshare.com/wiki/Tinker_Board_2](https://www.waveshare.com/wiki/Tinker_Board_2)


## 전원
처음에 팅커 보드를 살펴보는데 전원 부분이 5핀 방식으로 안되어 있어서 조금 당황했다. 

싱글보드컴퓨터는 라즈베리파이3b, 4b를 사용해 봤는데.. 전원이 핸드폰 충전기로 사용해도 되었었다. 
(A는 2. 가 였는데 전원이 충분이 들어왔었다.)

하지만 Tinker Board2는 전원이 노트북 어댑터 같은 놈이 필요하다

12V~19V까지 지원을 하고 케이블 연결 부분이 외경 5.5, 내경 2.5 가 되겠다.   
~~아무리봐도 몇 암페어를 사용하는지 설명서에 없다 ㅠ~~

왜냐하면 웹 검색을 하니 전원 어댑터를 파는 것은 많은데 암페어가 다 각기 다르다. 여기서 또 당황 ㅋㅋ   
12V 4A or 5A 직류전원장치 DC 전원 이라고 부르는 듯 하다

- DC: Direct Current, 직류.. 시간에 따라 흐르는 극성이 변하지 않는 전류 (+, - 가 바뀌지 않는다)
- AC: Alternating Current 교류.. 시간에 따라 크기, 극성(방향)이 주기적으로 변함. (+,-)로 바뀌는 극성이 바뀌는 횟수를 주파수 HZ로 표시(1초에 반복하는 횟수)

V볼트는 12V~19V 를 사용하면 되고, 전원 자체는 A 암페어는 4암페어보다 같거나 큰 놈을 사용하면 된다고 한다.  
왜냐하면 암페어가 부족하면 전원이 꺼질 수 있다고 한다.  
인터넷에서는 오히려 암페어가 낮으면 문제가되지만 높은면 상관이 없다고;; 하는데  

어느 블로그에서 찾은 내용...   
> 어댑터의 출력전압 보다 전자제품의 사용전압이 높으면 작동이 안될 수가 있고,   
어댑터의 출력전압 보다 전자제품의 사용전압 입력이 낮으면 전자제품 망가질 수 있다.  
출력 전류(A)는 전자제품이 요구하는 전류(A) 보다 크거나 같아야 한다.  
어댑터는 전자기기보다 V는 같게, A는 같거나 높게 구매한다.  
(A가 높을 수록 용량이 여유가 있어서 안정적이며, 비싸다)

그리고 마지막 전원 커넥터 부분은 외경과, 내경 사이즈를 살펴보고 사용해야하고   
만약 안 맞는다면 Jack 부분만 바꿔주는 변환 어댑터도 판매를 하는 듯 하다 

> DC 배럴잭 변환 젠더(DC power input jack) 라고 검색하면 외경, 내경 사이즈가 다를 때 사용할 수 있는 것도 있다

>다행히 설명서에는 **45w**까지 지원한다고 Power connection(up to 45w) 나와있는게 있어서 계산을 해보니.. 
3.75 암페어 인 듯 하다. W = V * A   

어느 판매처에서는 15V 3A 짜리로 어댑터를 같이 제공하는 것을 봐서는 45W를 지키는 것 같기도 하므로   
대충 12V에 4A 짜리를 사용하면 되는 듯 하다.  


## 리눅스 설치
아쉽게도 우분투를 공식지원을 하고 있지는 않아서  
공식지원은 데비안 리눅스를 지원하고 있다. 장점으로는 **안드로이드**를 지원한다는 점  

별다른 우분투 설치에 관한 정보가 없어서 일단 데비안으로 설치를 진행했다.  

> ~~방법이 있을 수도 있겠지만 여기에 쏟을 시간이 없다;;;~~   
~~라고 했지만 또 삽질을 했고....;;~~

On Oct21, 2023 기준으로   
Tinker_Board_2-Debian-Bullseye-v3.0.6-20230627   
Tinker_Board_2-Debian-Buster-v2.1.16-20230613   

데비안 10, 데비안 11 까지 지원한다.  
아무래도 안정성은 데비안 10 버스터가 나은듯 하다.(권장)   


### 실패: 일단 기록으로 남긴다  
- ubuntu 20.04 버전은 arm 버전으로 다운로드가 가능한데 아마도 ubuntu server 버전으로 제공을 하는 듯 한데... 결과는 실패.. 부팅이 안된다    

	라즈베리파이 같은 경우에는 desktop버전도 지원하지만 tinker board에서는 안되는 듯 하다  

- Armbian 도 있는데, Ubuntu 또는 debian로 만들어진 리눅스이다. 특히 Linux for ARM development boards 를 위해서 사용되는데...

	Tinker board s 버전 (예전 버전)에는 지원이 되었던 것 같다. sd 카드에 넣고 부팅을 했더니 역시 아무런 반응이 없다. 에러메세지도 안나온다;;;;

결론은 그냥 공식 지원하는 **debian 10 buster**를 설치하고, docker를 설치해서 사용하자!  
[ISO이미지는 여기에서 다운로드 https://tinker-board.asus.com](https://tinker-board.asus.com/download-list.html?product=tinker-board-2)

버전은 Tinker Board 2 Debian 10 V2.0.14, 용량은 압축을 풀련 4.1GB 

마이크로 SD카드를 컴퓨터에 연결하고 balena Etcher 프로그램을 이용해서 구워준다  
리눅스 같은 경우에는 Etcher 프로그램이 좋은 것 같다 

그 전에는 터미널창에서 dd 명령어를 이용해서 했었는데.. (괜히 터미널 이용해 보고 싶어서 ㅋㅋ)

어쨋든 데비안 10 buster이 다 완료가 되면 팅커보드2에 연결을 해서 부팅을 해보자


## 부팅
마이크로SD 카드를 넣고 12v 5a 전원을 넣었더니 데비안 10 으로 부팅이 금방 된다.   
슈퍼키, (윈도우키)가 작동을 안한다. 그 부분은 조금 불편하지만 마우스로 하면 되지 뭐..

~~추후 ROS 설치가 원할하지 않는다면 도커로 진행을 해봐야겠다.~~   
docker debian engine을 설치하면 실행이 된다. 설치시에 마지막에 에러가 발생하기는 했지만.. 
docker 시작 및 버전 확인에서는 에러가 없었음


## 메뉴얼

[tinker board2 메뉴얼 보기-(GPIO)](https://tinker-board.asus.com/doc_tb2.html#user)


## 기타

####  패스워드 변경은 터미널에서 
```
passwd
```

그리고 현재 비번은 linaro 를 입력한 후 새로운 비번을 입력하는데, 
다른 리눅스 배포판과 달리(?) 비번은 단순하고 짧게 하면 변경이 안된다;;;


#### vscode 설치
vscode를 설치하려면 공식 홈피에서 arm64버전 deb으로 다운받는다.  
download에서 other downloads 를 누른후에 .deb arm64 버전으로 다운 받는다 

[vscode 다운로드](code.visualstudio.com/Download)

> 보통 .deb 버전이나, 64 bit 버전을 받으면 호환이 안된다

다운 후에 설치는 
```
sudo dpkg -i code_1.73.1-1667966450_arm64.deb
```
처음 열리는데 시간이 좀 걸리지만, 천천히 사용할려고 하면 사용가능할 듯 하다



##  configuration

```
sudo tinker-config
```
위 커맨드를 이용하면 Hostname, Password, Boot Options, Advanced Options 등.. 설정을 할 수 있다

tinker board 2 initial settings 으로 로그인 할 수 있게하거나 자동 로그인 하거나 골라준다  
기본은 자동 로그인으로 되어 있다  

`sudo tinker-config`  

3. Boot Options -> B1 Desktop / CLI -> B3 Desktop or B4 Desktop Autologin (login with 'linaro' automatically)


Internationalisation Options -> I2 Change Timezone  
에서 시간대 변경 가능  

> 중요한 이유가 GUI 에서 메뉴에서 Preferences에서 메뉴가 Time and Date 있는데   
락이 풀리지 않아서 설정이 불가능 (root로 해봤지만 안됨)  
다른 cli 에서 설정하는 것이 아니라면 위의 tinker-config로 쉽게 설정 변경 가능함


## wifi 설정

dev만 입력해보면
```
nmcli dev
```
 
 아래와 같은 결과가 나온다 (데스크탑 결과라 싱글보드컴퓨터와는 다르다)
```
DEVICE      TYPE      STATE                   CONNECTION 
enp3        ethernet  connected                 enp3     
virbr0      bridge    connected (externally)  virbr0     
lo          loopback  unmanaged               --         
virbr0-nic  tun       unmanaged               --      
```


(r을 넣어서 하는 것은 해봐야할 듯.. 잘 모르겠음)
```
nmcli r wifi
nmcli dev wifi
```


이제  ap (access point)가 나오는데 이거에 맞춰서 이름 및 비밀번호를 넣어주면 된다 

```
nmcli dev wifi connect 와이파이AP이름 password "패스워드"
```

물론 윈도우의 gui를 이용해서 오른쪽 아래의 화면에서 쉽게 할 수 있다 ㅋㅋ

