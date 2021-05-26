# dd 명령어
rpi-imager, raspberry imager로 하다가 결국은 실패;;  
micro sd카드에 os를 카피해주는 것은 몇몇 프로그램이 있지만 (Etcher 등)

그냥 터미널에서 수동으로 작업하기로 결정했다!   
에러만 안 나면 이게 더 쉽지!    

CentOS 설치 usb를 만들기 위해서 썼던 그 명령어이다~  
dd 명령어를 이용해서 usb에 설치할 수 있다.

```
dd - convert and copy a file

# Copy a file, converting and formatting according to the operands
```

dd는 UNIX와 리눅스에서 변환하고 복사하는 게 주요 기능이며,    
부팅 설치 디스크를 만들기 위해서 사용하거나,   
하드디스크의 부트섹터를 백업할 때 사용할 수 있다. (그래서 라즈베리파이OS를 백업할 때 다시 사용할 예정)

<br>

# 라즈베리파이 이미지 파일 다운로드 받기
자 이제 본론으로..  
먼저 raspberry os 를 다운로드 받는다.  
https://www.raspberrypi.org/software/operating-systems/#raspberry-pi-os-32-bit

<br>

Raspberry Pi OS with desktop and recommended software 를 다운로드 받음   
용량이 거의 3기가 정도 되는데 다운로드 받은 후
압축을 풀어야한다.   
압축 풀면 8.1G 이므로 용량 주의

먼저 다운받은 곳으로 이동한 후에..
```
$cd Downloads
$unzip 2021-03-04-raspios-buster-armhf-full.zip -d raspberry
```

그리고 나서 micro sd카드를 삽입한 usb 또는 리더기를 컴퓨터에 연결한 후에  
장치 디렉토리를 확인한다
```shell 
$lsblk -p
```
또는 fdisk 로 확인
```shell
$fdisk -l
```

그러면 어떤 장치를 사용하고 있고 어떻게 연결되어 있는지 트리형식으로 확인할 수 있다.

예:
```
NAME                    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
...생략..

/dev/sdd                  8:48   1  28.3G  0 disk 
└─/dev/sdd1               8:49   1  28.3G  0 part /run/media/octa/9016-4EF8
```
32기가 짜리인데 MicroSD 카드인디..   
(작은 글씨로 용량은 다를 수 있다고... 28기가면 너무 오차가 큰거 아니요?!)
어쨌든...ㅋ

리눅스도 usb장치가 연결되자마자 자동으로 mount를 시켜주기 때문에..   
정확히는 File 프로그램으로 (파일 탐색기) usb 인식된 장치? 클릭만 해주면 
바로 마운트가 되기 때문에(권한을 묻기는 한다).. 편함 ㅋㅋ

<br>

어쨋든 lsblk명령어로 확인하면   
/dev/sdd1이 /run/media/octa/9016-4EF8 으로 마운트가 되어 있다.  
여기에서 중요한 것은 (sdd)숫자가 포함된 것이 아니고 **/dev/sdd** 로 사용해야하는 것에 주의해야한다!  

예를 들어 sda 은 아마도 대부분 메인 하드디스크 일테고..     
내 경우에는 sdd, 사용자 환경에 따라 sdb, sdc가 될 수 있다.  

이제 dd명령어로 usb에 먼저 다운받은 라즈베리 img 파일을 카피 할 것이기 때문에    
lsblk 로 장치 디렉토리명을 꼭 확인한다!   
잘못 입력하면 다른 하드디스크의 내용이 지워질 수 있기 때문에 **주의**한다.

이제 마운트를 해제하자. 해제할 때는 숫자도 포함한다 (파티션)
```
$umount /dev/sdd1
```

이제 라즈베리 파이 img 파일 있는 압축푼 디렉토리로 이동한다.  


<br>

# 본격 dd명령어로 카피 하기 (굽기)
이제 dd명령을 사용하는데, 여기에서는 더블체크하면 해보자.  
왜냐하면 /dev/(sd장치명)을 잘못쓰면 데이터가 날라갈 수 있기 때문  

lsblk로 확인한 장치의 디렉토리를 적어준다.

/dev/sdX (X로 표시, 숫자는 제외),    
예: /dev/sdd  또는 /dev/sdc   

dd의 파라미터
- if는 input file로 압축푼 img파일을 입력해준다.
- of는 ouput file 장치 디렉토리를 적어준다
- 위의 2개의 파라미터는 상황에 따라 바뀔 수 있다. (예: img파일로 내보내기를 할때)

이제 압축이 풀린 디렉토리로 이동 후 아래와 같이 입력
```shell
cd ~/Downloads/raspberry
sudo dd if=2021-03-04-raspios-buster-armhf-full.img of=/dev/sdd bs=4M conv=fsync status=progress
```
status파라미터는 꼭 넣어주자, 안 쓰게 되면 아무런 표시가 안되서 답답할 수 있다.  
시간이 꽤 걸리므로 같이 입력하는 것을 추천!

<br>

완료가 되면~  
파일 브라우저로 확인해 보면  
/boot 와 /rootfs 파티션이 생겨있다~  

만약 mount가 되어 있다면 다시 umount 시켜주고   
MicroSD카드를 분리해서 라즈베리 파이에 꽂아준다!

그리고 5핀 전원을 연결해주면 LED가 들어오며 부팅이 된다!

<br>

# 부록 백업하기
이것도 역시 dd명령어를 사용해서 of만 output파일명.img 파일로 내보낼 수 있다.

usb에 micro sd카드를 넣어서 컴퓨터에 연결한 후에
```
liblk -p
```

파티션정보를 확인한다.
자동으로 마운트가 되었다면 umount 해준다  
(마운트 경로는 환경에 따라 다를 수 있다.)
예:
```
$umount /run/media/octa/rootfs
$umount /run/media/octa/boot

```

if= input file은 장치로 지정해준다. 파티션 숫자는 빼준다. 예를 들어 /dev/sdd  
of= ouput file은 저정할 파일명.img로 지정

dd로 라즈베리파이를 설치할 때와는 반대이다. 
파일을 저장할 곳으로 이동한다. 그 위치에서 백업파일이 저장된다. 또는 절대경로를 지정해준다.

```
$cd test-backup
$sudo dd if=/dev/sdd of=sdcard-backup.img status=progress
```

당연한 것 이겠지만, 장치를 더블체크하고, if= of=가 바뀌는 순간 돌이킬 수 없게될 수도 있다.  
천천히 하자! 서두를 필요없다.

궁금하니깐 잘되는지 보기위해서 새로운 터미널을 열고  
test-backup 디렉토리로 가서 ls -l로 확인하면   
sdcard-backup.img 파일이 만들어 지고 있다.

용량이 무지막지하다.. 처음에 raspberrypi를 설치한 것보다 용량이 불어있다..;;

일단 용량이 너무 커서;;; 20GB가 나왔다;;
압축을 시키면 확 줄어들것 같기는 하지만...

오늘은 여기까지! 용량 부족하다고 워닝 메세지가 뜬다..ㅋㅋㅋ ㅠㅠ

