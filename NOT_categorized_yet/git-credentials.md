# git credential 무시하게 하기
private repo 인 경우에도 pull 하거나 할 때 자동으로 되는 경우가 있다.  

아마도 global로 설정이 되어 있거나, 다른 앱 사용 등으로 cache가 되어 있는 경우가 있을 수 있다.  
> 컴퓨터를 공용으로 사용하는 경우 (서버 등) 에 다른 사용자의 설정 등에 의해서 그런 듯 하다.  

어쨋든 특정 private git repo 에서는 해당 기능을 안 사용하려면  
일단 해당 디렉토리로 이동한 후 config 설정은 한번 해준다.  

```
cd my_package
git config --local credential.helper ""
```

empty 스트링으로 만들어서 사용하게 한다. 

해당 패키지의 .git 이하의 config 파일에는 
```
[credential]
        helper =
```

이렇게 만들어져서 확실하게 pull / push 할 경우에,  
확실하게 아이디와 비밀번호를 물어보게 된다.  


## 아예 깃 아이디 및 토큰이 들어가 있는 경우 

아래 처럼 config 에 remote repo 설정에 아예 아이디와 token이 들어가 있는 경우에도 따로 아이디/비번을 skip 하게 된다.  
```
[remote "origin"]
        url = https://my-github-id:ghp_Ely-token@github.com/github-id/package.git
        fetch = +refs/heads/*:
```
