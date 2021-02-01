#include <stdio.h>
int main() {
    int a = 10, b = 15, total;
    double avg;
    int *pa, *pb; //*포인터 변수와 포인터가 가리키는 변수와의 타입은 일치해야한다. 
    int *pt = &total;
    double *pg = &avg;

    int num1 = 10;
    printf("%p", &num1); // %p는 주소를 보여줌

    pa = &a; //pointer변수 pa와 가리키는 a변수의 타입은 일치해야함
    pb = &b;

    *pt = *pa + *pb;
    *pg = *pt / 2.0;

    printf("두 정수의 값: %d, %d\n", *pa, *pb);
    printf("두 정수의 합: %d\n", *pt);
    printf("두 정수의 평균: %.1lf\n", *pg);

    printf("\n\n");

    char ch = 'A';
    int in = 10;
    double db = 3.4;

    char *pch = &ch;
    int *pin = &in;
    double *pdb = &db;

    printf("ch,in,db 변수의 주소값\n");
    printf("ch 주소 %p\t", &ch);  //%p 주소를 보여줌
    printf("in 주소 %p\t", &in);
    printf("db 주소 %p\n", &db);
    printf("ch,in,db를 의 주소를 받은 pch,pin,pdb 포인터의 주소값\n");
    printf("pch 포인터 %p\t", pch);
    printf("pin 포인터 %p\t", pin);
    printf("pdb 포인터 %p\t", pdb);

    printf("\n포인터의 값\n");
    printf("pch 포인터 %c\t", *pch);
    printf("pin 포인터 %d\t", *pin);
    printf("pdb 포인터 %lf\t", *pdb);

    return 0;
}