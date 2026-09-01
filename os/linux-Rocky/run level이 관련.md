현재 기본 셋팅 보려면 
```
systemctl get-default
```

그러면 
```
graphical.target
```

위 처럼 출력이 될 것


/etc/systemd/system/default.target 이 어디를 심볼릭 링크로 가리키고 있는지 확인
```
ls -l /etc/systemd/system/default.target
```

만약 런레벨 3으로 변경이 된다면  ..
sudo init 5 를 해보자

또는 GUI 모드로 변경하려면 
```
systemctl set-default graphical.target
```

심볼릭 링크가 default.target 이 생기면서 /usr/lib/systemd/system/graphical.target 으로 생성이 되면 잘 만들어 진 것임   

확인은
```
systemctl get-default
```

