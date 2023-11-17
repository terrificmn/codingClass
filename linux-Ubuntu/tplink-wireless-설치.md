# tplink

archer 

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


