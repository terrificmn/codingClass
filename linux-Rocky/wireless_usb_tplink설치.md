참고 사이트   
[rtl8192eu-linux](https://github.com/clnhub/rtl8192eu-linux)

무선 usb 와이파이 tp-link TL-WN823N   
300Mbps 미니 무선 N USB 어댑터

Windows, Mac, Linux까지 폭 넓게 지원해서 다행이라 생각했지만..  
Rocky Linux나 Centos 에서는 인식은 하나 wifi 접속을 할 수가 없다   

> 참고로 우분투 20.04 에서는 별다른 설치 없이 wifi 잘 잡힘

기존 TP-link 사이트에서는 리눅스 버전으로는 beta버전만 제공하는데 리눅스 커널이 4.9까지 지원이라고 하는 듯하다.   
물론 실패했다.   

참고-   
**실패 케이스** TP링크 공식 드라이버 다운로드 후 설치 실패,   
rtl8192cu로 시도해봤지만 당연히 안됨  

현재 커널은 5.14가 넘는다. 이거 때문에 안되나?
```
uname -r
```

다른 깃허브등을 참고해서 빌드를 하려고 하다 실패를 해서 안 하고 있다가.. 성공한 방법이다  


## 설치

의존성 패키지 설치 
```
sudo yum groupinstall "Development Tools" && sudo yum install dkms git
```
> development tool는 dnf로는 `sudo dnf groupinstall "C Development Tools and Libraries" ` 

TL-WN823N 무선 와이파이 어댑터는 realtek의 rtl8192eu 드라이버를 사용하므로 깃 클론 후 설치  

먼저 rtl1892eu 를 깃 클론 한다 
```
git clone https://github.com/clnhub/rtl8192eu-linux.git
```
이동
```
cd rtl8192eu-linux/
```

매뉴얼로 설치를 할 수도 있지만 sh 스크립트로 한번에 실행할 수가 있다
```
sudo sh ./install_wifi.sh 
```
> 메뉴얼 설치는 실패했으므로 shell script로 설치하자. 잘 됨


이제 Rocky Linux에서도 무선 와이파이가 잘 된다. 

## 매뉴얼 방식 설치
기존의 설치되어 있다면 지우고 시작
```
sudo rmmod 8192eu
sudo rmmod rtl8xxxu
sudo dkms remove -m rtl8192eu -v 1.0
```

깃 클론 한 후 이동
```
git clone https://github.com/clnhub/rtl8192eu-linux.git
cd rtl8192eu-linux/
```

복사 및 dkms 설치
```
sudo cp -ar . /usr/src/rtl8192eu-1.0
sudo dkms add -m rtl8192eu -v 1.0
sudo dkms install -m rtl8192eu -v 1.0
```
로드
```
sudo modprobe 8192eu
```
> 또는 재부팅하면 되지만.. 오류 없이 설치되는데, 와이파이 인식도 되지만 AP 비번넣고 들어가도 계속 연결 시도하다가 실패한다


## 매뉴얼 방식으로 한 후 실패했을 때 지우기
위의 매뉴얼 설치의 첫 번째 삭제방법처럼 해주자

dkms remove 까지 하면. 아래 메세지를 봤다면 잘 삭제된 것
```
Deleting module rtl8192eu-1.0 completely from the DKMS tree.
```

마지막으로 디렉토리 삭제- /usr/scr/rtl8182eu-1.0 에 설치된 것을 삭제
```
cd /usr/scr
sudo rm -rf rtl8192eu-1.0/
```
