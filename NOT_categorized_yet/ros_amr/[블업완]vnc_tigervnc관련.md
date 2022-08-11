# VNC TIGER 설치 및 사용법  
https://www.tecmint.com/install-and-configure-vnc-server-on-ubuntu/

## 윈도우에서는
시작하기 전에 이 포스팅은 우분투 환경에서 설치 방법이라서   
Windows일 경우에는 바이너리 파일들을 제공하는데 아래 링크에서   
[stable버전 1.12.0버전-tigervnc 받기](https://sourceforge.net/projects/tigervnc/files/stable/1.12.0/)   
vncviewer64-1.12.0.exe 을 받으면 될 듯 하다. 클라이언트 뷰어 (실제로 테스트는 못해봄 ㅠ)  

<br/>

## 우분투 설치 desktop 설치 먼저
이제 우분투 환경에서 설치 법
먼저 vnc는 데스크탑 쉐어링 시스템이기 때문에 desktop 환경을 사용할 수 있게 desktop관련 설치를 먼저 해줘야 한다  

서버쪽에 ubuntu-desktop 과 ubunutu gnome을 설치를 하는데 (ubuntu gnome이 주로 사용된다)   
그리고 다른 종류의 데스크탑 관련해서는 선택해서 설치할 수 있다  

<br/>

## 서버 쪽 설치
만약 서버쪽 PC에서 접근해서 직접 사용이 가능하면 직접 서버 컴퓨터가 되는 곳에서 작업을 하고   

그냥 client쪽에서 진행을 하려면은 ssh로 접속을 한다 

터미널을 열어서 ssh {서버id}@{ip주소} 형태로 입력해 준다. 예:  
```
ssh ubuntu@192.168.1.100
```

이후 데스크탑 관련 설치  
```
$ sudo apt-get install ubuntu-desktop	
$ sudo apt install ubuntu-gnome-desktop	 
```
> ubuntu-desktop 은 우분투에서 기본으로 되어 있는 데스크탑  
ubuntu-gnome-desktop 은  공식 지원하는 환경  

옵션으로 추가로 설치 가능
```
sudo apt-get install xfce4		
sudo apt-get install lxde			
sudo apt-get install kubuntu-desktop		
```
순서대로 XFCE, LXDE, KDE라고 하는데 원하는 데스크탑 환경이 있다면 설치  
일단은 설치 안하고 넘어감

그리고 tigervnc 관련 패키지 설치하기 
```
sudo apt install tigervnc-standalone-server tigervnc-common tigervnc-xorg-extension tigervnc-viewer
```

<br/>

## vnc 실행
설치가 되었다면 vncserver 명령어로 실행 가능   
```
vncserver
```
를 하게 되면 비밀번호를 설정하라고 한다. 클라이언트에서 접속할 때 사용되는 비밀번호이다     
비밀번호를 설정하고 a view-only password에는 n를 선택  

그러면 ~/.vnc 디렉토리가 만들어진다  

이제 xstartup 파일을 만들어야 한다. 원하는 에디터로 열어준다(vi, gedit, code 등)   
``` 
vi ~/.vnc/xstartup   
```
그리고 아래 내용을 복사 한다 
```
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec /etc/vnc/xstartup &
vncconfig -iconic &
dbus-launch --exit-with-session gnome-session &
```
vnc 서버가 시작될 때 자동으로 실행되는 파일이고    
설치한 DE에 따라 명령어는 달라질 수 있다.   
마지막 줄의 gnome-session 은 gnome-desktop 임    

권한 조정해준다. 실행 가능하게 하고, 다른 유저와 그룹 권한은 빼 버린다  
```
sudo chmod 700 ~/.vnc/xstartup 
```

이제 실행할 때 -localhost 옵션을 넣어서 localhost만 사용되게 해준다   
그리고 -geometry 를 이용해서 해상도를 선택, -depth로 8, 24, 32 중에 선택  

:1의 부분은 포트번호 지정인데 tigervnc 기본이 5901 이므로  
:1로 하게 되면 포트 5901으로 하겠다는 의미이다(기본값)

```
vncserver :1 -localhost -geometry 1024x768 -depth 24
```

아래와 같은 메세지가 나온다면 성공
```
Use xtigervncviewer -SecurityTypes VncAuth -passwd /home/remove_user/.vnc/passwd :1 to connect to the VNC server. 
```
 
<br/>

## 추가 사용법
netstat으로 포트번호로 listen 중인지 확인하기
```
netstat -tlnp 
```
또 vnc 서버 리스트 보기, 실행시킨 서버 목록이 나온다     
```
vncserver -list
```

켜져있는 서버를 끌려면 숫자를 지정해준다 
```
vncserver -kill :1
```

또는 다 끄기  
```
vncserver -kill :*
```

<br/>

## 클라이언트 접속하기
vnc는 보안은 설정이 안 되어 있기 때문에  
원래 암호화가 되어 있지않고 누구든 볼 수 있다고 한다   

그래서 ssh tunnel을 만들어서 client와 server간 통로를 ssh를 통해서 만들어 준다 

만약 문제 ssh로 접속을 시도했는데   
ssh: connect to host 192.168.10.100 port 22: Connection refused  

이렇게 나온다면 openssh가 설치가 안되어 있을 수가 있다  
설치해주자  

```
sudo apt install openssh
```

SSH tunneling을 하려면 서버와 같은 방식인 5901 포트로 트래픽을 보내주게 된다   

클라이언트 쪽에서 아래와 같은 방식으로 입력
ssh -L 5901:127.0.0.1:5901 -N -f -l 서버아이디 서버ip주소로 입력  

```
ssh -i ~/.ssh/ubuntu20.04 -L 5901:127.0.0.1:5901 -N -f -l seruser 192.168.10.101
```
그러면 비밀번호를 물어보는데 이때에는 서버의 기본 계정 비번을 입력하면 된다  

> 만약 private 키를 가지고 있다면 -i 옵션을 사용한다    
```
ssh -i ~/.ssh/mykey -L 5901:127.0.0.1:5901 -N -f -l seruser 192.168.10.101
```

일단 만들어 놓은 것이 없으므로 스킵

<br/>

## tigervnc 접속하기  
클라이언트에는 뷰어만 있으면 된다  
```
sudo apt install tigervnc-viewer
```

터미널을 열고 (background로 작업하기)
```
vncviewer localhost:5901 &
```
해주면 vncserver 처음 시작할 때 설정 했던 암호를 입력하면 된다.  

<br/>

## 복사 & 붙여넣기 
처음에 실행을 하면 vncconfig 작은 창이 실행되어 있다. 아니면 Activies를 (왼쪽상단)을 눌렀을 때   
vncconfig 가 설정 화면이 보이는데 여기에서 클립보드로 복사 붙여넣기를 할 수 있는 기능을 제공하기 때문에  
종료 시키면 로컬 컴퓨터에서의 내용을 복사해서 vnc 화면에 붙여넣기가 안되므로 종료하지 않는 것이 좋다  

만약 불편하면 sudo apt-get install autocutsel 설치하고 (서버에도 설치해야하는지는 확인안해봄)  
~/.vnc/xstartup 파일을 열어서 아래 내용을 추가해준다. 
```
# allow copy & paste - autocutsel
autocutsel -fork 
```
서버를 kill 했다가 다시 켜주면 된다 

<br/>

## 트러블 슈팅 
x서버에서 마우스 키보드 안 될 때  
xserver-xorg-input-all 지워져버리면 발생한다 (vnc 관련해서 지울때 의존성 때문에 같이 지워져버린 듯하다)
```
sudo apt install xserver-xorg-input-all
```
> 그런데 어떻게 입력? ssh로 접속하거나~ 처음 부팅 시 wayland로 들어간다 (로그인 시 톱니바퀴)


