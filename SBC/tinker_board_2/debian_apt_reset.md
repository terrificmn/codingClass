# apt reset debian 

apt update 업데이트가 꼬일 경우에  
sources.list 파일을 지운 후에 다시 만들어 준다.
```
cd /etc/apt
sudo rm -i sources.list
```

이후 다시 만들어 준 후에 아래 내용을 복사 붙여넣기.
```
vi sources.list
```

`sudo apt update`


```
deb http://deb.debian.org/debian bullseye main contrib non-free
deb-src http://deb.debian.org/debian bullseye main contrib non-free

deb http://deb.debian.org/debian-security/ bullseye-security main contrib non-free
deb-src http://deb.debian.org/debian-security/ bullseye-security main contrib non-free

deb http://deb.debian.org/debian bullseye-updates main contrib non-free
deb-src http://deb.debian.org/debian bullseye-updates main contrib non-free
```
