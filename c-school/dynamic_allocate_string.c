#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
/*
    char temp[90];
    char *str[3];
    int i;

    for (i=0; i < 3; i++) {
        printf("���ڿ��� �Է��ϼ���: ");
        gets(temp);
        str[i] = (char *)malloc(strlen(temp) +1); //�迭�����Ϳ� �޸� �Ҵ� (�Է¹��� temp)�� ���̸�ŭ+1 �ؼ� �Ҵ����� (0�ι��� ����+1)
        strcpy(str[i], temp);  // �Ҵ�� str[i]�� �Է¹��� temp �־��ֱ�
    }

    for (i=0; i < 3; i++) {
        printf("%s\n", str[i]);
    }

    for (i=0; i < 3; i++) {
        free(str[i]);
    }
*/
    //todo: �����ʿ�!
    // ���� ������ �̿��ؼ� �޸� �Ҵ��ϱ�  2���� �迭�� ����
    char **p_mat = (char **)malloc(4 * sizeof(char *));
    int i, j, row, col;


    //p_mat = (char **)malloc(4 * sizeof(char *));
    row = sizeof(p_mat) / sizeof(p_mat[0]);
    //col = sizeof(p_mat[0]) / sizeof();
    //printf("%d", row);

    for (i=0; i < 4; i++) {
        p_mat[i] = (char *)malloc(5 * sizeof(char));
    }

    for (i=0; i < 4; i++) {
//            printf("���ڿ��� �Է��ϼ���: ");
  //          gets(p_mat[i]);
            
    }
    
    for (i=0; i < 4; i++) {
    //    printf("%s\t\n", p_mat[i]);
    }

    for (i=0; i < 4; i++) {
        free(p_mat[i]);
    }
    
    //todo: �ذ��ϱ� p473.
}