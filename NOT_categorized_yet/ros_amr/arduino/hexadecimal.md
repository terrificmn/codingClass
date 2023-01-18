
숫자 앞에 0x를 적는다. (prefix) - hexadecimal 이라고 표기하는 듯 하다

```cpp
void setup()
{
  Serial.begin(57600);

  byte b = 0x34;

  Serial.print("b = ");
  Serial.print(b);
  Serial.println(" in decimal");

  Serial.print("b = 0x");
  Serial.print(b, HEX);

  Serial.println(" in hexadecimal");
}

void loop()
{
}
```



Binary에는 0b 또는 0X 가 붙는다    
헥사에는 0x,또는 0X 붙는다 

> 의미는 Binary의 B를 의미하고, heXadecimal의 X를 의미한다
> c++14 부터 0b는 허용되었다고 함 (C standard는 아니라고 함)



참고
```
binary-digit:
    0
    1

octal-digit: one of
    0  1  2  3  4  5  6  7

nonzero-digit: one of
    1  2  3  4  5  6  7  8  9

hexadecimal-prefix: one of
    0x  0X

hexadecimal-digit-sequence:
    hexadecimal-digit
    hexadecimal-digit-sequence 'opt hexadecimal-digit

hexadecimal-digit: one of
    0  1  2  3  4  5  6  7  8  9
    a  b  c  d  e  f
    A  B  C  D  E  F
```

