#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct profile {
    int num;
    char name[20];
    char *skill; // �����ʹ� ����Ϸ��� �����Ҵ��� �������
};

struct sports {
    char *event;
    struct profile player;  //sports ����ü �ȿ� profile ����ü ������ ���� (player)
};

int main() {
    struct sports a; //����ü ���� ����
    a.event = (char *)malloc(10 * sizeof(char)); //#include <stdlib.h> ���� �������, �� ���� malloc()�Լ��� �������� �޸� �Ҵ��� ���ش�
    //strcpy(a.event, "figure skating"); //Ʋ�� ��//event�� �������̹Ƿ� �����Ҵ��� �����ؾ��� //
    a.event = "soccer game";

    //a.player.name = "Yuni Seo"; //Ʋ�� �� //name[]�迭������ �Ǿ��־� ���ڻ�� �Է� �Ұ�, strcpy()����ؾ���
    strcpy(a.player.name, "Yuni Seo"); //���� <string.h> ��������� ���Խ��Ѿ� ��
    
    //a.player = 19; //Ʋ�� ��   //player�� profile ����ü�� ������ �����̹Ƿ� a.player.num ���� �����ؾ��Ѵ�
    a.player.num = 19;

    a.player.skill = (char *)malloc(10 * sizeof(char)); // �׳� malloc(80) �ص� ��
    //scanf("%s", a.player.skill); //Ʋ�� ��: ���� �ڵ� ���� ���� �Ҵ� ���� scanf �� ���
    //skill�� �������̹Ƿ� �����Ҵ��� ���� ���ش�
    printf("��ų�� �Է��ϼ���: ");
    scanf("%s", a.player.skill);

    printf("a����ü��.event: %s\n", a.event);
    printf("a����ü��.player(profile����ü).name: %s\n", a.player.name);
    printf("a����ü��.player(profile����ü).num: %d��\n", a.player.num);
    printf("a����ü��.player(profile����ü).num: %s\n", a.player.skill);
    
    return 0;
}