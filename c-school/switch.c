#include <stdio.h>
int main() {
    /*
    switch (��) { //���⿡�� ���� ������ ������
        case �񱳰�1: ���๮;
            break;   //break�� ������ ���� ������ �����ڵ���� ����� �� ������ ����
        case �񱳰�2: ���๮;
            break;
        case �񱳰�3: ���๮;
            break;
        case �񱳰�4: ���๮;
            break;
        case �񱳰�5: ���๮;
            break;
        default: ���๮; //�⺻������ 
    }
    */
    int rank = 2, m =0;

    switch (rank) {
        case 1:
            m = 300;
            break;
        case 2:
            m = 200;
            break; //break ������ �����ϳ�, ���� ������ �ϸ� ���ϴ� ����� �ȳ��´�. �Ʒ��ڵ��� case3���� ������ �Ǿ m =100�� ��
        case 3:
            m = 100;
            break;
        default:
            m = 10;
            break;
    }
    printf("switch�� ��� m : %d\n", m);

    // if������ ��ȯ
    if (rank == 1) {
        m = 100;
    } else if (rank == 2) {
        m = 200;
    } else if (rank == 3) {
        m = 100;
    } else {
        m = 10;
    }
    printf("if�� ��� m: %d", m);

    return 0;
}