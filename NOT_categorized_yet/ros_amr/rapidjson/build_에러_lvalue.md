# rapidjson 관련 빌드시 에러
rapidjson 관련해서 프로그램 작성할 때 lvalue 과련해서 타입 관련 에러가 발생할 경우

```
/home/myuser/catkin_ws/src/mypkg/src/mqtt/json_parsing.cpp:561:65: error: cannot bind non-const lvalue reference of type ‘rapidjson::Value&’ {aka ‘rapidjson::GenericValue<rapidjson::UTF8<> >&’} to an rvalue of type ‘rapidjson::Value’ {aka ‘rapidjson::GenericValue<rapidjson::UTF8<> >’}
  561 |                             this->addNodes(row["nodes"].GetArray());
      |                                            ~~~~~~~~~~~~~~~~~~~~~^~
```

다른 컴에서는 이상없이 빌드 되는 것인데 에러가 발생한다.  
이때 /usr/include/rapidjson 디렉토리를 지운 후에  
다시 rapidjson 클론해서 헤더파일들을 설치한 다음에 다시 빌드하면 정상적으로 빌드가 된다. 

뭔가 다른 헤더와 충돌이 나거나 하는 상황이였던가 싶다.;;;

> 물론 lvalue 관련 에러가 아니고, 같은 코드로 잘 빌드가 되는데, 갑자기 안되는 경우에만 해당

