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

