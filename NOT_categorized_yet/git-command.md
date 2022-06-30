git 주요 명령어

일단 깃을 사용할 디렉토리를 만들어 준다
  $mkdir projects

해당 디렉토리 이동 cd git 으로 이동해서 초기화시키기 (repositiory 만들어 줌)
  $cd projects
  $git init

Initialized empty Git repository in /home/sgtocta/projects/git/.git/
이렇게 나옴, local에 git 할 준비가 된 것 임

파일 보기 (숨긴파일도 보기)
  $ls -al 해서 보면
drwxrwxr-x. 7 sgtocta sgtocta 119 Jan 11 07:36 .git
.git 요렇게 숨어 있음

git 지우려면 
  $rm -rf .git

깃 상태 보기
  $git status

자주 쓰는 명령어 alias 설정하기
(alias.단축으로쓸별칭 실제명령어)
  $git config --global alias.st status

깃 사용하다가 수정된 부분 버리기 
(add 하기전에 working directory에서 작업 중인 내용
즉, modified상태일 떄 반영하기 싫고 예전으로 돌아갈 떄)
예: git checkout filename 
$ git checkout resources/views/blog/create.blade.php

이러면 파일이 수정하기 전 상태로 돌아간다. 지워지는것은 아님

실 사용은 모르고 push (학교에서) 를 안한 상태에서 작업을 하려고 했더니 최신화가 안되어 있음
현재 집에서는 pull 해도 예전 최신상태.. 
작업은 하고 싶고, 그래서 일단 작업을 하고 수정된 내용을 따로 저장해둔다음에 
충돌을 방지하기 위해서 다시 작업내용을 discard 시킴
이제 최신본에 수정한거 합친다음에 push 하면 되겠다

아마 이럴 때 branch를 사용하는 거 같은데, 잘몰라서;; 일단 이런 방식으로 
근데 branch도 서로 같은 파일은 수정하는것은 아닐것같기도 하고;; 공부가 더 필요하다


깃 하나의 브랜치에서만 클론하기
git clone -b occupancy-mapping --single-branch https://github.com/IntelRealSense/realsense-ros
