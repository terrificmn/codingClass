## 모듈
```py
from sklearn.metrics import confusion_matrix, accuracy_score
```

```py
cm = confusion_matrix(y_test_argmax, y_pred)
accuracy_score(y_test_argmax, y_pred)
```

주의할 점은 
컨퓨전 매트릭스는 y_test와 y_pred 를 서로 같은 차원으로 만들어 줘야하기 때문에
만약 여러개 분류의 문제였다면  
예측 `predict` 나온 값에서 `argmax()`를 사용해 준다

```py
y_pred = y_pred.argmax(axis=1)
```

마찬가지로 y_test 값도 여러개가 (7개로 분류가 되어 나머지는 0, 정답만 1이 되어 있는 경우)
에는 마찬가지로 `argmax`를 해준다.   
`axis`는 1로 컬럼 중에 가장 높은 값을 찾게 한다

## 히트맵

```py
import seaborn as sns
sns.heatmap(cm, annot=True, fmt='.0f', cmap= "RdPu")
plt.show()
```