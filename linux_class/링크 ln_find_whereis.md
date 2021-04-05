타임관련 시간 KST로 바꾸기

lrwxrwxrwx. 1 root root 32 Mar 23 15:15 /etc/localtime -> ../usr/share/zoneinfo/Asia/Seoul

시간대 정보가 /usr/share/zoneinfo/Asia/Seoul 에 있는데 
심볼릭 링크를 /etc/localtime 로 만들어 주면 된다. 대신 연결이 되어있으므로 기존 연결을 제거하고 (-f 옵션) 다시 연결
```shell
$ ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
```

런레벨 을 찾아보면 각 심볼릭링크로 되어 있는데 원본 파일들을 각각 가리키고 있다 
$ ls -l /lib/systemd/system/runlevel?.target
으로 리스트를 보면
```
[sgtOcta@localhost hardAndSymbolicPrac]$ ls -l /lib/systemd/system/runlevel?.target
lrwxrwxrwx. 1 root root 15 Feb  1 18:05 /lib/systemd/system/runlevel0.target -> poweroff.target
lrwxrwxrwx. 1 root root 13 Feb  1 18:05 /lib/systemd/system/runlevel1.target -> rescue.target
lrwxrwxrwx. 1 root root 17 Feb  1 18:05 /lib/systemd/system/runlevel2.target -> multi-user.target
lrwxrwxrwx. 1 root root 17 Feb  1 18:05 /lib/systemd/system/runlevel3.target -> multi-user.target
lrwxrwxrwx. 1 root root 17 Feb  1 18:05 /lib/systemd/system/runlevel4.target -> multi-user.target
lrwxrwxrwx. 1 root root 16 Feb  1 18:05 /lib/systemd/system/runlevel5.target -> graphical.target
lrwxrwxrwx. 1 root root 13 Feb  1 18:05 /lib/systemd/system/runlevel6.target -> reboot.target
```

runlevel숫자.target 파일들이 원파일들을 가리키고 있는데
원래 원본 파일들을 같은 경로에 있다. /lib/systemd/system/ 안에 있음

바꾸고 싶은 원파일을 가리키게 default.target으로 심볼릭 링크를 만들어주면 된다

그래서 멀티user타겟으로(runlevel3) 바꿔주고   
```shell
$ln -sf multi-user.target default.target
```
재부팅하면 콘솔화면으로 로그인이 되는 것을 알 수 있다 

다시 원래 GUI로 돌아오기

먼저 경로로 이동하자
```shell
$cd /lib/systemd/system
$ln -sf graphical.target default.target
```
ln 명령어는 <원본파일:타켓> <심볼릭링크만들파일이름>


___

grep 파일 내용 찾기: 내용이 있으면 하이라이트 해주고 없으면 아무것도 안나옴
grep 문자열 파일명

```shell
$ grep string afile.txt
$ grep -n string afile.txt
```
라인 넘버를 매겨준다


___

find 파일 찾기 : 해당경로를 설정해주면 그 기준으로 파일을 찾는다
find 경로 -name 파일명
```shell
$find ./ -name a_find_file
$find ../ -name a_find_file
```
$find /lib -name default.target

-type d
로 하면 디렉토리를 찾아준다




___
whereis ls

which ls

파일이 어디에 있는지 해줌

___