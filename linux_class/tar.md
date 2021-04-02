파일 묶기
```shell
$ tar -cvf tarfile.tar text1 text2 text3
```
특정 디렉토리에서 다 묶기
```shell
$ tar -cvf tarfile.tar ./*
```

gunzip을 이용해서 압축하기
```shell
$ tar -zcvf tarfile.tar.gz *
```

gunzip 압축 풀기, 현재 경로에 압축을 푼다
```shell
$ tar -zxvf tarfile.tar.gz 
```

-C 옵션을 넣어서 풀어줄 경로를 지정해줄 수 있음
```shell
$ tar -zxvf tarfile.tar.gz -C ../원하는dir
```

만약 파일이 tar.gz 으로 압축이 되어 있다면 xvf 옵션만 써도 압축이 잘 풀린다
(파일에.tar.가 안들어가 있으면 안됨)
```
$ tar -xvf tarfile.tar.gz -C ../원하는dir
```


<br/>

참고 주의할점
tar는 절대경로로 압축이나 묶음을 하는 것은 비추임
예를 들어서 
```shell
$ tar -zcvf tarfile.tar.gz /home/user/tarfiles/project1/*
```
대개 압축할 곳으로 이동을 해서 압축할 곳에서 압축을 하는데 
만약 이런식으로 절대 경로를 이용해서 압축 파일을 만든다고 하면
프로젝트1에 있는 모든 파일들은 다 압축이 되지만
절대경로의 모든 디렉토리들도 같이 압축이 되어 버린다. (파일들은 제외)

```shell
$ tar -xvf tarfile.tar.gz 
```
그래서 압축을 풀게되면 /home 부터 생기는 것을 알 수 있다
암튼 보안상/프라이버시 상 좋지 않으므로 절대경로는 압축하지 말자!



