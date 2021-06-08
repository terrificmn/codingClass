# 도커 기본 튜토리얼 사용해보기
먼저 docker와 docker-compose 설치가 되어 있어야 한다 

[리눅스 (ubuntu) 도커 설치 보러가기](/blog/) -포스팅 예정:링크수정 해야함

먼저 터미널을 열고 docker 버전을 확인해 보자
```
[octa@localhost ~]$ docker --version
Docker version 20.10.6, build 370c289
```

이번에는 터미널에 
```
$ docker
```
만 입력해보자. 그러면 아래와 같은 안내가 나오는데

```
Usage:  docker [OPTIONS] COMMAND
... 이하 생략
...
```

도커는 docker 로 시작하고 옵션은 생략이 가능하고 그 이후에 명령어를 입력하는 방식인 것을 알 수 있다

예를 들면 docker pull, docker image, docker ps
이런식으로 명령어를 입력할 수 있다.

<br>

## pull 로 도커 이미지 다운받기
먼저 처음으로 명령어 pull을 해보자

깃허브를 경험해본 사람이라면 익숙할 그 pull이다. 도커 허브란 곳에서 도커 이미지를 다운받아 오는 것이다

> 참고로 pull 명령어에 대해서 더 알고 싶을 때는 터미널에 docker pull --help 라고 쳐보자
그러면 pull 명령어 사용방법 및 옵션등을 알 수 있다

먼저 CentOS 도커 이미지를 받아보자.

이미지 방식은 다음 처럼 된다 

이미지이름[:버전 또는 키워드]

예를 들어서 우분투는 18.04, 20.04 이런식으로 버전이 나오지만
centos는 7, 8 이런식이다

아래 처럼 입력해보자
```
docker pull centos:8
```
centos:latest 라고 하면 최신 이미지를 다운 받는다  
또는 centos 만 하고 뒤에를 생략해도 최신 버전을 다운 받는다

> 이거는 다른 이미지를 받을 때도 비슷하게 적용이 된다  
docker pull ubuntu:18.04  또는 docker pull ubuntu:latest

이제 도커 이미지가 다운이 된다

<img src=0>

이제 실제 이미지가 다운이 되었는지 확인을 해보자. 이것도 리눅스 명령어 처럼 사용이 되어서 
조금 친숙하다

```
$ docker image ls
```

그러면 다운 받은 docker 이미지를 보여준다

이제 확인은 되었고 
다운받은 이미지를 바탕으로 도커를 실제로 실행을 시켜보자 

run이란 명령어와 옵션을 넣어서 컨테이너를 실행해보자. 

명령어는 run 을 사용하는데 run 은 새로운 컨테이너에 명령을 해주는 것이 된다

```
$ docker run -it centos:8 /bin/bash
```




# 몇 개의 스크린 샷 필요함!!! 
# 실행과 이미지 삭제까지 만들어 줄것 

https://hub.docker.com/_/centos

