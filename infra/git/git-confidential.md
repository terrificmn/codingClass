# repository 를 찾을 수 없는 경우 
`Repository not found. fatal: repository`

깃 클론 등을 할려고 하는데 에러가 발생하는 경우   
git 주소가 정확하다면 confidential 문제  

```
git config --global credential.helper
```
로 확인했을 경우  
store, cache 로 나오는 경우에는 이미 저장을 해서 사용하고 있는 경우에 해당해서   
기존의 유저 및 token 이 맞지 않게 된다.   

> 공용으로 컴퓨터를 사용하는 경우에 발생  


해당 리포지터리에서 credential 을 사용 안하게 할 수 있다.  

```
git config --local --unset credential.helper
```
> 해당 프로젝트만 적용이 된다.  



다시 한번 확인 `git config --show-origin --get credential.helper`

안되면 global 로 제거 

```
git config --global --unset credential.helper
```

이렇게 하면 깃 유저와 token을 넣었을 때 잘 작동하게 된다. 