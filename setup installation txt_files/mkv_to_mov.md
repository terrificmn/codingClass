obs로 캡쳐를 하게 되면 동영상 플레이어로 보는데는 전혀 문제가 없는데 
편집을 하기 위해서 다빈치 리졸브에서 화면이 전혀 안보이게 된다. 
그래서 찾은 방법이 

obs에서는 캡쳐를 mkv로 하고, (권장이 그러하다..)
그리고 mkv 파일을 mov 파일로 변환. 변환할때 ffmpeg명령어를 사용한다.

따로 설치한적은 없었는데.. 기본으로 깔려있거나, 다른 것을 설치하면서 의존성 패키지로 설치되었을 거 같다

```
ffmpeg -i input.mkv -map 0:0 -map 0:1 -vcodec dnxhd -acodec:0 pcm_s16le -acodec:1 pcm_s16le -s 1920x1080 -r 30000/1001 -b:v 36M -pix_fmt yuv422p -f mov output.mov
```

다빈치에서 h264가 없다;;; 유료버전만 있다고 한다;;
렌더링 할 떄 그래서 quick타임 방식으로 렌더링 한다음에 다시 mp4로 컨버트 한다


davinci로 파일 수정한 후에 
mov->mp4 파일로 컨버트
```
ffmpeg -i tfod_image_processing_output.mov -c:v libx264 tfod_image_processing_output_final.mp4
```
이렇게 해야 브라우저에 잘 볼 수 있는 상태가 됨
