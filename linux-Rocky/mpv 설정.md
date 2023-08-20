설정파일은 /home/$USER/.config/mpv  
안에 위치를 시켜줘야하는데 원본 파일에서 복사를 해야한다   

```
cp -r /usr/share/doc/mpv/mpv.conf ~/.config/mpv/
```
input.conf 파일도 있는데 key 바인딩에 관한 파일임  

> 일단 필요한 설정 파일만 mpv.conf 정도만 있으면 될 듯 하다

다른 설정은 따로 할 필요는 없고, 소리가 100% 이상으로 되어 있어서 불편하므로;;  
mpv.conf를 열어서 한 줄 추가해준다  
```
volume=50
```

추가로 stereo 로 사운드 설정하기

소리가 5.1채널이나 다른 방식으로 되어 있을 경우에 소리가 안 나오게 되는데   
(아마도 5.1채널로 스피커가 구성되어 있다면 문제가 안될 듯 하지만.. )   

한번 mpv 실행 시 프로그램 내에서 따로 설정을 할 수 없고  
처음 실행 시 파라미터로 설정하거나 또는 위처럼 mpv.conf 파일에 넣어준다 
```
audio-channels=stereo
```

파라미터는 이런식으로 
```
mpv 영상파일이름.mp4 --audio-channels=stereo
```


[좀 더 알아보려면 참고](https://wiki.archlinux.org/title/mpv)

