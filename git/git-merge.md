
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

