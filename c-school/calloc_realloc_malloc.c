#include <stdio.h>
#include <stdlib.h>
int main() {
    int *pi;
    int size = 5, count = 0;
    int num, i;

    pi = (int *)calloc(size, sizeof(int));  //size만큼 (5)  int 4byte 메모리에 할당. 즉, 20만큼 할당
    while (1) {
        printf("양수만 입력하세요 :");
        scanf("%d", &num);
        if (num <= 0) break; // 입력된 값이 없으면 빠져나옴 break
        if (count == size) { // 입력된 값이 있을 때 마다 count++  되면서 size와 같으면
            size += 5;
            pi = (int *)realloc(pi, size * sizeof(int));  //realloc(기존*pi, 추가할 크기 (size * sizeof(int)) )
        }
        pi[count++] = num;  //pi포인터는 메모리 할당이 되었으므로 배열처럼 사용가능  
        // count++ 계속 +1 시켜주면서 동시에 배열의 인덱스를 가리킴 -----> num 입력된 값 넣어주기 
        //? count++ 일단 0에서 num을 할당, 그 후에 +1 되어 count가 1이 됨
    }
    
    for (i=0; i < count; i++) {
        printf("%5d", pi[i]);
    }
    free(pi);
    printf("총 카운트: %d", count);
    return 0;
}
