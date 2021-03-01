## 콜백함수
``` py
class MyCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        i = 0.999
        if (logs.get('accuracy') > i ):
           print("\n정확도 {}가 되어서 학습을 종료합니다".format(i*100))  
           self.model.stop_training = True
        # logs.get('loss')로 하게 되면 lost 결과로 계산할 수 있음
  #객체 생성
myCallback = MyCallback()
```

## 임포트
```py
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Conv2D, MaxPooling2D
```

## 모델링

```py
model = Sequential()
model.add (Conv2D (64, (3, 3), activation='relu', input_shape= (150, 150, 3) ))
model.add (MaxPooling2D(2, 2) )
model.add (Conv2D (32, (3, 3), activation='relu')) 
model.add (MaxPooling2D(2, 2) )
model.add (Conv2D (32, (3, 3), activation='relu')) 
model.add (MaxPooling2D(2, 2) )
model.add (Flatten() )
model.add (Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```

## 옵티마이져 RMSprop 사용
먼저 불러오기  
```py
from tensorflow.keras.optimizers import RMSprop
```

```py
# learning mate는 천천히 천천히 내려오게 된다 (gradient descent)
# RMSprop(lr= ) lr은 learning mate 0.03 크면  빨리 내려오고 , 적으면 천천히 내려온다
# 
#Regularization rate: overfitting을 막는 놈 참고로만 알고 있자 일단, 
model.compile(loss='binary_crossentropy', optimizer=RMSprop(lr=0.001), metrics=['accuracy'] )
```

## 이미지 제너레이터 사용
모듈  
```py
from tensorflow.keras.preprocessing.image import ImageDataGenerator
```

train과 test을 이미지를 2개를 하려면 train_generator를 다른 변수로 저장, 예: test_generator   
경로도 바꿔줘함.  
```py
train_datagen = ImageDataGenerator(rescale = 1 / 255.0)

train_generator = train_datagen.flow_from_directory(
        myPATH, # myPATH = '/tmp/happy-sad'
        
        # 타켓 사이즈는 여기서 바꿀 수 있음 : 여기서 바꾸면 input layer의 input_shape도 같게 해줘야 함
        target_size= (150, 150),
        class_mode='binary',
        #batch_size 생략 시 32로 됨
        batch_size = 8
)
```
위의 결과가 어떤 것이 0, 1 인지 알아볼 때는  
`test_generator.class_indices`

## 학습
```py
history = model.fit(train_generator, batch_size=40, epochs=30, verbose=1, callbacks=[ myCallback ], validation_data= test_generator)
```

## 사진 업로드에서 맞춰보는 코드
```py
uploaded = files.upload()

for fn in uploaded.keys():
  path = '/content/' + fn
  # 디렉토리안에 있는 하위디렉토리의 알파벳 순으로 순서가 됨 먼저가 (예: happy가 0, sad는 1)
  # 픽사베이등에서 받은 파일들을 처리할 때
  # 이미지를 load_img() 통해 target_size를 300x300 으로 바꿔준다 
  img = image.load_img(path, target_size=(150, 150) )
  # image를 ndarray로 
  x = image.img_to_array(img)

  # 원래 3차원 이지
  print(x.shape)

  # 행으로 한 차원을 늘림 (150, 150, 1) 이 되게 됨
  x = np.expand_dims(x, axis = 0)
  print(x.shape)

  images = np.vstack([x])
  classes = model.predict( images, batch_size = 10)

  print(classes)

  if classes[0] > 0.5 :
    print(fn + " is so sad")
  else:
    print(fn + " is so happy")

```
