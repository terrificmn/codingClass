#include <stdio.h>
int main() {
    char a[4][10] = { "horse", "fox", "hippo", "tiger" };
    char *pa[] = { a[0], a[1], a[2], a[3] }; //배열자체가 주소이므로 &사용안해도 됨
    int count, i; 
    count = sizeof(pa) / sizeof(pa[0]); //! 배열의 전체 크기에서 한개의 배열(row)를 나누면 몇개의 배열을 가지고 있는지 나옴
    // 64bit 에서는 pointer char는 8byte. 전체는pa 포인터는 32byte에서 한개를 나누면 결과는 4 가 나오는데 이는 배열의 개수와 일치한다

    //printf("%d ", sizeof(pa)); //printf("%d \n", sizeof(pa[0]));
    for (i = 0; i < count; i++) {
        printf("%c", pa[i][i]);
    }
    printf("\n");
    // 각 64bit에서 type별 sizeof()했을 때의 크기 
    // 32비트는 char, short, int 까지 64비트와 같다. 각각 1, 2, 4byte
    // 32비트 pointer는 모든 타입이 4byte 이고, 64비트 pointer는 모든 타입에서 8byte 임
/*

*/
    printf ("\n-- General Data Type Size --\n");
    printf ("char size : %d byte\n", (int)sizeof(char));
    printf ("short size : %d byte\n", (int)sizeof(short));
    printf ("int size : %d byte\n", (int)sizeof(int));
    printf ("long size : %d byte\n", (int)sizeof(long));
    printf ("double size : %d byte\n", (int)sizeof(double));
    printf ("long double size : %d byte\n", (int)sizeof(long double));
    printf ("\n-- Pointer Data Type Size -- \n");
    printf ("char* size : %d byte\n", (int)sizeof(char*));
    printf ("short* size : %d byte\n", (int)sizeof(short*));
    printf ("int* size : %d byte\n", (int)sizeof(int*));
    printf ("long* size : %d byte\n", (int)sizeof(long*));
    printf ("double* size : %d byte\n", (int)sizeof(double*));
    printf ("long double* size : %d byte\n", (int)sizeof(long double*));

    return 0;
    
}