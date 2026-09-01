# useradd 하기
아무래도 평상시에는 desktop으로 사용하다 보니 유저를 특별히 더 만들 필요는 없었는데  
이번에 서버를 옮기면서 일반 유저로 작업을 해야겠다는 생각이 들어서 일반 유저를 만들고 진행했다

먼저 root 로 로그인을 해서, 또는 ssh로 접속을 해서 유저 만들기
```
useradd -m -U -s /bin/bash user1
```

>-m 옵션은 /Home user의 디렉토리를 만들어줌  
-U 는 그룹을 user이름으로 생성해줌, -s 는 로그인할 쉘

비번 변경하기
```
passwd user1
```

그리고 user1이 sudo를 사용할 수 있게 sudoers 파일을 변경해준다
```
vi /etc/sudoers
```

/를 누르고 ALL 이라고 친다음에 엔터를 치고 n 키를 몇번 눌러주면   
아래와 부분을 찾을 수 있고 
```
## Allow root to run any commands anywhere
root    ALL=(ALL)       ALL
```
이런곳에 도달할 것임. root 아래에 추가해준다 ESC키를 누르고 i키를 눌러 추가를 해준다

```
user1   ALL=(ALL)       ALL
```
두번째 ALL=(ALL)을 모든 명령어에 접근할 수 있게 하는 것이고   
마지막 ALL 대신에 /sbin/특정명령어 를 넣어주면 그 명령어만 sudo를 사용해서 명령어를 사용할 수 있게 해준다   
물론 ALL이 다 sudo로 가능하게 됨   

> 관리자 인데도, read only라고 저장이 안된다고 하면  wa! 로 강제저장;;;

이제 (서버라면) user1로 ssh로 접속하자
```
ssh user1@222.123.123.10
```

