> 리눅스 에서 (Ubuntu)
3.7 파이썬 설치 위해서 리포지터리 추가
```
sudo add-apt-repository ppa:deadsnakes/ppa 
```

apt 업데이트
```
sudo apt update
```

파이썬 설치 (가상환경 구축을 위해서 3.7버전으로 설치)
```
sudo apt install python3.7
```

그 이후 pip3 설치
```
sudo apt install python3-pip
```

<!-- pip3가 설치되었다면 ,,,, 이 방법 말고 apt / apt-get 으로 설치할 것!
```
pip3 install virtualenv
``` -->

만약 python 이라고 쳤을 때 버전이 3.7이 안나오고 3.6이라고 나오면 
.bashrc 파일 편집해주기. 그리고 ~/.bash_aliases 도 만들어서 같은 내용 입력

```
alias python=python3.7
alias python3=python3.7
```

그리고 저장 후 source 입력해주기
```
source ~/.bashrc
source ~/.bash_aliases
```

참고:: 사이트 https://blog.arturofm.com/install-python-3-7-on-ubuntu-16-04/


이제 가상환경 만들기
pip으로 설치하지 말고  apt로 설치
sudo apt install virtualenv  

가상환경 만들기 
virtualenv mystreamlit  
그러면 현재 디렉토리에 mystrealit 이라고 디렉토리가 만들어 진다

가상환경에 python3.7로 깔아주기 (python3.7로 적어줘야함)
virtualenv -p python3.7 mystreamlit   

가상환경 실행
source mystreamlit/bin/activate    



--------------------
> windows 에서
MinMaxScaler()가 호환이 안되서 scikit버전을 0.23.2로 설치한다
pip install scikit-learn==0.23.2

결국 Fail! 아무래도 cross platform은 포기해야할 듯 
수업내내 실패, 강사님도 실패;;
-------------------------------------------------


리눅스 virtualenv 버전이지만 이것도 FAIL 
이제 
pip freeze > requirements.txt
python -m virtualenv myenv
python3 -m pip install -r requirements.txt



# 리눅스에서 anaconda를 이용해서 가상환경 만들기
 
처음에 설치가 완료가 되면은 **anaconda를 init** 하겠냐고 물어봄
그때 *yes*로 등록해줌 (엔터) 였는지 헛깔림
그러면 conda 명령어를 쳐도 바로 인식이 됨

만약 콘다 설치 후 
conda 명령어가 들지 않으면 
vi .bashrc 파일의 PATH를 등록해줘야함

export PATH="/home/ubuntu/anaconda3/bin:$PATH"
그리고 저장

sudo source .bashrc

그리고 conda 라고 치면 명령어 안내가 나오면 ok
만약 위에서 init을 안했다면 
conda init   

그리고 가상환경 만들어주면서 라이브러리 설치
conda create -n streamlit python=3.7.10 tensorflow numpy scipy matplotlib ipython scikit-learn==0.23.2 pandas pillow jupyter seaborn joblib

그러면 (streamlit) 라고 바껴야 함. (정확하지 않음) 아니면 activate 시키기
conda activate streamlit 

만약 streamlit을 못찼는다고 하면 streamlit 설치
pip3 install streamlit    

