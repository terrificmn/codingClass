#include <stdio.h>
#include <stdlib.h>
//4행 5열의 값을 저장할 2차원 배열의 동적 할당하기
int main() {
    int **p_matrix = (int **)malloc(4 * sizeof(int *));   // 4row 로 메모리 할당하기 //2차원은 더블포인터로 만든다 
    // malloc()함수로 만들 때 사이즈는 (int *) 포인터 크기로 만들어 준다 (참고: 8byte, int는 4byte)
    int i;

    for (i=0; i < 4; i++) {
        p_matrix[i] = (int *)malloc(5 * sizeof(int)); // 4번 반복하면서 5col 메모리 할당해주기
    }

    for (i=0; i < 4; i++) {
        free(p_matrix[i]); // 동적 할당 반환 (제거)
    }

    printf("%d\n", sizeof(int ));
    return 0;
}