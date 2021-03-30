먼저 쉘 스크립트를 하나 만들어준다
휴지통 만들기

```
#!/bin/sh

files=`ls`

echo $filies

for filename in $files
do
        echo $filename
        mv $filename $HOME/SchoolLinux/learning/trashStorage

done

exit 0
```

ls 명령어를 ` ` 백틱으로 묶어서 실행한 것을 files 변수에 넣어준다

for do문을 실행하게 되는데 $files에서 하나씩 꺼내와서 filename변수에 넣어주면서 반복
실제로는 파일이 mv 명령어로 특정경로로 이동시키게 된다

for문은 done으로 끝남


환경변수에 등록해주기- 어디에서든 실행할 수 있게 하기
먼저 스크립트 파일이 있는 곳으로 이동하기
```
cd /스크립트/to/있는곳/이동
export PATH=$PATH:`pwd`
```
`:`의 의미는 배열의 의미가 된다 PATH환경 변수에 실행할 수 있는 경로가 지정되고 
스크립트 파일을 실행하게 되면 각 경로에서 실행되는 파일이 있는지 확인하게 되는 것

그리고 실행권한을 755로 설정 (스크립트 파일의 권한을 바꿔준다)
```
$ chown 755 moveall
```

그리고 최종적으로 파일을 지운다고 가정하고 옮길 파일을 touch 로 만들어 준다
test 디렉토리를 만들고 이동을 한 후 파일을 마구 만들어 준다
```
$mkdir test && cd test
$touch 123 124 wer 124 adsfl 235lkj zdk tij 234ijadf alek234 23lk4jqwe
```




