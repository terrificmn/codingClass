
/*
int get_num(void);

int main() {
    int result;
    result = get_num();
    printf("??? ??: %d\n", result);
    return 0;
}

int get_num(void) {
    int num;
    printf("??? ???: ");
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

/*
#include <stdio.h>
void add_print(int a, int b) {
    printf(a+b);
}

int main() {
    add_print(3, 5);
    return 0;
}
*/

// �Էµ� ���� �߿� �ҹ��ڸ� �빮�ڷ� ���� ��Ű��
/*
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char str[100];
    int i, count = 0;

    printf("���� �Է�: ");
    gets(str);

    for (i = 0; i < str[i]; i++)
    {
        // if (isupper(str[i])) {
        //     count += 1;
        //     str[i] = tolower(str[i]);
        // }
        count += 1;
        printf("%d ", i);
    }
    printf("\n%d ", count);
    //puts(str);
    //printf("�ٲ� ���� ��: %d", count);

    return 0;
}
*/
