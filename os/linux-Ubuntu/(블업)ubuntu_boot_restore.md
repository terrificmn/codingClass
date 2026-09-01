# 트러블슈팅 ubuntu dual booting 우분투 멀티 부팅
물리적으로 디스크가 다를 경우에는 boot loader는 리눅스가 설치되는 하드 디스크에 설치를 해야한다

/dev/sda 에는 windows 10이 설치되어 있고 (C드라이브)  
/dev/sdb 에 리눅스 우분투를 설치했다 (D드라이브)  

> 원래 한 디스크에서 논리적으로 파티션으로 나눠서 할 때에는  
레거시 바이오스 (legacy bios 또는 CSM) 기준으로는 /dev/sda 에 부트 로더를 설치를 해줘야지  
윈도우10과 우분투를 인식을 한다

<br>

하지만 물리적으로 2개의 하드 디스크 (또는 SSD)에서 설치를 할 때에는   
부트로더를 설치하고 있는 하드 디스크로 선택을 해야 한다.

예전에 C드라이브, 즉 /dev/sda (환경에 따라 다를 수 있음)에 Dual boot 했던 것만 생각하고     
설치를 D드라이브 /dev/sdb에다 우분투를 설치하면서 /dev/sda에 (C드라이브)에 부트로더를 설치했던 것이 치명적 실수 였다.   
그래서 부팅이 안되는 문제가 생긴다. 

그래서 C드라이브의 windows 10도 부팅이 안되고, D드라이브 ubuntu도 부팅이 안되는 최악의 경우가 생김 

<br>

## 처음에 리눅스 인스톨이 끝나면 자동 재부팅 될 때 까지는 이상이 없다
그런데 재부팅을 하게 되면은 (C드라이브로 /dev/sda)로 부팅이 되면  
boot rescue 모드가 뜨면서 부팅이 안된다.. ㅋㅋㅋ 망  
```
error: unknwon filesystem.
Entering rescue mode...
grub rescue>
```
이런식으로 나왔던 것 같음 

이럴 때는 우분투를 구운 usb로 다시 부팅을 시도한다  
바이오스에서 F10이나 F12 등을 눌러 (컴퓨터 마다 다르다) usb로 선택을 해줘서 usb로 부팅이 되게 해주자  

try ubuntu 선택한 후 우분투가 켜지면 

터미널을 열고 
```
sudo apt update
sudo add-apt-repository ppa:yannubuntu/boot-repair
```
boot-repair 프로그램을 설치하기 위해서 리포지터리를 추가해준다

완료 되면 설치를 해준다
```
sudo apt install boot-repair
```

실행
```
boot-repair
```

이렇게 되면  
실행 프로그램이 뜨면서 

d 드라이브 (리눅스가 설치된) 가 제거 가능한 디스크 이냐고 물어봄  
그러면 yes를 누른다

<img src=0>
<br>

Recommended repair (repairs most request problems)
를 선택해준다

<img src=1>
<br>

실행이 완료된 후에   
재부팅을 하면 윈도우가 정상적으로 부팅이된다~

대신에 리눅스 부트로더가 설치가 안 되어 있기 때문에 d드라이브 (/dev/sdb) (나의 경우에는)
d 드라이브에 부트로더를 설치할 차례다

<br>

# /dev/sdb에 부트로더 설치 (D 드라이브)
다시 usb로 부팅을 시도한다

try ubuntu 를 선택해서 부팅

터미널을 열고 

```
sudo fdisk -l
```

어떤 장치에 리눅스가 설치되어 있는지 확인

<img src=2>
<br>

위의 사진 처럼~ 각각 /dev/sda 와 /sdb에 윈도우와 리눅스가 잘 설치가 되어 있다~  
부트로더가 제대로 설치가 안되서 부팅이 안 된 것임을 알 수 있다

이제 리눅스가 설치된 디스크에 부트로더를 설치한다. 내 경우는 /dev/sdb이고   
파티션인 /sdb1 에 루트가 설치되어 있는 것이므로 /**sdb1** 파티션을 마운트 해준다

```
sudo mount /dev/sdb1 /mnt
```
를 해서 / 리렉토리를 /mnt 에 마운트 시켜준다. 

부트로더 설치해주기. 
```
sudo grub-install --boot-directory=/mnt/boot /dev/sdb
```
여기에서는 파티션이 아닌 /dev/sdb임에 주의하자~

이제 다시 재부팅을 해준다

이제 /dev/sdb에 (D드라이브)에 부트로더가 설치되었으므로 

컴퓨터가 처음 시작될 때 바이오스 시모스를 들어가야 한다
(예: F10 이나 DEL 바이오스 마다 다름) 그래서 부팅 순서를 D드라이브가 먼저 실행이 되게 해주면 된다

리눅스가 설치된 하드 디스크를 선택해주면 부팅이 잘 되게 된다!
