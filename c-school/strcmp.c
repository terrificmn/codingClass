#include <stdio.h>

int main()
{
    int matrix[5][5];

    scanf("%d %d %d %d %d", 
        &matrix[0][0], &matrix[0][1], &matrix[0][2], &matrix[0][3], &matrix[0][4]);
    scanf("%d %d %d %d %d", 
        &matrix[1][0], &matrix[1][1], &matrix[1][2], &matrix[1][3], &matrix[1][4]);
    scanf("%d %d %d %d %d", 
        &matrix[2][0], &matrix[2][1], &matrix[2][2], &matrix[2][3], &matrix[2][4]);
    scanf("%d %d %d %d %d", 
        &matrix[3][0], &matrix[3][1], &matrix[3][2], &matrix[3][3], &matrix[3][4]);
    scanf("%d %d %d %d %d", 
        &matrix[4][0], &matrix[4][1], &matrix[4][2], &matrix[4][3], &matrix[4][4]);
    printf("\n");
    int i, j;
    int row = sizeof(matrix) / sizeof(matrix[0]);
    int col = sizeof(matrix[0]) / sizeof(int);
    
    for (i=0; i < row; i++) {
        for (j=0; j < col; j++) {
            printf("%d ", matrix[i][j+5]);
            
        }
        printf("\n");
    }
    char a[][6]  = {"apple","pear","banana"} 
}