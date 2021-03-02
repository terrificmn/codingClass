# 러닝 커브 차트과 오버피팅
train 데이터로 학습을 시킬 때 epoch 횟수를 많이 줘서  
계속 반복 학습 하게 되면 정확도는 높아지고, 오차는 낮아지게 된다.  
이렇게 되면 엄청 똑똑한 인공지능이 만들어지는 거 같지만,   
사실은 학습 데이터에 관련해서는 정확도가 높지만   
다른 새로운 데이터 예측에는 잘 맞추지 못하는 되는데 이를 Overfitting 이라고 한다.

이를 방지하기 위해서는 
- 학습 후 결과값을 리턴받은 것을 이용한다
- history['accuracy']와 history['val_accuracy'] 속성 이용
- history['loss']와 history['val_loss'] 값을 이용
- matplot 라이브러리로 차트를 그려서 적정 epoch 값을 찾아본다


## 함수로 만들기

먼저 모듈 불러오기
```py
import matplotlib.pyplot as plt
```

함수로 만들기
```py
def learning_curve(history, epoch):
  #정확도 차트 (accuracy)
  # x축을 epoch_range로 셋팅
  epoch_range = np.arange(1, epoch +1)

  plt.figure(figsize=(16,8))
  plt.subplot(1, 2, 1)
  
  plt.plot(epoch_range, history.history['accuracy'])
  plt.plot(epoch_range, history.history['val_accuracy'])
  plt.title('Model Accuracy')
  plt.xlabel('Epoch')
  plt.ylabel('Accuraycy')
  plt.legend([ 'Train', 'Val' ] )
  # plt.show() // 차트를 따로 그리려면 위의 subplot()을 제거
```

loss 차트  
같은 함수에 포함시켜야 함
```py
  # 오차 차트 (loss) 
  plt.subplot(1, 2, 2) 

  plt.plot(epoch_range, history.history['loss'])
  plt.plot(epoch_range, history.history['val_loss'])
  plt.title('Model loss')
  plt.xlabel('Epoch')
  plt.ylabel('loss')
  plt.legend([ 'Train', 'Val' ] )
  plt.show()
```

함수 호출
```py
# 1번째는 model의 fit의 history값 
# 2번째는 epoch 횟수
learning_curve(history, 10)
```
