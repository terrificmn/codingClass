#include <stdio.h>
int main() {
    int age = 25, chest = 95;
    char size;

    if (age < 20) {
        if (chest < 85) {
            size = 'S'; //���� ĳ���� �ϳ��� ''(�̱۷� ���´�)
        } else if (chest >= 85 && chest < 95) {
            size = 'M';
        } else if (chest >= 95) {
            size = 'L';
        }

    } else {
        if (chest < 90) {
            size = 'S';
        } else if (chest >= 90 && chest < 100) {
            size = 'M';
        } else if (chest >= 100) {
            size = 'L';
        }

    }

    printf("������� %c�Դϴ�.\n", size);
    return 0;
}












