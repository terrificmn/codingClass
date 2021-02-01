#include <stdio.h>
#include <stdlib.h>
//** malloc 함수를 사용하려면 <stdlib.h> 을 인쿠르드 해야함

int main () {
    int *numPtr = malloc(sizeof(int) *10); //동적 메모리 할당, int 사이즈의 10개 만큼
    // int numArr[10] 과 같은 효과
    int i, size;

    // 메모리 할당 받은 포인터를 배열 처럼 사용가능
    numPtr[0] = 10;
    numPtr[9] = 20;
    
    // size = sizeof(numPtr)/ sizeof(numPtr[0]); 메로리에 할당되어 있고 실제 numPtr에 들어가 있는 것은 0번째와 9번째 뿐임
    //numPtr 사이즈는 8, 배열하나는 4 (int)

    // printf("%d\n", sizeof(numPtr[0]));  //사이즈 ,fail
    // printf("%d\n", sizeof(numPtr));
    size = 10;
    for (i=0; i< size; i++) {
        numPtr[i] = i + 10;
        printf("메모리할당%d %d\n", i, numPtr[i]);
    }

    // printf("%d\n", numPtr[0]); 
    // printf("%d\n", numPtr[9]);

    free(numPtr); //메모리 해제

//------------두번째 예제------
    printf("\n\n");
    int *pi;
    double *pd;
    
    pi = (int *) malloc(sizeof(int)); //(int *) malloc으로 변환되는 것을 int변환  
    //int type에는 4byte 만큼 메모리에 할당 
    
    if (pi == NULL) {
        printf("# 메모리가 부족합니다.\n");
        exit(1);
    }
    pd = (double *) malloc(sizeof(double)); //(double *) 반환되는 주소를 double type으로 변환    
    //double type에는 8byte 만큼 메모리에 할당 

    *pi = 10;
    *pd = 3.4;

    printf("정수형으로 사용: %d\n", *pi);
    printf("실수형으로 사용: %.1lf\n", *pd);

    free(pi);
    free(pd);

    return 0;
}