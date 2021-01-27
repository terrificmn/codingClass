#include <stdio.h>
int main() {
    int A[3] = {1, 2, 3};
    int B[10];
    int i, j, k, u;

    for (i=0; i<10; i++) {
        B[i] = A[i % 3];
    }

    for (i=0; i<10; i++) {
        printf("%-3d", B[i]);
    }
    
    return 0;

}
