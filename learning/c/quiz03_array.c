#include <stdio.h>
//퀴즈1. 대각선으로만 출력하시오
int main() {
    int matrix[8][8] = {
        {  1,  2,  3,  4,  5,  6,  7,  8 },
        {  9, 10, 11, 12, 13, 14, 15, 16 },
        { 17, 18, 19, 20, 21, 22, 23, 24 },
        { 25, 26, 27, 28, 29, 30, 31, 32 },
        { 33, 34, 35, 36, 37, 38, 39, 40 },
        { 41, 42, 43, 44, 45, 46, 47, 48 },
        { 49, 50, 51, 52, 53, 54, 55, 56 },
        { 57, 58, 59, 60, 61, 62, 63, 64 }
    };

    int i, j, row, col;
    row = sizeof(matrix)/ sizeof(matrix[0]);
    col = sizeof(matrix[0]) / sizeof(int);

    // printf("%d\n", row);
    // printf("%d\n", col);
/*
    for(i=0; i < row; i++) {
        for(j=0; j < col; j++) {
            if( i == j) {
                printf("%3d", matrix[i][j]);
            } 
        }
        //printf("\n");
    }
*/
    //!위의 코드를 중복으로 돌릴 필요없이 for문 한번만으로 가능, 이런;
    for(i=0; i < row; i++) { //row만큼만 반복
        printf("%3d", matrix[i][i]);  // 총 8번을 반복하면서 [i][i]같은 i의 배열을 출력하면 
        //* 0,0  1,1  2,2 ....같이 i, j를 두번 돌린것 같은 효과를 냄
    }

    return 0;

}