
16진수. a numbering system with base 16
0에서 9까지, 그리고  A, B, C, D, E, F 까지 사용한다  

| Decimal | Binary | Hexadecimal |
| ------- | ------ | ----------- |
| 0       | 0      | 0           |
| 1       | 1      | 1           |
| 2       | 10     | 2           |
| 3       | 11     | 3           |
| 4       | 100    | 4           |
| 5       | 101    | 5           |
| 6       | 110    | 6           |
| 7       | 111    | 7           |
| 8       | 1000   | 8           |
| 9       | 1001   | 9           |
| 10      | 1010   | A           |
| 11      | 1011   | B           |
| 12      | 1100   | C           |
| 13      | 1101   | D           |
| 14      | 1110   | E           |
| 15      | 1111   | F           |


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


## 컴퓨팅에서 16진수를 사용하는 이유!

큰 수(10진수)는 binary를 사용하면 (2진수)로 꽤 길어지게 된다.  에러도 발생할 수 있을 만큼 16~ 32bit 를 사용하게 되면 길고 읽기도 힘들고 복잡해진다 
ex: 1000000000000000 (16bit)  --> 65536

여기에서 binary 를 4bits씩 묶어서 16진수를 사용하면 위의 문제를 해결할 수가 있다고 한다  

4bit씩 묶는다면 가능한 숫자는 0000 에서 1111 이다. 이러면 0 부터 15까지 16진수의 숫자를 세트로 맞출 수 있다  
(위의 표 참고)


### Converting Binary to Hexadecimal
먼저 binary를 4개 (4bit)씩 묶은 다음에 하나씩 매칭을 시킨다  (또 하나의 이유는 2진수의 2의 4승이 2^4가 16이기 때문에 )

1110010101100010

1110   0101   0110   0010

14    5    6   2   (10진수 변환)

E 5 6 2  (16진수로 매칭)
가 된다 



### 16진수에서 10진수로 변환하려면 2진수 변환하듯이 
16^n 으로 계속 더해 주면 된다  
> 만약 8진수이라면 8^n 해준다 

1 4 F 라는 16진수를   
1 * (16^2)  + 4 * (16^1) + 16^0  
256   64  15

335가 된다 


13A 는 
16^2  16^1 이 3개   16^0  의 자리수를 가진다   
그러면   
256   16이 3개있어서 48, 마지막 16^0 의 자리에는 A, A는 10
256 48 10

314가 된다  




### 10진수에서 16진수는 
16으로 계속 나눠준다  . 나머지를 적는다. (remainder)
또 16으로 나눈다. 나머지를 이어 적는다 .
마지막으로 나눌 없을 때의 몫 (result)을 마지막으로 적어준다   

127이라고 하면   16으로 나누면
7 에 15가 남는다   ---> 나머지를 15로 적고
7을  16으로 나누면  나머지는 7, 몫은 0이다   
거꾸로 적어주면  0 7 15, 15는 F 그래서 0는 필요없고 7F 가 된다  

> 10진수에서 2진수로 가는 방법도 동일하다. 단 계산기에서 나누면 나머지를 볼 수가 없다  
> mod 기능을 사용하면 나머지를 알 수가 있다.  흠.. 이러면 몫을 알 수가 없군 ㅋㅋㅋ













