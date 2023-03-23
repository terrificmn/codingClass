# double 소수점 이하 버리기 after decimal point 

double 등으로 선언하고 만들면 너무 소수점이 길어져서 곤란할 때가 있다  
floor() 함수를 이용해서 소수점 이하를 특정 수 만큼만 살릴 수 있다

```cpp
double x = 10.123456789;
double new_x = std::floor(x * 100000) / 100000;

std::cout << new_x << std::endl;
```

더블형에 원하는 만큼 곱하기를 해준다음에 그 floor 함수를 하면  
1012345.000000 가 나오게 됨. 원래 수에서 100000 배가 된 후에   
floor()함수로 소수점 나머지는 버리고 인티저로 만들려고 함

여기에 다시 100000을 나누게 되면 다시 5자리(?) 이동해서 10.12345 가 결과로 나오게 된다   

결론은;;; 곱하고 나눈 수 0의 갯수 만큼 소수점이 사라진다.  

> floor 는 반내림(?)을 해서 인티저로 만들어 주는 함수   
주어진 100000 만큼 곱해서 그 만큼 십만 배 큰 수 integer가 만들어 지고, 반내림으로 소수점을 버리게 된다     
그리고 다시 주어진 수 100000 십만으로 다시 나누니 원래의 소수점으로 돌아가는 것인 듯 하다   
여기서 주어진 수 (예: 100000)을 조절하면 소수점 컨트롤이 된다 

up to 5 *decimal places* (소수점 5자리가 되겠다)


### decimal point 이후를 place value라고 한다. (그냥 참고)   
예 10.123456    
소수점. 이하 ----->   
Tenths, Hundredths, Thousandths, Ten Thousandths, Hundred Thousandths, Millionths 라고 부름;;;



