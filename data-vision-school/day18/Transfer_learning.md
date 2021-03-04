# 이미지넷 Transfer Learning
MobileNetV2 활용
모바일이나, 임베디드에서도 실시간을 작동할 수 있게 모델이 경량화 되면서도, 정확도 또한 많이 떨어지지 않게하여, 속도와 정확도 사이의 트레이드 오프 문제를 어느정도 해결한 네트워크 입니다.

## Base 모델 가져오기
```py
base_model = tf.keras.applications.MobileNetV2(input_shape=IMG_SHAPE, include_top=False, weights="imagenet")
```
여기에서 `include_top=False`가 중요:  
이미 학습이 된 Base모델만 가져와서 뒷부분 즉, top 부분이라고 불리는 부분  
또는, Head모델을 가져오지 않겠다는 의미  
여기서 우리는 Head모델만 직접 구현해준다  
`weights="imagenet"` --> 이미지넷에서 썼던 weights를 가져옴

`tarinable` 속성을 **False**로 저장해서 학습이 안되게 함
```py
base_model.trainable = False
```

## Head 모델링
```py
base_model.ouput

#결과 <KerasTensor: shape=(None, 4, 4, 1280) dtype=float32 (created by layer 'out_relu')>
```
이 아웃풋으로 나오는 것을 Head 모델링에 각 layer 뒤에 넣어준다

```py
#변수로 저장해서 활용
head_model = base_model.output
```

```py
head_model = tf.keras.layers.GlobalAveragePooling2D()(head_model)
head_model = tf.keras.layers.Dense(units=1, activation='sigmoid')(head_model)

#개/고양이 같은 2개의 분류는 sigmoid를 액티베이션함수로 사용
```

## Define Model
**중요**  
최종 모델링을 마무리  
`inputs=`는 BASE모델  
`outputs=`는 내가 만든 HEAD모델

```py
model = tf.keras.models.Model(inputs=base_model.input, outputs=head_model )

# 만든 모델 요약
model.summary()
```

## 컴파일
```py
model.compile(optimizer=tf.keras.optimizers.RMSprop(lr=0.0001), loss="binary_crossentropy", metrics=["accuracy"])

# 2개 분류 문제는 loss 함수는 binary_crossentropy
```


## 이미지 제레레이터

여기부터 할.. 37_부분
