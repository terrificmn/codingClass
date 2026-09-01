
dialout 을 추가하듯이

root video 권한으로 되어 있다면  
id로 확인해서 속해있는 지 확인 후

잘 되다가 index를 열수가 없을 경우 

`ls -l /dev/video*`
```
crw-rw----+ 1 root video   81, 0  8월 18 20:27 /dev/video0
crw-rw----+ 1 root video   81, 1  8월 18 20:27 /dev/video1
```

이런식으로 나올 경우, 자신의 user 계정에 추가


sudo usermod -aG video $USER

재부팅 후 
다시 id 를 쳐보면 
44(video) 가 추가되어 있음



