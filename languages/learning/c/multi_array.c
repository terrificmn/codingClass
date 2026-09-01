#include <stdio.h>
int main()
{
    //2차원 배열 초기화
    int numArr[3][4] = {
        {11, 22, 33, 44},
        {55, 66, 77, 88},
        {99, 110, 121, 131}};
    // 위 처럼 2차원배열은 중괄호로 다시 한번 묶어 주는 것이 가독성 확보에 좋다

    int numArr1[3][4] = {0, }; // 2차원배열 모든 요소를 0으로 초기화
    int i, j;
    int col = sizeof(numArr[0]) / sizeof(int);    //  배열의 col 길이 구하기 /  1차원의 배열 하나를 int형으로 나누면 가로 col길이
    int row = sizeof(numArr) / sizeof(numArr[0]); // 배열의 row 길이 구하기 / 전체배열에서 하나의 배열(가로(col)) 나누면 row길이

    //출력
    for (i = 0; i < row; i++) {
        for (j = 0; j < col; j++) {
            printf("%3d ", numArr[i][j]);
        }
        printf("\n");
    }

    printf("반대로 출력\n"); 
    for (i = row - 1; i >= 0; i--) { //row의 값에서 -1을 해줘야 0까지 돌릴 수 있음 (전체배열에서 0포함, 1, 2 이렇게 3개이므로)
        for (j = col - 1; j >= 0; j--) {
            printf("%-4d", numArr[i][j]);
        }
        printf("\n");
    }

    return 0;
}