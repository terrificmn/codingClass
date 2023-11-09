# cartographer log

먼저 lua 파일에서 파라미터로 프린트 되는 log를 안 나오게 할 수 있다. (전부는 아님)  

로컬라이제이션으로 사용하는 lua 파일에 
```
POSE_GRAPH.constraint_builder.log_matches = false
```

이렇게 하면 constraint_2d.cc 파일에서 생성하는 로그가 안나오게 된다. 