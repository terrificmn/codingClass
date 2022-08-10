std::string으로 만들어 진 것은 그냥 메소드를 그대로 사용할 수가 있다   
.length() .size() 등으로 사용하면 됨  

예   
```
std::string name = "Duc";
std::cout << "Length: " << name.length() << std::endl;
std::cout << "Size: " << name.size() << std::endl;
```


단, char 형태로 만들어 진 것이라면 string 라이브러리를 통한 것이 아니므로 사용불가  

strlen() 함수를 사용해서 길이를 알아내면 됨  

```
char data = "hello world";
int length = strlen(data);
```


