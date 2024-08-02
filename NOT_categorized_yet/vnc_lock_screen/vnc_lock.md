# vnc lock
vnc를 사용하다가 실제 컴퓨터에서 스크린 락이 걸리면 풀 수가 없다...  

## 우분투 기준 20.04 
settings 에서 Power 탭에서   
Dim Screen When Inactive 를 꺼주고   
Blank Screen 도 Never 로 설정   

위에 것이 예전 버전인지 잘 모르겠지만 다시 찾아보니 같은 설정이 안 보임

**Power Saving** 의   
Blank Screen Never 를 선택   

**Suspend & Power Button** 의   
Automatic Suspend 는 Off  
Power Button Action 은 Nothing    

Blank Screen 은 Never로 설정하지 않으면 일정 시간 후에 blank screen이 되어  
vncviewer 에서는 다시 로그인이 안되는 현상이 발생한다.   

이런식으로 사용하면서 아예 화면이 안 꺼지게 하는 방법이 있다.


### Screen lock 사용 시
Power가 suspend 되버리면 당연히 안되겠지만, 실제 host 컴의 blank screen 화면이 꺼지는 것은 하는게 좋아보인다.  
실제 컴퓨터 모니터가 계속 들어와 있으면 그것도 좀 그렇다. (모니터 전원을 아예 꺼두는 것이 아니라면..)   

**Power Saving** 의 
Blank Screen 실제 접속할 컴에서 Black Screen은 최소 minute로 설정해서 사용   

**Suspend & Power Button** 의   
Automatic Suspend 는 Off  
Power Button Action 은 Nothing    

이제 보통 vnc 사용할 때 처럼 사용을 하다가 사용을 안하면 스크린 락이 걸리는데..   
증상은 로그인 화면에서 패스워드 입력을 해도 더 이상 진행이 안 되며 로그인이 화면이 안 풀린다.  

이때 ssh 터미널에 입력 
> vnc접속을 위해서 ssh 접속을 해야하기 때문에 어차피 ssh 연결은 되어 있는 상태라면 더 굿.   

```
loginctl list-sessions
```

이런 결과가 나온다 
```
SESSION  UID USER       SEAT  TTY  
      3 1000 myuser seat0 tty2 
     35 1000 myuser       pts/0
     39 1000 myuser            
     c1  126 gdm        seat0 tty1 
```

처음에 있는 SESSION 을 선택한다.
```
loginctl unlock-session 3
```

이제 바로 vnc 화면에서 락이 걸려있는 상태에서 자동으로 화면이 풀린다.


만약 화면에서    
`Can't close Authentication Required window after login` 라는 창이 왼쪽 상단에 표시되고  
비번을 입력해도 사라지지 않는 상태가 나올 수 있다. 이후 사라지지는 않지만 뒤의 화면은 클릭 가능한 상태   

방법은 2가지 

첫 번째, vncserver 를 종료 후 다시 실행한다.   
ssh 터미널에서     
```
vncservcer -kill :1
```
그리고 다시 vnc를 다시 열어준다.
```
vncserver :1 -localhost -geometry 1024x768 -depth 2
```
> `vncserver :1 -localhost` 만 입력해도 아마 될 듯  
또한 ssh 터널링은 유지한 상태라서 vncserver만 종료해주고 다시 열어줘도 잘 작동한다.


그리고 vncviewer로 다시 입력해서 접속을 시도하면 해당 화면이 깔끔하게 사라진다.


두 번재, alias를 등록해서 사용하는 방법인데 dbus-send 명령어를 해주는 것인데 괘 긴 명령어인데 alias로 등록한 후에 사용할 수가 있다.
```
alias gf='dbus-send --type=method_call --dest=org.gnome.Shell /org/gnome/Shell org.gnome.Shell.Eval string:"global.reexec_self()"'
```

`alias` 를 확인해보면 등록된 내용이 보인다.

이후 `gf` 만 입력해주면 바로 Authentication 화면이 사라지는 것을 볼 수가 있다.



### [우선 참고만 하자] 브라우저에 gnome shell 설치 - 플러그인 사용
파이어폭스를 사용한다면   
예전에는 이 방법이 되었는데 다시 시도 해보니, 잘 안된다..   

**그래서 일단 참고로만 알고 있자**   
[extensions gnome 사이트 접속](https://extensions.gnome.org/)    
```
To control GNOME Shell extensions using this site you must install GNOME Shell integration that consists of two parts: browser extension and native host messaging application.
Click here to install browser extension. See wiki page for native host connector installation instructions.
```
상단에 보면 이런 안내 문구가 있는데, 여기에서 GNOME Shell 을 설치하라고 되어 있다. 클릭을 해서 설치를 한다.   
허용을 해서 설치를 해준다. shell extension 이 설치 된다. 

이제 이를 사용할 native 프로그램을 설치해준다.   
```
sudo apt install chrome-gnome-shell
```
> 파이어 폭스는 없지만 크롬 버전으로 해도 된다.   
만약 chrome-gnome-shell 이 없다면 추가 extension을 설치하려고 할 때  
`No such native application org.gnome.chrome_gnome_shell` 에러가 발생한다.   

설치가 되었다면, 다시 위의 extensions.gnome.org 에서   
*Allow Locked Remote Desktop* 을 검색     

ON 버튼을 눌러서 (허용/ 인스토를 해준다) - 설치가 된다.


스크린 락을 걸어도 다시 암호를 입력하면 락이 풀린다   

(최근에 시도했을 경우에 실패 - 원래 잘 되던 경우였는데 이번에는 크롬 브라우저에다가 한번 설치를 해서 테스트를 해봐야겠다.)   


