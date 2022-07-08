# 프롬프트 Prompt 색 바꾸기
echo $PS1 을 해보면
현재 사용하고 있는 상태를 알 수 있다
```
[\u@\h \W]\$
```

데비안 계열을 쓰고 있다면 
```
echo $PS1
```
아래처럼 나온다
```
\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\u@\h:\w\$

```

이 $PS1을 바꿔주면 된다
\u 는 현재의 username을 표시
\h 는 hostname 표시
\w 는 현재 working directory 표시
\$ 는 UID가 0이면 #으로 (root표시), 아니면 $ 표시

다른것은 필요없고.. 도커로 컨테이너 들어가면 간혹 터미널 여러개 켜두다보면
헤깔려서 username 색깔만 바꿔보자


\e[    색깔 넣기 시작은 \e[ 로 시작
x;ym 그리고 x;y 값을 색깔 값을 넣어주고 (m은 끝에 붙여준다)
$PS1 에 들어갔던 shell prompt 변수를 넣어준다.
\e[m 으로 색깔 끝

이런식이 된다

\e[0;30m[\u@\h \W]\$ \e[m

위의 예는 프롬포트 처음부터 끝까지 해주는 것이였고
현재 username만 바꿔주고 싶기 때문에

\e[0;30m[\u@\h \W]\$ \e[m   를

[\e[0;36m\u\e[m@\h \W]\$  중간에 username만 적용되게 해보았다

이제 이것을 export 명령어로 PS1 변수에 넣어주자 ("로 묶어준다) --user이름만 변경

보통 대개의 blog 등에서는 아래 처럼 알려주고 있는데, 아래 처럼하면 결과가 잘 나오는 것은 맞다
하지만~ 긴 커맨드를 입력 할 때에는 **문제**가 발생한다~
[다음 User specific aliases and functions으로 넘어가서 보기](#user-specific-aliases-and-functions)

```
export PS1="[\e[0;36m\u\e[m@\h \W]\$ "
```

또는 전체를 변경할려면 아래처럼

```
export PS1="\e[0;32m[\u@\h \W]\$ \e[m "
```

> 전체를 변경했을 때의 문제가 발생하는지는 확인 안 해봤음

> 끝에 한칸 비워두고 "로 마무리하는것은 프롬포트을 한칸 여유있게 주는 것  
스페이스바 없이 해주면 바로 입력을 받게된다

export로 PS1이라는 환경 변수에 넣어주는 것이므로 계속 넣어서 테스트를 해보자
복사 붙여넣기로 할 때마다 프롬포트의 색이 바뀐다


# User specific aliases and functions
```
export PS1="[\e[0;36m\u\e[m@\h \W]\$ "
```
위 처럼 해도 잘 된다. 다른 블로그에서 본 것을 그대로 실행했더니~ 잘 된다
사실 처음에는 이렇게 잘 사용했다~

하지만 문제가 있었다~ 전혀 모르고 있었음 ㅋㅋ
긴 글(?) 긴 커맨드 라인을 입력하게 되면 이제 자동으로 줄 바꿈이 되는데 이때 
overlap이 되는 현상이 발생한다~ 다시 첫째이 수정이 되면서 오버랩되면서 써지면서   
뭘 쓰고 있는지 모를정도로 혼돈이 발생;;

좀 더 알아보니 ansi-escapes 라는 것을 해줘야한다고 한다
non-printing characters 표시하는 단어들이 아니고 위처럼 칼라를 바꿀 때는 쓰는 
것이라든이.. 어쨋든 이것은 출력(표시)할 것이 아니라고 하는 즉, escape를 해줘야한다

\[ 이걸로 시작을 해서 다시 \] 로 닫아준다
\[color code\]
그래서 위에 것을 옮기면 색깔코드 시작하는 문자와 색깔코드 끝나는 문자에 각각 넣어줘야한다

색깔코드 시작부분 \e[0;36m 에서 \[\e[0;36m\]
색깔코드 끝 부분 \e[m  에도 \[\e[m\] 

이제 나머지는 합쳐서 한 줄로 만들자
아래와 같다
```
# 이게 진짜
export PS1="[\[\e[0;36m\]\u\[\e[m\]@\h \W]\$ "
```

색깔표

| Color | 	Code |
| --- | --- |
| Black | 	0;30 |
| Blue  |	0;34 |
| Green  |	0;32 |
| Cyan | 	0;36 |
| Red  |	0;31 |
| Purple | 	0;35 |
| Brown  |	0;33 |

원하는 색깔을 넣어주자 (0 대신 1을 넣어주는 light color로 사용할 수 있다)


export 명령어는 한 세션에서만 유효하다 터미널을 끄면 초기화가 된다

그러므로 ~/.bashrc 에 추가를 해보자

vi로 열어준다
```
vi ~/.bashrc
```
그리고 i 를 눌러 편집모드에 들어간다음에 끝 줄에다가 
위의 export 명령어 한 줄 전체를 복사해준다 
이제 ESC키를 눌러서 편집모드에서 빠져나오고 : 를 누르고 wq 를 누른후 
저장하고 빠져나온다
이제 ~/.bashrc 파일을 다시 수정을 한 후에 저장을 하자

이제 적용된 모습을 보려면 새로 터미널을 켜주거나 
```
source ~/.bashrc
```
해주면 된다

이제 게속 바뀐 프롬프트를 볼 수가 있고~ 긴 명령어를 쳐도 문제 없이 줄 바꿈이 되면서 입력이 된다

앞으로 docker컨테이너에서 작업할 때 이제는 덜 헤깔리지 않을까?? ㅋㅋ


[여기참고했습니다~](https://www.cyberciti.biz/faq/bash-shell-change-the-color-of-my-shell-prompt-under-linux-or-unix/)



## ubuntu 기본 프롬프트  
```
\[\e]0;\u@\h: \w\a\]${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$
```

우분투에는 .bashrc 파일에 조금 더 if문으로 짜여져 있다  
```
if [ "$color_prompt" = yes ]; then
    #PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '  ## It is original 
    PS1="[\[\e[0;32m\]\u\[\e[m\]@\h \W]\$ "
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi

```

