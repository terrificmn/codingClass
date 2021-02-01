#include <stdio.h>

void func(int (*fp)(int, int)); //함수포인터 정의
int sum(int a, int b);
int mul(int a, int b);
int max(int a, int b);

int main () {
    int sel;

    printf("선택1: 두 정수의 합\n");
    printf("선택2: 두 정수의 곱\n");
    printf("선택3: 두 정수 중에서 큰 값 계산\n");
    printf("1~3 중 원하는 연산을 선택하세요: ");
    scanf("%d", &sel);

    switch(sel) {
        case 1: func(sum); break;
        case 2: func(mul); break;
        case 3: func(max); break; 
    }    
    return 0;
}

void func(int (*fp)(int, int)) {
    int a, b, res;
    printf("두 정수의 값을 입력하세요: ");
    scanf("%d%d", &a, &b);
    res = fp(a, b);  //* 함수포인터로 받은 것을 (입력한 값에 따라 함수명으로 받아짐 예: sum 이면 sum 함수의 주소값을 받아옴)
    // 결과적으로 sel 값에 따라서 맞는 함수를 호출한 뒤 결과 값을 리턴 받음
    printf("결과: %d\n", res);
}

int sum(int a, int b) {
    return (a + b);
}
int mul(int a, int b) {
    return (a * b);
}
int max(int a, int b) {
    if(a > b) return a;
    else return b;
}
