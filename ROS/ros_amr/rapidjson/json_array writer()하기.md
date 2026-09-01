# rapid json 을 사용해서 array 만들기

array를 만들 때는 writer의 StartArray() 메소드를 사용한다  
보통 만들 때 Key() , String() 메소드를 사용했는데  

Key()는 필요가 없게된다  


```cpp
rapidjson::StringBuffer strbuf;
rapidjson::Writer<rapidjson::StringBuffer> writer(strbuf);

writer.StartObject();
	writer.StartArray();
		writer.String("0 1 2 3");
	writer.EndArray();
writer.EndObject();

std::cout << strbuf.GetString() << std::endl;

```
처럼 하게 되면 
```json
{ [0, 1, 2, 3] }
```

이런식으로 생성이 된다  

그러면 중첩을 만들려고 해도 StartArray() 는 키 값을 줄 수가 없고 배열의 value만 넣어줄 수가 있다  

그래서 StartArray()를 하고 그 안에 중첩으로 다시 StartObject()메소드를 사용해서 만들어 주면 된다 

```cpp
writer.StartObject();
	writer.Key("array");
	writer.StartArray();
		writer.StartObject();
			writer.Key("pos_x");
			writer.String("0.123");
			writer.Key("pos_y");
			writer.String("1.63");
		writer.EndObject();
	writer.EndArray();
writer.EndObject();
```

그러면 아래처럼 중첩으로 json을 array로 구성할 수가 있다
```json

{ "array": ["pos_x": "0.123", "pos_y": "1.63"] }
```

검증은 안해보았지만 암튼 위와 같은 방식이다   

ROS msg를 받은 것을 이제 for loop를 이용해서 넣어주면 되겠다.   
예를 들어 double 형을 string으로 바꿀 때는 std::to_string() 을 사용한다   

```cpp
writer.StartArray();
	for(int i=0; i< pathArray.size(); i++) {
		writer.StartObject();
			writer.Key("pos_x");
			writer.String(std::to_string(pathArray.at(i).pose.position.x).c_str());
			writer.Key("pos_y");
			writer.String(std::to_string(pathArray.at(i).pose.position.y).c_str());
		writer.EndObject();
	}
writer.EndArray();
```

