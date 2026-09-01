#include <stdio.h>
int main() {
    /*
    int i;
    for (i=0; i < 10; i++) {
        printf("$");
    }
    */
    int i, j;
    /*
    for (i=0; i< 3; i++) {
        for (j=0; j < 4; j++) {
            printf("BE HAPPY!\n");
        }
    }
    */

//확인문제 3 (176p)
//! 2중 for문 규칙 파악시에는 표로 그린다음에 참고하면 도움될 듯 함 (i의 row와 j의 column)
    for (i=0; i < 5; i++){
        for (j=0; j < 5; j++) {
            if (j == i || j == i && j + 1 ==4 || j + i == 4) {  //or ||(or)로 한번에 else if 로 조건을 나눌 수도 있음
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n"); //j 반복 끝나면 줄바꿈
    }
    return 0;
}