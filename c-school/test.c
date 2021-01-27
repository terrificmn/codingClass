#include <stdio.h>
/*
int get_num(void);

int main() {
    int result;
    result = get_num();
    printf("반환 값: %d\n", result);
    return 0;
}

int get_num(void) {
    int num;
    printf("양수 입력: ");
    scanf("%d", &num);

    return num;
*/


/*
void print_char(char ch, int count);
int main(void) {
    print_char('@', 5);
    return 0;

}

void print_char(char ch, int count) {
    int i;

    for (i=0; i < count; i++) {
        printf("%c", ch);

    }
    return;
}
*/

void add_print(int a, int b) {
    printf(a+b);
}

int main() {
    add_print(3, 5);
    return 0;
}
