# group permission

그룹 권한 추가하기 sudo chmod -R 2775 path-to-dir

2 를 추가하게 되면 setgrp 가 되어서 sub-directory 에는 같은 권한을 물려받게 되는데  
해당 이하에 파일을 생성하거나 디렉토리를 생성하면 group 권한을 가질 수 있게 된다. 

예
drwxrwsr-x 2 amrlabs amr_group 4096  2월 27 13:17 bin

중간에 그룹 권한 표기에 s가 표시가 된다.  

그냥 775 만 했을 경우 
drwxrwxr-x 2 amrlabs amr_group 4096  2월 27 12:51 bin

s가 없다. 단, 그룹 권한이 설정이 되었으므로 해당 디렉토리 또는 파일에서 그룹 권한으로 생성, 삭제, 수정 등이 가능


## umask 
`umask` 를 해보면 결과는 0022 로 나오게 된다.  
그래서 파일을 만들 때 자동으로 그룹 권한은 빠지게 된다.   

유저 권한만 주로 설정하게 된다.  그래서 group 권한이 설정 되어 있다고 해도  
Ftp 등으로 파일을 올리거나 할 때에도 해당 시스템에서 umask 설정했던 것 처럼 설정이 된다. 즉, group 권한이 없어진다.



