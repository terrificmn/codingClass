# git submodule 추가
## git submodule
내 패키지의 root로 이동, 예를 들어서 my_pkg 라고 하면  
```
cd ~/my_pkg
```

이후 submodule 등록 하는데 여기에서는 실제 깃허브 주소를 넣어주고,   
예를 들어 lib/opentts 라고 디렉토리를 만들면서 깃클론을 해준다.  
```
git submodule add https://github.com/ttsmodule/opentts.git lib/opentts
```
> 해당 디렉토리는 최초 없어도 알아서 만들어주고, 예를 들어서 lib까지만 하면   
lib 디렉토리 이하에 해당 패키지가 클론이 되어서 이름자체가 lib 됨,   
그래서 실제 깃허브의 프로젝트 이름 그대로 사용해주는 것이 좋다   
만약에 예를 들어 opentts 가 실제로는 이름이 openTTS라고 하다면 any-dir/openTTS 라고 해주면 더 좋을 듯 하다.  

그리고 .gitmoulde 에 대한 것도 추가를 해주게 된다.  
```
git add .gitmodules lib/opentts
git commit -m "add opentts as a submodule"
```

그리고 이후 push를 해주면 된다. 

## clone 할 경우
해당 프로젝트를 클론할 경우에는 보통 clone 하는 방식으로 해 준다음에  
꼭 git submodule update 를 해준다 

```
cd ~/my_pkg
git submodule update --init --recursive
```

## 필요시 추가한 sub module 커밋하기  
sub module 이 새로운 커밋이나 checkout 를 하려고 하면 수동으로 변경 후에 다시하면 커밋을 해주면 된다  

예  
```
cd lib/opentts
git checkout new-branch
```
이후 다시 내 로컬의 프로젝트로 이동 후에   
```
cd ~/my_pkg
git commit
```

> 보통 opensource 를 sub-module 로 추가하면 내가 직접 변경하기는 어렵기 때문에   
해당 프로젝트의 변경이 있다면 변경을 하고 사용을 하면 된다  


