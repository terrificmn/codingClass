# Supervised Learning

## Feature Scaling (공통)
- 패키지/ 모듈 불러오기
```py
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
# X를 StandardSacler로 변환 
X = sc.fit_transform(X)
```

- 트레이셋, 테스트셋 나누기
```py
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state= 0)
```
___
## KNN 알고리즘
- KNeighborsClassifier `유클리디안 거리 (Euclidean Distance)` 공식으로 다차원 좌표에서 두 점 사이의 거리를 재는 방법으로 그룹화하는 방식
- 패키지/모듈 불러오기
```py
from sklearn.neighbors import KNeighborsClassifier
```
- 학습
```py
# 생성
classifier = KNeighborsClassifier( n_neighbors= 5, metric= 'minkowski' )

classifier.fit(X_train, y_train)
# 예측
y_pred = classifier.predict(X_test)
```
___
## Logistic Regression
- 모듈 불러오기
```py
from sklearn.linear_model import LogisticRegression
```
- 학습
```py
# random_state를 줄 수 있음
classifier = LogisticRegression( random_state = 0)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```

## GridSearchCV (Support Vector Machine)
GridSearchCV를 이용해서 하이퍼 파라미터를 지정해서 더 좋은 결과를 예측할 수 있게 할 수 있는데 가장 최적값을 리턴해 준다
- 그리드 서치 패키지 모듈 불러오기
```py
from sklearn.model_selection import GridSearchCV
```
- 하이퍼 파라미터 지정해주기. SVM의 rbf(가우시안)의 하이퍼 파라미터를 지정해 줄 수 있음 

```py
# 먼저 딕셔너리 형태로 만들어 줘야함
param = {
    'kernel': ['rbf'],
    'gamma': [0.001, 0.01, 0.1, 1, 10],
    'C': [0.1, 1, 10, 50, 100]
}
```
- 인스턴스 생성
```py
grid= GridSearchCV( SVC(), param, refit=True, verbose =4 )
#학습
grid.fit(X_train, y_train)

```
- 가장 좋은 조합 보기
```py
# 쓰임새는 거의 비슷
grid.best_params_
grid.best_score_
grid.best_estimator_
```

___
## Support Vector Machine

사과에서 가장 동떨어진 (오렌지 같은 헛갈리는 놈) 하나
오렌지에서 가장 동떨어진 (사과 같이 헛갈리는 놈) 하나
하나씩을 support vectors라고 한다
그 둘의 수직거리를 찾아서 
최대 마진을 구해서 분류하는 방식
linear 방식이 되게 됨

원으로 분류할 수 있는 문제 (직선으로 분류할 수 없을 때)
그런 방식을 Non-linear 라고 하는데
이런 방식은 딥 러닝으로 푼다고 함


support vector machine 으로도 똑똑한 사람들이 만들어 낸 방식이 2개 있음
하나는 2차원에 1차원으로 해서 다시 2차원으로 해서 직선을 그리는 방식
두번째는 3차원으로 공간을 분리해서 하는 가우시안 커널 방식

- 모듈 불러오기
```py
from sklearn.svm import SVC
```
- linear모델링
```py
# kernel=파라미터를 'linear' 방식으로 
classifier = SVC(kernel='linear', random_state = 0)
#학습/예측
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```
- 가우시안 모델링 rbf (꼬깔콘?)
```py
# kernel=파라미터를 'rbf' 가우시안 방식으로
classifier = SVC(kernel='rbf', random_state=0)
#학습
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```


## Decision Tree
tree 방식으로 분류 
- 모듈
```py
from sklearn.tree import DecisionTreeClassifier
```
- 학습
```py
classifier = DecisionTreeClassifier(random_state = 0)

classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
```

## 정확도 확인 counfusion_matrix
- 모듈 불러오기
```py
from sklearn.metrics import confusion_matrix
```
- 실행
```py
cm = confusion_matrix(y_test, cf_y_pred)
# 결과 예:
# array([[88, 19],
#        [14, 33]], dtype=int64)
# 정확도 공식
(88 + 35) / cm.sum()

# 위의 결과의 정답은
# 1번째 열 0, 1 --> 여기 답은 0, 88은 0인걸 맞춘 것
# 2번째 열 0, 1 --> 여기 답은 1, 35은 1을 맞춘 것
```
- 정밀도 계산 `35 / (19 + 35)` 
- 적중률 계산 `35 / (14 + 35)` 위의 예를 참고
