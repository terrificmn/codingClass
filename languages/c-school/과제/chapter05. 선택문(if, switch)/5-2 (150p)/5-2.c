#include <stdio.h>
int main() {
    int age = 25, chest = 95;
    char size;

    if (age < 20) {
        if (chest < 85) {
            size = 'S'; //문자 캐릭터 하나는 ''(싱글로 묶는다)
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

    printf("사이즈는 %c입니다.\n", size);
    return 0;
}












