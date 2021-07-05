# 우분투를 설치하다!
우분투로 리눅스 실습을 할 때에도 centos로도 거분히 대응이 되었고~

AWS는 강사님의 추천에 따라 서버에 ubuntu 18.04로 설치를 해놓았지만
집에서는 centos 를 사용하고 서버환경은 우분투이기 때문에 (같은 리눅스 이지만 ㅋ)
이렇게 개발환경이 달라서 고민했던 부분에서 docker로 해결했었다

그래서 ROS를 본격적으로 할 때에도 
신기하게도😚 그 전에 삽질(?)을 많이 해 놓은 덕에 ROS도 docker를 이용해서 했었기에 
내 컴에 우분투를 설치를 할 필요까지는 없는 듯 했다.

하지만 ROS는 아무래도 우분투에 최적화가 되어있기 때문에 
결국 우분투를 내 PC에 설치하게 되었는데, 설치를 시작하자마자 별 희한한 문제를 다 겪고~   
우분투도 꽤 많이 설치를 해보았는데도 속수무책이였다 ㅋㅋ 😭

<br/>

# 키보드가 작동을 안해! 😡
우분투 부팅 USB를 만든 다음에 설치를 시작할려고 했다~~  
설치 프로그램이 시작되면서 첫 화면 즉, 사용자 언어를 고르고 install ubuntu를 클릭해야하는 화면에서
마우스, 키보드 둘 다 작동을 하지 않는다. 

USB 몇번이 다시 굽고 ㅋ 그래서 USB 자체가 문제인 줄 알고 다른 USB도 사용해 보고  

참 검색도 많이 했지만, 
USB 3.0 포트에 껴보란 말도 있었고, USB 허브를 통해서도 해보고, 다른 마우스를 가져가다 껴보기도 하고
소용이 없다. 😭

정말 빨리 지나가는 메세지가 있었는데 사진을 찍어봤더니 (빨라서 읽을 수가 없었음ㅠ)

```
usb 2-4: device descriptor read/64, error -32
usb 7-3: device descriptor read/64, error -32
usb 2-4: device descriptor read/64, error -32
... 생략
usb 2-4: device not accepting address 4, error -32
usb 7-3: device not accepting address 4, error -32
usb 2-4: device not accepting address 5, error -32
usb usb2-port4: unable to enumerate USB device
```

이런 메세지 였고, 문제를 찾아보니  
USB에서 잘못된 신호를 주거나, 전류가 많이 흐르거나? 뭐 그래서 그런다고 한다.  

그럼 하드웨어 문제인듯했는데, 
원래 있던 centos 부팅 usb를 넣고 진행을 하니~ 설치 화면이 잘 뜨고 키보드 마우스 다 사용이 가능했다.

완전 하드웨어 문제는 아닌거에는 확실했지만 우분투가 뭐 그렇게 되어있나보다

어쨌든 이 방법 저 방법으로 재부팅만 수십번 했을까?
그러던 중에 ubuntu 포럼에서 옛날 글을 발견했다 2013년 7월에 작성된 글이었는데

우분투 13버전 쯤 되겠다. 다른 사람들이 마우스를 ps/2 방식으로 해봐다 다른키보드를 해봐라 하고 있을 때

어떤 사람이 말그대로 'magic' BIOS 옵션 IOMMU Controller를 Enabled 시키면 키보드 사용이 가능하다는 것이였다

> In case of Gigabyte 970A-UD3, the "magic" BIOS option is "IOMMU Controller". Set it to "Enabled" and your keyboard will work (didn't tried mouse yet). Good luck!

이런 대단 하신분 🤩

<br/>

## 바이오스에서 IOMMU를 활성화 해주세요
그러고 보니 정확한 모델명은 모르겠으나 기가바이트 메인보드를 사용하고 있었고 내 컴이 오래되서 그렇구나 했다 ㅠㅠ

아무튼 부팅 시 DEL키를 눌러서 바이오스에 진입 후 

IOMMU를 Enabled 시켜주면 된다

<img src=0>
<br/>

"magic" 이라고 한 것 처럼, 진짜 키보드가 사용이 된다.

<br/>

# 또 다른 문제가 발생
여기서 또 문제가 있는게 설치가 완료된 후 재부팅을 하면 이게 멈춰서 실행이 안된다

이번에는 다시 바이오스에 들어가서 IOMMU를 disabled를 시켜준다
이제 우분투로 잘 들어가진다.

필요한 프로그램들을 설치하고 하다가 보니, usb를 인식을 못한다. 하하하 🤬 
키보드, 마우스는 인식하지만 다른 usb 저장장치는 아예 인식이 안된다

```
$lsusb
```
를 해봐도 전혀 변화가 없다. 

이거에 대한 해결책은 grub를 건들여야 한다

다시 재부팅을 한 후에 *Ubuntu를 선택하는 화면이 나오는데 거기에서 e 버튼을 눌러준다

<img src=1>
<br/>

그러면 부팅에 문제가 생겼을 때 해결하기 위한 입력창(?)이 나오는데
여기에서 linux /boot/vmlinuz-5.4.0-42- 로 시작하는 부분이 있다. 아래에서 2번째

<img src=2>
<br/>

거기의 마지막으로 커서를 옮겨서 (키보드의 End를 눌러서 제일 마지막 줄로 가자)
한칸 띄고 iommu=soft 적고

이런식이 된다
```
linux /boot/vmlinuz-5.4.0-42- ....생략... splash $vt_handoff iommu=soft
```

그리고 ctrl+x 로 눌러서 부팅을 한다

재부팅이 된 후 usb스틱을 연결하니 잘 인식한다~

<br/>

## 이제 grub-update를 해서 아예 고정시키기
이제 잘 되는 것을 확인했으니 grub-update를 해줘야한다. 위에서 부트메뉴에서 한 것은 일회용이기 때문이다

먼저 백업을 해주자! 그리고 이 방법은 MBR(Bios-based) system에 해당한다고 한다~ (Legacy Bios용)

```
$sudo cp /etc/default/grub /etc/default/grub-backup
$sudo cp /boot/grub/grub.cfg /boot/grub/grub.cfg-backup
```
그 다음 /etc/default/grub 파일을 열어준다 GRUB_CMDLINE_LINUX= 부분의 마지막에 추가해준다
" " 쌍따옴표로 되어있으므로 그 안에다가 입력하자

```
$ sudo vi /etc/default/grub
```

대충 아래처럼 수정해 준다
```
GRUB_CMDLINE_LINUX="iommu=soft"
```
: 누른후 wq 로 빠져나온다

다음은 새로운 grub.cfg 파일을 생성해 줘야한다. 거의 다 왔다 ㅋㅋ
```
$ sudo grub-mkconfig -o /boot/grub2/grub.cfg
```
그러면 뭔가 진행이 되고 
done이라고 끝남. 이제 재부팅을 해도 따로 입력할 필요도 없고 usb 인식도 문제가 없다

> 혹시 AMD라데온 그래픽 카드를 사용한다면 듀얼모니터가 안되는 경우라면  
그럴때에는 위의 GRUB_CMDLINE_LINUX="amdgpu.dc=0" 라고 해주면 2개의 모니터를 사용할 수 있다
사실 이것도 아주~예전에 엄청 고생해서 찾았던 것인데, centos나 ubuntu나 모니터 2개를 인식 못하는 것은 똑같다


