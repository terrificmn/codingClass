물리적으로 디스크가 다를 경우네는 boot loader는 리눅스가 설치되는 디스크에 설치를 해야한다

daul boot를 생각하고 다른 디스크에 설치한게 치명적 실수 였다

/dev/sda 에는 windows 10이 설치되어 있고
/dev/sdb 에 리눅스 우분투를 설치했다

그런데 boot loader를 /dev/sda에 설치를 했다
이유는 착각을 함;; ㅠ

원래 한 디스크에서 논리적으로 파티션으로 나눠서 할 때에는 
레거시 바이오스 (legacy bios)에서는 /dev/sda 에 부트 로더를 설치를 해줘야지 
윈도우10과 우분투를 인식을 한다

그런데 치명적으로 실수를 물리적으로 다른 디스크에 설치 (예컨대 d드라이브)에 설치를 하면서 c드라이브에 부트로더를 설치한 셈이다;;

물론 리눅스 인스톨이 끝나면 자동 재부팅 될 때 까지는 이상이 없다

그런데 재부팅을 하게 되면은 (C드라이브로 /dev/sda)로 부팅이 되면 
boot rescue 모드가 뜨면서 부팅이 안된다.. ㅋㅋㅋ 망

이럴 때는 우분투를 구운 usb로 다시 부팅을 시도한다
바이오스에서 usb를 먼저 선택하게 해주고 
부팅을 해서 

try ubuntu 인가를 선택한 후 부팅
그리고 우분투가 켜지면 

터미널을 열고 
```
sudo apt update
sudo add-apt-repository ppa:yannubuntu/boot-repair
```
리포지터리를 추가해준다

```
sudo apt install boot-repair
```
설치 완료 되면 실행

```
boot-repair
```

이렇게 되면 
실행 프로그램이 뜨면서 
d 드라이브 (리눅스가 설치된) 가 제거 가능한 디스크 이냐고 물어봄
그러면 yes를 누른다
Recommended repair (repairs most request problems)
를 선택해준다

이제 다시 재부팅을 하면 윈도우가 정상적으로 부팅이된다~

대신에 리눅스 부트로더가 설치가 안되어 있기 때문에 d드라이브 (/dev/sdb) (나의 경우에는)
d 드라이브에 부트로더를 설치할 차례다

# 부트로더 설치
다시 usb로 부팅을 시도한다

try ubuntu ... 어쩌구로 부팅

이제 부팅이 되면
터미널을 열고 

```
sudo fdisk -l
```

어떤 장치에 리눅스가 설치되어 있는지 확인

그다음에 그 장치에 (디스크)에 부트로더를 설치한다 


```
sudo mount /dev/sdb1 /mnt
```
를 해서 / 리렉토리를 /mnt 에 마운트 시켜준다

```
sudo grub-install --boot-directory=/mnt/boot /dev/sdb
```
로 부트로더 설치해주기

이제 다시 재부팅을 해준다

이제 bios가 시작될 때 F10 이나 DEL 바이오스 마다 다름
눌러서 리눅스가 설치된 하드 디스크를 선택해주면 부팅이 잘 된다
