#include <stdio.h>
int main() {
    /*
    int i;
    for (i=0; i < 10; i++) {
        printf("$");
    }
    */
    int i, j;
    /*
    for (i=0; i< 3; i++) {
        for (j=0; j < 4; j++) {
            printf("BE HAPPY!\n");
        }
    }
    */

//Ȯ�ι��� 3 (176p)
//! 2�� for�� ��Ģ �ľǽÿ��� ǥ�� �׸������� �����ϸ� ����� �� �� (i�� row�� j�� column)
    for (i=0; i < 5; i++){
        for (j=0; j < 5; j++) {
            if (j == i || j == i && j + 1 ==4 || j + i == 4) {  //or ||(or)�� �ѹ��� else if �� ������ ���� ���� ����
                printf("*");
            } else {
                printf(" ");
            }
        }
        printf("\n"); //j �ݺ� ������ �ٹٲ�
    }
    return 0;
}