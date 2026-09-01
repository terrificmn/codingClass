## stringstream
iostream class로 부터 나온 것으로 ..  

추가, 추출 등.. string에서 number등 (int) 로 변환하거나 할 때 쓰이는 클래스

strainstream 는 좀 더 크고 좀 더 느린 퍼포먼스를 보일 수도 있다   

대표적 메소드에는 `str()` -- 문자열로 반환, `clear()` -- 말그대로 clear   
`<<` 는 새로운 문자열을 StringStream 오브젝트에 추가할 때 사용   
`>>` 는 StringStream에서 읽을 때 사용

<< 와 >> 잘 가려서 사용해야한다. 

```cpp
#include <iostream>
#include <string>
#include <sstream>
```
이 정도를 인쿠르드 해서 사용한다 


## ostringstream
text를 char array 형식으로 메모리에 쓰는 클래스   
char 데이터 타입에 대한 template class basic_ostringstream 이라고 한다 

output 스트링에만 쓰이고 operatror는 `<<` 만 사용한다  
즉, 스트링을 만들 때 주로 사용

> 경우에 따라 실수를 줄일 때 좋을 듯 하다

사용 방법은 string stream과 비슷


## istringstream
input 에 사용되는 클래스  
`>>` operator만 사용하며 입력을 할 때 사용된다  
또는 오브젝트로부터 추츨할 때 사용한다

