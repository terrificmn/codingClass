# argc, argv 파라미터 parameters

c++ 에서 main함수에서 받을 수 있는 파라미터인 int argc, char argv  가 되겠다  

여기에서는 사용법 보다는 argv 를 변환하는 방법에 대해서 정리

argc로 몇 개의 파라미터를 입력했냐에 따라서 한번 걸러주고   
그 다음에 실제 argv에 들어있는 값으로 내용을 처리하게 되는데   

```cpp
if(*argv[1] == '1') {
    std::cout << "1\n";
} else {
    std::cout << "else";
}
```
이렇게 처리하게 되면 argv의 배열에서는 오직 char 한 글자만 처리하게 되서   
파라미터로 `1`이 들어오던 `111`이 들어오던 첫 번째 자리 1만 처리하게 되서     
다른 숫자는 else 처리를 하고 싶은데 111도 1로 처리가 되는 문제가 있다   

결과는 1만 들어가게 되면  
```
1
```
이 출력되게 된다 

## string으로 만들어주기 (char에서), 또는 int로 
그래서 `std::string` 을 이용해서 변수에 넣어주고 int로 바꾸거나 string 자체로 처리해보는 방법이 있겠음

```cpp
std::string str_argv = argv[1];

// convert int
int int_argv = stoi(str_argv);

if(str_argv == "1") {
    std::cout << "1\n";
} else {
    std::cout << "else";
}

// use int
if(int_argv == 1) {
    std::cout << "1\n";
} else {
    std::cout << "else";
}
```

이렇게 하면 오직 1일 경우에만 처리를 해주고 11, 111 은 else 처리가 되니 원하는 결과로 만들어 갈 수가 있다  


## 번외로 char에서 숫자   
char는 ascii로 대입이 되기 때문에 그냥 int로 바꾸게 되면 아스키코드로 되어 버리기 때문에   
원하는 숫자로 만들려면 기준이 되는 '0'을 빼주면 된다  

```cpp
int i_argv = int(*argv[1] - '0');
```

그러면 아스키코드가 입력된 숫자(char) 에서 integer 숫자로 바뀌게 된다   



