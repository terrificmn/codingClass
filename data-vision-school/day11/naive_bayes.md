# Naive Bayes 로 스팸 학습

## 구두점 puncuation
- string 불러오기
```python
import string
string.punctuation
```

## 불용어 제어
- nltk (stopwords) 불러오기 
```python
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stopList = stopwords.words('english')
```

## 사용자 함수로 구두점과 불용어 제거하기
- 한줄 표현식
```python
def msg_cleaning(strings):
    punc_removed_list = [ char for char in strings if char not in string.punctuation ]
    punc_removed_joined = ''.join(punc_removed_list)

    #중간에 split()으로 공백으로 분리해서 리스트로 만듬
    # lower()을 해서 소문자로 만들어서 비교
    punc_removed_join_clean = [ word for word in punc_removed_joined.split() if word.lower() not in stopList ]
    
    return punc_removed_join_clean
```

## 벡터라이징 하기 CountVectorizer
- 불러오기 CountVectorizer
```python
from sklearn.feature_extraction.text import CountVectorizer
```
- analyzer=  파라미터 사용 (벡터라이징 전에 먼저 사용됨)

```python
# 객체 생성 analyzer= 로 위에서 만든 함수를 지정
vectorizer = CountVectorizer( analyzer = msg_cleaning)
```

- 문자 벡터라이징
```python
# 추가로 vectorizer를 사용할 때는 transform()만 사용
# 처음 적용은 fit_transform()메서드 적용
# 문자열인 text컬럼을 적용시키면서 벡터라이징
X = vectorizer.fit_transform(df.text)
```
- 추가로 할 수 있는 것들
`X.toarray()` --> ndarray 로 보여줌
`vectorizer.get_feature_name()`  --> 

## train / test 만들기
- 불러오기 train_test_split
```python
from sklearn.model_selection import train_test_split
```

- 변수 저장
```python
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.2, random_state =123)
```

## Naive_bayes 모델링 학습 / MultinomialNB
- 불어오기
```python
from sklearn.naive_bayes import MultinomialNB
```

- 학습 / 예측 시키기
```python
# 객체 생성
nb_classifier = MultinomialNB()
# .fit(X_train, y_train) 훈련
nb_classifier.fit(X_train, y_train)
# .predict(X_test) 예측
y_pred_nb = nb_classifier.predict(X_test)
```

## 컴퓨전 매트릭스 confusion_matrix
- 불러오기
```py
from sklearn.metrics import confusion_matrix
```
- 정확도 계산
```py
#생성
cm = confusion_matrix(y_test, y_pred_nb)
# 결과가 아래라고 가정하면
# array([[868,   8],
#        [  3, 267]])

# 정확도 계산
(868+267) / cm.sum()
```

## 새로운 텍스트 추가 예측
- 추가 데이터

`test1 = [ "give me money" ]` 이런 데이터가 있다고 하면
문자열을 [ ]리스트로 묶고 벡터라이징을 똑같이 해줘야한다
(여기에서 구두점과 불용어 제거가 됨)

- vectorize
```py
# 여기에서는 fit_transform() 아니다!
# 전에 변경된 것을 토대로 다시 transform() 임에 유의
test1_countvectorizer = vectorizer.transform(test1)
```

- Naive_bayes 학습
```py
# 기존 nb_classifier 인공지능한테 예측해달라고 하면 됨
test1_predict = nb_classifier.predict(test1_countvectorizer)
```

