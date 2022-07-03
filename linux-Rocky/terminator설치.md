최초로 설치를 할 때 
```
200~No match for argument: terminator
Error: Unable to find a match: terminator
```

yum에서 패키지를 찾지 못할 때에는
epel-release를 먼저 설치를 해준다음에 install 해준다
```
sudo dnf install epel-release -y
sudo dnf install terminator -y
```
