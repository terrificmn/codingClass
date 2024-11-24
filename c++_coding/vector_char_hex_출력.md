# vector char 형태를 hex로 출력
std::cout 을 사용하려면   
먼저 hex 이후 setw(2) 로 2자리로 설정해주고 앞자리가 없을 경우 0으로 채워주는 setfill('0') 을 해주면 되고   
또한 int 로 변환을 해줘야지 제대로 된 결과가 나온다. 

vector 로 구성된 것을 출력할 경우 
> 이미 HEX 형태로 구성이 되어 있는 경우
```cpp
std::vector<unsigned char> char_v = { 0xc2, 0xf8, 0xf8, 0xf7, 0xb5 };
for(unsigned char c : char_v) {
    std::cout << std::hex << std::setw(2) << std::setfill('0') << static_cast<int>(c) << " ";
    // printf("%02x", c);
}
```
물론 c style로 `print("%02x", c);` 를 해주면 아주 간단히 해결 될 수 있음  

