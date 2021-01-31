#include <stdio.h>
int main()
{
    //3항 연산자 사용
    int num1 = 5;
    int num2;

    num2 = num1 ? 100 : 200; // 참이면 ? 100 : 거짓 200;

    //-----------------
    int num3 = 10;
    int num4;

    num4 = num3 == 10 ? 100 : 200; // 조건 ? 참 이면 수행 : 거짓이면 수행
    printf("%d\n", num4);          // num4는 100이 됨

    // 쉬프트 연산자
    unsigned char num01 = 3;
    unsigned char num02 = 24;
    printf("%u\n", num01 << 3); //num01의 비트 값을 왼쪽으로 3번 이동 << (2진수) 3번이동하고 모자라는 공간은 0이 됨
    // 3은 2진수로 0000 0011 << 왼쪽으로 비트가 3번 이동, 0001 1000 이 됨, 그래서 10진수로 24가 됨
    printf("%u\n", num02 >> 2); //num02의 비트 값을 오른쪽으로 2번 이동
    return 0;
}

/*
    // 불 자료형 사용
    // stdbool.h 헤더파일 include 해야함 (bool, true, false가 정의됨)
#include <stdio.h>
#include <stdbool.h>

int main() {
bool b1 = true;
if (b1 == true)
	printf("참\n");
else
	printf("거짓\n");

printf("bool의 크기: %d\n", sizeof(bool)); // bool 크기는 1byte, int는 4byte

return 0;
}
*/
