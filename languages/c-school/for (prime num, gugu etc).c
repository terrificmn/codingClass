#include <stdio.h>
int main()
{
    // while문 형식
    // while (조건식) {
    //     실행문
    // }
    /*
    // while문 반복
    int i = 0;
    while (i < 2) {
        printf("%d\n", i);
        i++; //무한반복을 막기위해 i를 증가
    }

    // for문 반복
    for (i=0; i < 10; i++) {
        printf("%d ", i);
    }
    printf("\n");

    // do while문 : 한번은 실행하고 그 다음에 while조건을 맞춰서 반복실행
    int a =0;
    do {
        printf("반복 실행 do : %d\n", a);
        a += 1;
    } while (a < 3);

*/
    // 구구단
    /*
    int i, j;
    for (i=2; i < 10; i++) {
        printf("%d단\n", i);
        for (j=1; j < 10; j++) {
            printf("%d X %d = %d\n", i, j, i*j);
        }
    }
*/

    /*
    //i, j을 바꿔서 출력하기, 단 별로 출력
    int i, j;
    for (i=1; i < 10; i++) {
        //printf("%d단\n", i);
        for (j=2; j < 10; j++) {
            printf("%d X %d = %d\t", j, i, i*j);
        }
        printf("\n");
    }
*/

    //무한반복문 while의 조건을 1을 주면 됨
    // while (1) { 실행코드 }

    /*소수(prime number)출력 
    // 소수(prime number)출력 
    int nbr, i, j, c;
    printf("2 이상의 정수를 입력하세요 :");
    scanf("%d", &nbr);
    
    for (i=2; i< nbr; i++) {
        for (j=2; j < i; j++) {
            if (i % j == 0) {
                break;
            }
        }

        if (j == i) {
            if (c == 5) {
                printf("\n");
                c = 0;
            } 
            printf("%2d\t", i);
            c ++;
        }
        
    }

*/
    char str[100];
    int i, count = 0;

    printf("입력 (띄어쓰기X): ");
    scanf("%s", &str); //띄어쓰기로 구분해서 입력을 받으려면 %s%s 이런식으로 연속으로 받으면 가능

    //* for을 반복할 때 문자열 배열만큼 반복시킬려면 문자열[i] (예: i < str[i]) 알아서 문자열 배열만큼 반복한다
    for (i = 0; i < str[i]; i++)
    {
        count += 1;
    }
    printf("%s", str);
    printf("%d", count); //for문이 배열크기보다 작을때 반복해줌
    return 0;
}