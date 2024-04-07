# msi 노트북 ubuntu 설치
처음에는 설치가 되나, 첫 우분투 로그인 이후에는 잘 실행은 되나, 화면이 프리징이 되거나  
재부팅시에 우분투 로그인 화면 자체가 안나오거나.. 

외장 그래픽 카드가 일단 인식이 안 되어 있다. 아직 완전한 해결법은 찾지 못함.  

> 우분투만 몇번째 설치하고 결국은 노트북에서는 간단한 테스트용으로만 쓰기로 결정  

1. 최초 우분투 설치 시 wifi 를 통해서 그래픽 드라이버 등을 미리 받는 기능을 사용하지 말고 설치할 것
> (추후 기억을 위해서) fedora 에서 만들었던 efi 파티션에 boot loader를 지정함

2. nvidia 드라이버는 ubuntu-drivers 명령을 통한 추천되는 open소스 드라이버만 설치할 것   
*nvidia-driver-535-server-open*

최초 USB빼고 첫 로그인까지 시도하게 되면 대체적으로 우분투가 잘 실행이 되는 것 같다.   
최초 로그인 했을 경우에도 프리징이 되는 경우가 있다.   
일단 프리징이 되게 되면 일단 아래처럼 해서 다시 재부팅을 해준다.  
화면이 검게 나오거나(마우스는 표시가 된다던가) 아니면 아예 멈추는 등, 다양하다.;;

다만, 그 이후 **다시 재부팅**을 하게 되면 부팅 grub 선택 메뉴까지는 나오나 그대로 실행 시에는 우분투 화면을 볼 수가 없다.

Fedora 에서 했을 때 처럼 grub 옵션에서 nouveau.modeset=0 를 넣어서 실행을 한다. (quite slash 는 그대로 두고.. 뒤에다 입력)

> 우분투 20.04.5 에서는 위 옵션이 안 되었으나, 우분투 버전 20.04.6 에서는 위의 옵션이 됨 

## nouveau 대신에
만약 nouveau.modeset=0 도 안된다면,   
최초 grub 옵션에서 quiet splash 부분을 지워버리고 nomodeset 으로 넣어주고  
> 그 뒤에 있는 다른 변수등은 두고 nomodeset 만 대신 넣어주고 실행함

ctrl+x 로 실행을 해주자 

이렇게 하면 우부툰 로그인은 가능하다


## msi 노브툭 gf63 
```
ubuntu-drivers devices
```
로 해보면 몇가지 드라이버가 나오는 데 open source driver라고 한다  
이 중에서 recommended로 나오는 드라이버는 설치할 수는 있는데   

> 설치한 드라이버는  
```
sudo apt install nvidia-driver-535-server-open
```

이렇게 하면 다음부터 재부팅시에는 grub 옵션을 안 넣어도 부팅이 된다.   

주의 할 점은 그 외에 다른 드라이버를 설치하면 재부팅시에 바로 먹통이 된다.;;;
nvidia 홈피에서 제공하는 리눅스용 드라이버도 설치하지 말자. 노트북용 2050, 리눅스용 버전을 받을 수 있으나 안된다.  
위의 nomodeset 도 소용이 없음에 주의 한다.

그래도 안된다면, 위의 grub 옵션을 넣어서 다시 로그인 한 후에 nvidia 드라이버는 다 지우고  
xorg 버전만 남겨준다.
> 물론 다른 버전의 드라이버를 설치하면 아마도 이것조차도 안될 수도 있다.
```
sudo apt purge nvidia-driver*
sudo apt autoremove
sudo apt install xserver-xorg-video-nouveau
```


