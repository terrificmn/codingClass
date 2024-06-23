# object type 찾기 기본
json에서 object 형태라고 하면 key : value 형태가 멀티로 되어 있을 경우

예를 들어 이런 형태.
```json
{
    "nano" : {
        "number" : 123, 
        "name" : "hello"
    },
    "micro" : {
        "number" : 123, 
        "name" : "hello2"
    }
}
```

GetType() 함수를 사용해서 확인도 가능하고, 
몇번 이였는지는 기록을 못함, 다음에 다시 확인

또는 IsObject() 등의 함수로 사용

```cpp
rapidjson::Type t = my_object["nano"].GetType();
ROS_WARN("type is %d", t);

if(my_object["nano"].IsObject()) {
    ROS_WARN("yes");
}
```
