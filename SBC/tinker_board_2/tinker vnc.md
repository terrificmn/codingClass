# tinker vnc tiger vnc
기존 설치는 같다. 블로그 참고   
OS 버전은   
- Tinker Board 2 Debian 10 (Kernel 4.19) v2.1.16   
(Debian-Buster-v2.1.16)

단, ubuntu-desktop,  ubuntu-gnome-desktop 은 설치하지 않는다.  
대신  lxde 설치하는데 아마 설치가 되어 있다고 나올 것임. 

> 기본으로 사용하고 있는게 lxde 데스크탑

설치는 비슷하다,

## xstartup 설정
xstartup 파일을 만드는 부분에서 아래처럼 바꾼다.  

`exec /etc/vnc/xstartup` 에서 **`exec /usr/bin/startlxde`**

아래처럼 카피 후 사용
```
exec /usr/bin/startlxde &
vncconfig -iconic &
dbus-launch --exit-with-session &
```

lxde를 실행할 수 있게 해준다. 기존의 xstartup으로 실행을 하면 클라이언트에서 접속했을 경우 검은 화면만 보이게 된다   

또는 아래의 명령으로도 서버를 시작할 수 있다.  

```
vncserver -xstartup /usr/bin/startlxde :1 -localhost -geometry 1024x768 -depth 24
```


## 클라이언트 viewer 설치
Rocky linux 에서 tiger vnc viewer를 설치를 못 찾았다.  
소스코드를 제공해서 빌드하는 방법은 있는 듯 한데, viewer만 필요해서 따로 하기도 그렇고,,   
뭐 정확히 할 줄은 모른다 ㅋㅋ 

그냥 real vnc viewer를 설치함

[linux버전 선택 rpm 후 다운](https://www.realvnc.com/en/connect/download/viewer/linux/)

```
sudo rpm -ivh 다운로드된_패키지.rpm
```
ssh 터널링으로 만든 다음에 기존 방식처럼 remote 주소에 `localhost:5901'로 접속해주면 된다  


## 데비안 버전 별 데스크탑 환경이 다름 (업데이트)
이번에 리눅스 OS를 버전업을 해보았다. Tinker Board2 Debian 11 버전  

- Tinker Board 2 Debian 11 (Kernel 5.10) v3.0.6   
(Debian-Bullseye-v3.0.6)

이 경우에는 vnc viewer로 실행을 하면 검은화면만 나온다.  
이유는 데비안11 Bullseye 경우에는 lxde가 아닌 xfce4 를 사용  
```
vncserver -xstartup /usr/bin/startxfce4 :1 -localhost -geometry 1024x768 -depth 24
```
위의 xstartup 파일에서 `exec /usr/bin/startxfce4 &` 로 하면 될 지도 모르겠으나  
테스트를 안 해봄   

어쨋든 위의 커맨드로 vnc 서버를 시작하게되면 viewer에서 접속했을 때 화면이 잘 나오게 된다. 

> 아무래도 최신 버전이라 그런지 바탕화면이 더 세련되게 변햇지만,  
치명적으로 docker가 안되는 문제가 있다!! (그래서 다시 Debian 10 Buster로 돌아옴 ㅠㅠ)  



