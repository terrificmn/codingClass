#include <stdio.h>

// void �Լ� ���� 
void print_char(char ch, int count);

int main() {
    print_char('@', 11);
    return 0;
}

void print_char(char ch, int count) {
    int i;

    if(count > 10) return;  // void�Լ����� �Լ��� ���� ���� ��ų ���� return ���� �Լ��� �����ų �� ����, ������ �ѱ� ���� ���� 
    for (i=0; i < count; i++) {
        printf("%c", ch);
    }
    return;
}

