# 텐서플로우 기초

- 불러오기
```py
import tensorflow as tf
import numpy as np
from tensorflow import keras
```

## Define 뉴런 네트워크 모델링 
- 정의
input layer - hidden layer - output layer로 (일반적으로) 구성되는 것을 `Sequential` 이라고 함   
`Dense`는 한 레이어 구성을 말하고,   
`units=1` 은 뉴런이 하나,  그 안의 input_shape = [1]는 일차원으로 되어 있음

```py
tf.keras.Sequential( [keras.layers.Dense(units=1, input_shape = [1])] )
```

- 컴파일 2개의 함수 필요  

loss 와 optimizer.
> y = (2 * x) -1 을 예측하는 딥러닝을 만든다고 가정했을 시,   
학습을 통해 예측한 값과, 실제의 값 두개를 측정하는 LOSS function 을 설정해야 한다.  
위의 로스(오차)를 최소화 하기 위해서 OPTIMIZER function 을 설정한다.  
로스펑션으로 'MEAN SQUARED ERROR'를 사용하고, 옵티마이저로 'STOCHASTIC GRADIENT DESCENT' 를 사용한다.  

```py
# optimizer='sgd'는 STOCHASTIC GRADIENT DESCENT
model.compile(optimizer='sgd', loss='mean_squared_error')
```

## numpy xs와 ys만들기  
y = 2x-1 이 식에 따라, x의 데이터 6개와, 그에 해당하는 y의 데이터 6개를 준비한다. 머신러닝은 데이터로부터 학습하는 것이기 때문이다. 이 데이터로부터 우리는 위의 식을 컴퓨터가 찾아내도록 하는것이다. 

- xs 만들기
```py
# 데이터가 됨
xs = np.array( [-1.0, 0.0, 1.0, 2.0, 3.0, 4.0] , dtype=float )
```

- ys 만들기
```py
# 정답지가 된다
ys = np.array( [ -3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float )
```

## Training
- 학습 fit
`epoches=`파라미터는 100으로 설정한다면 위의 xs 데이터를 100번 반복하겠다. w값 (가중치 weight) 은 계속 바뀌므로 오차가 줄어든다
```py
model.fit(xs, ys, epochs=100)
```

- 예측 .predict()
```py
model.predict( [10.0])
# 처음에는 15.79나옴
# y = 2x - 1  ==> x가 10이면, y는 19 근처로 나와야 성능좋은 인공지능

# epochs=500으로 다시 한 다음에 다시 학습시키면
# 19에 가까운 수가 나옴. 18.98
```



