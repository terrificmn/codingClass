# 퀴즈1
wt = 75
ct = True

if wt >= 80 and ct == True:
    print('합격')
else:
    print('불합격')

# 실전퀴즈
kor, eng, math, science = map(int, input().split())

if ((kor > 100 or kor < 0) or (eng > 100 or eng < 0) or (math > 100 or math < 0) or (science > 100 or science < 0)):
    print("잘못된 점수")
else:
    if (kor+eng+math+science)/4 >= 80:
        print('합격')
    else:
        print('불합격')
