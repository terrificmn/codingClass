터미널 창에서 입력
```
gpio readlall
```

필요한 핀 넘버를 출력으로 지정 (output / input)
```
gpio -g mode 12 output
```

직접 명령을 입력  
핀넘버 1 을 주면 작동 

```
gpio -g write 12 1
```

핀넘버 0 을 주면 꺼짐
```
gpio -g write 12 0
```

