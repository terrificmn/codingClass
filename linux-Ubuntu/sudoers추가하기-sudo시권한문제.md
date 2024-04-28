# 권한 때문에 sudo로 해결하려고 했더니 그래도 sudoers files에 없다고 할 때
SUDO 유저 추가하기  

에러 메세지
```
[cta@localhost html]$ rm -d learningphp/
rm: cannot remove 'learningphp/': Permission denied
[cta@localhost html]$ sudo rm -d learningphp
[sudo] password for sgtocta: 
cta is not in the sudoers file.  This incident will be reported.
```
상황은 디렉토리를 지우려고 하는데 권한 때문에 다시sudo를 상용했는데 sudoers파일에   
없다면서 안되는 경우

/etc/sudoers 파일을 root로 로그인해서 편집을 해줘야한다  

먼저 su - 권한 얻기 (root)   
sudo 때는 자신의 비밀번호가 필요하지만 su - 같은 경우는 root로 로그인을 하는 것이기 때문에   
root 비밀번호를 입력해준다
```
$su -
```
(root) 비밀번호를 입력해준다

## root 비번이 안되어 있을 경우
`su -`을 했을 경우에 su: Authentication failure 로 나오는 경우   

먼저 sudo 를 이용해서 root의 비번을 정해준다 
```
sudo passwd
```

> 자신의 비번을 바꾸때에는 passwd 해주지만, sudo passwd는 관리자 비번을 바꿀 수 있게 된다   
까먹으면 안되니 잘 기억, 메모?   
sudo 없이 `passwd`만 하게 되면 현재 로그인 한 유저의 password를 바꾼다.  


파일 열기 
```
#vi /etc/sudoers
```
> 참고로 맨앞의 싸인이 $에서 #으로 바뀜 (root 라는 소리)

아래의 root ALL=(ALL) 부분을 찾아준다  

사용형식 아래와 같다
사용자	호스트		명령어   
root	ALL=(ALL)	ALL

root 바로 아래에 (자신)유저를 추가해 주면 가능하다  
cta		ALL=(ALL)	ALL

vi의 i 키를 눌러서 수정한다

*참고: 특정명령어만 사용할 수 있게 추가해줄 수 있는데   
cta		ALL=/sbin/shutdown, /usr/sbin/adduser   
이렇게 해주면 유저 cta는 shutdown, adduser 명령어만 사용할 수 있게 된다. (명령어 사이에는 ,로 구분)   

저장이 되었다면 이제 exit로 root에서 빠져나온다
```
exit
```

이제 파일/ 디렉토리가 지워지는 것을 확인! 


### read only 일 경우  
분명히 sudo로 열었는데 sudoers 파일이 read only라고 하면서 저장이 안 되는 경우가 있다.  
이런 경우에는 아예 권한이 'r'만 되어 있는 경우   

```
sudo chmod 740 /etc/sudoers 
```
등으로 바꿔서 쓰기 가능하게 해준 다음에   
다시 440으로 바꿔준다.

