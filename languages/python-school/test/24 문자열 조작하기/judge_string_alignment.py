#표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 
# 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 
# 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.

text = list(map(int, input().split(';')))
text.sort(reverse=True)

for i in range(len(text)):
    ''' #변수로 할당해서 format으로 숫자에 쉼표를 만들어 준 후에 
    commaTxt = format(text[i], ',')
    # 또는 $s를 이용하거나
    print('%9s' % commaTxt)
    # format()을 사용하기 
    print('{0:>9}'.format(commaTxt))
    '''
    # %9s(오른쪽정렬)과 format을 한꺼번에 써도 됨 (여기서 format함수는 ()중괄호로 묶어주기)
    print('%9s' % (format(text[i], ',')))
    