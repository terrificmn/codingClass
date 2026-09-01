#include <stdio.h>
int main() {
/*
    double ary[5] = {1.2, 3.5, 7.4, 0.5, 10.0};
    double *pa = ary;
    double *pb = ary +2;

    printf("%.1lf\n", ary[0]);
    printf("%.1lf\n", *(ary +1));
    printf("%.1lf\n", *(pa + 2));
    printf("%.1lf\n", pa[3]);
    printf("%.1lf\n", *pb);
    printf("%.1lf\n", *pb - *pa);
*/
    double ary[5] = {1.2, 3.5, 7.4, 0.5, 10.0};
    double * pb = ary;
    int i;

    for (i = 0; i < 3; i++) {
        printf("%.1lf ", *pb);
        pb++; //주소값을 +
    }
    return 0;
}