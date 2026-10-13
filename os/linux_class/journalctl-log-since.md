# journalctl
since & until 사용하기   
시간대를 특정해서 볼 수 있음 

`--since "18:40:00" --until "19:05:00"`  since 만 사용해도 가능  


날짜 까지 적용하려면  `--since "2026-06-25 18:40:00"`
  
mosquitto 등에서는 시간 로그를 활성화 했다면은 특정 시간대의 로그만 보는 식으로 활용이 가능하다 


이런식도 가능하다고 하는데 해보지는 못함  
`journalctl --since "1 hour ago" --until "30 minutes ago"`


## journalctl 시작 시간
dmesg logs 를 모두 복사해서 journal 에서 사용할 수 있게 하는데,  

`sudo dmesg` 로 로그를 보려고 할 때 너무 많은 에러 로그 때문에 시작 부분 또는 문제 발생 전의 로그를 
못 볼 경우가 있는데 이때에는 journalctl -k -b 의 옵션을 사용해서 사용하면 된다. 

```
journalctl -k -b 0
```


## 부팅 전 기록 보기
이미 재부팅이 되어서 dmesg 로 이전 로그를 못 보는 경우에 journalctl 를 이용해서 볼 수가 있음  
```
sudo journalctl --list-boots
```

전 기록들이 보이는데 맨 아래로 내리게 되면 0 번이 현재 기록  바로 그 전 기록은 -1, -2 식으로 표시 된다.  
```
 -3 792c784c58d94218a6bbda812233bbe9 Sun 2026-10-11 07:55:10 KST—Sun 2026-10-11 13:41:14 KST
 -2 362f370a732f442ab64924b0db50006a Mon 2026-10-12 08:21:12 KST—Mon 2026-10-12 21:31:48 KST
 -1 8339721334c445469c6a7a3d0c722053 Tue 2026-10-13 08:21:04 KST—Tue 2026-10-13 09:30:46 KST
  0 b08af76e35564d68877ca89012fe9c6b Tue 2026-10-13 09:31:37 KST—Tue 2026-10-13 11:00:23 KST
```

-b 옵션을 사용해서 지정해준다.  -1 이 바로 전 기록이므로 해당 기록을 보려면 아래처럼 해주면 되고,  
옵션을 더 추가해서 리다이렉트로 파일로 만들어 준다. 

```
sudo journalctl -k -b -1 -o short-iso-precise \
    > ~/dmesg-previous-boot.log
```


