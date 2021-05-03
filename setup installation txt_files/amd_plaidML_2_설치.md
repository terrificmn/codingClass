# plaidml 설치 후 트러블 슈팅 2

앱이 실행되면서 
Using TensorFlow backend.
라고 나오는데, Tensorflow가 나오면 안되는데..   

파이썬 코드안에 os를 import를 하고 아래 코드를 입력
```py
import os
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
```
실행을 할때 plaidml의 gpu로 되야하는데
cpu와 속도가 같다;; 뭔가 잘못됨

그래서 이번에는 
스트림릿을 끄고

vi ~/.keras/keras.json
을 수정해준다

vi 편집기로 열어서 backend키의 value부분을 "plaidml.keras.backend"로 바꿔준다
```
{
    "floatx": "float32",
    "epsilon": 1e-07,
    "backend": "plaidml.keras.backend",
    "image_data_format": "channels_last"
}
```
"tensorflow" --> "plaidml.keras.backend" 로 한 후 저장


다시 스트림릿 실행하면 다시 또 에러 발생;;;
```
partially initialized module 'plaidml' has no attribute 'library'

plaidml-keras 0.7.0 requires keras==2.2.4, but you'll have keras 2.4.3 which is incompatible.
```

keras가 2.4 버전이어서 지워준다. (언제 2.4로 깔렸나?? 하도 지웠다 깔았다 했더니;..)
```
pip3.8 uninstall keras
```

다시 설치
```
pip3.8 install keras==2.2.4
```

이번에는 이제 또ㅓ;;
```
Could not find PlaidML configuration file: "experimental.json".
```

파일위치가 
홈디렉토리안에 .local/share/plaidml 안에  
experimental.json ,config.json 파일들이 있는데 코드 내에서 넣어줘야한다

다른 시스템에서는 /usr/share/plaidml 에 들어있는 경우도 있고 
맥 같은 경우는 
/Library/Frameworks/Python.framework/Versions/3.7/share/plaidml
이런식인듯..

그래서인지 경로를 잘 못찾아 주는듯..

경로를 export 해서 환경변수 등록도 해줬는데 별 소용이 없다  
코드로 넣어줘야하는듯 하다

프로젝트 메인인 app.py 맨 위에 코드 삽입
```py
import os

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
os.environ["PLAIDML_NATIVE_PATH"] = "/home/sgtocta/.local/lib/libplaidml.so"
os.environ["RUNFILES_DIR"]="/home/sgtocta/.local/share/plaidml"
```
경로를 시스템에 따라 다른 듯 하다. 
centos와 우분투는 홈 디렉토리 안에 있는 듯하다..

이번에는 라이브러리를 못찾는다고 나오는데..  
아예 스트림릿을 종료 ^C 한 후에 (Ctrl+c)
다시 시작해보면     
```
 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://xxx.xxx.xxx.xxx:8501

Using plaidml.keras.backend backend.
```
이렇게 나오면 성공!! backend를 plaidml.keras로 한다고 ㅠㅠㅠㅠ  

단,  
주의할 점은 keras 모듈을 불러올 때 tensorflow.keras로 하면 안 된다고 한다

```py
import keras 를 먼저하고 
from keras.models import Sequential #모델 불러오고 Sequential() 불러오는 식으로 해야한다고 함
from keras import backend as K
```

계속 에러 메세지만 나오고 있었는데;;   
스트림릿을 껏다가 켰더니 되어서 조금 어벙벙하네;;  

중요한 점은 

마지막으로 해보자는 생각으로   
uninstall을 한 후에 했는데 pyopencl 을 설치 했는데 
이게 도움이 된지는 모르겠다  

그리고 이제 테스트 코드를 돌려보자  

아 실행하기 전에 마지막 정리.. 마지막으로 했던 코드 정리 입니다~

```shell
$pip3.8 install pyopencl
$pip3.8 uninstall plaidml-keras
$pip3.8 install plaidml-keras
$plaidml-setup
$pip3.8 install plaidbench
```

그리고 확실하게 파일내에 코드로 환경변수 정의해주고  
테스트 코드도 돌림

아래는 테스트 코드
```py
import os

# IMPORTANT: PATH MIGHT BE DIFFERENT. SEE STEP 6
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
os.environ["PLAIDML_NATIVE_PATH"] = "/home/sgtocta/.local/lib/libplaidml.so"
os.environ["RUNFILES_DIR"]="/home/sgtocta/.local/share/plaidml"
#os.environ["RUNFILES_DIR"] = "/Library/Frameworks/Python.framework/Versions/3.7/share/plaidml"
#os.environ["PLAIDML_NATIVE_PATH"] = "/Library/Frameworks/Python.framework/Versions/3.7/lib/libplaidml.dylib"
# Mac의 경우 경로가 위와 비슷한 듯하다.

# Don't use tensorflow.keras anywhere, instead use keras
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K
batch_size = 128
num_classes = 10
epochs = 12
# input image dimensions
img_rows, img_cols = 28, 28
# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')
# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

복사 붙여넣기해서 바로 vscode 기준 실행버튼을 누르면   
바로 실행이 되고  

```
Using plaidml.keras.backend backend. 라고 뜸  
```

흠.. 속도는 코랩으로 돌릴 때 보다는 당연히 느리지만..   
그래도 뭔가 그럴 듯하게 빨라졌다 ㅋㅋ  

