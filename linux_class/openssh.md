간단 버전 설치한 후 접속하기

ssh를 입력을 한 후 설치가 되어 있는지 확인

```shell
$sudo apt-get install openssh-server
```

```shell
$sudo systemctl start ssh
$sudo systemctl status ssh
```

방화벽에 22번 ssh용 포트 추가되어있는지 확인
```shell
sudo ufw status
```

상태가 active가 아니면 enable을 시켜주면 됨
그리고 포트가 없다면 포트를 추가해주기 

```shell
sudo ufw allow 22/tcp
```

```shell
$sudo systemctl reload ssh
```

먼저 가상머신의 아이피를 확인해야하는데 우분투이면 ifconfig를 안 사용해도 
처음에 ifconfig 설치 안되어있어서 net-tools 를 apt로 설치해야함
하지만 우분투에서는 
ip addr show 또는 ip address show로 입력하면 알 수 있음
```shell
$ip address show
```

이제 호스트 컴 윈도우에서 cmd 또는 파워셀로 접속을 할 수 있는데 실행 후 
ssh 명령어로 접속할 수 있음 
유저아이디@아.이.피.주소 를 사용해서 사용하면 됨

```shell
C:> ssh sgtubun@192.168.0.200
```
비번 입력 후 사용하면 됨

아주 기초만 해봄
자세한 설정이 있을텐데.. 그거는 차차 공부할 영역일 듯



