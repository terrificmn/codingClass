#include <stdio.h>
int main() {

/*
// array�ʱ�ȭ �����..
int array[5];
array[0] = 10;  //�ܼ��� �ε������� �ִ� ���
array[1] = 20;
array[2] = 30;
array[3] = 40;
array[4] = 50;
// �ʱ�ȭ�� ���ϸ� �� ������ �� (�����Ⱚ)�� �� ������ ����

// �Ǵ� �ѹ��� �ʱ�ȭ
int arr1[5] = {1, 2, 3, 4, 5};
int arr2[100] = { 0 }; //
int arr3[] = {1, 2, 3};  //�迭ũ�⸦ ������ �ʰ� {}�� ������ ������ ���� ����, 3���� �迭�� ����
*/

int score[5];
int i;
int total = 0;
double avg;

    for (i=0; i< 5; i++) {
        scanf("%d", &score[i]);
        total += score[i];
    }
    avg = total / 5.0;

    for (i=0; i< 5; i++) {
        printf("%5d", score[i]); // %5d�� ������ ȿ���� �ִ�. ������ ���ڸ� 5��ŭ ���������� ä��� �������� �������� ä������ 
                                // �ݴ�� -5%d�� �ϸ� �������� ���� ���ڰ� ��ġ�ǰ� �������� �������� ä����
    }
    printf("\n���: %.1lf\n", avg);

    return 0;


//todo: Ȯ���غ���
for (i=0; i< 10; i++) {
        printf("%d / 3 = %lf\t", i, (double)i/3);
        printf("%d %% 3 = %d\n", i, i%3);
    }
//todo: Ȯ���غ���

}