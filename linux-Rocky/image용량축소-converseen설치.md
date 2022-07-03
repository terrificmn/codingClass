블로그에 올리기에는 사진 용량이 좀 크다~
그래서 리눅스에서 용량 줄일 수 있는 프로그램을 찾아봤는데 
converseen이라는 프로그램이 있어서 설치를 해봤는데
간단하게 사용할 수 있는 프로그램이어서 좋다

소스코드를 받아서 빌드를 할 수도 있지만 의존성을 알아서 해결해줘야하므로

[converseen 공식사이트](https://converseen.fasterland.net/download-for-linux/)

그래서 yum 등의 패키지매니지먼트을 사용해주면 편하다!

CentOS 8, Fedora 계열
```
sudo yum install converseen
```

Ubuntu 에서는 
```
sudo apt-get update
sudo apt-get install converseen
```
