# 우분투 멀티 부팅 만들기 (하나의 디스크에 파티션 나누기)
한개의 하드 디스크에서 나누는 방법입니다~ 그리고 legacy Bios 방식이며 MBR 방식입니다. 참고하세요~

> UEFI는 새로운 방식의 boot mode 이며, 64비트 system에 사용됩니다. Legach Bios는 예전 부터 있던
전통방식의 boot mode 입니다.(32/64bit 지원). 

<br>

Fedora가 34 나왔다고 해서 설치를 해보고 싶었는데, 설치가능한 usb로 만들어서 
실행해보니~    
오 괜찮네! 뭔가 좋으다좋으다~ ㅋㅋ

<img src=0>
<br>

하지만 멀티 부팅을 할려고 하는데 인스톨 하는 부분에서 부트로더에 대해서 나오지를 않아서
설치를 하려다가 포기해버렸다. ㅠㅠ 
그놈 40버전이라고 하는데 아쉽다 ㅋㅋ

내컴이 아니라 학교 컴에다가 테스트를 해보는 것이었기 때문에 
어쩔 수 없이 우분투로 설치하기로

우분투에서는 부트로더 설치하는 부분이 잘 나와서 다행이었다  
물론 잘못 설치하면 windows가 날라가겠구나 하는 약간 쫄리는 맘이 있었지만 ㅋㅋ

<br> 

# 먼저 windows 바이오스 상태 확인하기
가장 먼저 windows10 에서 현재 바이오스가 어떤 것을 사용하고 있는지 확인해야 합니다  

명령어로 확인하는 방법은 시작 버튼을 누르고 cmd 타이핑해서 검색  
프로그램이 나오면 마우스 오른쪽을 누르고 관리자 권한으로 실행을 시킨다

터미널이 열리면 아래 명령어를 실행
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


<br>

# 먼저 설치가능한 usb를 만들자
4GB 이상의 usb가 있어야 한다.   
[우분투 웹사이트 -이미지 다운로드](https://ubuntu.com/download/desktop)

20.04 LTS 버전을 다운로드 받는다. 

이미지 파일을 굽는건 rufus로 쉽게할 수 있다.  
[설치가능 usb만들기: rufus 다운받기](https://rufus.ie/en_US/)

usb을 컴퓨터에 연결 시키고 rufus를 실행시키면
장치(Device) 부분을 usb 장치 연결한 드라이브를 선택해주면 된다.  
(기존 usb의 데이터가 다 **지워지므로** 장치 선택을 잘 해야함)

그리고 부트 선택(Boot selection) 부분은 선택 버튼을 클릭해서 다운받은 우분투 이미지 파일을 iso 파일을 선택해주면 된다

<img src=1>
<br>

위에서 말한대로 Legacy Bios이기때문에 Partition scheme은 MBR로 선택하고  
Target system은 BIOS or UEFI 로 선택해준다

다른 것은 건드릴 필요 없고, 시작(start) 버튼을 눌러서 실행이 되게 하자

<br>

# 하드디스크 볼륨 축소시키기
하나의 하드 디스크를 가지고 멀티 부팅을 만드는 것 이기 때문에 
디스크의 파티션을 나눠야한다.

먼저 윈도우즈 시작 버튼 위에서 마우스 오른쪽 버튼을 눌러서 디스크 관리를 실행 시켜준다

C드라이브를 선택하면 C드라이브가 빗살무늬가 들어가지면서 선택이 된다.

<img src=2>
<br>

이제 마우스 오른쪽 버튼을 누르고 볼륨 축소를 누르자

<img src=3>
<br>

이제 축소할 공간 입력(MB)로 입력해준다. 대충 10,000(MB) 당 약 10기가 정도라고 생각하면 된다.

<img src=4>
<br>

축소 버튼을 누르면 아래 사진 처럼 할당되지 않은 상태로 공간이 만들어 진다

<img src=5>
<br>

만약 공간 분할을 다시 하고 싶으면  
기존 C드라이브를 선택하고 볼륨 확장을 선택해주면 된다

<img src=6>
<br>

<img src=7>
<br>

<img src=8>
<br>

이제 창을 닫고 재부팅을 하자

<br>

# 부팅을 시도
usb가 컴퓨터에 꽂혀있는 상태에서 컴퓨터를 켜자~

컴퓨터 BIOS에 따라 다른데, F10, DEL 키 등.. F9 등의 키를 이용해서 부트 순서 정하는 메뉴로 들어가야한다

내 컴의 경우는 F12를 누르면 boot menu로 들어가진다

<img src=9>
<br>

<img src=10>
<br>

아래와 같은 화면에서 USB를 선택해주면된다.

아래는 삼성 컴퓨터의 BIOS, 여기서는 F10을 눌렀다

<img src=11>
<br>

위에서 usb를 선택하고 엔터를 누르면 바로 USB로 재부팅이 된다

만약 부팅 순서를 셋업 메뉴 진입을 누르고 (Enter Setup)

부팅 탭에서 -> 부팅 순위 정하기를 누르고

<img src=12>
<br>

화면의 안내에 따라서 순서를 바꿔주면 된다. 여기에서는 (삼성) 기준으로는
F6,F5키로 순서를 바꿈, page up, page down인 BIOS도 있고 조금씩 다르지만 비슷하니 잘 적응해서 진행하자  

<img src=13>
<br>

마지막으로 종료 탭에서 변경된 내용을 저장하고 종료를 선택해서 나가면 된다

<br>

# 이제 ubuntu install을 선택하고나서 설치를 진행하면 된다.
usb로 설치가 진행되면 ubuntu install을 선택해주고  

우분투 화면이 뜨면 오른쪽의 install ubuntu를 선택해준다

<img src=14>
<br>

순서대로 클릭클릭을 눌러주고 
installation type에서 something else를 눌러준다

<img src=15>
<br>

이제 여기에서 중요  
/dev/sda 장치가 보이고  
    /dev/sda1 ntfs  
    /dev/sda2 nfts   
라고 나오면 윈도우10이 설치된 파티션이 보이게 되고     

그 아래로 free space 라는 부분이 보이게 될 것이다. (위치는 다를 수 있음)

<img src=16>
<br>

free space가 윈도우즈에서 불륨 축소로 만들어진 용량인지 확인  
그러면 이 불룜 축소 했던 파티션에 리눅스를 설치할 것이다!

free space를 더블클릭 또는 + 버튼을 눌러준다

<img src=17>
<br>

이제 파티션을 생성하는데  
아래처럼 만들어 주면 된다. logical, Ext4 file system   
Mount point는 / 가 되게 해준다

<img src=18>
<br>

용량은 그대로 두고,  
Location for the new partition은 Begining of this space로 그대로  
Type of the new partition 부분은 Logical로   

Use as 를 Ext4 journaling file system으로 선택해준다.  
리눅스의 파일 시스템이다

만약 세부적으로 나누려면 swap 영역도 만들 수 있고  
/home 디렉토리까지 파티션을 나눌 수 있다.  

swap은 Use as 는 swap영역으로 만들어 주면 되고   
/와 home과 파티션은 용량을 잘 분배해서 만들어 주면 된다. (type은 logical)  

하지만 **쉽게 /만 만들어서** 진행했다

그리고 중요한 부트로더는 
Device for boot loader installation은 
/dev/sda 가장 상위 장치명으로 선택해준다.   
즉, sda1, sda2 같은 파티션이 **아닌** 장치명을 선택해줘야한다

<img src=19>
<br>

자신의 **/dev/sda** 즉 C드라이브의 메이커 및 용량이 나오는 것을 선택해준다.
그리고 이 부분은 legacy Bios에 해당하는 부트로더 선택이다.

이렇게 해줘야지 dual booting (멀티부팅)이 잘 되게 된다.   
즉, 처음에 컴퓨터를 켜면 윈도우, 리눅스를 선택할 수 있게 된다.

>UEFI는 /dev/sda1 처럼 특정 windows UEFI 부트로더가 있는 파티션을 선택해줘야하는데  
만약 UEFI면 좀 더 검색을 해보자

<br>

리눅스가 설치된 / 파티션이 체크가 들어와 있는지 잘 확인하고   
해당 파티션에   
Install now 버튼을 눌러서 설치를 진행하자

<br>

아래와 같은 경고가 뜰 수도 있으나, 살짝 무시해주자

<img src=20>
<br>

UEFI 시스템일 경우에는 안 된다는 메세지임


# 설치 완료 후 윈도우 선택이 안될 때
grub를 업데이트를 해야합니다~

[여기를 참고하세요](/blog/)
