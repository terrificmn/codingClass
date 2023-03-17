# lftp common command
주로 사용하는 커맨드 


## 이동
`cd` 접속한 remote ftp 의 directory를 이동한다   
```
cd Test/test_dir
```

`lcd` host 컴, 즉 local의 경로를 바꾼다. 다운할 때, 업로드할 때 경로를 바꿀 수 있어 편함
```
lcd
```
lcd만 치면 local의 home 경로로 이동 
 
이동했다고 알려준다 
```
lcd ok, local cwd=/home/myuser
```

local의 다른 경로로 이동할 때
```
lcd ~/Downloads
```

역시 이동했다고 메세지 알려줌
```
lcd ok, local cwd=/home/myuser/Downloads
```


## list
`ls` remote ftp의 dir및 파일들을 list 해준다 

## 현재 경로
`pwd` remote ftp의 경로를 알려준다 

`lpwd` host쪽 local 컴의 경로를 알려준다 



## 업로드
`put filename` local에 있는 파일명을 입력해주면 업로드가 된다. 탭으로 자동 완성 가능
```
put file1.tar
```
> 처음 로컬에서 (host) 접속한 부분에서 상대경로로 찾는다 

## 다운로드
`get filename` remote로 접속해있는 ftp 에서 다운로드를 받는다. 탭으로 완성 가능
```
get file2.tar
```

> 처음 터미널에서 접속했던 local 경로에 다운을 받는다. 혹은 lcd로 이동한 장소에 다운 받음
