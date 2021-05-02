amdgpu 그래픽 드라이버를 설치해준다
https://www.amd.com/en/support/graphics/amd-radeon-r9-series/amd-radeon-r9-300-series/amd-radeon-r9-380

https://amdgpu-install.readthedocs.io/en/latest/install-installing.html

tar.xz 파일을 압축을 풀어준다
```
$tar xvf amdgpu-pro-21.10-1247438-rhel-8.3/
```


그리고 해당 디렉토리로 이동을 한 후 실행
```
$cd amdgpu-pro-xxxxx(버전)
$ ./amdgpu-pro-install -y
```

그리고 재부팅

그리고 콘다 가상환경으로 들어가기
```
conda activate tfod
```

주인공 PlaidML을 설치한다. 
To install PlaidML with Keras, run the following:
```
pip install -U plaidml-keras
```

그 전에는 keras가 설치가 되어 있었는데 버전이 2.4.3 이었는데 설치과정에서 자동으로 지운 후에 
kears2.24 버전을 설치해준다

```
Attempting uninstall: keras
    Found existing installation: Keras 2.4.3
    Uninstalling Keras-2.4.3:
      Successfully uninstalled Keras-2.4.3
Successfully installed enum34-1.1.10 keras-2.2.4 keras-applications-1.0.8 plaidml-0.7.0 plaidml-keras-0.7.0
```

셋업하기
```
plaidml-setup
```

Enable experimental device support? (y,n)[n]

Save settings to /home/

yes를 눌러준다 


~/.keras/keras.json 파일을 열어서 수정
keras.josn 파일을 보면
```
{
    "floatx": "float32",
    "epsilon": 1e-07,
    "backend": "tensorflow",
    "image_data_format": "channels_last"
}
```
backend 키를 수정해준다 
 "backend": "plaidml.keras.backend"


파이썬 코드로 yolo코드를 실행해봤다.. 근데 cpu로 처리하던 속도랑 거의 똑같은거 같은데..
뭔가 잘 된다 했다..

데스트탑에서 setting > Details > About 에 보면
이렇게 바뀌어있음
AMD® Radeon
원래는 그래픽카드명이 나왔는데 세부 그래픽명이 안나온다.. 이상하다..

에러 전혀 인지를 못하고 있었으나... plaidml-setup 했을 때 cpu만 나오고 gpu가 나오지 않는다..;;
그래서 봤더니 amdgpu를 설치할 때 warning 에러가 발생한게 있었음..
```
amdgpu-pro-uninstall 
```

지운 후 다시 설치. 역시 같은 에러 발생

amdgpu-dkms-1:5.9.20.104-1247438.el8.noarch
Complete!
WARNING: amdgpu dkms failed for running kernel

이거를 고치겠다고 주말에 틈틈히 계속 매달려서 해봤지만 모두 실패~
그러다가 마치 소문이라도 들은양 커널 업데이를 해야한다고 해서 커널 업데이트까지 시도
그래서 커널 업데이트 포스팅은 여기

결국 다 똑같은 워닝 및 에러..

에러 로그를 찾아보자
vi /var/lib/dkms/amdgpu/5.9.20.104-1247438.el8/build/make.log
  /var/lib/dkms/amdgpu/5.9.20.104-1247438.el8/build/Makefile:26: "Local GCC version 80404 does not match kernel compiler GCC version 80401"

하지만.. 실마리는 찾았지만~
일단 다음에 시도하기로.. 뭐 내 컴으로 머신러닝을 돌릴꺼도 아닌데.. 그냥 확인만 해볼려고 했던건데..
힘들다...


# 지우기
```shell
$pip uninstall plaidml-keras
```
수정했던 keras.json파일은 원래 전 상태로 (수정 전) 상태로 바뀌어 있다. 


만약 tensorflow model을 사용할 때 아래와 같은 에러가 나온다면
ValueError: Unable to import backend : plaidml.keras.backend

혹시 ~/.keras/keras.json 가 제대로 복구되었는지 확인
의 backend value부분을 "tensorflow"로 바꿔준다
{
    "floatx": "float32",
    "epsilon": 1e-07,
    "backend": "plaidml.keras.backend",
    "image_data_format": "channels_last"
}






ROCm 다음에 알아보기 
일단 커널이 안 맞아서 안될 것 같다.. 
amd드라이버 설치 실패도 커널이 안맞아서 그런거 같은데.. 나중에...
https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel


이거도 실패..
좀 더 복잡도가 있는 거 같은데.. 문제는 GPU를 못잡는다...
모르겠다;;




 plaidml-setup
을 실행했을 때 
```
Traceback (most recent call last):
  File "/home/sgtocta/.local/bin/plaidml-setup", line 5, in <module>
    from plaidml.plaidml_setup import main
  File "/home/sgtocta/.local/lib/python3.8/site-packages/plaidml/__init__.py", line 50, in <module>
    import plaidml.settings
  File "/home/sgtocta/.local/lib/python3.8/site-packages/plaidml/settings.py", line 33, in <module>
    _setup_config('PLAIDML_EXPERIMENTAL_CONFIG', 'experimental.json')
  File "/home/sgtocta/.local/lib/python3.8/site-packages/plaidml/settings.py", line 29, in _setup_config
    raise plaidml.exceptions.PlaidMLError(
plaidml.exceptions.PlaidMLError: Could not find PlaidML configuration file: "experimental.json".
```
파일 위치를 못 찾을 때 


환경변수 등록해주기 

export PLAIDML_NATIVE_PATH=$HOME/.local/lib/libplaidml.so
export RUNFILES_DIR=$HOME/.local/share/plaidml


이렇게 해서 지운다음에 
```
plaidml-setup
```
하면 cpu 목록 gpu 목록이 셋업 페이지가 뜬다. 
하지만..;; GPU가 없다;;
돌아버리;..

먼저 언인스톨을 다시하고

깨끗하게 하고 싶으면 아래가 해당 패키지가 설치되는 곳인데 사실 안에 파일들을 거의 다 남아있었음
/home/sgtocta/.local/lib/python3.8/site-packages/plaidml/keras/*
/home/sgtocta/.local/lib/python3.8/site-packages/plaidml_keras-0.7.0.dist-info/*

아마도 도커랑 시도를 해봤는데 그때 생성된것 때문에 그러는 것 같기도하고;;
어쨋든 rm -rf 로 깨끗이 삭제

```shell
$cd ~/.local/lib/python3.8/site-packages
$rm -rf plaidml
$rm -rf plaidml_keras-0.7.0.dist-info
```

다시 설치를 해도 결과는 똑같음 그래서 로그를 봐야함
환경변수 등록해주기
```
export PLAIDML_VERBOSE=4
```
그리고 다시 plaidml-setup

그러면 역시 cpu밖에 안나오고 

화면에는 이렇게 출력됨
 
```
INFO:Verbose logging has been enabled - verbose level 4 

DEBUG:plaidml:Creating HAL: opencl
DEBUG:plaidml:Failed to initialize HAL: clGetPlatformIDs libOpenCL.so: cannot open shared object file: No such file or directory
DEBUG:plaidml:Creating HAL: opencl
DEBUG:plaidml:Failed to initialize HAL: clGetPlatformIDs libOpenCL.so: cannot open shared object file: No such file or directory
Default Config File Location:
   Unknown/
```



특정 라이브러리 설치 확인하기
```
sudo yum provides '*/libOpenCL.so' 
```

```
Repo        : amdgpu-pro-local
Matched from:
Filename    : /opt/amdgpu-pro/lib64/libOpenCL.so

ocl-icd-devel-2.2.12-1.el8.i686 : Development files for ocl-icd
Repo        : powertools
Matched from:
Filename    : /usr/lib/libOpenCL.so

ocl-icd-devel-2.2.12-1.el8.x86_64 : Development files for ocl-icd
Repo        : powertools
Matched from:
Filename    : /usr/lib64/libOpenCL.so
```

이렇게 나온다..; 이제 이게 힌트였는데 큰 의미는 없을 수도 있지만
ampgpu-pro opencl이 잘 설치는 되어있는거 같고..

중요한거는 아래 부분
```
[sgtocta@localhost lib]$ ls -li /usr/lib64/libOpenCL.*
73525982 lrwxrwxrwx. 1 root root     18 May 15  2019 /usr/lib64/libOpenCL.so.1 -> libOpenCL.so.1.0.0
73525983 -rwxr-xr-x. 1 root root 133472 May 15  2019 /usr/lib64/libOpenCL.so.1.0.0
```
여기에서 보면 libOpenCL.so.1 이 실제파일 libOpenCL.so.1.0.0 을 가리키고 있는데 
아무래도 plaidml-setup을 하면 libOpenCL.so.1 파일이 아닌,
libOpenCL.so 파일을 찾는 거 같다.. 그래서 새로운 심볼릭 링크를 또 만들어 준다

심볼릭 링크를 libOpenCL.so를 만들어서 이거를 다시 심볼릭 링크인 libOpenCL.so.1 에 연결!!
``` 
sudo ln -s libOpenCL.so.1 libOpenCL.so
```

이제 확인을 해보면
```
cd /usr/lib64
ls -li ./libOpenCL.*
```

```
73525982 lrwxrwxrwx. 1 root root     14 May  2 12:51 ./libOpenCL.so -> libOpenCL.so.1
74133376 lrwxrwxrwx. 1 root root     29 May  2 12:51 ./libOpenCL.so.1 -> libOpenCL.so.1.0.0
73525983 -rwxr-xr-x. 1 root root 133472 May 15  2019 ./libOpenCL.so.1.0.0
```

amd쪽 opencl을 연결해줘야했더니 먼저 연결했더 되지도 않고;;
그래서 좀 더 알아봤더니.. libOpenCL.so 심볼릭 링크를 만들어야하는 것

이제 다시 plaidml-setup 을 실행하면 
```
...
..
..
Experimental Config Devices:
   llvm_cpu.0 : CPU (via LLVM)
   opencl_amd_tonga.0 : Advanced Micro Devices, Inc. Tonga (OpenCL)
```
드디어 나온다
이제 y를 누르면
뭔가 셋팅을 시작하고 

Multiple devices detected (You can override by setting PLAIDML_DEVICE_IDS).
Please choose a default device:

   1 : llvm_cpu.0
   2 : opencl_amd_tonga.0

Default device? (1,2)[1]:2

라고 물어보면 2을 눌러준다.. 


마지막으로 
Success!
라고 나오면 끝!

눈물난다.ㅠ


참고 이슈
https://github.com/plaidml/plaidml/issues/560

아마도 우분투의 경우는 이렇게 되는듯.. 
/usr/lib/x86_64-linux-gnu/libOpenCL.so


이제 스트림릿을 실행해본다
streamlit run app.py

그러면
앱이 실행되면서 
Using TensorFlow backend.
라고 나오는데 

파이썬 코드로 
os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"
을 넣어주면 실행을 할때 plaidml의 gpu로 되야하는데
cpu와 속도가 같다;;

그래서 이번에는 
스트림릿을 끄고

vi ~/.keras/keras.json
을 수정해준다

다시 스트림릿 실행하면
partially initialized module 'plaidml' has no attribute 'library'

plaidml-keras 0.7.0 requires keras==2.2.4, but you'll have keras 2.4.3 which is incompatible.

keras가 2.4 버전이어서 지워준다
pip3.8 uninstall keras

다시 설치
pip3.8 install keras==2.2.4


이제 또ㅓ;;

 Could not find PlaidML configuration file: "experimental.json".

파일위치가 
홈디렉토리안에 .local/share/plaidml 안에
experimental.json 이 들어있고, config.json도 있는데 코드내에서 넣어줘야한다

다른 시스템에서는 /usr/share/plaidml 에 들어있는 경우도 있고 
맥 같은 경우는 
/Library/Frameworks/Python.framework/Versions/3.7/share/plaidml
이런식인듯..

그래서인지 경로를 잘 못찾아 주는듯..
경로를 export 해서 환경변수 등록도 해줬는데 안된는 걸로 봐서는 
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
아예 스트림릿을 종료 ^C 한 후에 
다시 시작해보면 
```
 You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://xxx.xxx.xxx.xxx:8501

Using plaidml.keras.backend backend.
```
이렇게 나오면 성공!!

주의할 점은 keras 모듈을 불러올 때 tensorflow.keras로 하면 안 된다고 한다
```py
import keras 를 먼저하고 
from keras.models import Sequential #모델 불러오고 Sequential() 불러오는 식으로 해야한다고 함
from keras import backend as K
```

계속 에러 메세지만 나오고 있었는데;; 스트림릿을 껏다가 켰더니 되어서 조금 어벙벙하네;;
중요한 점은 

마지막으로 해보자는 생각으로 uninstall을 한 후에 했는데 
이번에는 테스트 코드를 한번 돌려봤다.. 이때 도움이 된지는 모르겠다

마지막 정리.. 마지막으로 했던 코드 정리
```
$pip3.8 install pyopencl
$pip3.8 uninstall plaidml-keras
$pip3.8 install plaidml-keras
$plaidml-setup
$pip3.8 install plaidbench
```

아.. pyonecl이라는 것을 설치했었는데 이게 도움이 된것인지는 모르겠다..;;
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
역시 Using plaidml.keras.backend backend. 라고 뜸

그리고 나서, 아 되는 구나~ 라는 생각이 들어서 포기를 안함;;
테스트 코드를 실행해 보는 것도 괜찮은것 같다는 생각이 듬


