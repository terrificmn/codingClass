JSON 형태의 string을 받아서 이것을 사용하려면

c++ 같은 경우에는 const char* json_str 형태로 받게됨


인쿠르드 먼저  
```cpp
#include "rapidjson/document.h"
```

그 다음에는 
Document 클래스를 이용해서 객체를 만들어준다  

```cpp
using namespace rapidjson;

Document document;
```

json_str 변수에 JSON 형태의 문자열이 들어있다고 하면  
```JSON
{"Address":"04-7C-","X":56.594026227888335,"Y":-75.24767115185566, "Z":10.257462157745}
```

보기 편하게...
```JSON
{
	"Address":"04-7C-",
	"X":56.594026227888335,
	"Y":-75.24767115185566,
	"Z":10.257462157745
}
```


json_str 을 Parse() 메소드를 사용해서 DOM 형태의 tree 구조로 만들어진다    


 이제 각각 멤버에 있는지? 문자열인지? 정수? 인지 쿼리를 진행한 후  
```cpp
assert(document.HasMember("Address"));
assert(document["Address"].IsString());
```
이제 문제가 없다면 GetString() 메소드를 이용해서 내용 가져온다   

```cpp
ROS_INFO("Address is %s", document["Address"].GetString());
// 또는
std::cout << document["Address"].GetString();
```


X, Y, Z는 각각 IsNumber()로 쿼리 후 IsDouble()로 다시 한번 타입 확인  
```cpp
assert(document["X"].IsNumber());
assert(document["X"].IsDouble());

assert(document["Y"].IsNumber());
assert(document["Y"].IsDouble());
```

각각 내용을 사용하려면  GetDouble(); 이용한다 
```cpp
std::cout << document["X"].GetDouble();
```

그 밖에 타입 쿼리 확인은
bool type 은 IsBool()  
null 확인은 IsNull()  
인트는 IsNumber() , IsInt()

각각, Get**()형태의 메소드를 불러서 사용
```cpp
document["t"].GetBool();   
document["i"].GetInt();   

```

[더 자세한 내용은 공식 튜토리얼 확인](https://rapidjson.org/md_doc_tutorial.html)