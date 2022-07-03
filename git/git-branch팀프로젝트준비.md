git branch로 
현재 브랜치 확인

* main

git branch seongmin
[sgtocta@localhost patrol_robot]$ git branch
* main
  seongmin


git checkout seongmin
Switched to branch 'seongmin'

파일 추가 / 수정 후 git status
git add 파일명 

추가 다 할려면 git add .

그리고 커밋
git commit -m "branch commit"

푸쉬 main으로 하면 안되고 branch로
git push -u origin seongmin

pull request가 되면 



메인으로 와서
git checkout -b main

브랜치 삭제(로컬)
git branch -d seongmin


작업을 끝낸 후에 merge시키기. 먼저 main브랜치로 옮겨준다
git checkout main

그리고 main 브랜치에서 merge를 한다. merge는 자기 브랜치를 합치면 된다
```
git merge sm-mapping
```
그러면 merge가 된다

이제 main 브랜치와 sm-mapping이 합쳐짐
그리고 
git status
를 해보면

On branch main
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

이렇게 나온다~ 이미 sm-mapping에서 작업한 내용이 올라갔으므로 여기에서 git push까지 해주면 완료가 되는 것임



거의 쓸 일이 없을 듯
git rebase origin/main
