#include <stdio.h>
#include <string.h>
int main()
{
    char str[30];
    char replacedStr[30]; //���� �ٲ� ���ڿ� 
    char star[20]; // * ���ڿ� �־��� ����
    int len;

    printf("�Է��ϼ���: ");
    scanf("%s", &str);
    getchar(); //���� ����

    len = strlen(str);
    //printf("�������ڿ�%d\t", len); //test
    if (len > 5 && len < 15) {
        strncpy(replacedStr, str + 0, 5);
        replacedStr[strlen(replacedStr)] = '\0'; //*�ι��� �־��ֱ�, �����Ⱚ�� �о���� ����
            //printf("�ٲ﹮�ڿ� ���� %d\t", strlen(replacedStr)); //test
        strncpy(star, "********", len - 5);
        //printf("%d\t", strlen(star)); // ������ ���� ���� �־����� ���� �����Ⱚ�� � ���� �� //test
        //printf("%s ", star);  //���� �°� ���� �� �����Ⱚ�� ���� ���� ���� //test
        star[len - 5] = '\0'; //�Է¹��� ���̿��� 5�� ���� �׳� null ����
            //printf("%d\t", strlen(star)); // �°� ���� //test
            //printf("%s ", star); //test
        strcat(replacedStr, star); //����

    } else if (len >= 15) {
        strncpy(replacedStr, str + 0, 15); //15�ڷ� ����
        strncpy(star, "********", len - 5);
        star[len - 5] = '\0'; //�� �־��ֱ�
        strcat(replacedStr, star);

    } else { //�ܾ���� 4�ڸ� ����
        strcpy(replacedStr, str);
    }
    
    printf("�Է��� �ܾ�: %s,  ������ �ܾ�: %s", str, replacedStr);
    return 0;
}