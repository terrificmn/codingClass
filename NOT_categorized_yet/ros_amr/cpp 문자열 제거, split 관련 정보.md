[참고하기](https://www.techiedelight.com/trim-string-cpp-remove-leading-trailing-spaces/)

c++에서 문자열 split, 문자열 제거 등을 알아보자

## 먼저 문자열제거 
```cpp
std::string str = " space, hello, world";
size_t first_space = str.find_first_of(" ");
```

find_first_of() 함수는 인덱스를 리턴해준다. 이후 erase() 함수를 이용해서 제거 한다.   
해당 변수에 바로 적용되므로 주의

```cpp
str.erase(first_space, 1);
```

만약 글자의 마지막 배열에서 지우려면 length()함수와 -1을 사용 (배열의 갯수를 반환하고, 인덱스는 0부터 시작이므로 -1 해줘야한다)
```cpp
str.earse(str.lengh()-1, 1);
```


## 문자열 split

, 콤마로 되어 있는 문자열 나누기

```cpp
#include <iostream>
#include <vector>

int main() {
std::string str = "123, 4567, 890, ";
std::string delimiter = ", "; // split by , and space
std::string token;

size_t pos = 0;
std::vector<int> extracted_xy;
while ((pos = str.find(delimiter)) != std::string::npos) {
	token = str.substr(0, pos); // split it from found array index
	std::cout << "token: " << token << std::endl;
	extracted_xy.push_back(stoi(token));
	str.erase(0, pos + delimiter.length()); // caution: erased due to reference to variable
}

std::cout << extracted_xy[0] << std::endl;
std::cout << extracted_xy[1] << std::endl;
std::cout << extracted_xy[2] << std::endl;

}
```

> 주의 할 점은 while문에서 push_back()해서 하나씩 넣어주는 변수는 vector\<int> 로 되어 있는데  
> 문자열에서 되는 것이므로 넣어줄 때 stoi() 로 변환해서 넣어준다.   
> 더블형을 사용하고 싶다면 stod()

> 그리고 ", "로 구분을 하기 때문에 추출할 문자열인 str에서 ,스페이스가 3개가 있어야지 extracted_xy에 3개 배열로 만들어진다. 만약 스트링이 "123, 4567, 890" 이렇게 되면 마지막 콤마를 못찾으므로 while이 끝나게 되니, 적절하게 수정해준다. (if문을 추가?)


