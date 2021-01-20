'''
#연습문제
def get_max_score(*args):
    return max(args)

korean, english, mathematics, science = 100, 86, 81, 91

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)
'''

korean, english, mathematics, science = map(int, input().split())

def get_min_max_score (*args):
    #minValue = min(args)
    #maxValue = max(args)
    #return minValue, maxValue
    return min(args), max(args)

def get_average (**args):
    #가변파라미터로 딕션너리 구조로 값이 넘어오면 keys(), values()메소드를 사용해서 처리해야함
    #avgValue = sum(args)/len(args)
    #return avgValue
    return float(sum(args.values())/len(args.keys()))
    

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
#get_average(korea=korean) 처럼 함수를 딕셔너리 구조 넘겨줄 때는 함수내에서 values()/keys()메소드를 사용해야 함
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
