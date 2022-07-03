# 듀얼모니터 connected but no signal 일때 
증상:  
처음 bios 화면에서는 듀얼모니터 2개다 잘 나오는데 리눅스(현재 centos8)에 들어오면   
두 번째 모니터가 화면이 안나오는 현상   
셋팅에서도 모니터 2개는 잘 보이는데 신호없음으로 화면이 나오지 않는 현상   

라데온 계열 예전 그래픽카드에서 나타날 수 있는 현상(버그?) 
라데온 R9 380   
결론은 부팅 때 grub 에 아래 처럼 옵션을 넣어줘서 부팅하면 잘 됨   
부팅선택 grub화면에서 e 누르고 안쪽 커널이미지 선택하는 곳에 amdgpu.dc=0 이라고 입력해주고 부팅   
``` 
amdgpu.dc=0
```

좀 더 자세히 알아보자   

## Grub에서 임시로 설정하기 
부팅 시 처음 grub화면에서 (임시로)  
```
CentOS (4.18.8-277.e18.x86_64) 0

Press 'e' to edit the selected item, or 'c' for a command prompt.
```
처음 부팅을 할 때 Grub 이 뜨면서 커널을 고르는 화면에서 e 키를 눌러서 진입한다  
그러면 아래와 같은 화면이 나옴

```
load_video
set sfx_payload=keep
linux ($root)/vnlinux-4.18.8-277.e18.x86_64 ...생략 quiet [바로 여기]
initrd ($root)/initra.......생략

Press Ctrl-x to start, ....생략
```

여기에서 커널 이미지를 선택하는 linux로 시작하는 부분에서 quiet 바로 다음 [바로 여기]에   
amdgpu.dc=0 이라고 입력을 해준다 후    
Ctrl-x 를 눌러주면 부팅이 되고   
2번째 모니터가 잘 나와서 해결됨!! 새벽에 소리지를뻔함 ㅋㅋ   

이렇게 된다
```
linux ($root)/vnlinux-4.18.8-277.e18.x86_64 ...생략 quiet amdgpu.dc=0
```

## grub 업데이트를 해서 임시설정 필요없이 사용하기
위에 처럼하면 잘 되기는 하나~ 매번 grub화면에서 계속 amdgpu.dc=0 이라고 입력해야해서   
아예 커널 커맨드 라인을 업데이트 하기~ 그러면 재부팅시에도 입력이 필요없음

MBR(Bios-based) system에 해당한다고 함. 백업하기
```
$sudo cp /etc/default/grub /etc/default/grub-backup
$sudo cp /boot/grub2/grub.cfg /boot/grub2/grub.cfg-backup
```

그 다음 /etc/default/grub 파일을 열어서 GRUB_CMDLINE_LINUX= 여기에 추가해준다  
" " 쌍따옴표로 되어있으므로 그 안에다가 입력한다  
대충 아래처럼 
```
GRUB_CMDLINE_LINUX="crashkernel=auto ...생략.. rhgb quiet amdgpu.dc=0"
```
그리고 저장하고 나가기  : 누른후 wq  

다음은 새로운 grub.cfg 파일을 생성하기  
```
$sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

그러면 뭔가 진행이 되고 done이라고 끝남   

그 다음에 재부팅하기
```
$systemctl reboot
```

이제 재부팅 할 때 grub cmdline에 입력을 안해도 되고  
재부팅 후 업데이트가 잘 되었는지 확인은
```
$cat /proc/cmdline
```

입력했던 내용이 잘 나오는것 확인   
참고 사이트:
https://www.thegeekdiary.com/centos-rhel-7-how-to-modify-the-kernel-command-line/
https://bugzilla.redhat.com/show_bug.cgi?id=1594488

