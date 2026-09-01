그 전 작업은 기존에 만들었던 것 복사해서 만들어 놓기


commit 후 푸쉬하기  
주의 할 점은 main으로 push하는 것이 아니고 자신이 만든 branch명으로 푸쉬를 해야한다
```
git push -u origin sidedev
```
Branch 'sidedev' set up to track remote branch 'sidedev' from 'origin'.

어느정도 sidebar 작업이 마무리가 된 듯 하여서 

Compare & pull request 버튼을 눌러서 요청을 한다

branch 끼리 충돌 없는지를 자동으로 확인해 준다.
예를 들어 
Able to merge. These branches can be automatically merged.  이런식으로 표시가 됨

간단하게 Write 부분에 적어준다. 

그리고 Create Pull request 를 눌러준다.

그러면 
terrificmn wants to merge 2 commits into main from sidedev

main브랜치에 sidedev브랜치를 병합하고 싶다고 안내가 나오면서 페이지가 바뀐다.

아마도 이부분에서 팀장이나 선임이 내용을 확인해보고 merge를 할지 최종 결정하는 단계가 되는 듯 하다

> 현업이 아니여서 잘 모름 ㅋㅋ ㅠㅠ

그러면 This branch has no conflicts with the base branch
Merging can be performed automatically. 

merge해도 괜찮다고 안내가 나온다. 
이제 
Merge pull request 버튼을 눌르자. 

> 여기에 options이 3개나 되는데 아.. Squash and merge, RAebase and merge...잘 모르겠다..

이제 버튼이 
Confirm merge로 바뀌는데 한번 더 눌러준다

그리고 branch를 지울꺼냐고 물어본다.  
그래서 지워봤다. 

브랜치도 잘 지워졌다. 
그러면 일단 깃허브에서는 끝!

브랜치에서도 표시가 더 이상 안된다.


이제 배포한 서버에 가서 깃 pull을 해 줍시다. 

[linlb@webblog-01-prod src]$ git st
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean

git fetch 를 해서 remote repo로 부터 최신화를 해준다. merge/rebase를 하지 않는다. 

```
[linlb@webblog-01-prod src]$ git fetch
remote: Enumerating objects: 67, done.
remote: Counting objects: 100% (67/67), done.
remote: Compressing objects: 100% (14/14), done.
remote: Total 45 (delta 30), reused 41 (delta 28), pack-reused 0
Unpacking objects: 100% (45/45), 20.78 KiB | 417.00 KiB/s, done.
From https://github.com/terrificmn/laravelBlog
   3f9c7e1..6aa6832  main       -> origin/main
[linlb@webblog-01-prod src]$ git st
On branch main
Your branch is behind 'origin/main' by 3 commits, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean

```
편집 필요

최신화가 되었으므로 브랜치가 최신화 되어 있다고 나와있었지만 fetch이후   
main 브랜치로 부터 3 commits 가 뒤쳐저 있다고 나옴   

이제 git pull 을 하자
```
git pull origin main
```

최신 업데이트가 배포가 되었다. 

## 한편 로컬에서는 

이제 로컬에서도 브랜치를 이동해 줍니다.

git checkout main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
[sgtocta@localhost src]$ git branch
* main
  sidedev
[sgtocta@localhost src]$ git st
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean


이제 로컬에서  main 를 확인해보면 main에는 sidedev에서 작업했던 내용들이 전혀 보이지 않는다. 
병합을 했었는데??

참 신기한게 branch를 바꾸니 작업했던 파일들이 보이지를 않는다. 
(사진)

다시 git checkout sidedev 를 입려갷서 넘어와서 다시 파일을 확인해보니
(사진)

즉, remote인 깃 허브에는 sidedev 브랜치 내용이 main 브랜치에 잘 병합이 되어서 끝이났지만  
로컬에서는 아직 병합이 되지 않는 상태인 것이다.  

> remote인 깃허브에는 따로 push를 해서 나중에 병합을 했으니 이해가 가는데  
로컬에서 내가 작업한 디렉토리에서도 브랜치를 변경하니~ 내용이 사라지는게 좀 신기했다 (그리고 헤깔린다 ㅋㅋㅋ)

만약 브랜치를 살려서 계속 작업을 한다면 계속 두면 될 듯 하고  
그게 아니고 여기고 최신화를 하고 싶다하면 merge를 진행해야한다

대충 작업이 마무리가 되어서 merge를 하려고 한다 

먼저 main으로 체크아웃

```
git checkout main
```
main으로 바뀐 후 
```
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
```

여기 main 브랜치는 변경한 적이 없었으니깐 fast-farward 방식으로 합쳐진다   
merge [병합할블랜치명] 명령어를 사용

```
git merge sidedev
```

그러면 merge가 진행되고
```
Updating 3f9c7e1..096da9f
Fast-forward
 app/Http/Controllers/CategoryController.php           |  21 ++
 app/Http/Controllers/PostController.php               |  57 ++++-
...생략...
```

이제 git status를 해본다 
```
On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```
오히려 2번의 commit이 앞서있다고 push를 하라고 한다. 뭔가 이상하다~  아마도 마지막 sidedev에서 마지막으로 commit을 한 시점으로 병합이 되는 듯하다. 

하지만 이미 깃허브에서는 병합이 끝났으므로   
git fetch를 해줘서 remote 리포지터리의 정보를 가져오자
```
git fetch
```

다시 git status를 해보면
```
git status
```

이제야 좀 제대로 나오는 듯 하다
```
On branch main
Your branch is behind 'origin/main' by 1 commit, and can be fast-forwarded.
  (use "git pull" to update your local branch)

nothing to commit, working tree clean
```

fast-forwarded를 받기위해서 git pull을 해주자
```
git pull origin main
```

만약 아래와 같은 warning이 발생한다면 
```
warning: Pulling without specifying how to reconcile divergent branches is
discouraged. You can squelch this message by running one of the following
commands sometime before your next pull:

  git config pull.rebase false  # merge (the default strategy)
  git config pull.rebase true   # rebase
  git config pull.ff only       # fast-forward only

You can replace "git config" with "git config --global" to set a default
preference for all repositories. You can also pass --rebase, --no-rebase,
or --ff-only on the command line to override the configured default per
invocation.
```

git config pull 관련해서 수정해달라는 말인데  
그냥 
```
git pull origin main --ff-only
```
로 처리했다~

이 부분은 좀 더 알아봐야겠다~


마지막으로 이제 필요없는 브랜치를 지우기   
git branch -d [브랜치명]
```
git branch -d sidedev
```

