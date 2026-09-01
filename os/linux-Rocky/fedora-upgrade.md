# fedora 38 에서 40으로 업그레이드
```
sudo dnf upgrade --refresh
sudo dnf system-upgrade download --releasever=40
```
패키지 호환성 문제가 없다면 잘 진행이 된다.

만약 특정 패키지에서 문제가 있다면 아마도 서드파티에서 발생할 문제가 크므로,   
해당 패키지만 지우고 실행하거나, --allowerasing 옵션을 넣어서 다시 실행해준다.
> 해보지는 않음

마지막으로 시스템 업그레이드 실행
```
sudo dnf system-upgrade reboot
```
재부팅하면서 업그레이드를 한다. 시간이 꽤 걸린다.

40으로 변경이 되면 몇몇 프로그램에서 문제가 발생한다. 아래를 참고   

## 그래픽 드라이버 및 모듈 재설치
nvidia-install.md 를 참고

## vscode 재설치
vscode 실행이 안 되는 경우,  
vscode 를 dnf remove로 지운 후에 vscode 홈피에서 rpm 버전 다운 받은 후 설치해준다.

```
sudo dnf remove code
```

## alt 키 설정 변경
설정을 다시 해줘야 한다.  
```
sudo vi /usr/share/X11/xkb/keycodes/evdev 
```

RALT 주석처리,   
HNGL 을 108로 변경

