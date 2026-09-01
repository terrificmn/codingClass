#include <stdio.h>
void print_str(char **pps, int cnt);

int main() {
    char *ptr_ary[] = {"eagle", "tiger", "lion", "squirrel"};
    int count;

    count = sizeof(ptr_ary) / sizeof(ptr_ary[0]);
    print_str(ptr_ary, count);

    return 0;
}

void print_str(char **pps, int cnt) {
    int i;
    for (i=0; i < cnt; i++) {
        //printf("%s\n", pps[i]);
        printf("%s\n", *(pps + i)); //같은 표현 또는 pps[i]

    }
}

//todo: 복습하기 (425부근)