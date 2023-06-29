# Serial3 write

write()함수를 사용할 경우 0을 넣어주면 빌드 시 에러 발생  

이유는 0 이어서 그런가? 

byte로 형 변환을 해주면 해결

0x00 (HEX) 혹은 0을 사용하는 것은 AScii로 NUL 을 의미하는데 이게 에러가 발생되는 하다   

그래서 byte로 바꿔줘서 널이 아니게 만들어 주는 것

```cpp
Serial3.write((byte)0x00);
```

