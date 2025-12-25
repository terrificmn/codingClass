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


## 회전 시키기
동영상을 가로로(Landscape) 찍었는데, 실제로는 세로(Portrait) 로 저장이 되어 있을 경우, 또는 그 반대?  

vf 옵션 video filter 를 사용하는 방법

transpose=1 은 90도 (Clockwise)

transpose=2 은 -90도 (Counter-Clockwise)

transpose=3 은 180도

```
ffmpeg -i input.mp4 -vf "transpose=2" output.mp4
```
단, 화질이 형편없다.  

스케일을 1280:720 으로 사용해서,  libx264코덱 사용, -crf 은 Constant Rate Factor  
The CRF range is 0 (lossless) to 51 (worst quality). 기본은 23 (숫자가 낮을 수록 하이퀄리티)  
 
-c:a copy 은 오디오를 원본에서 그대로 복사해오는 것, 시간 줄이는데 좋다.  
```
ffmpeg -i input.mp4 -vf "transpose=2,scale=1280:720" -c:v libx264 -crf 18 -preset medium -c:a copy output.mp4
```

이렇게 하면 1920x1080 영상이 꽤 괜찮은 사이즈로 줄어든다. 1.5G 영상이 약 600MB 정도로 줄었다.  

## 특정 사이즈로 변경
하지만 이렇게 해도 카톡에 안올라간다. 300MB 이하만 가능하다.;;; 600Mb를 올리면 알아서 인코딩 해줄 것 같았으나,  
이미 인코딩이 되어서 그런지 용량이 크다고 거부된다;;

특정 사이즈에 좋을 영상 퀄리티를 유지하려면 2번의 인코딩 작업을 거쳐야 한다.  

필요한 평균 video bitrate 먼저 비트레이트를 계산해야한다. 
```
ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 input.mp4
```
ffprobe 를 이용해서 input 파일을 넣어주면 시간 초가 나온다.  
예를 들어서 673.184146 이 결과로 나오는데  

여기에서 계산식은  
1. Total Bitrate (kbps) = Target File Size (MB) x 8192   /   Duration (seconds)   
2. 여기에서 나온 Total Bitrate(kbps) 에서 128 를 다시 빼준다.  

Duration 에 위의 ffprobe 명령어로 나온 시간을 넣어주고  원하는 용량 300mb 로 계산해보면  
값은 3650.709860894 이 나옴   
그리고 128을 빼주면  Video Bitrate(kbps)가 나온다.  

> 128은 오디오 bitrate 임 (128이면 꽤 괜찮은 오디오 품질이라고 함)

이렇게 하면 대충 3522 가 나오는데 좀더 300MB 가 잘 나올 수 있게 좀 더 줄여준다.(약간의 마진을 준다)   
3490k 정도 추천하는데 조금 더 낮춰야 할 수도 있다.  

> 3490k 정도로 하면 300Mb가 조금 넘어서 304mb 정도 나온다. 무조건 300Mb 이하여야 한다면 bitrate를 좀 더 줄여준다.  
약 100~200 정도 더 빼준다.


Two-Pass Encoding Commands 를 적용하면 위에서 나온 최종 Bitrate 를 적고, **k** 를 꼭 넣어준다. 

패스1, 패스2 두번을 인코딩해서 사이즈를 맞출 수가 있다.  

패스 1
```
ffmpeg -y -i output_20251205_165102.mp4 -vf "transpose=2,scale=1280:720" -c:v libx264 -b:v 3290k -pass 1 -preset medium -an -f mp4 /dev/null
```
바로 결과 파일들이 나오지는 않지만, ffmpeg2pass-0.log, ffmpeg2pass-0.log.mbtree 파일들이 생긴다.  
결과물이 나오면 지워주자.  

패스 2, 한번더!
```
ffmpeg -i output_20251205_165102.mp4 -vf "transpose=2,scale=1280:720" -c:v libx264 -b:v 3290k -pass 2 -preset medium -c:a aac -b:a 128k output_300.mp4
```
Finally, output 파일을 지정해준다. 

> 만약 회전에 필요 없다면 transpose 만 뺴주고 진행  

1080p의 1.5G 영상이 720p 287Mb 영상으로 나왔다. 화질도 꽤 괜찮고, 용량도 작다. 



## webm 파일 mp4로 변환
리눅스에서 스크린샷으로 저장된 영상은 webm  
영상이 점프, 앞 뒤로 이동하면 거의 볼 수가 없다. 단, 계속 틀어놓으면 잘 보인다.  

```
 ffmpeg -i dongwon-demo-Screencast_from.webm -vf "scale=1280:720" -c:v libx264 -crf 18 -preset medium -c:a copy output.mp4 
```

