인쿠루드를 해서   
```cpp
#include <iomanip>
```

출력할 때는 아래처럼 사용 
double doubleNumber = 10.12345678

그냥 출력하게되면 6자리 정도만 나온다   
아마도 10.1234 이런식으로   

```cpp
std::cout << std::setprecision(10) << doubleNumber
```

파일을 열어서 저장할 때에도 비슷하게 사용 
```cpp
myfile << std::setprecision(10) 
```


string으로 되어 있던 값을 double 등으로 바꾸면 발생하는 듯 하다   
```cpp
std::string string_number="25.123456";
double double_num = stod(string_number);

std::cout << double_num << std::endl;
```

출력이 
`25.1235` 이렇게 짤려서 나온다   

이제 출력을 할 때 setprecision(총자리수)  로 출력을 하면
```cpp
std::cout << std::setprecision(8) << double_num << std::endl;

```

`25.123456` 다 출력이 된다 

> 소수점 앞 뒤 총 숫자로 정해주면된다 



