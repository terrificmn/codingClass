인쿠루드를 해서   
```
#include <iomanip>
```

출력할 때는 아래처럼 사용 
double doubleNumber = 10.12345678

그냥 출력하게되면 6자리 정도만 나온다   
아마도 10.1234 이런식으로   

```
std::cout << std::setprecision(10) << doubleNumber
```

파일을 열어서 저장할 때에도 비슷하게 사용 
```
myfile << std::setprecision(10) 
```