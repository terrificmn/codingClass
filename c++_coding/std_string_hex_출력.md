# std string HEX
iostream 을 이용해서 cout 으로 데이터를 출력하면 보통 헥사 값은 화면에서 깨지면서 나오게 된다   

그래서 헥사 값으로 프린트를 하려고 하면 `std::hex` 를 사용해 준다
```cpp
uint16_t my_data = 0xFF;
std::cout << "HEX value: " << std::hex << my_data << std::endl;
```

만약 int, uint16_t 등으로 선언했다면 정상적으로 출력이 되나,   
데이터형이 적은 uint8_t 등이라면  **�** 이런식으로 글자가 깨지게 된다  
이때 (int)로 캐스팅 변환을 해준후 출력을 하면 잘 나오게 된다  

```cpp
uint8_t my_data = 0xFF;
std::cout << "HEX value: " << std::hex << (int)my_data << std::endl;
```

