# pass array through the function
보통 array를 함수에 전달하려고 하면 syntax 관련 에러가 발생하는데  

배열을 파라미터로 전달하게되면 가지고 있던 배열의 갯수를 잃게 된다   
그러므로 포인터로 넘길려고 하면 원래 사이즈도 같이 넘겨주면 사용이 가능하다  


예:  
```cpp
void myArray(int *my_array, int my_array_size) {
    for(int i=0; i < my_array_size; i++) {
        std::cout << "my array's index " << i << ": " << my_array[i] << std::endl;
        // 포이터 자체가 주소 이어서 * 사용안해도 됨
    }
}

int main() {

    int array_[5] = { 10, 20, 30, 40, 50 };
    std::cout << sizeof(array_) << std::endl;
    std::cout << sizeof(array_[0]) << std::endl;
    int size = sizeof(array_) / sizeof(array_[0]);
    
    myArray(array_, size); // array_ 자체가 첫 번쨰 주소가 되므로 

    return 0;
}
```

이 중 배열에는 `size()` 함수를 사용할 수 없으므로, `sizeof()`를 사용해서 전체의 길와 한개의 길이를 나눠서   
배열 갯수를 알아 낼 수가 있고 이를 사용해서 myArray 함수에 파라미터로 넣어줄 수가 있다   

그러면 array의 주소는 알고 있고, 필요한 배열의 갯수도 알았으니 배열을 사용할 수가 있다  
