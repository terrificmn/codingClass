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
