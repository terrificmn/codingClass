# ANN: Artificial Neural Network

## import
```py
import numpy as np
import datetime
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
```
## 준비 / normalization
```py
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

X_train = X_train / 255.0
X_test = X_test / 255.0

```
3차원 2차원으로 변환 시키기  
`X_train.shape` 를 해보면  
>(60000, 28, 28)
로 나오는데 28X28사이즈가 60000장이 있다고 생각하면 됨, 3차원 배열임  
`type(X_train)`를 해보면 numpy.ndarray 를 알 수 있음  
그러므로 reshape()메소드로 바꿔주면 됨
```py
X_train = X_train.reshape(-1, 28 * 28)
# 또는 배열갯수를 알 경우는 (60000, 28*28)도 무방, 하지만 -1 굿
X_test = X_test.reshape(-1, 28 * 28)
```
`X_train.shape`을 해보면 (60000, 784)로 바뀐 것을 알 수 있음


## 모델링
이제 `input_shape` 또는 `input_dim` 으로 784의 데이터를 input_layer 입력되게 할 수 있음  
```py
model = Sequential()
model.add ( Dense( units=128, activation='relu', input_shape = (784, )) )

```

## Dropout layer 추가
오버 피팅을 막아주는 기능    
특정 w선을 잘라? drop out 해서 노드를 막아줌  

```py
model.add( Dropout(rate=(0.2) ) )
```

## output layer 설정 및 complie
```py
model.add( Dense(units=10, activation='softmax' ) )

model.compile( optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# 3개 이상의 분류는 sparse_categorical_crossentropy
```

## 학습 및 evaluate
evaluate()메소드는 2개를 리턴 loss와 accuracy
```py
model.fit(X_train, y_train, epochs=30)

test_loss, test_accuracy = model.evaluate(X_test, y_test)
```



#저장하는 것 만들기
#저장하는 것 만들기
#저장하는 것 만들기
#저장하는 것 만들기
#저장하는 것 만들기
#저장하는 것 만들기
