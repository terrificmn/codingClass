#include <stdio.h>
#include <string.h>

int main () {
    char str1[80], str2[80];
    char temp[80];

    printf("�� ���ڿ� �Է��ϼ���: ");
    scanf("%s %s", str1, str2);
    printf("�ٲٱ� �� : %s, %s\n", str1, str2);
    strcpy(temp, str1);
    strcpy(str1, str2);
    strcpy(str2, temp);
    printf("�ٲ� ��: %s, %s\n", str1, str2);

    return 0;

}