//int f;
    //int a = -4, b=3, c= -5, d=2;
    //f = a*b % c /d;
    //printf("%d", f);

    // int a=2, b=3, c=4, d=5;
    // a = ++c + c++ + ++c + c++;
    // printf("%d", c);

/* ////////////////13��
#include <stdio.h>

struct point {
        int xpos;
        int ypos;
    };
void OrgSymTrans(struct point * ptr) {
    //printf("%d ", ptr[0]); //���� �� �׽�Ʈ
    //printf("%d \n", (ptr+0)->ypos); //���� �� �׽�Ʈ

    if ((ptr+0)->xpos > 0) {
        (ptr+0)->xpos -= 14;  //���� ��ȯ
    } else if ((ptr+0)->xpos < 0) {
        (ptr+0)->xpos += 14;  //��� ��ȯ
    }  

    if ((ptr+0)->ypos < 0) {
        (ptr+0)->ypos += 10;  //��� ��ȯ
    } else if ((ptr+0)->ypos > 0) {
        (ptr+0)->ypos -= 10;  //���� ��ȯ
    }
    //printf("%d ", ptr[0]);  //���� �� �׽�Ʈ
    //printf("%d \n", (ptr+0)->ypos); //���� �� �׽�Ʈ
}
void ShowPosition(struct point pos) {
    printf("[%d, %d]\n", pos.xpos, pos.ypos);
}

int main() {
    struct point pos={7, -5};
    OrgSymTrans(&pos);
    ShowPosition(pos);
    OrgSymTrans(&pos);
    ShowPosition(pos);
    return 0;

    
}
*/

#include <stdio.h>
void ShowArr(int (*arr)[4]);
void RotateArr(int (*arr)[4]);

int main(void) {
    int i = 0;
    int arr[4][4] = {
                {1, 2, 3, 4},
                {5, 6, 7, 8},
                {9, 10, 11, 12},
                {13, 14, 15, 16}
    };

    for(i=0; i<4; i++) {
        ShowArr(arr);
        RotateArr(arr);
    }

    return 0;
}

void ShowArr(int (*arr)[4]) {
    int i, j;
    printf("----Show Array----\n");

    for(i=0; i<4; i++) {
        for(j=0; j<4; j++) {
            printf("%5d", arr[i][j]);
        }
        printf("\n");
        
    }
}

/* �ð���� 90���� �̵����� ����ϱ�
 1  2  3  4    13   9  5   1    16  15  14  13     4  8  12  16 
 5  6  7  8    14  10  6   2    12  11  10   9     3  7  11  15
 9 10 11 12    15  11  7   3     8   7   6   5     2  6  10  14
13 14 15 16    16  12  8   4     4   3   2   1     1  5   9  13


*/

void RotateArr(int (*arr)[4]) {
    int i, j, k = 3;
    int count = 1; 
    static int func_count = 0;
    func_count += 1;  //�Լ� ȣ�� �� ������ ī��Ʈ ���ֱ�
    //printf("%d", func_count); //test
    int tmp[4][4];
    k *= func_count;  // 3, 6, 9, 12
    //printf("%d", k);
    
    for(i=0; i<4; i++) {
        for(j=3; k >= 0; j--) {
            arr[i][j] = count;
            count += 4;
        }
        count = i + 1; //�ʱ�ȭ //i==0�϶� +1�ؼ� 1�� �ʱ�ȭ
        count += 1; // i��°�� �Ѿ�� 1���� �迭 �ݺ��� �Ͼ �� ���ϴ� ���ڰ� ������ ����
    }
    // for(i=0; i < 4; i++) {
    //     for(j=0; j < 4; j++) {
            
    //     }
    // }
    

/* 
// switch ���� 3�� �ݺ�
    switch (func_count) {
        case 1: 
            for(i=0; i<4; i++) {
                for(j=3; j >= 0; j--) {
                    arr[i][j] = count;
                    count += 4;
                }
                count = i + 1; //�ʱ�ȭ //i==0�϶� +1�ؼ� 1�� �ʱ�ȭ
                count += 1; // i��°�� �Ѿ�� 1���� �迭 �ݺ��� �Ͼ �� ���ϴ� ���ڰ� ������ ����
            }
            break;
        
        case 2:
            for(i=3; i >=0; i--) {  //�Ųٷ�
                for(j=3; j >= 0; j--) {  //�Ųٷ�
                    arr[i][j] = count++;  //�׳� �ܼ��� �Ųٷ� ����Ѵ�, count�� �ܼ��� +1��
                }
            }
            break;
        
        case 3:
            for(i=3; i>=0; i--) {
                for(j=0; j < 4; j++) {
                    arr[i][j] = count;
                    count += 4;
                }
                count = j-i; //�ʱ�ȭ //j�� �׻� 4�� ������ 4- (i)�μ�, i�� 3, 2, 1, 0 �� ��
                count += 1; //�� �ڵ� ����� ���� +1�� ���Ѽ� ī��Ʈ�� i��° ������ �� ���ϴ� ���ڰ� �ǰ� ��
            }
            break;

        default: 
            break;
    }
*/
}

/*
    // �� ��° �����̼� ����
    for(i=3; i>=0; i--) {
        for(j=0; j < 4; j++) {
            arr[i][j] = count;
            count += 4;
        }
        count = j-i; //�ʱ�ȭ //j�� �׻� 4�� ������ 4- (i)�μ�, i�� 3, 2, 1, 0 �� ��
        count += 1; //�� �ڵ� ����� ���� +1�� ���Ѽ� ī��Ʈ�� i��° ������ �� ���ϴ� ���ڰ� �ǰ� ��
    }
*/

/*  
    // �� ��° �����̼� ����
    for(i=3; i >=0; i--) {  //�Ųٷ�
        for(j=3; j >= 0; j--) {  //�Ųٷ�
            arr[i][j] = count++;  //�׳� �ܼ��� �Ųٷ� ����Ѵ�, count�� �ܼ��� +1��
        }
    }
*/

/*
    //ù ��° �����̼� ����
    for(i=0; i<4; i++) {
        for(j=3; j >= 0; j--) {
            arr[i][j] = count;
            count += 4;
        }
        count = i + 1; //�ʱ�ȭ //i==0�϶� +1�ؼ� 1�� �ʱ�ȭ
        count += 1; // i��°�� �Ѿ�� 1���� �迭 �ݺ��� �Ͼ �� ���ϴ� ���ڰ� ������ ����
    }
*/



