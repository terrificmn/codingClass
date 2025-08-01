# h264 problem 
vlc 에서는 h264 관련해서 에러가 발생하면서 동영상 재생을 못하는 경우   

mpv에서는 명확하게 codec 을 열 수 없는 상황인 것을 말해준다.  

```
[ffmpeg/video] libopenh264: libopenh264.so.7: cannot open shared object file: No such file or directory: libopenh264.so.7 is missing, openh264 support will be disabled
Could not open codec.
Decoder init failed for libopenh264
Failed to initialize a decoder for codec 'h264'.
Video: no video

Exiting... (Errors when loading file)
```

관련 프로그램을 설치해주면 쉽게 해결 된다.

```
sudo dnf install openh264 mozilla-openh264
```

## openh264 mozilla-openh264 경우로 해결이 안 되는 경우
이걸로 안될 경우에는 다시 지우고 rpmfusion repo로 해본다
```
sudo dnf remove openh264 mozilla-openh264
```

## libavcode-freeworld 설치 (추천)
웬만한 **h264 영상은 잘 재생** 해주는 듯 하다  
 
```
main decoder error: buffer deadlock prevented
```
처럼 에러 발생 했을 경우에도 코덱 설치로 해결이 된다.

rpmfusion 등록 free버전, non free 버전 등록
```
sudo dnf install https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```

안될 경우
```
sudo dnf install \
  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
```

> $(rpm -E %fedora) 40 버전의 rpm fusion   
(워크스테이션 42기준) Fedora 41, 42 버전도 있다고 하지만 (의존성이 해결되지 않아서) 잘 되지 않는다.  
다행히 40 버전 리포 등록으로도 코덱 설치가 잘 된다.  


이후 **libavcode-freeworld** 설치
```
sudo dnf install ffmpeg-free libavcodec-freeworld
```

또는 `sudo dnf install libavcodec-freeworld --allowerasing`   

x264-libs, x265-libs 등을 설치해준다.

위가 안될 경우에는 
```
sudo dnf install ffmpeg --allowerasing
```

libavfilter-free, libavformat-free, libavutil-free   
libpostproc-free, libswresample-free, libswscale-free   
를 삭제하게 된다.

> Optional  
input/Codes 설정에서 Hardware-accelerated decoding 을 Disable 시켜서 테스트  


## speed 변경 하기
기본 명령어는   
```
ffmpeg -i input.mp4 -vf "setpts=0.5*PTS" -an output.mp4
```
속도 자체는 0.5 숫자만 변경 해주면 된다. 이 명령어만 사용하게 되면 화질이 저하 된다.  
> 속도는 예를 들면 0.5 는 2배속, 0.25 는 4배속, 0.1 은 10배속  

실제로는 아래 명령어를 사용하는 것이 좋다.  

```
ffmpeg -i my_file.mp4 -vf "setpts=0.1*PTS" -c:v libx264 -crf 18 -preset slow -an output.mp4
```

이렇게 하면 속도 및 화질도 유지 된다.  

옵션 중에 crf 는   
-crf 18: Constant Rate Factor (lower = higher quality, 18 is visually lossless)   

preset은  
-preset slow: Better compression efficiency (slower encoding, better quality)   

