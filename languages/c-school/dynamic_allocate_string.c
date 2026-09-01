#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
/*
    char temp[90];
    char *str[3];
    int i;

    for (i=0; i < 3; i++) {
        printf("문자열을 입력하세요: ");
        gets(temp);
        str[i] = (char *)malloc(strlen(temp) +1); //배열포인터에 메모리 할당 (입력받은 temp)의 길이만큼+1 해서 할당해줌 (0널문자 포함+1)
        strcpy(str[i], temp);  // 할당된 str[i]에 입력받은 temp 넣어주기
    }

    for (i=0; i < 3; i++) {
        printf("%s\n", str[i]);
    }

    for (i=0; i < 3; i++) {
        free(str[i]);
    }
*/
    //todo: 복습필요!
    // 이중 포인터 이용해서 메모리 할당하기  2차원 배열로 구성
    char **p_mat = (char **)malloc(4 * sizeof(char *)); //메모리 영역을 2차원 배열처럼 사용하기 위해서 이중포인터 선언
    // (type 더블포인터) malloc(할당할 row 사이즈: 여기서 사이즈 구할때는 포인터로 구해줌-sizeof(char *))
    int i, j, row, col;


    //p_mat = (char **)malloc(4 * sizeof(char *));
    row = sizeof(p_mat) / sizeof(p_mat[0]);
    //col = sizeof(p_mat[0]) / sizeof();
    //printf("%d", row);

    //처음 만들어진 더블포인터에 할당된 메모리를 바탕으로 2차원배열 느낌으로 5개(col) 를 더 만들어 주기 
    for (i=0; i < 4; i++) {
        // [i]번째에 메모리를 5개를 더 할당
        p_mat[i] = (char *)malloc(5 * sizeof(char));
    }

    for (i=0; i < 4; i++) {
//            printf("문자열을 입력하세요: ");
  //          gets(p_mat[i]);
            
    }
    
    for (i=0; i < 4; i++) {
    //    printf("%s\t\n", p_mat[i]);
    }

    for (i=0; i < 4; i++) {
        free(p_mat[i]);
    }
    
    //todo: 해결하기 p473.
}