#include <stdio.h>
    int main() {
        int a = 10, b = 20;
        int *pa = &a, *pb = &b, *pt;
        pt = pa; //포인터 pt에 pa 주소참조 하면 pa는 &a주소를 참조하므로 10
        pa = pb; //포인터 pa에 pb 주소참조 하면 pb는 &b주소를 참조하므로 20
        pb = pt; //포인터 pb에 pt 주소참조 하면 pt는 pa 주소 참조 즉, &a주소를 참조하므로 10

        printf("%d, %d, %d\n", *pa, *pb, *pt);

        return 0;
    }


