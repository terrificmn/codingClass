# cartographer log

먼저 lua 파일에서 파라미터로 프린트 되는 log를 안 나오게 할 수 있다. (전부는 아님)  

로컬라이제이션으로 사용하는 lua 파일에 
```
POSE_GRAPH.constraint_builder.log_matches = false
```

이렇게 하면 constraint_2d.cc 파일에서 생성하는 로그가 안나오게 된다. 



## 주석 처리로 처리하려면 

ros_Log_sink.cc 에서 LOG_INFO 부분을 주석처리 해서 사용할 수도 있다

pose_graph_2d.cc 에서 LOG_INFO의 "Remaing work.. " 부분을 주석 처리


constrain_build_2d.cc 에서 options_log_matches() 부분을 주석 처리 할 수도 있다.  
> 단, contrain_build_2d 에서의 로그는 lua파일(위의 설명)로 disable이 가능


