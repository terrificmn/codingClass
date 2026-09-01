
```
time stamp
int64 num1
```
이렇게 만들어 놓고 msg파일   
이런 에러 발생

```
warning: format ‘%d’ expects argument of type ‘int’, but argument 8 has type ‘yh_topic_service::pubNumber_<std::allocator<void> >::_num1_type {aka long int}’ [-Wformat=]
```

ROS_INFO("send msg = %d", msg.stamp.sec); 이런식으로 하면 에러가 나며   
%ld 및 (long int)로 바꿔야 한다니면 int32로 바꾼다

