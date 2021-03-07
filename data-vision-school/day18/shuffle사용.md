shuffle 모듈  
random 사용안해도 shuffle 모듈로 할 수 있다

```py
from sklearn.utils import shuffle
```


```py
X_train, y_train = shuffle(X_train, y_train)
# X_train의 정답이 Y_train이 정답인데 X_train만 섞어버리면 답이 없다
# shuffle은 X,y 모두 믹스해준다
```

위의 방식으로 섞어주면 
X_train과 y_train에 들어있는 것을 같은 순서로 섞어줌  
하는 이유는 X_train이 무조건 섞여버리면 y_train의 정답지를 확인할 수 없기 때문
셔플된 후에는 
간단하게 y_train[0] 와 x_train[0]을 비교해보면 되는데 x_train[0]이 행렬이면 `plt.imshow(X_train[0])`로 확인해본다

