# iwd build
기존의 우분투의 iwd stable 버전은 너무 낮다. 1.2  로밍을 안하고 제자리에서 사용한다면 문제 없지만,  
Wi-Fi 로밍을 적극적으로 사용할 경우에는 해당 버전은 너무 예전 버전이서 로밍 기능을 실행하지 못함  

의존성 설치
```
sudo apt update
sudo apt install -y git build-essential pkg-config python3-docutils \
                     libdbus-1-dev libreadline-dev automake libtool
```

ell 라이브러리 필요
```
git clone https://git.kernel.org/pub/scm/libs/ell/ell.git
cd ell
./bootstrap
./configure --prefix=/usr
make
sudo make install
cd ..
```

ell 이 빌드가 되었다면 iwd 클론 하고 아래 내용을 따른다. (빌드한 ell 를 사용하게 해서 빌드를 해준다.)

(Note: Using --enable-library without --enable-external-ell tells iwd to use the version of ELL bundled in its own source tree.)

iwd 깃 클론
```
git clone https://git.kernel.org/pub/scm/network/wireless/iwd.git
cd iwd
./bootstrap
./configure --prefix=/usr \
            --sysconfdir=/etc \
            --localstatedir=/var \
            --enable-external-ell
```
여기에서 extenal-ell 대신에 --enable-library 로 해준다. 
```
./configure --prefix=/usr --enable-library
make
sudo make install
```
이렇게 하면 빌드가 된다. 


*참고 여기에서 ell 빌드 및 --nable-library 를 하는 이유는*  
*그냥 빌드 할 때에 ell 를 찾지 못하는 컴파일 에러가 발생하기 때문.*   
```
 CC       monitor/nlmon.o
client/station-debug.c:2:10: fatal error: ell/useful.h: No such file or directory
    2 | #include "ell/useful.h"
      |          ^~~~~~~~~~~~~~
compilation terminated.
src/band.c:29:10: fatal error: ell/useful.h: No such file or directory
   29 | #include "ell/useful.h"
      |          ^~~~~~~~~~~~~~
```

최종 iwd 깃 정보 
```
commit d003d0e593323b3de427f01284ede81ba61e9dcc (HEAD -> master, tag: 3.12, origin/master, origin/HEAD)
Author: Marcel Holtmann <marcel@holtmann.org>
Date:   Fri Mar 13 14:22:48 2026 +0100

    Release 3.12
```



버전 확인 하기
```
/usr/libexec/iwd --version
# OR
iwd --version
```

이제 iwd 를 실행하고 enable 해주면 된다. 중요 wpa_supplicant 는 중지, disable, mask 까지 해준다. 
```
sudo systemctl enable --now iwd
```
 
> enable 만 해주면 시작은 하지 않고, start 만 하면 start만 한다.  
enable --now 를 하면 둘 다 적용해준다. start 와 부팅 후에 자동 시작  


## 설치된 곳
```
 /usr/bin/mkdir -p '/usr/bin'
  /bin/bash ./libtool   --mode=install /usr/bin/install -c client/iwctl monitor/iwmon '/usr/bin'
libtool: install: /usr/bin/install -c client/iwctl /usr/bin/iwctl
libtool: install: /usr/bin/install -c monitor/iwmon /usr/bin/iwmon
 /usr/bin/mkdir -p '/usr/libexec'
  /bin/bash ./libtool   --mode=install /usr/bin/install -c src/iwd '/usr/libexec'
libtool: install: /usr/bin/install -c src/iwd /usr/libexec/iwd
 /usr/bin/mkdir -p '/usr/share/dbus-1/system-services'
 /usr/bin/install -c -m 644 src/net.connman.iwd.service '/usr/share/dbus-1/system-services'
 /usr/bin/mkdir -p '/usr/share/dbus-1/system.d'
 /usr/bin/install -c -m 644 src/iwd-dbus.conf '/usr/share/dbus-1/system.d'
 /usr/bin/mkdir -p '/usr/share/man/man1'
 /usr/bin/install -c -m 644 client/iwctl.1 monitor/iwmon.1 '/usr/share/man/man1'
 /usr/bin/mkdir -p '/usr/share/man/man5'
 /usr/bin/install -c -m 644 src/iwd.config.5 src/iwd.network.5 src/iwd.ap.5 '/usr/share/man/man5'
 /usr/bin/mkdir -p '/usr/share/man/man7'
 /usr/bin/install -c -m 644 src/iwd.debug.7 '/usr/share/man/man7'
 /usr/bin/mkdir -p '/usr/share/man/man8'
 /usr/bin/install -c -m 644 src/iwd.8 '/usr/share/man/man8'
 /usr/bin/mkdir -p '/usr/lib/modules-load.d'
 /usr/bin/install -c -m 644 src/pkcs8.conf '/usr/lib/modules-load.d'
 /usr/bin/mkdir -p '/lib/systemd/network'
 /usr/bin/install -c -m 644 src/80-iwd.link '/lib/systemd/network'
 /usr/bin/mkdir -p '/lib/systemd/system'
 /usr/bin/install -c -m 644 src/iwd.service '/lib/systemd/system'

```