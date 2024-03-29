# AWS 의 EC2 가상서버
EC2 는 가상서버   
데이터베이스 (RDS)


## EC2 (가상서버) 만들기
1단계. Amazon Machine image (AMI) 선택   
- 단 프리티어 (CPU 1, 메모리 1GB 짜리 선택)   
- Amazon Linux (centOS 기반)   
- Ubuntu는 (18.xx 버전 추천)   

<br/>

## 7단계: 보안 그룹 설정하기
- SSH 로 연결할 수 있음 (설정해야함)   
- 파일을 올릴 수 있는 FTP 프로토콜    
- HTTPS 인터넷 프로토콜    
- 즉, 방화벽에서 위 3개의 통로를 열어줘야함   
- 프로토콜과 포트 범위를 입력해 준다   

보안그룹에서 Security Groups 에서    
ssh은 기본으로 열려있고   
스트림릿이 쓴느 8501 8502 포트를 추가해줘야 함   


<br/>

## 터미널로 접속하기
- ssh 명령어 사용   
- 인스턴스 요약에서 퍼블릭 IPv4 주소로 입력을 해서 접속   
```
$ssh ip주소 -i .\ai.pem -l username
```
AWS를 우분투로 했을 경우는 유저이름을 ubuntu로 aws에서 정해줌   
그래서 -l 이후는 ubuntu로 하면 됨

-i 옵션(인증파일 입력) `ai.pem` (경로/파일명을 적어주면 됨)   
-l 옵션(로그인유저) 

* 윈도우에서는 powershell 로 하면 됨   
```
ssh 내가상서버ip주소 -i C:\Users\5-20\Downloads\myawskey.pem -l ubuntu
```


<br/>

## 데이터베이스 사용하기
- Amozon RDS 선택해서    
- sql 엔진을 선택해서 사용할 수 있음


## 가상환경 설정하기
일단 ssh로 접속이 되었으면    
1. 먼저 python을 있는지 확인한다
```
python
```
2. 버전을 확인한 후 일단 로컬의 host컴에서 아나콘다를  다운을 받는다  
브라우저에서 검색한 후 리눅스 운영체제에 맞는 것을 찾은 후 다운링크를 복사  
다시 터미널로 돌아와서
```
wget 링크주소붙여넣기 
```

3. 다운이 되었으면 다운로드된 경로로 이동해서 설치를 해준다   
*설치는 `프로그램 설치 in linux.txt` 파일 참고*

4. 로컬host컴에서 깃허브에 requirement.txt 파일을 add 한 후 commit 및 push를 해준다   
*자세한 설명은 `Streamlit 가상환경.md` 또는 `aws_installation_setup.md` 파일 참고*

5. 그리고 다시 터미널 ssh로 돌아와서 git을 먼저 설치해준다.   
그리고 git을 clone 시켜준다


