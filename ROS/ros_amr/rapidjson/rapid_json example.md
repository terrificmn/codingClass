# rapid json writer 예제
writer를 이용해서 json 형태의 string을 만들 수 있다

[apidjson/tree/master/example여기에서확인](https://github.com/Tencent/rapidjson/tree/master/example)

```cpp
#include "rapidjson/writer.h"
#include "rapidjson/stringbuffer.h"
#include <iostream>
using namespace rapidjson;
using namespace std;

int main() {
	StringBuffer s;
	Writer<StringBuffer> writer(s);
	writer.StartObject(); // Between StartObject()/EndObject(),
	writer.Key("hello"); // output a key,
	writer.String("world"); // follow by a value.
	writer.Key("t");
	writer.Bool(true);
	writer.Key("f");
	writer.Bool(false);
	writer.Key("n");
	writer.Null();
	writer.Key("i");
	writer.Uint(123);
	writer.Key("pi");
	writer.Double(3.1416);
	writer.Key("a");
	writer.StartArray(); // Between StartArray()/EndArray(),
	
	for (unsigned i = 0; i < 4; i++)
		writer.Uint(i); // all values are elements of the array.
		writer.EndArray();
	writer.EndObject();
	
	
	cout << s.GetString() << endl;
return 0;
}
```

결과
```
{"hello":"world","t":true,"f":false,"n":null,"i":123,"pi":3.1416,"a":[0,1,2,3]}
```

