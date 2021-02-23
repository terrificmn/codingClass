# A Priori Algorithm 연관규칙분석
먼저 라이브러리를 설치해줘야함  

```
# 리눅스 터미널에서 입력, 윈도우는 아나콘다 터미널
pip install apyori

# colab에서는 아래처럼 실행, 재 접속했을 때는 메모리 등 다시 할당되므로
# 매번 접속할 때 설치를 해줘야한다
!pip install apyori
```

## 파일가져오기
pd.read_csv()로 파일을 가져올 때 데이터베이스에서 가져온 csv이기 때문에
컬럼명이 따로 없음 처음 row에 있는 데이터일뿐, 유저가 장바구니에 각각 담은 목록  
그래서 A priori 알고리즘을 할 때에는 `header=None` 파라미터로 불러와야 함

- read_csv() 파라미터 header=None
```py
pd.read_csv('Market_Basket_Optimisation.csv', header=None)
```

- NaN 데이터 처리
NaN 데이터를 지우는 전략이 아니라 문자열 'nan'으로 바꿔줌  
`df.fillna('nan', inplace=True)`


## apriori 모듈 불러오기
apriori 알고리즘 모듈  
```py
from apyori import apriori
```

- apriori() 사용 파라미터  
apriori()를 만들 때의 파라미터들
transactions =df.values ---> data프레임의 numpy array를 넣어줘야함  
min_support는 예를 들어 햄버거와 프렌치 프라이가 같이 있을 경우  
min_support = 0.002 ---> 1000개중에 2개    
min_lift = 3 ----> 3이상인 것을 찾음 (1 이면 관련이 없는 것)  
```py
rules = apriori( transactions=df.values, min_support= 0.002, min_confidence= 0.3, min_lift = 3, min_length= 2, max_lengh= 2)

```

- 리스트로 만들기, inspect(사용자함수)
```py
# 먼저 위의 rules를 리스트화 해준다
list(rules)

# 이 함수는 가져다 쓰면 됨
def inspect(results):
    lhs         = [tuple(result[2][0][0])[0] for result in results]
    rhs         = [tuple(result[2][0][1])[0] for result in results]
    supports    = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts       = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
```

- pandas DataFrame로 만들기  
위의 inspect()함수를 이용해서 데이터프레임으로 만든다
```py
# 컬러명은 priori에서 정해져 놓은 명칭
# Left Hand Side를 사면 Right Hand Side를 산다로 보면 됨
pd.DataFrame(data= inspect(result), columns= ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift' ] )
```

- 'Lift' 컬럼으로 정렬  
'Lift'가 높을 수록 높은 관계이며, 1이면 관련이 없음
```py
result_df.sort_values(by ='Lift', ascending=False)
```


