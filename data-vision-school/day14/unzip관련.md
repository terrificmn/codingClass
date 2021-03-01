## unzip하기
리눅스 명령어로 처리하려면  
unzip 파일경로/파일명.zip -d /압축풀경로  
```
#예
!unzip /tmp/validation-horse-or-human.zip -d /tmp/vali-horse-human
```

참고 지우기, rm은 더블체크 후 사용
```
!rm -Rf /tmp/cats-v-dogs
```

## 파이썬 모듈 사용하기
불러오기
```py
import os
import zipfile
```

테스트 셋과 트레이닝 셋으로 나누기
```py
# 테스트셋
local_zip = '/tmp/horse-or-human.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp/horse-or-human')
zip_ref.close()

# 트레이닝 셋
validation_local_zip = '/tmp/validation-horse-or-human.zip'
zip_ref = zipfile.ZipFile(validation_local_zip, 'r')
zip_ref.extractall('/tmp/validation-horse-or-human')
zip_ref.close()
```

## os 모듈 이용
파이썬에 사용가능한 경로로 만들기    path.join()
```py
validation_train_horse_dir = os.path.join('/tmp/validation-horse-or-human/horses')
```

특정경로 파일 이름을 리스트로 가져오기 listdir()
```py
os.listdir(train_horse_dir)
```

디렉토리 만들기  
```py
try:
  os.mkdir('/tmp/cats-v-dogs')
  os.mkdir('/tmp/cats-v-dogs/training')
  os.mkdir('/tmp/cats-v-dogs/testing')
  os.mkdir('/tmp/cats-v-dogs/training/cats')
  os.mkdir('/tmp/cats-v-dogs/training/dogs')
  os.mkdir('/tmp/cats-v-dogs/testing/cats')
  os.mkdir('/tmp/cats-v-dogs/testing/dogs')
except OSError:
    pass
```







