#include <stdio.h>
#include <string.h>
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

int main() {
/*
    int ch;

    //getchar()와 putchar()
    printf("문자 입력: ");
    ch = getchar(); // getchar()는 integer형태로 아스키코드로 받음
    putchar(ch);    //putchar(문자열변수) 로 getchar로 받은 입력값을 출력할 수 있음
    printf("%d", ch); // integer이기때문에 출력하면 숫자가 나오는데 바로 아스키코드이다
*/

    char str[80];
    char str1[80];
    // printf("입력 공백 포함: ");
    // fgets(str, sizeof(str), stdin); // 마지막에 \n 이 추가됨
    // printf("%s\n", str);
    
    scanf("%s", str);
    printf("또 입력: ");
    scanf("%*c");
    gets(str1);
    
    printf("%s\n", str1);
    return 0;
}
