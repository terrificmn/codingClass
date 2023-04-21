# c++ string stream
file로 읽은 후에 string으로 변환하는 방법에는 c++에서는 공식적으로는 streams를 이용하는 방법인데    

그 중에 하나가 istreambuf_iterator를 이용, 또 하나는 streambuf를 사용하는 것   

- istreambuf_iterator 사용하기
```cpp
std::ifstream fs("파일패스/file명");
std::string str = std::string(std::istreambuf_iterator<char>(fs), std::istreambuf_iterator<char>());
```


- streambuf를 이용하기
```cpp
std::ifstream fs("파일패스/file명");
// 스트링버퍼로 열면서 빈 스트링 버퍼로 만들어준다
std::ostringstream os = std::ostringstream{};
// 스트링 버퍼로 넣어준다
os << fs.rdbuf();
std::string str = os.str(); //string 변환
```

C 방식은(fread를 사용) 써야 할 코드는 길지만, c++의 stream 방식보다 퍼포먼스 차원에서 빠르다고 한다  

> 뭐 그래도 요새 컴터가 좋아져서;;; 암튼 그렇다고 한다   


## C fread 이용한 코드 샘플
```c
std::string load3(const std::string& path) {

    auto close_file = [](FILE* f){fclose(f);};
    auto holder = std::unique_ptr<FILE, decltype(close_file)>(fopen(path.c_str(), "rb"), close_file);
    if (!holder)
      return "";

    FILE* f = holder.get();

    // in C++17 following lines can be folded into std::filesystem::file_size invocation
    if (fseek(f, 0, SEEK_END) < 0)
      return "";

    const long size = ftell(f);
    if (size < 0)
      return "";

    if (fseek(f, 0, SEEK_SET) < 0)
        return "";

    std::string res;
    res.resize(size);

    // C++17 defines .data() which returns a non-const pointer
    fread(const_cast<char*>(res.data()), 1, size, f);

    return res;
}
```


[참고 사이는 여기](http://0x80.pl/notesen/2019-01-07-cpp-read-file.html)