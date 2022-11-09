
### nested json 
```json
{
	"class":
	{
		"subject": "english",
		"level": 5
	}
}
```

이런식으로 중첩이 되어 있다고 하면   
Document를 만들고 Parse()로 만들어 준다음에 해당 class를 특정 변수에 넣어준 (예: result)
이제 result는 해당 class의 내용을 가지고 있으므로 GetInt()함수를 사용하면 됨

```cpp
using namespace rapidjson;
Document document;
document.Parse(json_string.c_str());

#변수에 넣어준다음에 바로 출력할 수 있다
Value& result = document["class"];

ROS_INFO("Extracted From JSON string \nsubject : %s\n", result["subject"].GetString());
ROS_INFO("Extracted From JSON string \nheader : %d\n", result["level"].GetInt());

```



### Document를 만든 후에 array이면 

```cpp
using namespace rapidjson;
Document document;
document.Parse(json_string.c_str());

Value& a_array = document["array_example"];
assert(a_array.IsArray());

# 이제 for문을 돌려준다
for(SizeType i=0; i < a_array.Size(); i++)  { // Uses SizeType instead of size_t
	printf("a_array[%d] = %d\n", i, a_array[i].GetInt());
}
```

