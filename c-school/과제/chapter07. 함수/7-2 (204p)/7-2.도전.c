#include <stdio.h>
int rec_func (int n);
int fac(int num);

int main() {

    printf("%d\n", rec_func (10));
    printf("%d", fac (5));
    return 0;
}

int rec_func (int n){
    int count=0;
    
    if (n == 0) {
        return 0;
    }
    //-1���ҽ��Ѽ� �Լ� ȣ�� ..�׸��� �� �ݺ�
    // ���������� ���� if������ 0�� �Ǿ� 0�� ���Ϲ����� �ٽ� �� ���� �Լ��� ȣ���� �κ����� ���ư��� 
    // ���ϰ���(-1�� ��) + ����n���� ������ ���� ����
    count = rec_func(n -1);
    count += n;
    return count;
    
    //���� �ڵ带 �ѹ��� ����
    //return rec_func(n -1) + n;  
}


int fac(int num) {
    
    if (num == 1) {
        return 1;
    }
    
    return fac(num - 1) * num;

}
//todo: ����!