# 아나콘다 설치
먼저 다운로드   
구글 anaconda download로 검색해서 individual Edition으로 다운로드하기   
Linux 버전 64-Bit (x86) Installer   
로 다운받으면 됨

참고 메뉴얼 사이트  
https://docs.anaconda.com/anaconda/install/linux/   
여기에 나온 방법대로 그대로 하는것이 좋음

인스톨 방법은   
먼저 dependencies 해결   
레드헷 계열  
```
sudo yum install libXcomposite libXcursor libXi libXtst libXrandr alsa-lib mesa-libEGL libXdamage mesa-libGL libXScrnSaver
```
이미 다 설치되어 있음 ;; 

다운로드 디렉토리로 이동 후 SHA-256으로 데이터 확인작업   
sha256sum /path/filename 형식인데   
이미 다운로드 디렉토리로 진입을 했기에  

```
sha256sum Anaconda3-2020.11-Linux-x86_64.sh
```
요렇게 입력

그 다음은
```
bash ~/Downloads/Anaconda3-2020.11-Linux-x86_64.sh
```

여기서 중요한 점은   
bash 라는 명령어는 그냥 써야하고    
다운로드 디렉토리에 파일이 없다면 경로는 바꿔주기   
그 다음은 엔터 밑 yes 만 눌러주면 설치가 된다

마지막에 conda init을 하겠냐고 물어보면 yes  

modified      /home/cta/.bashrc   
이 파일에 수정이 되면서 처음 시작할때 anaconde base 환경이 시작된다    
아래 나와있는 말 처럼 터미널의 shell을 껏다가 켜야함. 그럼 (base)가 붙은채로 시작된다   

==> For changes to take effect, close and re-open your current shell. <==


## (base) actviate 하기 싫으면 아래처럼 하면 될 듯
If you'd prefer that conda's base environment not be activated on startup, 
   set the auto_activate_base parameter to false: 

conda config --set auto_activate_base false

