도커 이미지 받기
```
$ docker pull ubuntu:18.04
```
우분투 18.04를 다운 받음
여기에서 ubuntu만 하면 최신버전을 받게 된다. 또는 ubuntu:latest

```
$ docker image ls
```
어떤 설치된 이미지 파일을 확인할 수 있다

지우기 (정확하지 않음;;)
```
$ docker image rm 숫자id
```

도커 명령어 실행하기 (bash 프로그램 열기)

```
$ docker run -it ubuntu:18.04 /bin/bash
```

```
$ dudo docker run -it ubuntu:18.04
```
여기까지만 해도 우분투 실행됨

-t 옵션이 터미널로 열 수 있는 방식으로 -i로 하면 계속 터미널에 열려있게 됨 
바로 /bin/bash 를 열어준다 

옵션 설명
-i, --interactive   Keep STDIN open even if not attached 
-t, --tty           Allocate a pseudo-TTY     



우분투를 실행해서 sudo 설치하기

처음에 도커 우분투를 실행하면 root로 로그인하게 되는데 
공부하는 입장에서 집에는 centOS를 사용하는데 우분투를 실습하게 되어서 
vmware 나 virtualBox를 사용해봤지만 이번에는 docker를 사용해보고 싶어서;; 흠..

어쨌든 sudo 가 없으므로 
```
# apt-get update
# apt-get install sudo
```
해주면 sudo가 설치된다

useradd <userId> 와 passwd <userId>를 해준다음에 로그인해서 사용하면 됨