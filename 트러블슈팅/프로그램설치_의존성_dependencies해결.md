# 프로그램 설치 의존성 dependencies 해결 하기
프로그램 설치 의존성 dependencies 해결 하기

## VirtualBox 를 설치할 때 
```
Failed dependencies:
	libSDL-1.2.so.0()(64bit) is needed by VirtualBox-6.1-6.1.18_142142_el8-1.x86_64
```

이제 인스톨을 해주는데 yum install libSDL 이런식으로 입력을 하면  
```
Error: Unable to find a match: libSDL 
```
찾지를 못한다. 구글링 하기 전에

위에서 나온 libSDL을 그대로 입력해보자  
```
sudo yum install libSDL-1.2.so.0 
```

바로 찾는다 또는 SDL 만 쳐도 찾아준다

패키지 없다고 할 때   
이제 yum install 한 다음에 없다는 패키지를 좀더 다양하게 쳐봐야겠음



## Davinci Resolve 설치 시 에러
GUI모드에서 실행이 아예 안되고 아무런 에러도 안남   
그래서 터미널에서 /opt/resolve/bin 으로 이동해서 resolve를 실행해보면

libGLU.so.1: cannot open shared object file: No such file or directory on centos

이때는 libGLU.so.1 설치를 해야하는데 
```
sudo yum -y install libGLU
```

이제 실행이 잘 된다.



## libXss.so.1  vscode 설치 시 에러
```
error: Failed dependencies:
	libXss.so.1()(64bit) is needed by code-1.50.1-1602601064.el7.x86_64
```
그러면 libXScrnSaver 설치해줘야 한다. 다행이도 친절하게 뭐가 필요한지 알려준다.  
구글링 해보면 libXScrnSaver필요하다고 함. 
 
yum 으로 libXScrnSaver 설치하자
```
$sudo yum install libXScrnSaver
```

필요한 의존성을 해결했기때문에 (설치로) 다시 rpm 명령어로 vscode를 설치한다   
(다시 처음으로..)
  $sudo rpm -ivh code-1.50.1-24.rpm




