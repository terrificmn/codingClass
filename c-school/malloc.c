#include <stdio.h>
#include <stdlib.h>
//** malloc �Լ��� ����Ϸ��� <stdlib.h> �� ������ �ؾ���

int main () {
    int *numPtr = malloc(sizeof(int) *10); //���� �޸� �Ҵ�, int �������� 10�� ��ŭ
    // int numArr[10] �� ���� ȿ��
    int i, size;

    // �޸� �Ҵ� ���� �����͸� �迭 ó�� ��밡��
    numPtr[0] = 10;
    numPtr[9] = 20;
    
    // size = sizeof(numPtr)/ sizeof(numPtr[0]); �޷θ��� �Ҵ�Ǿ� �ְ� ���� numPtr�� �� �ִ� ���� 0��°�� 9��° ����
    //numPtr ������� 8, �迭�ϳ��� 4 (int)

    // printf("%d\n", sizeof(numPtr[0]));  //������ ,fail
    // printf("%d\n", sizeof(numPtr));
    size = 10;
    for (i=0; i< size; i++) {
        numPtr[i] = i + 10;
        printf("�޸��Ҵ�%d %d\n", i, numPtr[i]);
    }

    // printf("%d\n", numPtr[0]); 
    // printf("%d\n", numPtr[9]);

    free(numPtr); //�޸� ����

//------------�ι�° ����------
    printf("\n\n");
    int *pi;
    double *pd;
    
    pi = (int *) malloc(sizeof(int)); //(int *) malloc���� ��ȯ�Ǵ� ���� int��ȯ  
    //int type���� 4byte ��ŭ �޸𸮿� �Ҵ� 
    
    if (pi == NULL) {
        printf("# �޸𸮰� �����մϴ�.\n");
        exit(1);
    }
    pd = (double *) malloc(sizeof(double)); //(double *) ��ȯ�Ǵ� �ּҸ� double type���� ��ȯ    
    //double type���� 8byte ��ŭ �޸𸮿� �Ҵ� 

    *pi = 10;
    *pd = 3.4;

    printf("���������� ���: %d\n", *pi);
    printf("�Ǽ������� ���: %.1lf\n", *pd);

    free(pi);
    free(pd);

    return 0;
}