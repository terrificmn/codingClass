# 피클데이터 열기
```py
import pickle
```
파일열기
```py
with open('train.p', mode = 'rb', ) as training_data:  # training_data 로 읽어서 
  train = pickle.load(training_data) # pickle로 로드

```