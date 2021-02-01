#include <stdio.h>

void add() {  //void 리턴값이 없는 함수
    printf("%d + %d = %d\n", 2, 3, 2+3);  //단순 출력만 하고 리턴을 하지 않음
}

void add2(int a, int b) {  //void 리턴값이 없는 함수, 리턴값이 없더라도 파라미터로 변수값을 받을 수 있다
    printf("%d + %d = %d\n", a, b, a+b); //파라미터로 받은 값으로 계산 및 출력만 하고 리턴을 하지 않음
}

int add3(int a, int b) {  //리턴값이 있을 때는 리턴값에 맞는 Type으로 정의해야한다 
    int sum = a + b;
    return sum;  //리턴하는 sum이 integer이므로 함수는 int로 정의
}


int main() {
    int a = 10, b =20;
    int sum;

    add(); //아규먼트 넘길 것이 없을 때는 빈괄호만 씀
    add2(a, b);
    
    sum = add3(a, b);
    printf("%d", sum);

    return 0;
}
