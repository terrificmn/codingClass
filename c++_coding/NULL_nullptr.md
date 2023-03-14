# null check

모던 cpp에서는 NULL은 포인터를 확인할 경우에 사용.  
물론 포인터가 아닌 경우에도 안되는 것은 아니다.   

하지만 NULL 값이면 0으로 처리하게 되어 있다   

```cpp
if(x == NULL) {
    ROS_WARN("x is NULL");
    ///처리
} 

if(y == NULL) {
    ROS_WARN("y is NULL");
    ///처리
} 
    
```
이렇게 해서 컴파일을 하게 되면 경고 메세지가 나온다. 실행에는 문제가 없음
```cpp
warning: NULL used in arithmetic [-Wpointer-arith]
   61 |         if(x == NULL) 
```

> arithmetic 수학의 한 분야라는데.. 산수, 산술을 의미한다. 수의 개념, 계산하는 것을 의미

## 0으로 처리하자
이제 NULL은 포인터가 아닌 변수에서는 0으로 처리하는 macro로 생각하면 될 듯 하다.   
그래서 위와 같은 경우에 경고 메세지가 나오니  
```cpp
if(x == 0) {
        ROS_WARN("x is NULL");
    ///처리
} 

if(y == 0) {
    ROS_WARN("y is NULL");
    ///처리
} 
```

또는 `if(x != 0)` 식으로 사용하자


### 그외 포인터가 null인지 확인할 때에

간단하게 하는 방법이 좋은 방법이라고 함
```cpp
int a;
int* ptr_a;

if(!ptr_a)  {
    // 뭔가 처리
    return; //에러 방지
}
```
포인터 같은 경우에는 위의 일반 포인터가 아닌 변수가 NULL인 경우와는 다르게 아주 치명적이다.   
nullptr일 경우에 메모리를 참조하려고 하다가 **segmentation fault core dumped** 가 발생   
결국 프로그램이 죽는다(?) 이유는 접근이 허용되지 않는 경우인데 접근하면 에러발생하는 것

> 존재 하지 않는 주소에 접근해서 읽거나 쓰려고 하려다가 실패하는 현상


또는 아예 nullptr인지 확인
```cpp
if(ptr_a == nullptr)
```
