```
nothing provides libSDL2-2.0.so.0()(64bit) needed by ffmpeg
```
처럼 나온다면 
dependency 부터 해결 후 

의존성 설치
```
dnf --enablerepo=powertools install SDL2
```

ffmpeg 설치를 해준다
```
sudo dnf install ffmpeg
```

