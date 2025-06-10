## nemo 설치
```
sudo dnf install nemo
```

## .desktop 설정하기
/usr/share/applications 이하에 있는 nemo.desktop 파일을 복사해서 사용한다. 
```
cp /usr/share/applications/nemo.desktop ~/.local/share/applications/
gedit ~/.local/share/applications/nemo.desktop
```

Exec=nemo %U 검색
Exec=env GTK_THEME=Adwaita:dark nemo %U 로 변경

update 명령어로 업데이트 해주기
```
update-desktop-database ~/.local/share/applications/
```

log out and log back in 해준다.


단 위처럼 하면 하나의 SCHEME 만 적용할 수가 있는데 환경변수를 받아서 다이나믹하게 만들어 줄 수가 있다.  

___
## gsettings
먼저 gsettings 를 이용할 수가 있다.

~/.bashrc 파일에서 GTK_THEME 만 등록해서 사용  
```
GTK_THEME=Adwaita:dark
```

어쨋든 이렇게 사용하면 되기는 한다.

___
Fedora42 는 GNOME 46인데 GTK4 를 사용한다고 하는데  
Nemo은 GTK3 이다.  

desktop 파일은 윈도우 상태에서 클릭했을 때 사용이 된다고 보면 되고, 
bashrc 에서는 터미널에서 실행할 때를 생각하면 된다.  

아쉽게도 gsettings 에서의 darkmode 등을 환경 변수를 직접 지정해서 사용할 수는 있지만  
변수 자체로 적용은 안되는 듯 하다.  

그래서 Exec 부분에 shell script를 실행할 수 있게 하고   
그 스크립트에서 환경 변수를 사용할 수 있게 해주면 쉽게 활용할 수가 있다.  

데스크탑 관련 변수를 읽어오거나 set/get 할 수 있는 것은  
gsettings 라는 것을 통해서 set/get 를 해서 변수등을 받아올 수가 있다. 
그 중에 
 
`org.gnome.desktop.interface color-scheme` 를 받아와서 변수로 셋팅  
예를 들면  
```sh
#!/bin/bash
SCHEME=$(gsettings get org.gnome.desktop.interface color-scheme)

if [[ "$SCHEME" == "'prefer-dark'" ]]; then
    export GTK_THEME=Adwaita-dark
else
    export GTK_THEME=Adwaita
fi

nemo
```
이렇게 하면 SCHEME 에 현재 시스템에서 사용하는 값이 들어가지고 이를 이용해서 GTK_THEME 을 지정해주면 된다.  
이렇게 한 후 nemo 를 실행하게 되면 해당 테마로 실행이 되게 된다.  

> gsettings 을 사용할 때 color-scheme 를 사용하자   
gsettings get org.gnome.desktop.interface gtk-theme 는 워크스테이션 42 버전에서는 안 되는 듯 하다.  

이후이를 메모.데스크탑 파일에서 변경해서 사용해준다.

먼저 위에서 복사했던 desktop 파일에 ~/.local/share/applications/ 이하에서  
nemo.desktop 파일을 만들고  
아래처럼 구성
```
[Desktop Entry]
Name=Nemo (Dark)
Exec=/home/my_user/.local/share/applications/nemo.sh
Icon=system-file-manager
Type=Application
Terminal=false
Categories=Utility;
```

물론 스크립트 +x가 되어야 한다.  

실제 스크립트 nemo.sh 에는 
```
#!/bin/bash
CURRENT_THEME=$(gsettings get org.gnome.desktop.interface color-scheme)
if [[ "$CURRENT_THEME" == "'default'" ]]; then #or 'prefer-dark'
	export GTK_THEME=Adwaita
else 
	export GTK_THEME=Adwaita-dark
fi

# nemo 
# nemo 로도 할 수 있지만. 해당 스크립트를 터미널에서도 사용할 경우에는 full path를 적용해준다.
exec /usr/bin/nemo "$@"
```

update 명령어로 업데이트 해주기
```
update-desktop-database ~/.local/share/applications/
```


이제 윈두우 상에서 Files , nautilus, nemo 로 검색하는 아이콘으로 실행하면 해당 theme 이 적용이 되서 실행이 된다.  

## 터미널에서 nemo 지정하기
가장 편한 것은 위에서 만든 것은 재활용해서 해당 스크립트 파일을 열게 해주면 된다. 

PATH 변수에 가장 앞에 위치하게 변수를 다시 셋팅해주게 되면 /usr/bin/nemo 보다 먼저 읽게 되므로 이를 사용하면 
해당 스크립트를 사용할 수가 있다. 

```
export PATH="$HOME/.local/share/applications/scripts:$PATH"
```

단 주의 할 점은 이렇게 하면 
```
/bin/bash: warning: shell level (1000) too high, resetting to 1
```
워닝이 발생, 이유는 스크립트에서 nemo 를 실행하게 되는데 이러면 recursive 로 nemo 를 계속 실행하게 된다  
해당 스크립트를 실행하게 되고 또 해당 스크립트를 실행하게 되는 무한루프가 된다고 보면 된다 

그래서 스크립트에서 nemo 로 실행하던 것은 변경해준다. 
```
exec /usr/bin/nemo "$@"
```

그리고 위의 export $PATH 경로 설정을 ~/.bashrc 에 넣어준다.   
> $PATH 실제 PATH는 마지막에 다시 저장해주는게 포인트 : 이후, PATH="내경로:$PATH"

## Files 
default 설정
```
xdg-mime default nemo.desktop inode/directory application/x-gnome-saved-search
```

디폴트 된 것 확인
```
xdg-mime query default inode/directory
```
nemo.desktop 으로 나오면 ok

