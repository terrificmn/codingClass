////////// �����͸� �̿��� �Լ� 

#include <stdio.h>
int *sum (int a, int b); // ���Ϲ��� �Լ��� �����ͷ� ����
int *get_num();

int main() {
    int *resp;

    resp = sum(10, 20); //resp�� �����ͷ� sum()�Լ��� ����� ���Ϲ��� ����� �ּ� &res�� �ּ��̹Ƿ� ���� ����� ����Ű�� ����
    printf("�� ������ ��: %d\n", *resp);
    printf("���Ϲ��� ����: %d\n", *get_num()); //������ �Լ��� ���Ϲ���

    return 0;
}

int *sum (int a, int b) { //* ������� �ּҰ����� ���� //�����ͷ� res�ּҰ��� ��ȯ��Ŵ
    static int res; //* ����ƽ���� �������� ������ �����ؼ� �޸𸮿� ��� �����ְ� ��
    res = a + b;
    return &res; //����ƽ���� ����� res�� �ּҰ��� ��ȯ
} 

int *get_num() {
    static int n;
    printf("get_num()�Լ��Դϴ�. �Է��ϼ���: ");
    scanf("%d", &n); //�ּҰ� �ѱ��
    return &n;
}