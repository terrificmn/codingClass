# 리졸브 편집 전에 동영상 변환하기

obs로 캡쳐를 하게 되면 동영상 플레이어로 보는데는 전혀 문제가 없는데 
편집을 하기 위해서 다빈치 리졸브에서 화면이 전혀 안보이게 된다. 
그래서 찾은 방법이 

obs에서는 캡쳐를 mkv로 하고, (권장이 그러하다..)
그리고 mkv 파일을 mov 파일로 변환. 변환할때 ffmpeg명령어를 사용한다.

따로 설치한적은 없었는데.. 기본으로 깔려있거나, 다른 것을 설치하면서 의존성 패키지로 설치되었을 거 같다
obs-studio에서 캡쳐링 한 영상인 mkv를 mov로 변환해 준다.


## mkv/mp4를 mov 파일로 변환 
```
ffmpeg -i input.mkv -map 0:0 -map 0:1 -vcodec dnxhd -acodec:0 pcm_s16le -acodec:1 pcm_s16le -s 1920x1080 -r 30000/1001 -b:v 36M -pix_fmt yuv422p -f mov output.mov
```

또는 dnxhd 가 아닌 mpeg4로 쉽게 하기 (조금 퀄리티가 떨어질 수 있다고 함- 용량이 훨씬 작아짐 (위의 방식은 용량이 큼))
```
ffmpeg -i input.mp4 -c:v mpeg4 -qscale:v 1 -c:a pcm_s16le -f mov output.mov
```


만약 아래와 같은 메세지가 뜬다면
```
Stream map '0:1' matches no streams.
To ignore this, add a trailing '?' to the map.
```

이런식으로 -map 0:1 뒤에 ? 를 붙여준다
```
ffmpeg -i color_tracker1.mp4 -map 0:0 -map 0:1? -vcodec dnxhd -acodec:0 pcm_s16le -acodec:1 pcm_s16le -s 1920x1080 -r 30000/1001 -b:v 36M -pix_fmt yuv422p -f mov tracker-output-cap.mov
```

## 힘들게 변환한 이유는...
obs-studio로 캡쳐한 방식 mkv 또는 mp4방식 둘 다 다빈치 리졸브에서 열리지를 않는다.
대신에 이제 mov로 파일은 열려서 위에 처럼 해주면 다빈치 리졸브에서 편집을 할 수가 있다.
 
하지만.. 여기에도 또 한번 더 거쳐야 하는 과정이 있는데...
무료 버전 다빈치에서 h264로 인코딩을 할 수가 없다. 물론 유료버전에는 있지만..
아.. 이 부분은 윈도우랑은 다를 수 있다. 
윈도우는 h264로 mp4로 랜더링을 할 수가 있었던 것 같은데.. GPU를 사용 못하고 CPU만 사용해야하서 
랜더링과 편집시에 느리다.
근데 리눅스에서는 GPU를 사용할 수 있지만, 랜더링을 mp4로 못한다.. 

어쨋든 이제 mov파일로는 편집할 수 있으니...
이제 원하는 컷 편집을 하고 나서..
마지막 랜더링 할 때 quick타임 방식에 MPEG 코덱으로 정하고 랜더링을 하면
new.mov파일이 랜더링으로 생성됨

단, 이 상태에서는 웹 브라우저에서 재생이 안됨, 유튜브 등에서는 지원하는지도?
어쨋든.. 뭐가 이리 복잡하노 ㅋㅋ 
타입은 QuickTime video (video/quicktime) 인데..  
```
No video with supported format and MIME type fund.
```


## 다시 mp4로 재생가능하게 convert해주기
웹브라우저에서는 재생이 안되므로 다시 또 convert를 해줘야한다 ㅋㅋㅋㅋ ;;;;

그래서..  
이제 new.mov 파일을 다시 h264코덱으로 다시 컨버트 해준다. 
고마운 ffmpeg,  mp4 로 바꿀 수 있다.
mov->mp4 파일로 컨버트
```
ffmpeg -i tfod_image_processing_output.mov -c:v libx264 tfod_image_processing_output_final.mp4
```
이제 웹 브라우저에도 영상이 나오게 된다.  

기회가 되면 아래 방식도 비교해보기
```
ffmpeg -i render.mov \
    -c:v libx264 -pix_fmt yuv420p -crf 16 \
    -force_key_frames 'expr:gte(t,n_forced/2)' -bf 2 \
    -vf yadif -use_editlist 0 \
    -movflags +faststart \
    -c:a aac -q:a 1 \
    -ac 2 -ar 48000 \
    -f mp4 out.mp4
```

하지만.. convert 하는 과정이.. 흠.. 1분 정도의 영상을 진짜 간단하게 편집할려고 한 거였으니.. 
별 문제는 안되지만.. 나중에 파일이 커지고 하면.. 또 새로운 숙제구먼..


