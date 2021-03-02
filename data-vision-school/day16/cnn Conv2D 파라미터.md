## 모델링
```py
model = Sequential()
model.add ( Conv2D( filters=32, kernel_size=(3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)) )
# 5행5열을 컨볼루션을 하면 커널크기에 따라 3행3열로 줄어드는데
# 5행5열 크기를 유지시키고 싶을 때는 (크기는 줄어들지만 )
# padding=same으로 주고, 줄어든공간에 0을 넣어주고 
# 원래 크기는 유지함 (padding 값으로 0이 들어가게 됨)
```

```py
model.add ( Conv2D( filters=32, kernel_size=(3, 3), padding='same', activation='relu') )
model.add ( MaxPooling2D( 2, 2) ) 

```

```py
model.add ( MaxPooling2D( pool_size=(2 , 2), strides=2, padding='valid' ) )
# maxpool 의 strides는 원본이미지를 커널로 훑을 때(컨볼루션 할때) 기본 1칸씩 이동하는데
# 몇칸씩 띄어서 이동할지를 지정하는것이 strides
# 사실 pool_size가 2x2 이므로 2칸씩 이동하므로 strides=2 맞다 (그래서 여기에서는 생략도 가능)
model.add ( Conv2D( filters=64, kernel_size=(3, 3), padding='same', activation='relu') )
model.add ( Conv2D( filters=64, kernel_size=(3, 3), padding='same', activation='relu') )
model.add ( MaxPooling2D( pool_size=(2 , 2), strides=2, padding='valid' ) ) 

```

dropout , flatten
```py
model.add ( Dropout(0.4 ) )
model.add( Flatten() )
```

ann
```py
model.add( Dense(units= 1024, activation='relu' ) )

model.add (Dense( units=10, activation='softmax') )

```
3개 이상의 분류시 액티베이션 함수는 softmax 사용

컴파일 
```py
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr = 0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
```

학습
```py
history = model.fit(X_train, y_train, batch_size=32, epochs=10, verbose=1, validation_split=0.25 )
```

학습할 때  validation_data 와 validation_split

데이터가 있어야 함
validation_data=(X_test, y_test)  --> X_train, y_train으로 학습하는 중에 
X_test, y_test 값으로 검증을 해본다. 이때 y_test 값을 알려줘서 학습하는 것은 아니다. 검증만함

만약 테스트 데이터가 없다면 
자체 train데이터의 일부분을 검증하게 하면서 할 수 있다, validation_split



## 예측
```py
#model 을 evaluate 한다.
result = model.evaluate(X_test, y_test)

y_pred = model.predict( X_test)
```




y_pred 결과 값은 10개의 분류를 했기때문에
즉, 모델링에서 output layer를 10개로 했기 때문에 
10개중에서 가장 큰 값이 가장 확률이 높음 (softmax는 전체를 다 더하면 1이 됨) 
그래서 argmax로 높은 수를 찾아줘야한다

## 분류의 문제 시에는 argmax
```py
y_pred = y_pred.argmax(axis=1)
```
컨퓨전 매트릭스를 하려면 차원을 맞춰저야함

## confusion matrix
```py
from sklearn.metrics import confusion_matrix, accuracy_score
```

```py
y_pred = y_pred.argmax(axis=1).reshape(-1, 1)

cm = confusion_matrix(y_test, y_pred)
# 정확도를 계산해 본다.
accuracy_score(y_test, y_pred)
```

## 학습 결과 보기 histroy
마지막 요소
```py
history.history['accuracy'][-1]
history.history['loss'][-1]
```


