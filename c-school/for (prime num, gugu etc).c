#include <stdio.h>
int main()
{
    // while�� ����
    // while (���ǽ�) {
    //     ���๮
    // }
    /*
    // while�� �ݺ�
    int i = 0;
    while (i < 2) {
        printf("%d\n", i);
        i++; //���ѹݺ��� �������� i�� ����
    }

    // for�� �ݺ�
    for (i=0; i < 10; i++) {
        printf("%d ", i);
    }
    printf("\n");

    // do while�� : �ѹ��� �����ϰ� �� ������ while������ ���缭 �ݺ�����
    int a =0;
    do {
        printf("�ݺ� ���� do : %d\n", a);
        a += 1;
    } while (a < 3);

*/
    // ������
    /*
    int i, j;
    for (i=2; i < 10; i++) {
        printf("%d��\n", i);
        for (j=1; j < 10; j++) {
            printf("%d X %d = %d\n", i, j, i*j);
        }
    }
*/

    /*
    //i, j�� �ٲ㼭 ����ϱ�, �� ���� ���
    int i, j;
    for (i=1; i < 10; i++) {
        //printf("%d��\n", i);
        for (j=2; j < 10; j++) {
            printf("%d X %d = %d\t", j, i, i*j);
        }
        printf("\n");
    }
*/

    //���ѹݺ��� while�� ������ 1�� �ָ� ��
    // while (1) { �����ڵ� }

    /*�Ҽ�(prime number)��� 
    // �Ҽ�(prime number)��� 
    int nbr, i, j, c;
    printf("2 �̻��� ������ �Է��ϼ��� :");
    scanf("%d", &nbr);
    
    for (i=2; i< nbr; i++) {
        for (j=2; j < i; j++) {
            if (i % j == 0) {
                break;
            }
        }

        if (j == i) {
            if (c == 5) {
                printf("\n");
                c = 0;
            } 
            printf("%2d\t", i);
            c ++;
        }
        
    }

*/
    char str[100];
    int i, count = 0;

    printf("�Է� (����X): ");
    scanf("%s", &str); //����� �����ؼ� �Է��� �������� %s%s �̷������� �������� ������ ����

    //* for�� �ݺ��� �� ���ڿ� �迭��ŭ �ݺ���ų���� ���ڿ�[i] (��: i < str[i]) �˾Ƽ� ���ڿ� �迭��ŭ �ݺ��Ѵ�
    for (i = 0; i < str[i]; i++)
    {
        count += 1;
    }
    printf("%s", str);
    printf("%d", count); //for���� �迭ũ�⺸�� ������ �ݺ�����
    return 0;
}