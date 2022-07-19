## openssl
dnf 

sudo dnf install openssl-devel


apt

sudo apt-get install libssl-dev



## boost 설치   
dnf
sudo dnf install boost-devel


apt
apt install libboost-all-dev




https://github.com/jgaa/restc-cpp/blob/master/doc/GettingStarted.md

## cpp 빌드

boost libraries 이용해서 빌드하기 
```
g++ ./http_test.cpp -o http_test -L /usr/lib/ -lboost_system -lboost_thread -lpthread
```

-o 옵션으로 (linker flags) 만들때에 파일명이 먼저 나오고 그 다음에 -o 옵션이 와야 한다 

