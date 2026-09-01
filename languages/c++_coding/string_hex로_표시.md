hex로 출력할 경우에 std::cout << std::hex 로 붙여주면 되지만  

이미 hex로 나온 것이 저장된 string 이라고 하면 한 글자씩 변환을 해주기 때문에 맞는 결과가 나오지를 않는다.  
즉 hex 구분 따위가 없는 그냥 string 이기 때문이다  

단순하게 스트링을 `vector<char>` 로 만들기
```cpp
std::string input = "c2f883f7b5";
std::vector<unsigned char> vec(input.begin(), input.end());
for(unsigned char c : vec) {
    std::cout << c << " ";
}
```
이렇게 되면 한 글자씩 출력하게 때문에 hex 코드로 보여줄 수가 없다.  
```
c 2 f 8 8 3 f 7 b 5
```

두 자리씩 다시 만들어 줘야 한다. 
TODO: update

