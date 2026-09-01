# Bash Startup files
로그인 셸이 시작되면 Bash는 /etc/profile 파일을 먼저 찾아보게 되고  
그 다음에 .bash_profile, .bash_login, .profile 등을 실행하게 된다고 한다.

로그인이 아닌 셀이 실행될 때에는 .bashrc 파일이 실행되게 된다.

숨김파일로 되어 있으며 모두 홈디렉토리안에 유저 디렉토리 안에 있다

<br>

# bashrc 파일과 bach_profile 의 차이
.bashrc 파일은 로그인을 하지 않고 bash에서 명령어가 수행되었을 때 실행이 되고
.bash_profile 파일은 로그인을 하면서 읽어지면서 실행이 된다고 한다.

.bashrc 파일은 새로운 shell을 실행할 때마다 실행이 되게 할 때 사용할 수 있다.  
여기에는 aliases(별칭) functions(함수)등을 정의할 수 있다.

.bash_profile 파일에서는 한번만 실행하면 되는 것이나, 환경 변수를 적용하게 한다던가할 때 사용한다

대부분의 리눅스 디스트리뷰션에서는 .profile 을 사용한다고 한다.
.profile은 모든 shells 에서 읽히고, .bash_profile은 Bash shell만 읽는다.

결론은 상황에 따라 다르겠지만.. .bashrc를 사용하고..  
재미있는 것은 .bash_profile 에는 쉡 스크립트가 하나 들어가 있는데

```shell
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi
```
.bashrc 파일이 있다면 실행을 하는 if문이 들어가 있음.  
즉, 셀을 열면 (터미널을 열면) 두 개의 파일이 실행되게 된다는 것이다. 

<br>

# 부록 alias 등록하기
파이썬 버전별로 특정 버전으로 별칭을 주기

그리고 alias를 지정해 줄 수 있는데...  
python 또는 python3 이라고 터미널에 입력했을 때,   
파이썬3.8 버전이 실행되게 해보자

홈디렉토리에 있는 .bashrc 파일을 읽는다.
```shell
$sudo vi ~/.bashrc 
```

그리고 파일에 아래 내용을 추가 한 후 저장 후 빠져나온다.
```shell
# python alias
alias python=python3.8
alias python3=python3.8
```

이제 다시 source 로 실행하면 적용이 된다. 또는 위에서 말한대로 터미널을 빠져나간 후 다시 들어오면 .bashrc 파일이 적용이 된다.
```shell
$source ~/.bashrc
```

