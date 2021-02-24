# callbacks
callbacks는 내가 실행하는 것이 아니고 어떤 조건이 되었을 때 callbacks 함수가 작동을 하면서 내가 만든 사용자함수를 호출 (실행)시켜주는 것    
(내가 사용한 적은 없음, 만들기만 했지만, 텐서플로우에서 자동으로 실행하는 것: callbacks)  


## 클래스 만들기
클래스 내가 맘대로 만들고 Callback 클래스를 상속 받음  
그리고 함수도 지정되어 있음  
함수 안에서 조건은 마음대로 짤 수 있음, logs 변수로 넘어온 값을 사용할 수 있음  
`logs.get('accuracy')` 또는  `logs.get('loss)`  

```py
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        i = 0.995
        if (logs.get('accuracy') > i ):
           print("\n정확도 {}가 되어서 학습을 종료합니다".format(i*100))  
           self.model.stop_training = True
        # logs.get('loss')로 하게 되면 lost 결과로 계산할 수 있음
#객체 생성
myCallback = myCallback()
```

## 사용
모델을 만들고 fit() 메소드로 학습을 시킬때   
`callbacks=[myCallback ]` 으로 args 추가시켜준다
```py
model_history = model.fit(X_train, y_train, epochs=10, batch_size=100, callbacks=[myCallback ], verbose=1) 

```

