#include <stdio.h>
int main() {
    char a[4][10] = { "horse", "fox", "hippo", "tiger" };
    char *pa[] = { a[0], a[1], a[2], a[3] };
    int count, i; 
    count = sizeof(pa) / sizeof(pa[0]); //! 배열의 전체 크기에서 한개의 배열(row)를 나누면 몇개의 배열을 가지고 있는지 나옴
    // 64bit 에서는 pointer char는 8byte. 전체는pa 포인터는 32byte에서 한개를 나누면 결과는 4 가 나오는데 이는 배열의 개수와 일치한다

    //printf("%d ", sizeof(pa));
    //printf("%d \n", sizeof(pa[0]));

    for (i = 0; i < count; i++) {
        printf("%c", pa[i][i]);
    }
    return 0;
    
}