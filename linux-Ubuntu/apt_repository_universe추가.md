# add-apt-repository

어느 프로그램을 설치하려고 하는데 패키지를 apt 에서 전혀 못 찾는 경우   
보통 블러그나, 사이트에서 우분투 버전에 맞게 설치하는 apt install 이 나와 있으나  
**내 컴터에서만** 안되는 경우에는 universe repository 가 추가 안되어 있는지 체크 해야한다   

```
sudo add-apt-repository universe
sudo apt update
```

adb 라는 안드로이드 연결 패키지를 설치하려고 할 때, 패키지를 못 찾음

위 처럼 다시 리포를 추가해주고 update 후에 다시 
```
sudo apt install adb
```
또는 다른 패키지를 응용해서 시도해보면 된다  



