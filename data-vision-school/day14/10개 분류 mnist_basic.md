# 10개 분류 딥러닝

## 준비 
- 모듈
```py
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
```
- mnist 데이터셋 준비
```py
mnist = tf.keras.datasets.fashion_mnist
# train set, test set을 받아오기
(training_images, training_labels), (test_images, test_labels) = mnist.load_data() 
# 괄호()로 2개씩 가져오기
# labels는 y가 된다
# 즉 === X_train, y_train, X_test, y_test
```

- 받아온 training_images 확인  
`training_images.shape` 를 해보면 (60000, 28, 28) 결과로 나오는데 3차원으로 되어 있음  
`training_labels.shape` 를 해보면 (60000, ) 벡터  
받아온 데이터는 숫자로 되어있고  

|색깔| 숫자|
|--|--|
|검정색 | 0 |
|흰색| 255 |  

참고로 색은 R G B

|색깔| 숫자|
|--|--|
|Red	|(255, 0, 0)|
|Green	|(0, 255, 0)|
|Blue	|(0, 0, 255)|

## Featur Scaling - Normalizing
최대값인 255로 나누어서 최대값이 1이 되게 하는 것  
실수 처리를 하려면 소숫점으로 나눠준다. 255.0  

```py
training_images = training_images / 255.0 
```
또는 실수로 바꾸기
```py
test_images.astype(float)
test_images = test_images / 255
```

## 모델링
모델링 순서는 모듈 import -> Sequential 모델 -> Flatten -> Dense추가 -> complie -> fit

### import 
케라스 모델과 레이어 불러오기
```py
import tensorflow.keras
from keras.models import Sequential
from keras.layers import Dense, Flatten
```
### Sequential
```py
# 객체 생성 (변수 저장)
model = Sequential()
```

### Faltten
2차원의 사진 데이터(숫자)를 평평하게 해준다는 의미로 일자로 하나로 붙여서  
input layer에서 입력이 될 수 있게 해줌
```py
model.add( Flatten() )
```
만약 Sequential를 import 안했다면   
`model.add( tf.keras.layers.Flatten() )` 이런식으로 다 써줘도 됨

이미지 행렬 예:    
0 1 2 0 3 1 0  
2 3 5 1 3 1 0  
9 1 0 2 3 9 0  
2차원 이미지 를 행으로 쭈욱 평평하게 연결해주는 것  
(아래처럼) 하나의 행으로 만들어 줌  
0 1 2 0 3 1 0 2 3 5 1 3 1 0 9 1 0 2 3 9 0  

### Dense
이제 레이어를 추가  
`unists=`*파라미터*는 입력노드의 갯수  

```py
model.add( Dense(units= 128, activation=tf.nn.relu ))
```
### 최종 output layer 설정
activation함수는 **softmax**로 설정한다  
- output layer가 10개
- 3개 이상의 분류는 해당 분류수 만큼 `units=` args를 같게 지정해준다
- 이번프로젝트의 분류 10개임
- 액티베이션 함수로 소프트맥스를 사용  
- 소프트맥스 0 과 1사이의 데이터로 나오게 되는데 결과의 총 합이 1이 되게 만드는 액티베이션 함수, 우리는 그 결과중에 가장 높은 수를 찾으면 됨

그 이유는 학습의 정답지가 되는 training_labels (혹은 y_train)에는 0~9까지 10개의 목록이 있는데 이것로 어떤 이미지가 어떤것인지 알 수 있음

Each training and test example is assigned to one of the following labels:

| Label | Description |
|:--:|:--|
|0| T-shirt/top|
|1| Trouser|
|2| Pullover|
|3| Dress|
|4| Coat|
|5| Sandal|
|6| Shirt|
|7|	Sneaker|
|8|	Bag|
|9| Ankle boot|


#### 액티베이션 함수 설명
각 레이어에는 activation=액티베이션 함수를 정하게 되어 있는데 그 중 
- relu  
**Relu** effectively means "If X>0 return X, else return 0" -- so what it does it it only passes values 0 or greater to the next layer in the network.

- softmax
**Softmax** 여러개의 값 중에서 가장 큰 값을 선택. [0.1, 0.1, 0.05, 0.1, 9.5, 0.1, 0.05, 0.05, 0.05], 여기서 가장 큰 값을 1로 만들고 나머지는 0으로 만들어준다. [0,0,0,0,1,0,0,0,0] 

### 컴파일
컴파일 메소드로 optimizer를 지정, loss함수도 지정  
```py
model.compile(optimizer=tf.optimizers.Adam(), loss = 'sparse_categorical_crossentropy', metrics= ['accuracy'] )
```

**중요** 3개 이상의 분류일 때는 `loss=`를 `sparse_categorical_crossentropy`로 하고  
training_labels를 원 핫 인코딩을 했을 경우에는 categorical_crossentropy 를 사용한다  
또 2개의 분류 문제는 `mean_squared_error`

### 학습 시키기 fit
fit전에 요약정보 보기 .summary() 메소드

```py

```

epochs= , batch_size 등 설정
```py
model.fit(training_images, training_labels, epochs=5, batch_size=20)
```

### 예측
```py
y_pred = model.predict(test_images)
# 3번 인덱스 확인
y_pred[3]
```
위의 결과는 아래처럼 나오는데   
>array([8.8223921e-08, 9.9999952e-01, 4.4609085e-09, 3.8448508e-07,
       3.8152045e-08, 7.9590855e-14, 4.4398401e-09, 1.6717402e-24,
       2.9675925e-11, 5.8565989e-17], dtype=float32)
여기에서 가장 큰 값이 정답일 확률이 높다라는   

결과 비교해보기
```py
y_pred[3].argmax()
# 결과 1
test_labels[3]
# 결과 1
# 예측이 맞음

# 실제 파일 보기
plt.imshow( test_images[3] )
plt.show
# 를 하면 Trouser 그림인 것을 알 수 있음
```

## 정답은 없다
epochs, batch_size, layer추가, units 노드갯수, activation 함수 등등  
여러가지를 바꾸고해면 학습이 더 좋아지기도 하고 
학습이 잘 되다가 오히려 오차가 커지고 정확도가 떨어지기도 하는 현상도 있음  (overfitting)
결론은 정답은 없고 많이 실험을 해봐야한다고 함

