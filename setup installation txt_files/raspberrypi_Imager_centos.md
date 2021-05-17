# 라즈베리파이 Imager 설치하기 - CentOS 8
CentOS에서 라즈베리파이 이미저를 설치하려면 snaps를 이용해서 설치를 해줘야한다.  

https://www.raspberrypi.org/software/

각 os에 맞춰서 선택하면 될 듯..  
보니깐 윈도우10 이든,, 맥 버전별로 잘 되는 사람도 있겠지만..
주변을 보니깐.. 안되는 경우가 더 많은 거 같다...;;

다른 프로그램:  에쳐   
https://www.balena.io/etcher/

<br>

다시 본론으로 돌아와서 ..  

snapd로 (패키지매니저 비슷하다) rpi-imager를 설치할 수가 있다.  
(리눅스 distributions에서 한번의 빌드로 의존성을 해결해주는 프로그램)  

공식 매뉴얼에 따른 것이지만... 역시나 울 집에서는 안된다.   

잠깐 하소연을 하자면... 누가 윈도우즈가 별로고 리눅스가 최고라고 했어?!  
물론 리눅스를 사랑? 하지만 ㅋㅋ 한번에 되는게 많이 없다 ㅠㅠ 개발하다 보면 이게 현실~
그래도 어찌어찌 고쳐나가면서 사용하는 재미~ 아 너무~~~~ 좋다 ㅋㅋ ㅠ

<br>

먼저 snapd를 설치하는데,   
CentOS 7.6 이상부터는 추가 패키지를 설치할 수 있는 저장소를 등록해줘야한다.  
EPEL이란? Extra Packages for Enterprise Linux repository 이다~

```
sudo yum install epel-release
```

이제 yum으로 snap을 설치할 수 있다
```
sudo yum install snapd
```

snapd Enable 시키기
```
sudo systemctl enable --now snapd.socket
```

/snap을 심볼릭링크로 만들어 준다
```
sudo ln -s /var/lib/snapd/snap /snap
```

Raspberry Pi Imager 를 설치한다
```
sudo snap install rpi-imager
```
간단하쥬?

이제 설치가 완료 되었으면 아래 명령어로 실행. 프로그램이 뜨면 sd카드에 구워?주면 된다
```
rpi-imager 
```

하지만.. opengl 관련해서 에러가 발생;; 프로그램을 실행시키면 하얀색 화면만 나온다..

```
Qt: Session management error: None of the authentication protocols specified are supported
/usr/share/libdrm/amdgpu.ids: No such file or directory
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: radeonsi
/usr/share/libdrm/amdgpu.ids: No such file or directory
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: radeonsi
libGL error: No matching fbConfigs or visuals found
libGL error: failed to load driver: swrast
```

해당 경로에 파일이 있는데,,, 안되는 걸로 봐서는 어딘가에서 못찾고거나.. 암튼 뭐가 꼬인듯 하다..;

아마도.. 특별한 경우 아니면(나 같은 경우 아니면..) 잘 될꺼 같지만..   
다음에 참고하는 걸로...  

몇번 고치려고 시도 하다가 실패;; 시간도 많이 없고..ㅋㅋ 


방향을 매뉴얼 설치 dd 명령어로 하기로 결정!





