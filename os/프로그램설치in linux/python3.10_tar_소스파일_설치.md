# python3.10 소스파일 설치

python 소스파일로 설치.md 에서 했던 라즈베리 파이에 설치한 것과 매우 비슷

우분투 20.04 에 설치를 해봄   

[여기에서stable 버전으로 3.10 다운](https://www.python.org/downloads/source)   

다운로드 후에   

압축을 풀어주고  
```
cd ~/Downloads
tar xvf Python-3.10.11.tar.xz 
```

압축이 풀린 해당 디렉토리로 이동 

```
cd Pyhthon-3.10.11
./configure --enable-optimiztions
```

완료가 되면  Makefile 파일이 만들어지고 본격 인스톨

```
sudo make altinstall 
```


끝


