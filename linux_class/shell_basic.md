# 쉘 스크립트
php와 매우 비슷하다.  c언어 때문에 

변수 할당하기 
$ GREETING=hello
변수는 $ (달러사인)을 넣어주고 echo로 호출하면 됨
$ echo $GREETING
hello

변수 할당 (메모리)에서 제거 
$ unset GREETING


환경변수 보기
```
$ env
```
라고 치면 환경변수에 저장된 것들을 볼 수 있다

변수 값에는 띄어쓰기가 안되므로  변수 = 로 값을 지정할 때 띄어쓰기 하면 안됨
예:
$ EXAMPLE = test example  ------ X 이렇게 하면 안됨
$ EXAMPLE="test example"  ------ O 이렇게 해야함

___

export 로 변수를 환경변수에 저장하기
$ export MYNAME
$ env | grep MYNAME

env로 확인해보면 MYNAME으로 저장했던 것이 있음

export했던 것 지우기  (-n : 지우기)
$ export -n MYNAME



___
유용하게 쓰는 기능 **~** 와 **-**
~ 은 홈디렉토리를 의미하고  
\- 는 이전에 있었던 디렉토리로 이동

그래서
$cd ~/가고싶은경로/사용할/수있음


___
셀이 이해하는 ''은 모든 특수문자를 기능을 못하게 한다. 원래 문자로 취급이 된다
""은 $ 

`` 백틱으로 묶어 주게 되면 변수가 아닌 명령어로 인식하게 된다

```
$ echo "I'm at `pwd`"
```
이렇게 하면 `pwd`를 명령어로 인식해서 출력을 해준다
-> I'm at /home/users


백틱을 활용해서 env에 환경변수로 저장해보기
```
$ $HEL=Hello
$ $WOR=World
$ export GREETING="`printf $HEL` `printf $WOR`"
$ env | grep GREETING
```
위의 결과는 변수로 저장한 것을 ` `으로 묶어서 printf함수로 출력한 것을 그대로 GREETING변수에 저장, 그리고 그것을 env 목록에 입력함


