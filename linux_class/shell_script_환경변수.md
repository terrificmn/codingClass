먼저 쉘 스크립트를 하나 만들어준다  
휴지통 만들기

```shell
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
```shell
cd /스크립트/to/있는곳/이동
export PATH=$PATH:`pwd`
```
`:`의 의미는 배열로 읽어서 기존 환경변수 PATH에 이어서 :(콜론) 으로 구분을 해주게 된다는 의미.   
그래서 기존에 $PATH의 값을 가지고 와서 현재 경로 넣어준다.   
(만약 PATH=string)이렇게 넣어버리면 기존의 PATH값에 새로운 값인 string값이 들어가게 되므로 주의  
스크립트 파일을 실행하게 되면 각 경로에서 실행되는 파일이 있는지 확인하게 되는 것  
pwd라는 명령어를 실행해서 현재 위치를 넣어주기 위해서 백틱으로 ` `감싸준다  

그리고 실행권한을 755로 설정 (스크립트 파일의 권한을 바꿔준다)
```shell
$ chown 755 moveall
```

그리고 최종적으로 파일을 지운다고 가정하고 옮길 파일을 touch 로 만들어 준다   
test 디렉토리를 만들고 이동을 한 후 파일을 마구 만들어 준다
```shell
$mkdir test && cd test
$touch 123 124 wer 124 adsfl 235lkj zdk tij 234ijadf alek234 23lk4jqwe
```
   
파일을 옮기고 싶은 곳으로 가서 mval을 실행하면 됨    
끝


환경변수 추가 설명   
원래는 해당 스크립트가 있는 디렉토리로    
~/SchoolLinux/learning/shell_script_prac 로 이동해서 직접 실행을 해야하는데   

만약 다른 경로에서 실행을 하면    
실행이 안됨    
Command 'mval' not found, did you mean:   
이렇게 실행이 안됨

그래서 위에서 환경변수 PATH에 디렉토리 위치를 (`pwd`) 로 등록하게 되면    
실행을 했을 때 PATH에 들어가 있는 디렉토리를 다 찾아서 보게 되는데   
마침 쉘스크립트가 있는 디렉토리가 있으므로 그 디렉토리에서도  
해당파일 (mval)이라는 파일이 있는지 확인하고 있으니 실행이 되는것 
