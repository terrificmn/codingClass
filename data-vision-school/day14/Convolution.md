CNN Convolutional neural network
ANN Artificial neural network

- Convolutional Layer   
피쳐, 필터, 커널이라고 함  
이미지가 Kernels (2차원 행렬) 처음에는 랜덤으로 셋팅  
(몇행 몇열로 할지는 사람이 정한) - 하이퍼 파라미터  
커널을 몇개로 할지도 하이퍼 파라미터   
Convolutional Layer에서 사진을 필터링을 한다 (연산)

- pooling layer (downsampling)  
2차원을 1차원으로 flatten하게 해서 

[참고 사이트](setosa.io/ev/image-kernels/)


커널은 (피쳐 디텍터 라고도 함)

|커|널| |
|--|--|--|
|0 |-1 |0|
|-1| 5 |-1|
|0 |-1| 0|


원본의 이미지의 숫자 

|원 |본 | |
|--|--|--|
|206 |205 | 247|
|244|161| 137|
|192| 154| 75|

여기에서 커널과 원본의 이미지의 숫자 두개를 곱함  
(0 * 206) + (-1 * 205) + (0 + 247) +  
(-1 * 244) + (5 * 161) + (-1 * 137) +  
(0 * 192) + (-1 * 154) + (0 * 75)   
9개를 각각 곱하고 더한다 --> 312 하나의 값이 나옴  

그리고 오른쪽으로 한칸 이동.   
3 X 3 행렬로 각각 9개를 커널과 원본과 매칭되는 것들끼리 곱하고 다 더함  
그러면 숫자 하나 나옴  
(-가 나오면 0으로 처리, 255 이상이면 255로 처리)  

이런식으로 처리가 된다고 함  

커널 갯수만큼 이미지가 변환되서 나온다  
여기에서 액티베이션 함수를 relu를 적용  
convolution을 마치면 activation함수까지 마쳐진다

원본이미지가 28x28에서 컨볼루션을 거치면 26x26 사이즈로 바뀜 (위,아래,옆 하나씩 빠짐)

(Pooling Layer 전에 이미지가 나옴)  

[참고 사이트](https://poloclub.github.io/cnn-explainer/)

Pooling은 2행 X 2열로 한다고 하면 그대로 2행2열씩 이동
(필터링/커널과 다름)

Dropout 을 통해 Overfitting을 줄인다  
(학습시에는 오차율이 거의 없어서 완벽할정도인데, 신규 데이터가 들어가면 오차가 심해지는 것)


## 모듈 임포트
```py
import tensorflow as tf
import tensorflow.keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Flatten
```

## 준비 
```py
mnist = tf.keras.datasets.fashion_mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

## Normalization
```py
# 3차원 일때 
# 28 x 28짜리 사진이 60,000장이 쭉~ 있다고 생각하면 됨
X_train = X_train.reshape(60000, 28, 28, 1)
X_test = X_test.reshape(10000 , 28, 28, 1)

X_train = X_train / 255.0
X_test = X_test / 255.0
```

## Conv2D, MaxPooling2D
```py
from keras.layers import Conv2D, MaxPooling2D
```

## 모델링
```py
model = Sequential()

#filters의 갯수는 필터(커널의) 갯수, kernel_size로 만든 것의 갯수, 아래코드는 3x3가 64개라는 의미
#kernel_size= ( , ) 커널의 크기. 아래에서는 3행3열로 만듬
# Conv2D === Convolutional Layer 설정도 하이퍼 파라미터로 밑에 MaxPooling2D와 쌍으로 사용되었는데
# 이것도 하이퍼 파라미터이기 때문에 꼭 쌍으로 안하고 하나씩만 해도 된다
# 정답이 없다
model.add ( Conv2D( filters = 64, kernel_size=(3, 3), activation='relu', input_shape= (28, 28, 1) ) )

# MaxPooling2D - 사진을 줄임 특징은 그대로 가지되, 컴퓨팅 효율을 높힌다
# 얼마나 줄일지 정함 (2, 2) --> 2행2열로 줄임
# 위의 Conv2D로 나온 결과물 커널 수 만큼 64개가 나오게 되는데 
# 그 다음에 MaxPooling2D는 2행2열로 셋팅했다면 그 커널 1개를 2행2열로 훓는다
# 2행2열로만 이동해서 그 영역에서 가장 큰 수만 뽑게 됨
# (풀링에는 숫자가 들어가지고 않고 거기에서 큰 수만 뽑음)
model.add( MaxPooling2D( 2, 2 ) )

# 위에서 MaxPooling2D 처리가 된 것 (원본에서 작아짐) 에서 
# Conv2D를 실행다시 64개의 (3x3)으로 필터링을 진행
# filters=, kernel_size= (,) 생략가능 (순서대로)
model.add( Conv2D(64, (3, 3), activation='relu'))

# 이거를 또 반복
model.add( MaxPooling2D( 2, 2) )

# 마지막 풀링 된 것을 Flatten() 시킴
# 숫자하나씩 일렬로 만듬 이것들 input으로 들어가짐
model.add( Flatten())

# units=생략가능  (처음에 써야함)
# 신경망으로 노드 128개 만들어 짐
model.add( Dense(128, activation='relu') )
model.add( Dense(10, activation='softmax'))

```
## 위의 코드를 한줄로 만들기
처음에 Sequential 호출 후 ( ) 안에 리스트 형태로 쭉쭉 넣어준다
```py
c_d_model = Sequential( [
  Conv2D(filters= 16, kernel_size=(3,3), activation='relu', input_shape=(150, 105, 1) ),
  MaxPooling2D(2, 2),
  Flatten(),
  Dense(units=512, activation='relu'),
  Dense(units=1, activation='sigmoid') # 1개 분류할 때 (0/1)
  ]
)
```


## 모델 요약
```py
model.summary()
```

## 컴파일 및 학습
```py
model.compile( optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# validation_split=0.25 ---> X_train에 있는 데이터를 각 에포크를 할 때 75%만 학습을 하고 25%로 검증을 해보라는 것
model_hist = model.fit(X_train, y_train, epochs=6, batch_size=100, validation_split=0.25, callbacks=[ myCallback ])
```

## overfitting확인
차트로 그리기


```py
plt.plot(model_hist.history['accuracy'], color = 'b')
plt.plot(model_hist.history['val_accuracy'], color ='r')
plt.title('model accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['Train', 'Val']) #Val은 training셋에서 자체 25%테스트 한 것
plt.show()


```