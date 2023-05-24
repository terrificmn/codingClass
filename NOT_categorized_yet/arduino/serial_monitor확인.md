# serial monitor 활용

serial을 이용해서 통신을 할 때~ 데이터가 잘 전송이 되고 있는지 확인을 하기 위해서는   
serial monitor 프로그램 등을 사용하면 되는데   

vscode의 PlatformIO을 사용해서, 해당 보드를 선택을 해준 다음에   
예를 들어 stm32f..  이렇게 검색을 해서 프로젝트를 만들어서 열어 주면 serial monitor 기능을 사용 가능


**arduino IDE** 사용하기  
가장 추천은 arduino IDE를 다운받은 후에 serial monitor를 사용하는 것

마찬가지로 보드를 선택하고 USB 장치를 선택해주면 사용이 가능하다   
PlatformIO와는 다르게 직접 메세지를 시리얼 통신으로 전송도 가능해서 테스트에 엄청 유용하다! 기본으로 가져가야할 듯 하다



## serial data 
시리얼 데이터를 만드는 방법은 여러가지가 있겠지만  

```cpp
uint8_t data_buff[13] = "Hello World\r\n";
```

이런식으로 하면 문자열도 배열로 만들어지기 때문에 가능   

vector를 이용하는 경우라면
```cpp
std::vector<uint8_t> data;
data.push_back('H');
data.push_back('e');
data.push_back('l');
data.push_back('l');
data.push_back('o');
data.push_back('\r');
data.push_back('\n');
```

실제 serial을 write()하는 함수등에서 어떤 type을 받느냐에 따라서 달라질 듯도 하다   

> 주의할 점은 아스키 ascii 코드로 넘어가는 것이기 때문에 int형으로 `10`을 넘기면 `\n`이 되게 된다.    
왜냐하면 10 (decimal) 은 아스키로 한칸 엔터인 new line을 의미하기 때문이다

숫자를 보낼 때에도 char형태로 보내면 이해하기 쉽다. 대신 하나씩 push_back()을 해준다   
```cpp
data.push_back('1');  // hex: 0x31 // decimal: 49
data.push_back('0');  // hex: 0x30 // decimal: 48
```  

`0x`형태로 16진수인 hex 방식으로 보내도 된다   

예를 들어 `\r`, `\n`은 각각 hex로 `0x0D`, `0x0A` 이다 . 

> 위에서 말한 것 처럼 0x0A는 또한 10진수로는 10이기 때문에 숫자 10을 보내려면   
ascii로 코드를 참고해서 보내야한다. 

