#include <stdio.h>
//* c����� Ư¡: �޸𸮿� �Ҵ�Ǵ� ������ ���� �Լ��� �ν��ϹǷ� ȣ��޴� �Լ��� �׻� ���ʿ� �ڵ��ؾ��Ѵ�
//* ��, main()�Լ� ���� �Լ��� ���� �ϸ� ���� ���� ����� �� �ִ�

/* void add() {  // ������ ���� ���� ���� void�� �Լ��� �����
    }
*/
int sum(int x, int y); //�Լ��� ������ , �Լ� ��ü�� main()�Լ� �Ʒ��� �ִٸ� �ν��� ���ϳ�,
// �Լ� ���ǰ� �ȵǾ��ִٸ�, warning: implicit declaration of function 'sum' ���� ������ ������, ���� ������ ������
// �� ó�� �Լ� ���Ǹ� �ϸ� main()�Լ����� �Լ� �ν��� �Ѵ�

//! �Լ� ���ǽÿ� �߿��� ���� ������ ���� � type�ΰ��� ���� �Լ��� type�� ����������Ѵ�
// ���� �Լ��� ��� �Ʒ��� centi_to_meter()�Լ��� doublt�� �Ǽ��� �����ϰ� �Ǵµ� ���⿡�� 
// int centi_to_meter()�̷������� �����ϰ� �Ǹ� ���� �Ҽ����� ©���� ���ϵǰ� �Ǿ�, ���ϴ� ������� ������ ���� �� �ִ�.
// �߰��� ������ ���� ���� �Լ��� void function_name() ���� �����Ѵ�
// �Ķ���͵� type�� �°� �����ϸ� ��
double centi_to_meter(int cm);


int main () {
    int a = 10, b =30;
    int result;

    result = sum(a, b);
    printf("result : %d\n", result);

    /// centi_to_meter() ��� ����: 187cm���� m�� ��ȯ�ϴ� ����� �Լ� *�Լ� type�� ����
    double res;
    res = centi_to_meter(187);
    printf("%.2lfm\n", res);

    return 0;
}

int sum(int x, int y) {
    //int temp;
    //temp = x + y;
    //return temp;
    return x+y;
}

double centi_to_meter(int cm) { //��ȯ�Ǵ� ���� ���� type�� �Լ��� ������ �ش�. (return�� ���������� �Ǹ�, �Լ��� double�� ����)
    double temp;
    temp = (double)cm / 100.0;
    return temp;
}