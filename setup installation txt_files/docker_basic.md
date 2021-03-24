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
-t 옵션이 터미널로 열 수 있는 방식으로 -i로 하면 계속 터미널에 열려있게 됨 
바로 /bin/bash 를 열어준다 

옵션 설명
-i, --interactive   Keep STDIN open even if not attached 
-t, --tty           Allocate a pseudo-TTY     



