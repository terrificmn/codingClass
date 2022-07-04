기존에는 catkin_make 라는 툴을 사용했는데 이번에는 catkin tools를 사용

[더 자세한 내용은 메뉴얼 페이지를 참고하자 https://catkin-tools.readthedocs.io](https://catkin-tools.readthedocs.io/en/latest/verbs/catkin_config.html)


## Workspace 만들기
mkdir로 디렉토리를 만들어준다음에 이동
```
mkdir ~/tutorial_ws
cd ~/tutorial_ws
```

그리고 catkin build 를 해준다
```
catkin build
```
그러면 build, devel 디렉토리가 만들어진다.   



## config를 merge로 만들기
이 명령어는 config로 설정을 merged로 바꿔준다
```
catkin config --merge-devel
```

```
Devel Space Layout:          linked   

Devel Space Layout:          merged
```

config 로 설정상태 보기
```
catkin config
```

### 지우기
지우기 build devel 을 모두 지워준다
```
catkin clean -b -d
```



