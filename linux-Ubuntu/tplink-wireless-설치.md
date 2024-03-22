# tplink

TPlink archer T2U 무선랜 와이파이 USB 어댑터   

RTL8812AU 칩셋 사용

https://community.tp-link.com/en/smart-home/forum/topic/655330

> official 드라이버가 없으나, 아래로 설치는 가능하나, ... 
단점으로는 kernel 유지보수자는 커널의 802.11 stack을 사용하기를 원하지만, 자체적으로 802.11 stack 을 따로 가지고 있다고 하며,     
중복된 코드, 버그 등이 있을 수 있으며,   
Realtek drivers의 코드 등이 중복되어 있고, 많은 코드가 중복이 되어 있다고 함   

하지만, 아래의 내용을 통해서 TPlink의 wifi usb 어댑터를 인식 시킬 수 있고   
사용도 잘 된다. 
(아주 가끔 끊기는 경우가 생기는데... 버그일지는 모르겠음)  

dkms 관련 및 현재 커널에 대한 headers 등을 설치해준다.  

```
sudo apt install dkms
sudo apt install build-essential libelf-dev linux-headers-$(uname -r)
```

rtl8812au 깃 클론
```
git clone https://github.com/aircrack-ng/rtl8812au.git
```

이동 후 
```
cd rtl8812au/
```

빌드 하기
```
sudo make dkms_install 
```

이후 secure boot이 enable 되어 있어 사용해야 한다고 하면, 비밀번호를 입력해주고 (2번)  
**잘 기억해준다**

이후 재부팅을 하고 나서  
부팅 전에 secure boot 관련 선택 화면이 나오는데 

그냥 continue boot 를 누르면 **안됨**  

**Enroll MOK** 를 눌러준다 
이후 키에 대한 것을 볼 수도 있고, 등록하기 비슷한 것이 있다..(정확히 기억이 안남;;)  

그러면 비밀번호를 물어본다. 입력해 주면 된다..


## 문제 발생 시 삭제 
```
sudo dkms remove -m 8812au -v 5.6.4.2_35491.20191025 --all
```

> -m 옵션 후 탭, -v 옵션 후 탭 해주면 좋다(자동완성 이용)


