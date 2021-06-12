time stamp
int64 num1

이렇게 만들어 놓고 msg파일

ROS_INFO("send msg = %d", msg.stamp.sec); 이런식으로 하면 에러가 나며
(long int)로 바꿔야 한다

warning: format ‘%d’ expects argument of type ‘int’, but argument 8 has type ‘yh_topic_service::pubNumber_<std::allocator<void> >::_num1_type {aka long int}’ [-Wformat=]

이런 에러 발생

아니면 
int32로 선언

---

cpp BASIC

케이스문 알아보기
switch case
```cpp


switch(조건) {
    case  ; break;

    default;
}

```

do while 문 문법
```cpp
int count = 11;
do {
    cout << "hello c++ world" << endl;
} while (count <= 10) {

}
```
do 는 while의 조건과는 상관없이 한번은 실행한다

while은 조건이 참이면 계속 루프
```cpp
int count = 0
while (count <= 10) {
    cout << "hello c++ world" << count << endl;
    count++;
}
```
