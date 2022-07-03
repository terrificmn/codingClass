# git 사용 관련 에러 및 트러블 슈팅
git 사용 관련 에러 및 트러블 슈팅

## 깃 허브에 commit을 push할 때 워닝
CentOS 계열에서 깃을 commit 후 push 하면 아래와 같은 waring 메세지가 나온다
```
Gtk-Message: 04:29:58.177: Failed to load module "canberra-gtk-module"
Gtk-Message: 04:30:01.473: Failed to load module "canberra-gtk-module"
```

libcanberra-gtk-module 가 필요하다는데, 이건 이미 설치가 되어 있다   
git push하는데 따로 문제가 발생하지는 않음

그래도 해결 방법은 
```shell
$sudo yum install libcanberra-gtk2
```

이제 깃 허브 푸쉬할 때 warning message가 뜨지 않는다. 

우분투에서 해결책으로 나와 있는 것들이  
libcanberra-gtk3 libcanberra-gtk-module 설치   
테스트는 해보지 못함



## push 했을 때 refjected 에러 main -> main (non-fast-forward)>
트러블슈팅 refjected 에러 main -> main (non-fast-forward)  
```shell
[cta@localhost projects]$ git push origin main
To https://github.com/terrificmn/codingClass.git
 ! [rejected]        main -> main (non-fast-forward)
error: failed to push some refs to 'https://github.com/terrificmn/codingClass.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```
이런 문제가 생기는 이유는 non-fast-forward 라고 하는데   
remote와 local의 commit이 일치하지 않아서 그렇다고 함   
무조건 올리는 족족 할 수 있는 줄 알았는데 아니였다.

먼저 원격의 저장소 pull 받기 (origin은 git config로 등록해두기(원격 repo))  
```
  $git pull --rebase origin main
```
그러면 conflict가 있는 것을 해결 후 --continue 또는 --skip을 하라고 되어 있는데   
일단 --continue를 해야하나 바꿀게 따로 없어서 그냥 skip을 함  
```
  $git rebase --skip
```
그 다음에 다시 모든 staging상태로 만들기 위해서 다시 add 후 commit   
```
  $git add .
  $git commit 
```
vscode가 뜨면 Title만 적어주고 저장 후 나감 (vscode로 core.editor 등록 되어 있음)

다시 git status 보기
```
  $git status
```
아래처럼 나오면 성공
```
On branch main
nothing to commit, working tree clean
```
ㅠㅠ오오굿 clean!

마지막으로 remote저장소에 push 하자
```
  $git push origin main
```
잘 된다.

**참고: 아직은 배우는 단계라 나중에 다시 수정 요망   
아마도 로컬 저장소와 원격 저장소의 상태가 적어도 서로 어떤파일들이 수정되고 commit되었는지   
알고 있어야 하는 것 같다. 테스트로 파일들을 remote로 몇개 올려보고   
본격적으로 할려고 remote repository에 있는 파일들을 지웠던게 화근인듯하다   
그러면 로컬에서 pull을 하면 원격에서는 파일이 지워져있고 로컬에서는 지운적이 없으니
서로 충돌(?)이 나는 듯 하다. 그냥 블로그나 이메일 보내듯이 파일을 올리는 것은  아닌듯하다.   

흠.. 쉬우면서도 복잡하다 ㅠ


## error: insufficient permission for adding an object to repository database .git/objects
```
error: insufficient permission for adding an object to repository database .git/objects
fatal: failed to write object
fatal: unpack-objects failed
```
깃 pull 할 때 퍼미션 에러나는 경우  
디렉토리를 다 찾아봐도 퍼미션 문제 있어 보이는 경우는 없었는데

전에 학교에 서둘르다가 PUSH 를 하면서 뭔가 꼬였던거 같은데   
그게 집에서 PULL받는거랑 관계가 있지는 않은거 같은데 어쨌든 파일도 별로 문제가 있어보이지는 않는데   
```
drwxrwxr-x.  8 root root 201 Mar 17 22:29  .git
```

어쨋든 해결책은 chown 자신의 계정으로 소유권 가져오기  
```
sudo chown -R cta:cta .git
```
.git 파일의 그룹 권한을 다시 주고 다시 pull 하니 깔끔하게 됨  



