
사용자 폴더에서 .wslconfig 파일을 만들어준다  

> .wslconfig 파일은 전역에 해당


내용은 아래 처럼
```
[wsl2]
memory=12GB
processors=4
```

memory	size	50% of total memory on Windows or 8GB, whichever is less; on builds before 20175: 80% of your total memory on Windows	How much memory to assign to the WSL 2 VM.
processors	number	The same number of logical processors on Windows

> 예제는 processors가 2여서 2로 했더니.. 오히려 느려짐..;  실 호스트pc와 같게 해주자

그리고 docker desktop을 재시작해준다  




## docker가 build 시 apt-get 이 느릴 때 
2가지 방법

#### 첫 번째 `apt-get install ...` 명령을 하기 전에 
```
RUN sed -i 's/htt[p|ps]:\/\/archive.ubuntu.com\/ubuntu\//mirror:\/\/mirrors.ubuntu.com\/mirrors.txt/g' /etc/apt/sources.list
```
/etc/apt/sourceslist 에 가장 좋은 mirror 사이트를 선택할 수 있게 해준다  


#### 두 번째
```
RUN apt-get install curl ca-certificates -y
```
이거는 별 효과 없는 듯 하다 ?

을 넣어주고 apt-get을 여러번 실행할 때에는 마지막에 apt-get을 사용하는 부분에서  
```
RUN apt-get install .... && \ 
...
...
rm -rf /var/cache/apt && \
    apt-get clean
```
해준다 
