char pointer 리턴

**일단 금지 std::string을 사용하자**   

char 값이 필요해서 뭔가 처리를 한 후에 다시 리턴을 char로 받을려고 했는데  
char 자체가 배열로 되어 있기에 함수안에서는 처리가 가능하지만 리턴하기가 안됨  

```cpp
char convertChar(char greeting[]) {
    std::cout << greeting;
}

int main(int argc, char** argv) {
    char teststr[6] = "hello";
    convertChar(teststr);
    return 0;
}
```

이런식으로는 가능하나 c++ 에서는 array 리턴을 허용하지 않으므로 안됨  

그래서 포인터로 리턴해주면 되겠구나해서  

어느 간단하게 새로 구성해 봤는데 char 값이 필요해서 구지 char를 포인터로 리턴 받을려고 해봤는데  
에러는 발생하지 않으나   
```cpp
char* convertChar(std::string greeting) {
    
    char *return_ch = &greeting[0];
    //char *return_ch = new char[strlen(converted_char)];
    
    std::cout << "in fuaction: " << return_ch << std::endl;
    return return_ch;
}

int main() {
    std::string teststr = "hello";
    char* result = convertChar(teststr);
    std::cout << "return value: " << result << std::endl;
}
```

결과는 리턴값이 발생하지 않는다  
```
in fuaction: hello
return value: 
```

이유는 함수안에서 즉 로컬 함수에서는 사용이 되고 리턴을 하면서 바로 메모리 어드레스가 없어진다고 한다   

그래서 함수내에서는 출력을 하고 리턴 받은 값에서는 사용을 못하게 됨  

그래서 방법중에 주석처리 되어 있는 new 키워드로 다이나믹으로 메모리 할당을 한 후 사용하면 괜찮다고 하나  
사용을 잘못해서 그런지? 이것 역시 리턴 값이 없다  


## 결론
물론 아직 방법이 있을 수도 있으나  
중요한 것은  
1. 배열은 리턴 못한다  
2. 포인터를 리턴해도 그 함수를 빠져나오는 순간 overwritten 된다 

그래서 malloc 이나, new 로 메모리를 할당하면 사용할 수 있다는데 이것 역시 잘 안되는 듯 하다  


그러므로 std::string 을 사용하자  c++에는 string을 사용할 수가 있으므로  
char type 필요하면  
```cpp
// from string to char
std::string str.c_str();

// from double to string
double형을 string으로 변환하려면 std::to_string(str)
```




