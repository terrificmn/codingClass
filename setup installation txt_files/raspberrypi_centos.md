# 라즈베리파이 Imager 설치하기 - CentOS 8
CentOS에서 라즈베리파이 이미저를 설치하려면 snaps를 이용해서 설치를 해줘야한다.
snapd로 (패키지매니저 비슷하다) rpi-imager를 설치할 수가 있다.
(리눅스 distributions에서 한번의 빌드로 의존성을 해결해주는 프로그램)
공식 매뉴얼에 따른 것이지만... 역시나 울 집에서는 안된다. ㅠㅠ

어쨋든;; 하는 방법이다..
먼저 snapd를 설치하는데, CentOS 7.6 이상부터는 추가 패키지를 설치할 수 있는 저장소를 등록해줘야한다.
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

해당 경로에 파일이 있는데,,, 안되는 걸로 봐서는 어딘가에서 못찾고 있는 거 같은데;;;

몇번 하다가;; 방향을 매뉴얼 설치 dd 로 하기로 결정!

ㅜㅜ

