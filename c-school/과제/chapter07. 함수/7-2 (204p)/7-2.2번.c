#include <stdio.h>
int sum (int total);

int main() {
    sum(10);
    sum(100);
    return 0;
}

int sum (int total){
    int i, count =0;
    
    for (i=1; i<=total; i++) {
        count += i;
    }
    printf("1���� %d������ ���� %d �Դϴ�\n", total, count);
    
}
