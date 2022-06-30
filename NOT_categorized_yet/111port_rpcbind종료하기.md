```
sudo netstat -tlpn
```

tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      1/systemd  

가 열려있다


nfs가 설치가 될 때 함께 설치되는 의존성 패키지라고 한다 
sudo systemctl status nfs
확인

사용을 안하는 것 같으므로 종료시키기

systemctl stop rpcbind.socket 
systemctl stop rpcbind.service
systemctl stop rpcbind.target 
systemctl stop rpc-gssd.service


추후 문제가 없다면 
systemctl disable rpcbind.socket
systemctl disable rpcbind.service

sudo systemctl status rpc


오픈되어있는 포트 확인하기
```
nmap -p 0-65000 ip주소
```
```
netstat -tlpn
```

