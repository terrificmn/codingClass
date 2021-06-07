# ROS를 설치하자
[공식 ROS.org 웹 사이트를 방문해서 알아보기](http://wiki.ros.org/melodic/Installation/Ubuntu)

멜로딕 ROS를 설치해보자 

먼저 ROS는 미들웨어, 메타OS 로 불리는데~ 로봇 운영체제가 작동을 하기 위해서는 
우리가 익히 알고 있는 OS (Operating System)이 필요하게 되는데

<img src=0>
<br>

이 중에서 우분투 배포판 리눅스에 설치가 되게 되며 가장 호환이 잘 된다고 생각하면 된다.

> Long Term Support 로 2년 주기로 새로운 버전이 나오며, 약 5년 동안 동안 업데이트 및
지원이 되며 안정적인 버전이다 (예전에는 3년 지원)

> 2년 사이 마다, 즉 정확히는 9개월 마다 나오는 우분투 버전은 STS: Short Term Support 라고 부르며
LTS에는 없는 새로운 기능들이 많이 나오지만 지원기간이 짧다

<br>

그러면 우분투 배포판 LTS에 맞춰서 ROS도 나오게 되는데 현재 우분투 리눅스는 focal
20.04 배포판이 있고~ 2025 4월 까지 지원이 되는데, 
여기에 맞는 ROS는  Noetic Ninjemys on Ubuntu Linux 버전이다

<img src=1>
<br>

<br>

## 왜 그런데 하위버전인 Melodic Morenia 를 설치할까?
Noetic Ninjemys 아래 버전인 **Melodic Morenia ROS** 버전을 설치하는 이유는 

ROS는 오픈소스임을 생각해야한다. ROS Noetic 는 나온지 얼마 안 되어서
그 하위 버전인 Melodic ROS 버전이 패키지도 훨씬 많이 있고 커뮤니티에서 얻을 수 있는 
오픈소스 프로젝트도 많이 있을 것이다. 
그리고 뭔가 문제가 생겼을 때 같은 문제 혹시 문제를 해결 해줄 만한 사람들이 많이 있다는 장점 있다
그래서 Melodic 버전을 설치하는 것이다

그래서 Melodic 버전에 맞춰서 OS도 맞춰줘야한다
그래서 우분투 18.04 버전 Bionic Beaver를 설치를 먼저 해줘야하고 
그 위에 ROS Melodic을 설치하게 된다

<img src=2>
<br>

<br>


## 본격 ROS를 설치해보자
먼저 sources.list를 설정해준다. 터미널을 열고 아래를 복사 입력한다
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
sh 쉘을 이용해서 echo 문자열 출력을 해서 
/etc/apt/sources.list.d/ros-latest.list 파일을 만들어 준다

그 다음으로는 apt-key를 설정해준다
```
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
```

대개 위의 apt-key 설정으로 문제 없이 되지만, 
만약 위의 key설정이 안 된다면, 아래의 방법을 사용한다. 
```
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
```

이제 위에서 등록한 sources.list를 이용해서 리포지터리 업데이트를 해준다
```
$ sudo apt update
```

이제 드디어 ROS를 설치할 수 있게 된다
설치는 apt 또는 apt-get 으로 설치하게 되며, 풀버전, 데스크탑 버전, 베이스 버전 등으로 나눠서 받을 수 있다
full 데스크탑 버전으로 받아보자

```
$ sudo apt install ros-melodic-desktop-full
```

참고로 풀버전이 아닌 버전을 설치하고 싶다면 아래 명령어 처럼 한다  

옵션 1 -  ROS, rqt, rviz, and robot-generic 라이브러리가 포함된 버전
```
$ sudo apt install ros-melodic-desktop
```

옵션 2 - 베이스 버전 설치 ROS 패키지, 빌드, 통신 라이브러리 등이 포함되어 있지만 GUI(그래픽) 관련은 없다
```
$ sudo apt install ros-melodic-ros-base
```

여기까지 해봤으면 눈치를 챘겠지만,  
ros-melodic-ros-*** 의 식으로 패키지를 설치한다는 것을 알 수 있다  
ros-melodic-**PACKAGE** 식으로 넣어주면 된다

매뉴얼 사이트에 나온 예를 보면
```
$ sudo apt install ros-melodic-slam-gmapping
```
다른 패키지를 설치한 것을 알 수 있다. 위의 방식은 각각의 패키지를 설치할 때 사용한다


<br>

설치가 완료 되었다면, 환경 설정을 해줄 차례이다.

vi편집기를 ~/.bashrc 파일을 열어서 터미널을 열 때마다 명령어가 실행 될 수 있게 해주자~
```
$vi ~/.bashrc
```
파일이 열리면 가장 아래로 내려간 후에 i 를 눌러준다. **INSERT** 모드로 바뀌는데
이때 아래 줄을 입력해주거나 복사하자

```
source /opt/ros/melodic/setup.bash
```
그리고 ESC키를 한번 누르고 : (콜론)을 누른 후에 wq 를 누르자
그러면 w(저장) q(빠져나가기) 가 된다

위의 vi 편집기 쓰는게 불편하거나 더 쉽게 하려면 아래의 명령어로 실행을 할 수 있다.
```
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
```

어떤 방식을 했던 간에 .bashrc 파일을 다시 한번 읽어 줘야지 실행이 되는데  
방법은 터미널을 끈다~ 그리고 다시 켜면 된다. (새 탭으로 켜도 된다)

옵션 - 또는 아래처럼 명령어를 친다.
```
source ~/.bashrc
```

> 위의 명령어를 정리하자면~ echo 명령어는 출력을 해주는데 출력한 문자열을 리다이렉트 기능을 이용해서   
~/.bashrc 파일에 추가로 넣어 준 뒤에 저장해 주는 기능이고  
vi편집기로 한 것은 .bashrc 파일을 열어서 직접 수정/저장 한 것이 된다.

<br>

이제 /opt/ros/melodic/setup.bash 파일이 실행이 되게 된다. (매번 터미널이 켜질 때마다 실행됨)

<br>

## 추가 패키지 설치하기
의존성 관련 패키지를 설치하기 위해서 다음 명령어를 써 준다
ROS 패키지들을 빌드를 해주기 위한 tool 및 다른 의존성을 해결해 주기 위해서 설치를 하는 것이다
```
$ sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
```

거의 다 설치가 완료 되었다.

이제 ROS tool을 사용하기 전에 rosdep를 시작을 해줘야한다. 

>rosdep은 ROS에서 핵심 컴포넌트를 실행할 때 꼭 필요한 것들을 컴파일을 하거나 실행할 때 시스템 의존성 설치를 쉽게 할 수 있게 도와주게 된다

아래 처럼 입력하자
```
sudo rosdep init
rosdep update
```

이로써 설치가 성공적으로 마무리가 되었다!

다음은 간단한 튜토리얼을 하면서 설치가 잘 되었고 작동이 잘 되는지 확인해 보자  

[거북 투토리얼 해보기](/blog/) 링크 수정해야 함
