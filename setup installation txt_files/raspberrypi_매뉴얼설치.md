# 매뉴얼 설치
rpi-imager, raspberry imager로 하다가 결국은 실패;;
micro sd카드에 os를 카피해주는 것은 몇몇 프로그램이 있지만 (Etcher 등)

그냥 터미널에서 수동으로 작업하기로 결정! 에러만 안나면 이게 더 쉽지!
dd 명령어를 이용해서 usb에 설치할 수 있다.

먼저 raspberry os 를 다운로드 받는다.  
https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit

<br>

Raspberry Pi OS with desktop and recommended software 를 다운로드 받음   
용량이 거의 3기가 정도 되는데 다운로드 받은 후
압축을 풀어야한다.   
압축 풀면 8.1G 이므로 용량 주의

```
$cd Downloads
$unzip 2021-03-04-raspios-buster-armhf-full.zip -d raspberry
```

그리고 나서 micro sd카드를 삽입한 usb 또는 리더기를 컴퓨터에 연결하고  
장치 디렉토리를 확인한다
``` 
lsblk -p
```

그러면 어떤 장치를 사용하고 있고 어떻게 연결되어 있는지 트리형식으로 확인할 수 있다.

예:
```
NAME                    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
/dev/sdd                  8:48   1  28.3G  0 disk 
└─/dev/sdd1               8:49   1  28.3G  0 part /run/media/octa/9016-4EF8
```
32기가 짜리인데.. (작은 글씨로 용량을 다를 수 있다고... 28기가면 너무 오차가 큰거 아니요?!)
어쨌든...

리눅스도 usb장치가 연결되자마자 자동으로 mount를 시켜주기 때문에.. 
정확히는 File 프로그램으로 (파일 탐색기) usb 인식된 곳을 클릭만 해주면 
바로 마운트가 되기 때문에.. 편함 ㅋㅋ

<br>

어쨋든 lsblk명령어로 확인하면   
/dev/sdd1이 /run/media/octa/9016-4EF8 으로 마운트가 되어 있다.
여기에서 중요한 것은 장치 숫자가 포함된 것이 아니고 /dev/sdd 로 사용해야하는 것에 주의한다!

예를 들어 sda 은 아마도 메인 하드디스크 일테고..   
이제 dd명령어로 usb에 먼저 다운받은 라즈베리 os를 카피 할 것이기 때문에  
lsblk 로 장치 디렉토리명을 꼭 확인한다!   
잘못 입력하면 다른 하드디스크의 내용이 지워질 수 있기 때문에 주의한다.

이제 마운트를 해제하자
```
$umount /dev/sdd1
```

이제 라즈베리 파이 img 파일 있는 압축푼 디렉토리로 이동한다.  
그리고 나서 dd명령을 사용, 여기에서 주의!

<br>
서두르지 말고 천천히 확인하면 할 것!  
/dev/sd알파벳 (숫자는 제외), lsblk로 확인한 장치의 디렉토리를 적어준다
예: /dev/sdd  또는 /dev/sdc 

```
cd ~/Downloads/raspberry
sudo dd if=2021-03-04-raspios-buster-armhf-full.img of=dev/sdd bs=4M conv=fsync status=progress
```
*간단한 설명:  
- if는 input file로 압축푼 img파일을 입력
- of는 ouput file 장치 디렉토리를 적어준다

<br>

완료가 되면
/boot , /rootfs 파티션이 생기고..
만약 mount가 되어 있다면 다시 umount 시켜주고   
sd카드를 분리해서 라즈베리 파이에 꽂아준다!

그리고 5핀 전원을 연결해주면 LED가 들어오며 부팅이 된다!


# 부록 백업하기
이것도 역시 dd명령어를 사용해서 of만 output파일명.img 파일로 내보낼 수 있다.
먼저 적당한 곳으로 이동
```
$cd Download
```

usb에 micro sd카드를 넣어서 컴퓨터에 연결한 후에
```
liblk -p
```

파티션정보를 확인한다.
자동으로 마운트가 되었다면 umount 해준다
예:
```
$umount /run/media/sgtocta/rootfs
$umount /run/media/sgtocta/boot

```

dd로 설치할 때와는 반대이다. 

if inputfile은 장치로 지정해준다. 파티션 숫자는 빼준다. 예를 들어 /dev/sdd  

개인적으로 sudo를 빼고 하는 편이다. 그러다가 명령어가 권한 때문에 제대로 실행이 안되기도 하고  
확실히지면은 home키와 키보드 화살표 를 이용해서 sudo를 나중에 적어주는 편이다.

아.. 그리고
status를 빼먹으면 아무런 표시가 되지 않는다. 꼭 써주도록 하자.

```
$sudo dd if=/dev/sdd of=sdcard-backup.img status=progress
```

당연한 것 이겠지만, 장치를 더블체크하고, if= of=가 바뀌는 순간 돌이킬 수 없게될 수도 있다.
천천히 하자! 서두를 필요없다.


궁금하니깐 잘되는지 보기위해서 새로운 터미널을 열어서 Downloads 디렉토리로 가보면
ls 로 확인하면 파일이 sdcard-backup.img 파일이 만들어 지고 있다.

용량이 무지막지하다.. 당연히도 처음에 raspberrypi를 설치한 것보다 용량이 불어있다..;;

일단 용량이 너무 커서;;; 20GB가 나왔다;;
압축을 시키면 확 줄어들것 같기는 하지만...
일단 백업을 하는 방법만 알아보기로 해야겠다;;

용량이 없어서 지웠음..;; 다른 하드디스크에 백업을 해봐야겠다;
아니면 다른 방법을 ..




