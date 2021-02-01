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
        // 지역 변수이기 때문에 swap()함수를 호출한다음에 리턴값을 받아야지 결과가 값이 반영이 되는데
        // 여기에서는 void 함수이기 때문에 리턴값이 없음
        //** 그래서 포인터 변수를 이용하면 주소값을 알기 때문에 a, b 변수를 바꿔준 결과가 나오게 됨!
        
        printf("함수 호출후- a:%d, b:%d\n", a, b);
        return 0;
    }


