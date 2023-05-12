# array cpp

c++에서 array를 만들어 사용할 경우
```cpp
const int my_keywords[5] = { 'H', 'E', 'L', 'L', 'O' };
```

위 처럼 char로 만들지 않고 int로 선언한 뒤 'char' 를 넣어주면 assii 코드로 입력이 되어 진다  

이를 출력하려고 하면  
```cpp
std::cout << "my_keyword[0]: " << this->my_keywords[0] << std::endl;
```

보통 인덱스로 접근해서 사용할 수가 있다  

재미있는 것은 char로 변수를 만들어서 넣어주면 char로 출력이 되고 
```cpp
char test= this->my_keywords[0];
std::cout << test << std::endl;
```
`H`

```cpp
int test= this->my_keywords[0];
std::cout << test << std::endl;
```
`72`  (아스키코드로 입력이 됨)


## array for loop
보통 array는 size() 메소드를 사용할 수가 없다. 그래서 `sizeof()` 함수를 사용한다

```cpp
for(int i=0; i < sizeof(my_keywords); i++) {
    std::cout << my_keywords[i] << std::endl;
}
```
> 기본적인 것이였는데, vector만 사용하다가, size() 메소드가 왜 안될까? 하고 헤매다 찾아보았음   

또는 좀 더 편하게 사용할 수도 있다
```cpp
for(const int keyword : this->my_keywords) {
    std::cout << keyword << std::endl;
}
```


