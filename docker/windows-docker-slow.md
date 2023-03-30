
사용자 폴더에서 .wslconfig 파일을 만들어준다  

내용은 아래 처럼
```
[wsl2]
memory=4GB
processors=2
```

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
을 넣어주고 apt-get을 여러번 실행할 때에는 마지막에 apt-get을 사용하는 부분에서  
```
RUN apt-get install .... && \ 
...
...
rm -rf /var/cache/apt && \
    apt-get clean
```
해준다 

