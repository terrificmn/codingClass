#include <stdio.h>
#include <stdlib.h>
int main() {
    int *pi;
    int size = 5, count = 0;
    int num, i;

    pi = (int *)calloc(size, sizeof(int));  //size��ŭ (5)  int 4byte �޸𸮿� �Ҵ�. ��, 20��ŭ �Ҵ�
    while (1) {
        printf("����� �Է��ϼ��� :");
        scanf("%d", &num);
        if (num <= 0) break; // �Էµ� ���� ������ �������� break
        if (count == size) { // �Էµ� ���� ���� �� ���� count++  �Ǹ鼭 size�� ������
            size += 5;
            pi = (int *)realloc(pi, size * sizeof(int));  //realloc(����*pi, �߰��� ũ�� (size * sizeof(int)) )
        }
        pi[count++] = num;  //pi�����ʹ� �޸� �Ҵ��� �Ǿ����Ƿ� �迭ó�� ��밡��  
        // count++ ��� +1 �����ָ鼭 ���ÿ� �迭�� �ε����� ����Ŵ -----> num �Էµ� �� �־��ֱ� 
        //? count++ �ϴ� 0���� num�� �Ҵ�, �� �Ŀ� +1 �Ǿ� count�� 1�� ��
    }
    
    for (i=0; i < count; i++) {
        printf("%5d", pi[i]);
    }
    free(pi);
    printf("�� ī��Ʈ: %d", count);
    return 0;
}
