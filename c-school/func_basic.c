#include <stdio.h>

void add() {  //void ���ϰ��� ���� �Լ�
    printf("%d + %d = %d\n", 2, 3, 2+3);  //�ܼ� ��¸� �ϰ� ������ ���� ����
}

void add2(int a, int b) {  //void ���ϰ��� ���� �Լ�, ���ϰ��� ������ �Ķ���ͷ� �������� ���� �� �ִ�
    printf("%d + %d = %d\n", a, b, a+b); //�Ķ���ͷ� ���� ������ ��� �� ��¸� �ϰ� ������ ���� ����
}

int add3(int a, int b) {  //���ϰ��� ���� ���� ���ϰ��� �´� Type���� �����ؾ��Ѵ� 
    int sum = a + b;
    return sum;  //�����ϴ� sum�� integer�̹Ƿ� �Լ��� int�� ����
}


int main() {
    int a = 10, b =20;
    int sum;

    add(); //�ƱԸ�Ʈ �ѱ� ���� ���� ���� ���ȣ�� ��
    add2(a, b);
    
    sum = add3(a, b);
    printf("%d", sum);

    return 0;
}
