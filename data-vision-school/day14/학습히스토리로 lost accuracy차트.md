# 2개의 분류 학습
## 학습
```py 
epoch_history = model.fit(
    train_generator, 
    epochs=15, 
    steps_per_epoch=8, 
    validation_steps=50,
    # image generator로 생성된 것임, imgage generator 코드 참고할 것
    validation_data=validation_generator,
    verbose=1
)
```
## 리턴값 저장 (fit()으로 학습)
```py
train_acc = epoch_history.history['accuracy']
val_acc = epoch_history.history['val_accuracy']

train_loss = epoch_history.history['loss']
val_loss = epoch_history.history['val_loss']
```

정확도는 계속 높아지고 오차는 계속 떨어진다  
학습을 시키면 시킬 수록 정확도, 오차는 좋아지지만,   
이것은 오버피팅이 될 수 있다.  

그래서 val_accuracy, val_loss에 주목해서 본다  

```py
# 차트에 그릴 X를 표시하기 위해 
X = range( len(train_acc))

# train_정확도와 validation_정확도 비교
plt.plot( X, train_acc)
plt.plot( X, val_acc)
plt.legend( ['train', 'validation'])
plt.show()

# train의 오차와 validation의 손실 비교
plt.plot( X, train_loss)
plt.plot( X, val_loss)
plt.legend( ['train', 'val'])
plt.show()
```


