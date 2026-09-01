#include <stdio.h>
int main() {
    char mark[5][5] = { 0 }; //초기화
    int i, j;

    for (i=0;i < 5; i++) {
        for (j=0; j < 5; j++) {
            if (i == j) {
                mark[i][j] = 'X';
                printf("%c", mark[i][j]);
            } else {
                printf(" ");
            }
        }
        printf("\n");
    }
    
    printf("-----------\n");
    
        for (i=0;i < 5; i++) {
            for (j=0; j < 5; j++) {
                if ((i == j) || (i + j == 4)) {
                    mark[i][j] = 'X';
                    printf("%c", mark[i][j]);
                } else {
                    printf(" ");
                }
            }
        printf("\n");
    }

}
