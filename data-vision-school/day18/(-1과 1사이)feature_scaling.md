```py
X_train_gray = np.sum(X_train / 3, axis = 3, keepdims = True)
# X_train에는 
# r 0-255 행렬
# g 0-255 행렬
# b 0-255 행렬
# 이 각각 있는데 이를 각각 3으로 나눔 
# 만약 각 255가 있었다고 가정하면 3으로 나눠서 85로 바뀌게 되면 다시 sum을 하면 255가 되므로 
# 하나의 이미지로 됨 (행렬 하나로 바뀜)

# 또 여기에 keepdims 은 4차원인것을 4차원으로 유지하라는 파라미터
```

feature scaling
```py
# -1과 1사이로 만들어 주는 feature scaling 방법
(X_train - 128) / 128

# 가장 큰 값을 넣으면 255 --> 0.99가 됨
# 가장 작은 값은 넣으면 0 --> -1이 됨
```


X_train_gray_norm = (X_train_gray - 128) / 128
X_test_gray_norm = (X_test_gray - 128) / 128
X_val_gray_norm = (X_val_gray - 128) / 128