#include <stdio.h>
    void swap(int *pa, int *pb) {
        int temp;

        temp = *pa;
        *pa = *pb;
        *pb = temp;
    }

    int main() {
        int a = 10, b = 30;
        
        printf("함수 호출전- a:%d, b:%d\n", a, b);
        
        swap(&a, &b); //주소값을 넘겨줌 (swap(함수에서는 주소를 받는 pointer변수로 받음))
        
        printf("함수 호출후- a:%d, b:%d\n", a, b);
        return 0;
    }


