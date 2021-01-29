////////// 포인터를 이용한 함수 

#include <stdio.h>
int *sum (int a, int b); // 리턴받을 함수가 포인터로 선언
int *get_num();

int main() {
    int *resp;

    resp = sum(10, 20); //resp도 포인터로 sum()함수의 결과로 리턴받은 결과는 주소 &res의 주소이므로 같은 결과를 가리키고 있음
    printf("두 정수의 합: %d\n", *resp);
    printf("리턴받은 값은: %d\n", *get_num()); //포인터 함수로 리턴받음

    return 0;
}

int *sum (int a, int b) { //* 결과값을 주소값으로 받음 //포인터로 res주소값을 반환시킴
    static int res; //* 스태틱으로 정적지역 변수로 선언해서 메모리에 계속 남아있게 함
    res = a + b;
    return &res; //스태틱으로 선언된 res의 주소값을 반환
} 

int *get_num() {
    static int n;
    printf("get_num()함수입니다. 입력하세요: ");
    scanf("%d", &n); //주소값 넘기기
    return &n;
}