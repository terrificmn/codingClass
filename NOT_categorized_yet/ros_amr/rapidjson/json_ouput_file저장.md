# json output to save a file

save a json file 
```cpp
...생략
std::string json_path = "path/path/json_file.json";

std::string json_str (result_json.GetString(), result_json.GetSize());
std::ofstream of_stream (json_path.c_str(), std::ios::app);
// of_stream << json_str; //(그냥 하면 다음줄이 바로 옆에 붙음)
of_stream << json_str << "\n"
if(!of_stream.good()) {
    throw std::runtime_error("Can't write the json.. open failed");
}
```

여기에서 생략이 많이 되었지만 result_json은 `rapidjson::StringBuffer result_json;` 임   
즉, 이미 json을 다 만들어서 반환된 StringBuffer 를 사용하는 것이고   
예를 들어서 아래 처럼 이미 json으로 만들어진 경우에 사용
```cpp
rapidjson::StringBuffer str_buf;
rapidjson::Writer<rapidjson::StringBuffer> writer(str_buf);
writer.StartObject();
    writer.Key("first_value");
    writer.StartObject();
        writer.Key("number");
        writer.Int(10);
        writer.Key("status");
        writer.Int(0);
    writer.EndObject();
writer.EndObject();
```

ofstream은 약간 함수같은 느낌으로 바로 파라미터를 넣어주면 된다.  
이제 ofstream으로 열어주는데 `std::ofstream`으로 열었을 때 `std::ios::app` 은 마지막 부분부터 수정이 되게 된다   
파일이 없으면 다시 만들어준다  



## json 파일로 부터 열어서 publish가 필요한 경우

여러 방법이 있겠지만, 이미 저장한 string들이 json형태이고 한줄 한줄 저장이 되었기 때문에   
fstream 과 std::getline()을 이용해서 vector를 만들어주는 방법을 사용함


대략적으로는.. 아래와 같은 느낌으로 만들어준다
```cpp
std::fstream fs;
std::vector<std::string> v_json_line;
fs.open(json_path.c_str(), std::ios::in);

if(fs.is_open()) {
    std::string a_line;
    while(getline(fs, a_line)) {
        v_json_line.push_back(a_line);
    }
    ROS_INFO("Json file load finished");
} else {
    ROS_WARN("Json file open failure");
}
```
이제 vector 로 만든 변수에 다 저장이 되었으므로 .size()를 확인해서 (for loop등으로) 퍼블리쉬 하면 됨

mqtt같은 경우는 이미 스트링(json형태)이기 때문에 다른 형태로 변환할 필요 없이 바로 넣어주면 된다. *특히 char형태로 .c_str()을 사용*

> Rapidjson 을 사용해서 다시 뭘 변환해야하나 걱정했지만, 이미 완전한 json형태이기 때문에   
parsing이나, 다시 만들 필요가 없다. (물론 수정이 필요하면 다르겠지만..)


## std::ios:: 종류 in/app/trunc
- std::ios::app  
    append (but not overwrite) : 맨 뒤에서 저장하게 됨 (파일이 없으면 생성)
- std::ios::trunc   
    overwrite : 덮어씌움 --- ofstream의 기본값   

