# hostname 변경
터미널에서 username@my_pc  또는 username@localhost 식으로 나오며  
`uname -a` 를 해보면
```
Linux Localhost 6.14.6-300.fc42.x86_64 #1 .....
또는 
Linux MyPc 6.8.0-60-generic #63~22.04 .....
```
여기에서 Linux 뒤에 나오는 것이 host명 이다.   

host이름을 확인하는 것은 

```
hostname
#또는 
vi /etc/hostname
```



## 변경하기
hostnamectl 서비스를 이용한다. 

아래 처럼 사용한다. 
```
sudo hostnamectl set-hostname 새로운_host명
```

ssh 접속이였다면 다시 재접속하면 바뀐 것을 확인할 수가 있다.  


## hosts 확인
/etc/hosts 확인을 해보면  

```
127.0.0.1 localhost
127.0.1.1 old_my_hostname
```

/etc/hostname 과는 다르게 예전의 hostname이 남아 있다.  
그래서 수동으로 새로운 호스트명으로 저장을 시켜준다.  

만약 서비스 나 프로그램 등에서 예전 호스트명을 사용하고 있다면 hostname 관련 셋팅을 다시 해줘야 할 수도 있다.   
(web, db 등..)  


