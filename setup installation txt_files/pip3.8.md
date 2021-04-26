# pip 업그레이드

파이썬 3.8을 설치한 후에 pip을 실행해서 패키지를 다운받았더니 속도가 엄청 느리다.  
그리고 친절하게도 업그레이드를 하라고 명령어까지 알려주더라.. 

```shell
$python3.8 -m pip install --upgrade pip
```
그런데 패키지 다운도르 속도는 변함이 없다 ㅜㅜ 

어쨋든 여기에서 알게된 사실은 
예를 들어 버전 **pip3.8** 과 **pip**은 
```shell
$pip3.8 --version 
# 또는
$pip --version
```
버전은 pip 21.0.1 이라고 나오고  

<br/>

그러나 **pip3** 라고 하면 
```shell
pip3 --version
```
pip 예전 버전이 표시된다.  pip 9.0.3 이렇게 나옴. 

그러니깐 예전에는 pip3로 install 했던거 같은데 버전 확인한 다음에   쓰면 될 듯하다.   
어쨋든 이제 pip만 쳐도 된다

<br/>

*참고로~   중요한거 아니니 SKIP~  
파이썬 버전이 여러개가 깔려있으면 python 실행할때에도 지정을 해줘야한다.   
(여러버전 설치를 지원해서 아나콘다의 파이썬 버전, 기본 파이썬 버전, 예전 파이썬 버전 등등... )  

그래서 python3, python3.8 이런식으로 달라지는 듯하다.  
예:
```
[octa@localhost ~]$ python3
Python 3.6.8 (default, Mar 19 2021, 05:13:41) 
[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

[octa@localhost ~]$ python3.8
Python 3.8.8 (default, Apr  9 2021, 10:26:29) 
[GCC 8.4.1 20200928 (Red Hat 8.4.1-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit()

```

<br/>

# pip 다운로드 향상 시키기 , 미러사이트 추가 하기
pip config list -v 를 해보면 리스트를 볼 수 있는데  
환경 파일이 위치한 경로들을 보여준다..   

```
for variant 'global', will try loading '/etc/xdg/pip/pip.conf'
For variant 'global', will try loading '/etc/pip.conf'
For variant 'user', will try loading '/home/octa/.pip/pip.conf'
For variant 'user', will try loading '/home/octa/.config/pip/pip.conf'
```
그러나 (centOS 8 기준)에는 파일은 커녕 디렉토리도 없다..

미러 사이트를 추가하고 싶은데.. 여기저기 찾아봤는데 속 시원한 해답은 없음 ㅠ

미러사이트를 추가 할려는 이유는 opencv 라이브러리를 설치 해야하는데 한 50여분을 다운을 받았다.  

그래서.. 디렉토리가 없으면 그냥 만들어 주면 되는듯 하다.   
허무하지만 그냥 만들자.. 고민말고 ㅋㅋㅋ


홈 디렉토리 밑에 숨긴 디렉토리와 conf파일을 만들자  
```shell
$mkdir .pip 
$vi .pip/pip.conf
```

pip.conf 파일에 아래 내용을 추가한 후 저장을 해준다.
```conf
[global]
index-url=http://ftp.daumkakao.com/pypi/simple
trusted-host=ftp.daumkakao.com
```

그리고 테스트를 하기가;;; 딱히 받을 게 없어서;;;  
그리고 어쩌다 matplotlib 모듈이 없어서 다운을 받았다.. ㅋㅋ   
아나콘다도 안 깔려 있음 ㅋㅋ

결과는 두둥!

```
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: http://ftp.daumkakao.com/pypi/simple
Collecting matplotlib
  Downloading http://mirror.kakao.com/pypi/packages/de/cf/d81fece6931ab0a3427eb29c2da7c3dc8e611927609d737a55964a3e0ef5/matplotlib-3.3.3-cp38-cp38-manylinux1_x86_64.whl (11.6 MB)
```
뭐 이런식이다.. 카카오 미러 사이트로 다운을 받는다.   
용량은 20mb 가까이 되는 듯 한데..
몇초만에 다 받음~ 굿!!   

그리고 마지막으로는 파이썬 라이브러리/패키지 설치할 때 참고하는 pypi  
[Python packages찾기](https://pypi.org/)