# 우분투 nvidia 그래픽 드라이버 설치하다가 날려먹었을 때 
일단 학교 프로젝트를 진행하다보니 프로그램에서 워닝으로 그래픽드라이버를 새로운 것으로 바꾸라는 말에 
그래픽 드라이버를 새로 받아서 설치했다

그래픽 드라이버 제품번호도 맞고 공식사이트에서 받았는데도 불구하고 
설치하던 중에 에러가 나면서 설치에 실패했다. 거기까지면 좋았는데 이게 화면이 이상하게 나온다;;;

화면이 계속 깜빡깜빡 거리면서 작업을 할 수가 없다.
그래서 컨트롤 + 알트 + F3을 눌러서 콘솔 터미널을 열어준다

이것도 계속 깜빡거릴 때 마다 다시 눌러야 콘솔로 돌아왔다
계정 아이디와 비번으로 로그인을 한 다음에

lightdm을 설치를 해줘야한다. 원래 우분투18.04 기준으로는 gdm3 인 것 같은데

```
sudo apt-get install lightdm
```
으로 설치를 하면 설치화면이 나오면서 lightdm을 설치할 수 있다

그러면 
sudo dpkg-reconfigure lightdm
으로 설정한 후에 재부팅

이제 무한로그인이 된다. 해결할 수 있는 방법은 다 찾아봤지만 안됨
다시 그래픽 드라이버를 설치를 해주자

```
sudo add-apt-reposiitory ppa:graphics-drivers/ppa
sudo apt update

ubuntu-drivers devices
```
하면 recommended 라고 나오는 그래픽 드라이거 있을 것임
```
sudo apt-get install nvidia-340 
```
이런식으로 입력

사실 이게 좀 헤깔리는데 이렇게 해도 안됬던 것 같다;;;;


워낙 시도한게 많아서 좀 헤깔리지만 다 지우고 
sudo apt-get purge lightdm
sudo dpkg-reconfigure gdm

으로 해서 gdm으로 돌려놓고 
```
sudo apt-get install xserver-xorg-core
sudo apt-get install xserver-xorg-video-nouveau
```
를 설치해준다음에 재부팅을 했다 (history를 보니 조금 기억이 난다)

이쯤되서 무한 재부팅이 멈춘거 같은데 확실치는 않다 ㅠㅠ

재부팅 했더니 마우스 키보드가 아예 작동을 안한다 
로그인을 할 수가 없다

```
sudo apt-get install xserver-xorg-input-all
```
만 해주면 키보드 동작할 수 있다.

그런데 뭔가 잘못 되었는지 apt-get update로 먼저 업데이트를 해줘야하는데 안된다

GUI로 오면 키보드가 작동을 안하니
처음 Grub 선택화면에서 복구화면을 선택하고
네트워크가 되게 해주고 , root로 로그인을 한다

그리고 나서 
```
apt-get clean
rm -rf /var/lib/apt/lists/*
apt-get update
```
이쯤 되면 되면 좋겠건만 리스트가 꼬였나 보다 
kr.archive에서 에러가 난다

sudo vi /etc/apt/sources.list
로 열어서 

맨 아래에 있는 deb http://security.ubuntu.com/ubuntu 이 주소는 빼고
한 3개정도 있다

맨 위에서 부터 deb kr.archive 로 시작하는 주소를 
deb http://ftp.daumkakao.com/ubuntu/ 처럼 바꿔준다
즉 인터넷 주소만 바꾸면 된다. bionic 또는 bionic-updates 식으로 되는 뒷부분은 건들일 필요없이 다 수정한 후 저장

이제 apt-get update가 된다
sudo apt-get install xserver-xorg-input-all 
마저 수행하면 잘 된다.

이제 재부팅. 마우스 키보드 작동한다




