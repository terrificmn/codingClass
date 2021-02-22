# 협업 필터링 Collaborative Filtering영화 추천
tsv (tab으로 되어 있는 형식) 일때는 

`pd.read_csv('u.data', sep='\t', names=[  'user_id', 'item_id', 'rating', 'timestamp' ])` 
- set='\t' 파라미터를 이용한다
- names='[ ]'파라미터는 컬럼명을 정해줌


## 데이터 프레임 합치기
- merge 두 개의 데이터프레임 합치기
```py
pd.merge(movies_rating_df, movie_titles_df, on='item_id')
```
on='컬럼명' --> 공통되는 컬럼이 있을 때 merge() 메서드 사용가능

- concat 두 개의 데이터프레임 합치기
```py
#axis=1 파라미터로 컬럼으로 합치기
# 리스트로 묶어 준다
pd.concat( [ratings_df_count, ratings_df_mean], axis=1) 
```
원래는 위 아래 row로 데이터를 합쳐준다
그래서 row로 데이터를 붙일 때는 axis=파라미터를 생략하거나 axis=0 한다

- join 두 개의 데이터프레임 합치기
```py
# 기존의 DataFrame에다가 합침?
retings_df_count.join( ratings_df_mean)
```
join은 시리즈 일 때는 사용이 안된다


## 데이터프레임 컬럼명 바꾸기
- 데이터프레임 컬럼명 바꾸기 
기존 컬럼이 각각 rating, rating 일 때
```py
ratings_mean_count.rename(columns={'rating': 'count', 'rating': 'mean'})
```
 이런 경우는 딕셔너리에서 키 값이 중복이면 마지막 키만 처리하기 때문에 마지막컬럼 2번째 컬럼만 바뀜
(참고: cpu는 왼쪽->오른쪽, 위->아래 연산함)

다른방법은 columns 속성을 이용해서 바꿀 수 있다. 리스트로 저장시키면 끝
```py
ratings_mean_count.columns #columns 속성으로 데이터 접근 
ratings_mean_count.columns = ['count', 'mean']
```

## 피봇 테이블 하기
피봇팅 한다. 즉 컬럼의 값을 행으로 만드는것. (unique하게 만들어 준다)
그래서 여러개의 숫자 데이터를 합치거나 평균을 내거나, 표준편차를 연산할 수 있음
한 컬럼의 값이 겹칠 때 그 컬럼을 합치면서 이와 관련된 다른 컬럼의 값을 더하거나 해줌

- 피붓 테이블 pivot_table()
```py
# 아래 설명 참고
movies_rating_df.pivot_table(index='user_id', columns='title', values='rating')
```
피봇테이블 `pivot_table( index=, columns=, values= )`  
  
`index=` 파라미터: 특정컬럼을 index (row)(왼쪽)를 만들어준다  
`columns=`파라미터: 특정컬럼을 말그대로 컬럼으로 만들어 준다. 컬럼에서 여기서는 title컬럼에서 중복되는 문자열들이 컬럼이 된다. 즉 unique()같은 효과이다  
`values=`파라미터: 이제 인덱스와, 컬럼이 셋팅이 되었고 그 안에 어떤내용으로 넣을 지 결정, 여기에서는 'rating' 타이틀을 이용했고, rating값들이 들어가진다
___  
  
## 특정 컬럼과 다른 컬럼들과의 상관관계 분석 할 때 
- DataFrame.corr()  
데이터 프레임 전체 컬럼들을 상관분석해줌

- corrwith() 메소드: 컬럼들과 특정컬럼의 상관관계를 분석할 때  
```py
#데이터프레임에서 한개의 특정컬럼과 상관분석할 때
userid_movieTitle_matrix.corrwith( userid_movieTitle_matrix['Titanic (1997)'] )

# 상관분석 변수 저장
titanic_series = userid_movieTitle_matrix.corrwith( userid_movieTitle_matrix['Titanic (1997)'] )
```  

- 시리즈 데이터이므로 
```py
# 데이터 프레임으로 만들어줌
titanic_correlations = pd.DataFrame(data= titanic_series, columns=['Correlation'] )
```

- count 컬럼을 만들어 주기  
여기에는 사람들이 영화를 몇 번이나 추천했는지가 없다. 5점을 받더라도 1명~2명한테 별점을 받은거라면 신뢰성이 없기 때문에 count컬럼을 가져와서 붙여준다. join()을 이용
```py
# 기존 상관분석 끝난 df에 join()으로 'count' 컬럼을 가져와서 붙인다
titanic_correlations = titanic_correlations.join( ratings_mean_count['count'] )
```

- NaN 제거
```py
titanic_correlations.dropna(inplace=True)
titanic_correlations.isna().sum()
```

- 정렬하기 'Correlation'컬럼으로 정렬  
'Correlation' 으로 정렬하면 상관분석이 높은 것부터 볼 수 있다
```py
titanic_correlations.sort_values(by='Correlation', ascending=False)
# 위의 결과는 타이타닉 영화와 상관관계는 높은 영화들만 보여주지만
# 카운트를 한 사람이 너무 적다 10명 내외

# 카운트를 80명 이상으로 지정해서 다시 저장
titanic_correlations_above80 = titanic_correlations.loc [ titanic_correlations['count'] >= 80, ]
```
___
## 특정 컬럼명 찾기  
userid_movieTitle_matrix 는 컬럼명으로 각 영화 타이틀로 되어 있어서 영화명을 찾을려면 어렵다. 그래서 기존의 title이 들어간 데이터프레임으로 찾아볼 수 있음. (물론csv파일에서 검색한다면..;;;) 

- 시리즈 데이터를 to_frame()
`문자열.str.contains()를 활용하면 좋지만 시리즈로 나왔을 때는 원할한 contains()를 사용이 안됨, 그래서 to_frame()을 이용
```py
# lower() 소문자로 바꿔서 검색이 잘 되게
my_title_df = movie_titles_df['title'].str.lower().to_frame()

# 이제 contains()로 검색 가능
my_title_df['title'].str.contains('star wars')

# 데이터 가져오기
my_title_df.loc [ my_title_df['title'].str.contains('star wars'), ]
```

한줄로 길게 한번에 표현  

`movie_titles_df.loc [ movie_titles_df['title'].str.lower().to_frame()['title'].str.contains('star wars'), ]`


















