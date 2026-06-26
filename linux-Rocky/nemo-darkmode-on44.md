# nemo desktop 
페도라 44에서는 기존 설정처럼 하면 아이콘을 눌렀을 때 다크 테마가 적용이 안된다. 

nemo자체가 일단 gtk3 를 사용하므로  

```
sudo dnf install nemo
sudo dnf install adw-gtk3-theme
```

~/.local/share/applications$ vi nemo.desktop  에는 
기존 처럼 만들어 준다.
```
[Desktop Entry]
Name=Nemo (Dark)
Exec=/home/sgtraphaelfed/.local/share/applications/nemo
Icon=system-file-manager
Type=Application
Terminal=false
Categories=Utility;
```

> 여기에서는 nemo 쉘스크립트를 터미널에서도 실행할 경우에 사용하기 위해서 nemo 확장자 없이 만들어 준다.  
스크립트는 +x 퍼미션 해주고  

위의 nemo 스크립트
```
#!/bin/bash
CURRENT_THEME=$(gsettings get org.gnome.desktop.interface color-scheme)
echo "Theme: $CURRENT_THEME"
if [[ "$CURRENT_THEME" == "'prefer-dark'" ]]; then #or 'prefer-dark' or default
        export GTK_THEME=adw-gtk3-dark
else
        export GTK_THEME=adw-gtk3
fi

exec /usr/bin/nemo "$@"
```

> GTK_THEME 를 adw-gtk3-dark 를 사용하는걸로 바뀜


update 명령어로 업데이트 해주기
```
update-desktop-database ~/.local/share/applications/
```

## 환경 변수 PATH 설정
export PATH="$HOME/.local/share/applications/:$PATH"

PATH 변수 맨 먼저 방금 만들 경로를 먼저 확인할 수 있게 넣어준다. 그리고 뒤에 정상적으로 원래의 PATH 경로를 설정  
터미널에서 nemo 라고 치면, /usr/bin/nemo 을 실행해야 하지만,,   
PATH 경로에 처음 있는 .local/share/applications/ 경로의 nemo (실행가능한 스크립트 같은 이름이다.)  
를 실행하주게 된다.  

이렇게 되면 system의 dark 테마를 잘 물고 실행해준다.  

~/.bashrc 에 넣어주자.

nautilus 를 사용할 때에도 alias 로 nemo가 실행되게 해주기

```
echo "alias nautilus='$HOME/.local/share/applications/nemo'" >> ~/.bashrc 
```


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


## warning
그냥 참고  
`Action '90_new-launcher.nemo_action' is missing dependency: cinnamon-desktop-editor`  
에 대해서는 
`sudo dnf install cinnamon-desktop` 를 설치하면 될 듯 하나, 크게 필요하지 않은 듯 하여 설치하지는 않음.  


## nemo terminal open
윈도우 창에서 오른쪽 마우스 클릭 시 Open in Terminal 을 클릭하면 터미널이 열리지 않음   

기본 터미널 설정이 gnome-terminal 로 되어 있기 때문인데, gnome-terminal 은 설치되어 있지 않다.  

Fedora 44 에서는 ptyxis 터미널이 사용된다.  
qsettings 를 이용해서 기본 터미널 설정을 해줘야 한다.   

```
gsettings set org.cinnamon.desktop.default-applications.terminal exec "ptyxis --new-window"
```
> --new-window 옵션으로 새로운 창이 열리게 해준다.  

새로운 창이 열린 후에 nemo 윈도우에서 현재 디렉토리가 안 열릴 경우에는  
ptyxis 에서 preference 를 열고 Behavior 탭에서 **Restore Session 을 해제**해준다.  
Preserve Working Directory 는 Safe 설정  

저장 후에 `nemo -q` 를 해서 적용해준다.  

다시 nemo 를 열고 terminal 을 띄어보면 잘 열린다. 

다른 방법으로는  gnome-terminal 를 설치하는 방법이 있는데, 딱히 시도해 보지는 않음   
`sudo dnf install gnome-terminal`  

