# 포스팅 update 예정

# 우분투 멀티 부팅 만들기
한개의 하드 디스크에서 나누는 방법입니다~ 그리고 legacy Bios 방식이며 MBR 방식입니다. 참고하세요~

> UEFI는 새로운 방식의 boot mode 이며, 64비트 system에 사용됩니다. Legach Bios는 예전 부터 있던
전통방식의 boot mode 입니다.(32/64bit 지원). 

<br>

Fedora가 34 나왔다고 해서 설치를 해보고 싶었는데, 설치가능한 usb로 만들어서 
실행해보니~ 오 괜찮네! 뭔가 좋으다좋으다~ ㅋㅋ

하지만 멀티 부팅을 할려고 하는데 인스톨 하는 부분에서 부트로더에 대해서 나오지를 않아서
설치를 하려다가 포기해버렸다. ㅋㅋ

내컴이 아니라 학교 컴에다가 테스트를 해보는 것이었기 때문에 

하지만 우분투에서는 부트로더 설치하는 부분이 잘 나와서 설치하는데 어렵지 않았다.
물론 잘 못 설치하면 windows가 날라가겠구나 하는 약간 쫄리는 맘이 있었지만 ㅋㅋ

# 먼저 windows 바이오스 상태 확인하기
명령어로 확인하는 방법은 시작 버튼을 누르고 cmd 검색  
프로그램이 나오면 마우스 오른쪽으로 관리자 권한으로 실행을 시킨다

그 다음에 
```
bcdedit
```
그러면 Windows Boot Manager , Windows Boot Loader 정보가 나오는데 Windows Boot Loader를 보자
그 중 path 부분을 보면 됨

```
Windows Boot Loader
-------------------
identifier              {current}
device                  partition=C:
path                    \WINDOWS\system32\winload.exe
description             windows 10
...
생략...
```
위처럼 path부분이 \WINDOWS\system32\winload.exe **exe** 파일로 나온다면, legacy BIOS 이다

만약, \WINDOWS\system32\winload.efi 라고 나오면 UEFI 모드이다.

다른 방법으로 쉽게 체크할 수 있는 방법은 
윈도우의 시스템 정보를 확인하는 방법이다.
system information에 BIOS Mode가 legacy 또는 UEFI 인지 확인해보자

<img src=>
<br>

<br>

# 먼저 설치가능한 usb를 만들자
4GB 이상의 usb가 있어야 한다. 
[우분투 웹사이트 -이미지 다운로드](https://ubuntu.com/download/desktop)

20.04 LTS 버전을 다운로드 받는다. 

이미지 파일을 굽는건 rufus로 쉽게할 수 있다.

[설치가능 usb만들기: rufus 다운받기](https://rufus.ie/en_US/)

usb을 컴퓨터에 연결 시키고 rufus를 실행시키면
Device 부분을 usb 장치 연결한 드라이브를 선택해주면 된다.

그리고 Boot selection 부분은 우분투 이미지 파일을 받은 iso 파일을 선택해준다

위에서 말한대로 Legacy Bios이기때문에 Partition scheme은 MBR로 선택하고  
Target system은 BIOS or UEFI 로 선택해준다

다른 것은 건드릴 필요 없고, start 버튼을 눌러서 실행이 되게 하자


# 하드디스크 볼륨 축소시키기
하나의 하드 디스크를 가지고 멀티 부팅을 만드는 것 이기 때문에 
디스크를 파티션을 나눠야한다.

먼저 윈도우즈 시작 버튼 위에서 마우스 오른쪽 버튼을 눌러서 디스크 관리를 실행 시켜준다

C드라이브를 선택하면 C드라이브가 빗살무늬가 들어가지면서 선택이 된다.
이제 마우스 오른쪽 버튼을 누르고 볼륨 축소를 누르자

<img src=> 이미지 꽤 들어갈 듯..
<br>

<br>

# 부팅을 시도
usb가 컴퓨터에 꽂혀있는 상태에서 컴퓨터를 켜자~

컴퓨터 BIOS에 따라 다른데, F10, DEL 키 등.. F9 등의 키를 이용해서 부트 순서 정하는 메뉴로 들어가야한다

처음 컴퓨터를 켜자마자 위의 해당 단축키를 눌러준다
그러면 boot 장치 선택화면이 나오게 되고 여기에서 usb를 선택해줘야 한다.

(컴퓨터에 따라 다르므로 처음 나오는 화면을 보고 검색해보는게 좋다)

<img src=>

# 이제 ubuntu install을 선택하고나서 설치를 진행하면 된다.
순서대로 클릭클릭을 눌러주고 
installation type에서 something else를 눌러준다

이제 여기에서 중요
/dev/sda 장치가 보이고
    /dev/sda1 ntfs
    /dev/sda2 nfts 
라고 나오면 윈도우10이 설치된 파티션이 보이게 되고   

그 아래로 
free space 라는 부분이 보이게 될 것이다. (위치는 다를 수 있음)
free space가 윈도우즈에서 불륨 축소로 만들어진 용량인지 확인
그러면 이 불룜 축소 했던 파티션에 리눅스를 설치할 것이다!

free space를 더블클릭 또는 + 버튼을 눌러준다

조금 어렵게 가려면 swap, /home, /boot 디렉토리까지 파티션을 나눌 수 있지만
쉽게 / (root 디렉토리)만 만들자

용량은 그대로 두고, Type of the new partition 부분은 Logical로 
왜냐하면 파티션을 논리적으로 나눴기 때문에, (하드디스크는 하나)

Location for the new partition은 Begining of this space로 그대로 두고

Use as 를 Ext4 journaling file system으로 선택해준다. 
리눅스의 파일 시스템이다

그리고 Mount point는 / 를 선택해준다

그리고 중요한 부트로더는 
Device for boot loader installation은 
/dev/sda 가장 상위 장치명으로 선택해준다. 즉, sda1, sda2 같은 파티션이 아닌 장치명을 선택해줘야한다

Legacy Bios에서는 이렇게 해줘야지 dual booting (멀티부팅)이 잘 되게 된다.
즉, 처음에 윈도우, 리눅스를 선택할 수 있게 된다.

<img scr=>
이미지도 꽤 있음

그리고 다음다음 설치를 진행한다

<br>

# 이제 설치가 진행 트러블 슈팅하기
설치가 완료가 되면 자동 재부팅이 된다. 
이때 usb를 제거해 주면 된다

그리고 나서 다시 윈도우즈10으로도 잘 되나 보려고 하면 
윈도우즈 선택하는 것 없이 바로 리눅스 우분투로 실행이 되 버린다.

간단하게 fdisk -l 로 확인한 후 
장치가 잘 있는 것 확인

이제 update-grub를 실행해준다
이제 부트로더가 업데이트가 되었고, 재부팅을 할 시에 windows10이 잘 보이게 된다.
