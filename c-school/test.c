#include <stdio.h>
#include <string.h>
/*
int get_num(void);

int main() {
    int result;
    result = get_num();
    printf("��ȯ ��: %d\n", result);
    return 0;
}

int get_num(void) {
    int num;
    printf("��� �Է�: ");
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

    //getchar()�� putchar()
    printf("���� �Է�: ");
    ch = getchar(); // getchar()�� integer���·� �ƽ�Ű�ڵ�� ����
    putchar(ch);    //putchar(���ڿ�����) �� getchar�� ���� �Է°��� ����� �� ����
    printf("%d", ch); // integer�̱⶧���� ����ϸ� ���ڰ� �����µ� �ٷ� �ƽ�Ű�ڵ��̴�
*/

    char str[80];
    char str1[80];
    // printf("�Է� ���� ����: ");
    // fgets(str, sizeof(str), stdin); // �������� \n �� �߰���
    // printf("%s\n", str);
    
    scanf("%s", str);
    printf("�� �Է�: ");
    scanf("%*c");
    gets(str1);
    
    printf("%s\n", str1);
    return 0;
}
