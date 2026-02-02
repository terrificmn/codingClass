
의존성
sudo apt update
sudo apt install -y git build-essential pkg-config python3-docutils \
                     libdbus-1-dev libreadline-dev automake libtool

ell이 필요
git clone https://git.kernel.org/pub/scm/libs/ell/ell.git
cd ell
./bootstrap
./configure --prefix=/usr
make
sudo make install
cd ..



그 다음이 iwd 로 빌드인데, 빌드에서 실패


 CC       monitor/nlmon.o
client/station-debug.c:2:10: fatal error: ell/useful.h: No such file or directory
    2 | #include "ell/useful.h"
      |          ^~~~~~~~~~~~~~
compilation terminated.
src/band.c:29:10: fatal error: ell/useful.h: No such file or directory
   29 | #include "ell/useful.h"
      |          ^~~~~~~~~~~~~~


그래서 

configure 를 할 때 --enable-library

(Note: Using --enable-library without --enable-external-ell tells iwd to use the version of ELL bundled in its own source tree.)



git clone https://git.kernel.org/pub/scm/network/wireless/iwd.git
cd iwd
./bootstrap
./configure --prefix=/usr \
            --sysconfdir=/etc \
            --localstatedir=/var \
            --enable-external-ell

여기에서 extenal-ell 대신에 

./configure --prefix=/usr --enable-library
make
sudo make install

이렇게 하면 빌드가 된다. 


버전확인
/usr/libexec/iwd --version
# OR
iwd --version




## 설치된 곳
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
amrrobot@sgtubunmsi:~/iwd$ 

