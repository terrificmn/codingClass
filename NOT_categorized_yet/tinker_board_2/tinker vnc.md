# tinker vnc tiger vnc
기존 설치는 같다. 블로그 참고   

단, ubuntu-desktop,  ubuntu-gnome-desktop 은 설치하지 않는다.  
대신  lxde 설치하는데 아마 설치가 되어 있다고 나올 것임. 

> 기본으로 사용하고 있는게  lxde 데스크탑

설치는 비슷하다,

## xtartup 설정
xstartup 파일을 만드는 부분에서 아래처럼 바꾼다.  

`exec /etc/vnc/xstartup` 에서 `exec /usr/bin/startlxde`

아래처럼 카피 후 사용
```
exec /usr/bin/startlxde &
vncconfig -iconic &
dbus-launch --exit-with-session &
```

lxde를 실행할 수 있게 해준다. 기존의 xstartup으로 실행을 하면 클라이언트에서 접속했을 경우 검은 화면만 보이게 된다   


## 클라이언트 viewer 설치
tiger vnc viewer를 rocky linux 용을 찾을 수 없다.  
소스코드를 제공해서 빌드하는 방법은 있는 듯 한데, viewer만 필요해서 따로 하기도 그렇고,,   
뭐 정확히 할 줄은 모른다 ㅋㅋ 

그냥 real vnc viewer를 설치함

[linux버전 선택 rpm 후 다운](https://www.realvnc.com/en/connect/download/viewer/linux/)

```
sudo rpm -ivh 다운로드된_패키지.rpm
```

ssh 터널링으로 만든 다음에 기존 방식처럼 remote 주소에 `localhost:5901'로 접속해주면 된다  

