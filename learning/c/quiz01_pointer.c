#include <stdio.h>

int main()
{
    int *numPtr;
    int num1 = 10;
    int num2 = 20;
    int *numPtr1;
    int **numPtr2;
    int num3;

    //포인터에 주소값을 넣어서 역참조 하기
    numPtr = &num1;
    printf("%d\n", *numPtr);
    numPtr = &num2;
    printf("%d\n", *numPtr);

    //더블 포인트 만들어 보기
    scanf("%d", &num3);
    numPtr1 = &num3;    //포인터에 입력받은 num3의 주소 할당
    numPtr2 = &numPtr1; //포인터를 받는 것은 포인터 변수이므로 이중포인터인 numPtr2에 &numPtr1의 주소 할당
    // 결국 numPtr1, numPtr2는 모두 num3의 주소를 참조

    printf("%d\n", **numPtr2);

    return 0;
}