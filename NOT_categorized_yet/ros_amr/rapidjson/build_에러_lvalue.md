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

## release 버전, zip 다운로드 시
공식 사이트등에서 다운로드로 zip 파일등으로 받아서 include 디렉토리에 넣어서 사용하는 경우에  
```
/usr/local/include/rapidjson/document.h: In member function ‘rapidjson::GenericStringRef<CharType>& rapidjson::GenericStringRef<CharType>::operator=(const rapidjson::GenericStringRef<CharType>&)’:
/usr/local/include/rapidjson/document.h:319:82: error: assignment of read-only member ‘rapidjson::GenericStringRef<CharType>::length’
  319 |     GenericStringRef& operator=(const GenericStringRef& rhs) { s = rhs.s; length = rhs.length; }
```

이렇게 에러가 발생했다.  
코드 없이 header파일만 include 만 했는데도 빌드 시 에러가 발생. json버전이 1.1.(이하 버전 숫자는 모르겠음)   

그냥 include만 하면 안 되는 모양인가? 더 트러블 슈팅은 안하고  
깃허브에서 클론 후에 include 이하의 rapidjson을 /usr/local/include 에 넣어 주는 방식으로 진행했더니   
빌드 에러가 해결됐다.

