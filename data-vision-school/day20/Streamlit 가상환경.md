## Streamlit 설명

| streamlit | | | | |
|--|--|--|--|--|
Sourcce data access | Data processing | Modeling | Deployment | Monitoring
Raw data를 | Clean data로 | Models: 등등.. | Production components | Monitoring data

Deployment 부분에서 프론트엔드를 배울 필요없이 
ui를 쉽게 구성할 수 있게 도와주는 app
: 이때 Flask 나 django 프레임워크를 사용


<br/><br/>

## 개발환경
회사와 학교 집의 컴퓨터의 각 개발환경이 다 다르기 때문에 
예를 들어 버전이 
학교에서도 파이썬 버전이 컴1은 3.8 컴2는 3.7 이런식으로 다른데
이게 문제가 되서 인공지능을 개발했어도 프로그램이 원할이 돌아가지 않는다

라이브러리도 마찬가지 
Colab에는 prophet 라이브러리가 깔려있는데 집에는 라이브러리가 없다면 개발환경이 달라서 프로그램 실행이 안될 수 있다.

그래서 이 개발환경을 다 맞춰주기가 힘들다
그래서 나온게 가상환경!!

아나콘다에서 프롬프트 앞에 보이는 (base) 라고 써있는 것도 가상환경 중에 하나다

학교 컴의 파이썬은 3.8.5

구글 코랩에서 `!python --version` 해보면 (!는 코랩에서만 쓰는 리눅스명령어라고 알려주는 기능) 하면 3.7.10

어떤 파이썬 패키지 리스트 보기
`!pip list` 를 해보면 
깔려있는 패키지가 보임

<br/><br/>

## 개발환경 셋팅하기
위의 리스트를 확정하기
`!pip freeze`

위의 리스트를 저장하기
```
!pip freeze > requirements.txt
```

코랩 왼쪽 패널을 열어서 보면
파일이 저장되어 있는데 다운로드하면 txt 파일이 저장됨



아나콘다 작업환경(가상)보기
아나콘다 터미널에서
conda info --envs
그러면 base로 저장된 경로가 나옴

가상환경 만들기
-n (가상환경이름)  
python=3.7.10 구글코랩의 파이썬 버전, 이것은 필수로 맞춰야함 아니면 최신버전으로 됨
```
conda create -n colab python=3.7.10
```
이 후에 다운로드될 패키지와 인스톨할 패키지가 표시되는데
여기에서 y 누르기

설치가 완료되면
가상환경으로 이동하기
```
conda activate colab
```
이렇게 하면 프롬프트가 
(base) C:\projects> 에서 
(colab) C:\projects> 으로 바뀌는 것을 확인

가상환경 종료 또는 base환경으로 돌아가기
```
>conda deactivate
```

이제 코랩에서 받았던 pip 패키지 파일 리스트를 이용해서 
pip 인스톨 한다
(colab) 환경으로 들어와야함!
먼저 cd로 해당파일이 있는 곳으로 이동하던가 경로를 지정해주면 됨
```
pip install -r requirements.txt  
```
이렇게 하면 
코랩과 같은 환경을 맞추기 위해서 requirements.txt파일에 있는 내용대로 다운로드 설치를 한다

<br/>

[파이썬 패키지 찾기](https://pypi.org/)  
파이썬 공식 repository

만약 설치 중 특정 패키지를 찾을 수 없다고 할 때는 특정패키지를 
위의 사이트에서 찾아볼 수 있다


참고!!
코랩은 아나콘다 환경이 아니므로
가상환경 구축할 때 계속 패키지 호환이 안맞아서 에러가 날 수 있다


가상환경 리스트 보기
```
conda env list
```

가상환경 삭제하기
또는 colab 이라는 가상환경 지우기
```
conda env remove -n colab
```
완전 깔끔해줄려면
리스트에서 나온
C:\Users\5-20\anaconda3\envs\colab:
디렉토리를 지워버리기

<br/><br/>

## 가상환경 패키지 리스트 보는 또 다른 방법

conda list 하면 설치되어 있는 패키지 목록이 나옴
```
conda list
```

먼저 가상환경을 activate 시켜줘야 한다   
conda activate 가상환경이름
```
conda activate streamlit
```

conda env export > requirements.yaml

패키지 목록 requirements.txt 파일로 만들기
```
conda list e > requirements.txt
```
pip freeze와 다른 점은 파일에 친절하게도   
다음에 설치할 수 있는 명령어가 주석으로 달린다  
주석 내용은 아래와 같음

```
# This file may be used to create an environment using:
# $ conda create --name <env> --file <this file>
```

## 가상 환경 설치

다시 설치하려면 위에 명령어를 사용하면 될 듯
conda create -n <streamlit가상환경이름> --file <파일>
```
conda create -n streamlit --f requirements.txt
```

___
<br/><br/>

## CICD 방식 추후 배움 (docker)
위와 같이 가상환경을 서버에 구축해서 같은 환경을 만드는 전통적인 방법이 있지만  
CICD 방식을 Docker를 이용해서 구현할 수 있음


## 최소 필요한 라이브러리만 가지고 가상환경 만들기
가상환경을 (이름)만들면서 한번에 설치할 수 있음
예: 이름은 streamlit python=3.7.10 으로 맞춰주고 그 다음부터는 쭉쭉 라이브러리 목록을 적어주면 된다
```
conda create -n streamlit python=3.7.10 tensorflow numpy scipy matplotlib ipython scikit-learn pandas pillow jupyter seaborn
```

<br/><br/>


## 스트림릿 선택하기
VSCODE에서 왼쪽 하단에서 커널을 선택해준다  
그러면 위쪽 화면에서 커널을 선택할 수 있는데 
가상환경을 위에서 3.7.10으로 셋팅했으니 
반드시 커널을 streamlit 만든 가상환경을 선택

그리고 터미널에서 
만약 가상환경인 stremalit 으로 이동이 안되면
Select default sheel을 cmd로 기본으로 선택해준다. 터미널을 끄고 다시 터미널을 시작해준다


정상적인 경우면 바로 자동으로 `conda activate streamlit` 입력이 되면서   
(base) 에서 (streamlit)로 변경 된다

이제 설치
(streamlit) > 프롬프트인지 확인 후 
``` 
(streamlit) > pip install streamlit
```

그리고 터미널에서 app.py이 있는 경로로 이동
그 후 
스트림 시작
``` 
streamlit run app.py
```

그러면 streamlit이 시작된다 

[https://streamlit.io/](https://streamlit.io/#install)