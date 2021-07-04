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


git pull origin main

git rebase origin/main
