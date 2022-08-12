std::stringstream 을 사용해서 
형식을 바꿀 수 있다 

string 에서 char로 

예
```cpp
#include <sstream>
//....생략
    std::stringstream ss;
    char xtest[10], ytest[10];

// string 에서 char로 변환
    ss << xtest;
    ss >> converted_char_x;
    ss.clear();

    ss << ytest;
    ss >> converted_char_y;
    ss.clear();
```

**하지만** 몰랐다... string 에서 char로 변환이 되는 것을 ㅠㅠ
std::string xtest.c_str() 하면 된다 ;;;;

결론 stringstream 사용할 필요는 없는 듯 하다 

