
만약 develop 브랜치에 main 브랜치의 최신 버전을 반영하고 싶으면  fetch를 한 후 정보를 받아오고   

## Step 1: From your project repository, bring in the changes and test.

```
git fetch origin
git checkout develop origin/develop
git merge main
```

## Step 2: 또는 conflicts 가 없을 경우에는   (위의 방법으로 실행해도 됨)
먼저 develop (각자 브랜치)로 이동한 후에   git pull origin main 으로 실행 
```
git checkout develop
git fetch
git pull origin main
```

이렇게 하면 알아서 merge를 시켜준다. 자동으로 merge관련해서 실행되는데 (code로 연결되어 있으면 실행됨)  또는 nano?   
'recursive' strategy 로 merge가 된다고 함 

그래서 `git log`로 확인을 해보면 commit이 되어 있다    
```
Merge branch 'main' of https://github.com/te*******n/****ros into develop
```


## Step 3: Merge the changes and update on GitHub.

이 방법은 로컬 main으로 이동한 후에 메인에서 develop 브랜치를 merge 한 다음에   
push 해주는 방법
```
git checkout main
git merge --no-ff develop
git push origin main
```


conflicts가 있을 경우에는 
```
git merge --abort
```


## remote 에서 PR 하기

다른 branch에서 작업을 해서 push를 하게 되면 PR Pull Request를 할 수가 있다   
github에서 해당 리포지터리의 main 브랜치에서 PR을 하게 되면   
특정 브랜치에서 main으로 PR을 하게 되고  
몇번의 Pull Request 버튼 및 Merge 승인을 누르게 되면  
자동으로 병합이 된다.  물론 문제가 없을 경우   

main에서 갈라져 나온 브랜치에서 작업을 하고 main은 작업을 안했을 경우에는 거의 문제 없이  
Merge pull request가 완료된다   

이후 해당 브랜치를 삭제하겠냐고 나오는데, 삭제해도 되고 안해도 되는 듯 하다   


## local에서 PR이후 main 브랜치 pull 받기
이제 로컬에서는 main으로 이동 후에 
```
git checkout main
git pull origin main
```
pull 을 받으면 되고, local에서 작업하던 브랜치.. 예를 들면 devel 브랜치라고 하면   
지울 수도 있다 


#### 브랜치 삭제
```
git branch 
```
로 확인 한 후 * 표시로 다른 브랜치에 현재 상태를 확인 한 후에    
(지우려면) 삭제한다  

```
git branch -d devel
```



