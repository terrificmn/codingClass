Cannot locate node of type [move_base] in package [move_base]. Make sure file exists in package path and permission is set to executable (chmod +x)

소스파일을 직접 build한 경우라면 이럴 수 있는데  빌드 에러가 없고, 다른 것은 건들지 않은 상태라면..


```
rospack profile
```
을 해주면  update package list를 해주게 되고   
다시 실행을 하면 잘 인식한다  


