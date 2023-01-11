설정파일은 /home/$USER/.config/mpv  
안에 위치를 시켜줘야하는데 원본 파일에서 복사를 해야한다   

```
cp -r /usr/share/doc/mpv/mpv.conf ~/.config/
```
input.conf 파일도 있는데 key 바인딩에 관한 파일임  

> 일단 필요한 설정 파일만 mpv.conf 정도만 있으면 될 듯 하다

다른 설정은 따로 할 필요는 없고, 소리가 100% 이상으로 되어 있어서 불편하므로;;  
mpv.conf를 열어서 한 줄 추가해준다  
```
volume=50
```

[좀 더 알아보려면 참고](https://wiki.archlinux.org/title/mpv)

