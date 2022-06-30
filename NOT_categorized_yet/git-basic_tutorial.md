실제 사용해 보기- 튜토리얼

일단 git 만들어진 디렉토리에서 a.txt b.txt c.txt를 만들어 본다
  $echo hello world! > a.txt
이런식으로 3개 만들고 

staus확인
  $git status
On branch master

Initial commit

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	a.txt
	b.txt
	c.txt

nothing added to commit but untracked files present (use "git add" to track)
이런식으로 나오게 되는데 
untracked files에 a,b,c.txt 파일이 있는 것을 알 수 있다

다음은 git add를 이용해서 tracked 으로 (commit할 준비를 해주는 것)
git add 파일명으로 staged filed로 추가
  $git add a.txt

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   a.txt

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	b.txt
	c.txt
이렇게 a.txt파일이 변경된 것을 볼 수 있음

  $git add a.txt b.txt 이런식으로 해도 되고
  $git add *.txt 라고 하면 모든파일.txt

  $git add .
git add . 위에처럼 하면 모든 파일을 add 시켜줌

여기에서 add된 파일을 수정하기
  $echo mike >> a.txt
로 파일에 내용을 추가하게 되면 git status에 수정되었다고 나옴

  $git status

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   a.txt
	new file:   b.txt
	new file:   c.txt

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   a.txt
또 이렇게 나옴

즉 git add로 파일을 추가하게 되면 staged files이 되어서 staging area에 들어가게 되고
그런 파일을 수정하게 되면 그 파일은 modified file이 되어서 
untracked 상태로 되어져 있게 됨, 즉 버전 별로 파일이 존재하게 됨

다시 untracked 상태로 바꾸기
  $git rm --cached *

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	a.txt
	b.txt
	c.txt
요렇게 된 것을 알 수 있음

만약 파일이 디렉토리 안에 있을 경우 
fatal: not removing 'phpClass/includes' recursively without -r
에러가 발생

[sgtocta@localhost projects]$ git rm -r --cached *
usage: git rm [<options>] [--] <file>...

    -n, --dry-run         dry run
    -q, --quiet           do not list removed files
    --cached              only remove from the index
    -f, --force           override the up-to-date check
    -r                    allow recursive removal
    --ignore-unmatch      exit with a zero status even if nothing matched
이때에는 -r 옵션을 해줘야하고 --cached 를 꼭 써야함 (index에서 제거하는것은 staging area에서 제거하는 것)
--cached를 안사용하면 파일이 지워질 수도 있다. 

예:
git rm --cached .env
use --cached to keep the file, or -f to force removal
이래야 --cached 옵션을 줘야지 파일이 안 지워진다, -f 옵션이면 파일 지워짐

위처럼 하면 add 한 후 취소를 한 것이 되서 git status를 하면
deleted: .env 
라고 나오지만 실제 파일은 지워지지는 않는다.


<트러블슈팅>
디렉토리가 포함되었을 때는 
  $git rm -r --cached phpClass/*
으로 해주면 됨


트랙킹 하기 싫은 파일 (추가하기 싫은 파일)은 .gitignore 에 넣어준다
예를 들어서 test.log 파일이 있다고 했을 때
  $echo test > test.log
  $echo *.log > .gitignore
을 하게 되면 
또는 그냥 vi로 연 후에 편집 후 저장해도 됨
  $vi .gitignore

  $ls -al 
.gitignore 이 생겨있고 
staus에서 untracked files 로만 나오고 test.log 파일을 추적이 안되고 있음을 알 수 있다
(.gitignore 에 파일형태로 추가할 수 있음)

.gitignore 파일 편집하기
파일에서는 주석 가능 #으로 주석
test.log
또는 특정확장자의 모든파일 
*.log

특정디렉토리 
build/

특정디렉토리의 특정 파일들
build/*.log 

특정디렉토리의 모든 파일
phpClass/uploads/*


변경된 사항 확인할 때는 
$git diff
파일이 변경되었다면 

diff --git a/a.txt b/a.txt
index 7a6f78f..4606027 100644
--- a/a.txt
+++ b/a.txt
@@ -1,2 +1,3 @@
 hello world!
 mike
+add txt
이런식으로 나옴
q를 누르면 빠져나온다

config파일 열어서 설정 추가해주기
  $git config --global -e
해서 vscode가 열리면 파일에 추가해줌
[diff]
	tool = vscode
[difftool "vscode"]
	cmd = code --wait --diff $LOCAL $REMOTE

저장하고 끔. 터미널에서 
$git difftool
이라고 치면 (modified 된 파일이 있다면
Viewing (1/1): 'a.txt'
Launch 'vscode' [Y/n]
으로 나오게 됨 y하면 vscode가 열림

staging area에 있는 파일들 볼려면
  $git difftool --staged

마찬가지로 해당파일을 vscode에서 열겠냐고 물어보고 열어서 확인하면 됨

드디어 commit하기
  $git commit
vscode로 staging area 에 있는 파일이 commit되기 위한 파일이 열림
그럼 맨 위에 Title과 Description을 넣어주고 저장하면 commit이 됨 
(git repository에 넘어가게됨)

아래 처럼 입력 (Title과 Description만 간략하게 적어주면 되는 듯)
Title

Description

# Please enter the commit message for your changes. Lines starting
# with '#' will be ignored, and an empty message aborts the commit.
# On branch master
#
# Initial commit
#
# Changes to be committed:
#	new file:   a.txt
#	new file:   b.txt
#	new file:   c.txt
#
# Changes not staged for commit:
#	modified:   a.txt
#
# Untracked files:
#	.gitignore
#

그리고 저장 후 끄기. 그러면..
[master (root-commit) b1b5c42] Title
 3 files changed, 4 insertions(+)
 create mode 100644 a.txt
 create mode 100644 b.txt
 create mode 100644 c.txt
b1b5c42 해쉬코드 앞부분과 Title이 나오게 됨 
그리고 3개 파일이 created 파일이 생겼다고 나옴

방금 커밋한 히스토리 보기
  $git log

commit b1b5c427d6a6d54043dc75c502e63b99a45dcdac
Author: mike <이메일@gmail.com>
Date:   Mon Jan 11 08:33:25 2021 -0800

    Title

    Description

실제 해쉬코드 전체와 만든사람, 날짜, 타이틀, 설명까지 나오게 됨

간단하게 commit 할때는 -m 을 넣어서 가능

일단 파일을 한개 더 추가한다고 가정하고 파일만든다음에 add
  $echo test add > d.txt
파일만들고 다시 git add  시켜줌
  $git add d.txt 

간단 버전 commit 하기
  $git commit -m "second commit"

[master b58d728] second commit
 1 file changed, 1 insertion(+)
 create mode 100644 d.txt
바로 실행되는 것을 알 수 있음

커밋 옵션에 -a를 붙이면 전부다 커밋하게 됨
(git add로 안하고 staging area와 working directory에 있는 전부다 
모든 게 맘에 든다고 했을 떄 )
  $git commit -am "third commit"

Add 취소하기
모든 file staging 취소하기
  $git reset 

git reset HEAD file명으로 add한 file을 취소할 수 있고 file명을 쓰지 않으면 전체 파일 취소가 된다!
(HEAD는 지금 현재 최신상태)


push 하기
로컬에서 commit이 되었고 remote repository에 업로드 하려면 push 명령어를 사용
  $git push origin main 

**참고: 현재 저장소에서는 main이 branch default로 되어 있음
원래 master였으나 인종차별언어로 main으로 바꾸기로 하였다고 함

그 밖에 Viewing branches (-a 옵션 모든 branches 보기)
  $git branch -a
*main
master 
이런식으로 나옴 (* 되어 있는 것이 default branch)

새로운 branch 만들기 (-b 옵션 뒤에는 만들고 싶은 브랜치명)
  $git checkout -b develop


이것은 oldbranch명을 바꾸는 것  (branch 만드는 것과는 다름)
$git branch -M main 

With a -m or -M option, <oldbranch> will be renamed to <newbranch>. 
If <oldbranch> had a corresponding reflog, 
it is renamed to match <newbranch>, 
and a reflog entry is created to remember the branch renaming. 
If <newbranch> exists, -M must be used to force the rename to happen.


Switched to a new branch 'develop'
이렇게 나옴

브랜치 바꾸기
  $git checkout master
