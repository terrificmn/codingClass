python3 기준으로  그냥 pip을 사용하게 되면 skbuild가 없다라는 에러 발생함

이유는 (from stack overflow)   
> This is because your pip is too old to understand the new manylinux2014 package format and tries to compile from source.   
That will also fail because pip is too old to understand how to use pyproject.toml to install build dependencies such as scikit-build.

```
Collecting skbuild
  Could not find a version that satisfies the requirement skbuild (from versions: )
No matching distribution found for skbuild

Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-v6pab3k3/opencv-python/
```
pip을 먼저 업그레이드를 시켜야 한다 . permission 에러 발생 시 sudo 
```
pip3 install --upgrade pip
```

그리고 나서 
```
python3 -m pip install opencv-python
```
또는
```
pip3 install opencv-python
```


Successfully installed numpy-1.19.5 opencv-python-4.6.0.66  
이라고 나오면 굿!

확인해보려면 
python3를 눌러서 진입 후 opencv import해보기
```
$ python3
>>> import cv2
>>> print(cv2.__version__)
>>> exit()
```
4.6.0 이라고 나오면... import 부터 에러가 발생안하면 잘 설치된 것임

> $는 프롬포트, >>>는 python 진입했을 때 나옴

찾다보면 아래 방법도 있기는 하나 python에서 전혀 인식 하지를 못한다 **(비추천)**
```
sudo dnf install opencv*
```
