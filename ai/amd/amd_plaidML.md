# 머신러닝 GPU로 하기! - AMD Radeon

원래 Nvidia 에서는 tensorflow 지원이 되는걸로 알았지만..  
현재 내 그래픽카드는 라데온이다..    
라데온으로 할 수 있는 방법을 찾아보니    
ROCM 과 인텔에서 오픈소스로 만든 PlaidML 이라는 것이 있었다..

PlaidML은 맥이나 AMD 그래픽카드도 지원을 한다고 해서    
설치도 쉽고 설정도 쉽다고 해서    
이걸로 해야겠다해서 설치를 알아보고 했지만.. 

역시 쉬운게 없지;. 될리가 없지 ㅋㅋ 안되는 거 며칠째 붙들고 있다가   
거의 포기했는데 obs-stdio, Davinci Resolve를 설치하면서    
(간단한 영상 편집이 필요했음- 프로젝트;)   
gmdgpu-pro 드라이버가 설치가 안되어 있으니 위의 프로그램들도 안됨;;

그래서 결국은.. 거의 1주 넘게 해서 성공했다.. ㅠㅠ
암튼 그 방법을 기록

기존에 원래 그래픽 드라이버가 설치되어 있지만.. OpenCL이 있어야    
GPU로 연산을 할 수가 있다.

amdgpu 그래픽 드라이버를 설치해준다. 자신의 그래픽 드라이버를 맞게 선택해주자  

https://www.amd.com

https://www.amd.com/en/support/graphics/amd-radeon-r9-series/amd-radeon-r9-300-series/amd-radeon-r9-380  

https://amdgpu-install.readthedocs.io/en/latest/install-installing.html

<br>

> 여러번 시도를 했다가 실패를 했었는데 결국 깨달은 것은   
amd 드라이버를 설치할 때 커널 버전이 맞아야 한다는 것이다!! 중요하다  
그래야 에러 없이 잘 설치될 수 있다.

위에서 언급한 것처럼 커널도 업데이트 해도 예전 커널로 설치해볼려고 했으나     
번번히 설치 실패..   

현재 쓰고 있는 CentOS 8 stream 인데.. 이게 왠지 8.3 버전 일 것이라고 생각했으나..   
정확한 버전을 알기는 좀 어려웠다..  amd 사이트에서는 centos 8 은 8.3버전 지원이라고 했으니..   
stream은 몇 버전인지 모르겠다.. 추측하기로는 커널 버전이 높으니 더 높은 버전 같았다..   

암튼 이게 문제였다..  나중에 안 것이지만
```
uname -r
```
이라고 입력하면 커널 버전을 알 수 있다. 

우분투도 지원하니.. 맘편하게 우분투로 넘어갈까 하다가도..    
왠지 센트os에 적응이 되서.. CentOS 8로 설치하기 결정..   
아~ 이거 올해까지만 지원되는데.. 모르겠다.  
사실 컴터로 머신러닝을 돌릴 것은 아닌데,, 동영상 편집도 좀 해보고.. 사실 너무 많이 왔다.. 돌아가기에는 ..ㅠ

<br>

# 답은 CentOS stream은 지원이 안되는 것이었음
사실 커널 아래 버전을 설치하면 될 것도 같았으나.. 번번히 실패해서 결국은 os배포판을 바꿔버렸다.  

이게 시작이였다...  
일단 업데이트를 했다면 새로 업데이트 된 커널에서 다시 설치하여야 하므로   
재부팅을 한다.

----dkms 설치를 한다를 참고----

<br>

amdgpu-pro 가 잘 설치가 되었다면.. (dkms 부분도 잘 설치고)    
다시 
```
pip3.8 install plaidml-keras 
```

# 트러블슈팅~
plaidml 설치 후 plaidml-setup 을 실행하면..
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
파일 위치를 못 찾는다면서 실행이 안된다..


환경변수 등록해주기 
```shell
$export PLAIDML_NATIVE_PATH=$HOME/.local/lib/libplaidml.so
$export RUNFILES_DIR=$HOME/.local/share/plaidml
```
이 부분은 운영체제마다 조금씩 다를 수 있다.   
알아본 바로는 우분투, 센트os는 위의 경로가 맞는 듯 하다.. 

mac os 같은 경우에는 아래처럼 되는 듯 함..
```shell
export PLAIDML_NATIVE_PATH=/usr/local/lib/libplaidml.dylib
export RUNFILES_DIR=/usr/local/share/plaidml
```

```
plaidml-setup
```
을 다시하면 셋업을 할 수 있는 페이지? 가 나오고 설정을 할 수가 있는데   
그토록 원하던 gpu가 안나온다..  
하지만..;; GPU가 없다;;    
돌아버리;..ㅋㅋ
 
침착하게...   
먼저 언인스톨을 다시하고    
깨끗하게 하고 싶으면 아래가 해당 패키지가 설치되는 곳인데 사실 안에 파일들을 거의 다 남아있었음  
```
/home/sgtocta/.local/lib/python3.8/site-packages/plaidml/keras/*
/home/sgtocta/.local/lib/python3.8/site-packages/plaidml_keras-0.7.0.dist-info/*
```

아마도 도커랑 시도를 해봤는데 그때 생성된것 때문에 그러는 것 같기도하고   
어쨋든 rm -rf 로 깨끗이 삭제

```shell
$cd ~/.local/lib/python3.8/site-packages
$rm -rf plaidml
$rm -rf plaidml_keras-0.7.0.dist-info
```
언제 rm을 할때는 더블 체크한 후에 진행하자!

다시 설치를 해도 결과는 똑같음~ 하.. 그래서 로그를 봐야함    
환경변수 등록해서 로그를 볼 수있게 하자

```
export PLAIDML_VERBOSE=4
```

그리고 다시 plaidml-setup 을 하면  
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
libOpenCl.so를 못 찾고 있다.  

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

이렇게 나온다..;    
ampgpu-pro opencl이 잘 설치는 되어있는거 같고.. 다행 ㅠ

중요한거는 /usr/lib64/libOpenCL.so 부분이다 (distro에 따라 다를 수 있음)
```
[octa@localhost lib]$ ls -li /usr/lib64/libOpenCL.*
73525982 lrwxrwxrwx. 1 root root     18 May 15  2019 /usr/lib64/libOpenCL.so.1 -> libOpenCL.so.1.0.0
73525983 -rwxr-xr-x. 1 root root 133472 May 15  2019 /usr/lib64/libOpenCL.so.1.0.0
```
여기에서 보면 libOpenCL.so.1 이 실제파일 libOpenCL.so.1.0.0 을 가리키고 있는데   
아무래도 plaidml-setup을 하면 libOpenCL.so.1 파일이 아닌,  
libOpenCL.so 파일을 찾는 거 같다..   
그래서 새로운 심볼릭 링크를 또 만들어 준다  

심볼릭 링크를 libOpenCL.so를 만들어서   
이거를 다시 심볼릭 링크인 libOpenCL.so.1 에 연결!!
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

amd쪽 opencl을 연결해줘야했더니 먼저 연결했더 되지도 않고   
그래서 좀 더 알아봤더니.. libOpenCL.so 심볼릭 링크를 만들어야하는 것   

이제 다시 plaidml-setup 을 실행하면 
```
..생략
..
Experimental Config Devices:
   llvm_cpu.0 : CPU (via LLVM)
   opencl_amd_tonga.0 : Advanced Micro Devices, Inc. Tonga (OpenCL)
```
드디어 나온다 이제 y를 누르면 뭔가 셋팅을 시작하고 

```
Multiple devices detected (You can override by setting PLAIDML_DEVICE_IDS).
Please choose a default device:

   1 : llvm_cpu.0
   2 : opencl_amd_tonga.0

Default device? (1,2)[1]:2
```
라고 물어보면 2을 눌러준다.. 

마지막으로 Success! 라고 나오면 끝!


참고 이슈   
https://github.com/plaidml/plaidml/issues/560 

아마도 우분투의 경우는 이렇게 되는듯..   
/usr/lib/x86_64-linux-gnu/libOpenCL.so


이제 스트림릿을 실행해본다  
streamlit run app.py

그러면
앱이 실행되면서 
Using TensorFlow backend.   
라고 나오는데, Tensorflow가 나오면 안되는데..   

아.. 눈물난다.ㅠ 하지만 끝이 아니였음;; 

2차 트러블 슈팅 보러가기  
[amd_plaidML_2_설치]참고하기


