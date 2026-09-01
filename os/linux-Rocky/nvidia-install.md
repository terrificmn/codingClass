
# fedora 40 버전에서 nvidia 드라이버 설치
40 에서 그래픽 드라이버를 잡지 못함.

기존 38에서 잘 잡히던 것이였으나 뭔가 잘 안됨


자신의 그래픽 드라이버 확인. 그래픽카드 모델명 등을 알 수 있다.
```
/sbin/lspci | grep -e VGA
```

일단 secure boot 가 *disabled* 되어야 한다. 
> enable 되어야 하는 줄 알았더니, 오히려 disable 되어야 작동한다.


```
sudo dnf install akmod-nvidia
```
옵션이지만... (설치 함)
```
sudo dnf install xorg-x11-drv-nvidia-cuda
```

## 지우고 다시 할 경우
그래도 안되는 경우에는 지우고 다시 설치해준다.
```
dnf list installed '*nvidia*' | tail -n 15 | awk '{print $1}' | xargs sudo dnf remove -y
```

위의 설치를 다시 진행 한다. akmod-nvidia 설치 부터 해준다.

이렇게 해도 안될 경우..   
특히 부팅하면서 `Nvidia kernel module missing falling back to nouveau` 이렇게 나오는 경우  
다시한번 bios에서 secure boot 를  disable 확인 해주고  

nvdia 모듈을 지웠다가 다시 생성해준다. 아래의 커맨드를 사용

```
sudo dnf remove kmod-nvidia-\*
```

이렇게 하면 커널 nvidia 모듈을 삭제한다. 

바로 설치 재설치,  
```
sudo akmods --force
```

다시 모듈를 빌드해준다.

재부팅하면 부팅 시에 Nvidia kernel moudle missing 메세지도 안나오고   
setting에서 보면 System Details -> Hardware Information 에 graphics 에서 Intel내장 그래픽이 보이고   
graphics 1에서 NVIDIA GeForce RTX 2050 이런식으로 나오게 된다.

