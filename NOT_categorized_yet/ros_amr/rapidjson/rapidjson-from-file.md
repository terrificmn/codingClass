# rapidjson from file 해서 string 만들기

```cpp
    std::string path = "/home/myuser/myjson.json";
    
    // read from file
    FILE* fp = fopen(path.c_str(), "r");
    if(fp == nullptr) {
        ROS_ERROR("%s file not found.", path.c_str());
        /// return 등 false 처리
    }

    /// rapidjson의 FileReadStream 을 이용해서 FILE을 넘겨서 읽는다.
    char readBuffer[65536];
    rapidjson::FileReadStream inputStream(fp, readBuffer, sizeof(readBuffer));

    rapidjson::Document d;
    d.ParseStream(inputStream);
    fclose(fp);

    if(!d.IsObject() || !d.HasMember("map")) {
        /// 에러 처리하기
    }

    /// 이제 d 는 이미 파싱이 되었으므로 바로 스트링으로 만들 수가 있다.
    rapidjson::StringBuffer strbuf; 
    rapidjson::Writer<rapidjson::StringBuffer> writer(strbuf);
    d.Accept(writer);

    std::cout << "file read: json: \n\n";
    std::cout << strbuf.GetString() << std::endl;

    return true;
```




```cpp
std::string path = "/home/myuser/myjson.json";
    
    // read from file
    FILE* fp = fopen(path.c_str(), "r");
    if(fp == nullptr) {
        ROS_ERROR("%s file not found.", path.c_str());
        /// return 등 false 처리
    }

    /// rapidjson의 FileReadStream 을 이용해서 FILE을 넘겨서 읽는다.
    char readBuffer[65536];
    rapidjson::FileReadStream inputStream(fp, readBuffer, sizeof(readBuffer));

    rapidjson::Document d;
    d.ParseStream(inputStream);
    fclose(fp);

/*
    {
        "my_object": {
            "my_key": 1234,
            "my_key2": 1234,
            "my_kye3": "123"
        }
    }
*/
// json 파일을 읽어서 해당 오브젝트를 다시 만들고 싶다면 
/// 다시 Document를 만들어 주고, object 이므로 json object를 만들고, document 객체에 AddMemeber() 할당 해준다.
/// 그냥 key라면 AddMemeber() 를 활용 (object 없이 활용) 

    // 만약 위에서 이어서 json 파일을 열었고 object라면
    rapidjson::Value& my_read_object = d["my_object"];
    // Value 에 넣어준다. 이때 GetObject()를 하지 않는다.

    // 이제 위에서 만든 d는 역활을 다 함.
    rapidjson::Document new_docu;
    new_docu.SetObject();

    rapidjson::Document::AllocatorType& allocator = new_docu.GetAllocator();

    rapidjson::Value myObject(rapidjson::kObjectType);
    myObject.AddMember("key1", 0, allocator);
    myObject.AddMember("key2", 1, allocator);
    new_docu.AddMember("myObject", headerObject, allocator);
    //  "myObject" 이름으로 key1, key2 가 만들어지고 이를 new_docu 에 할당해주게 됨

    rapidjson::Value alreadyReadObject(rapidjson::kObjectType);
    bodyObject.AddMember("myReadObject", my_read_object, allocator);
    new_docu.AddMember("body", alreadyReadObject, allocator);
    /// newe_docu 에 위에서 읽었던 object를 "myReadObject" key 이름으로 다시 할당해준다. 
    
    rapidjson::StringBuffer strbuf; 
    rapidjson::Writer<rapidjson::StringBuffer> writer(strbuf);
    new_docu.Accept(writer);

    /// 이제 strbuf 를 .GetString() 하게 되면 스트링을 받을 수 있다.

```

/// TODO: 테스트 해보기!