# vscode 관련 에어

## 트러블 슈팅: 권한 바꾸기 - vscode로 파일 편집 시 후 저장할 때 권한 에러
/var/www/html/ 권한이 drwxr-xr-x, 2 root root 되어 있어서 내 유저 (내 계정 ex:octa)로 로그인하고   
vscode 에디터로 편집할 때 퍼미션 에러 나는 경우 (특히 저장하려고 할 때 -권한이 없어서 안된다고)

먼저 디렉토리 권한 보기
```
$ls -l /var/www/
```
root로 되어 있다면
```
$sudo chown -R octa:${USER} html
# 또는 
$sudo chown -R 유저네임:유저네임 html
```

확인은 다시 ls -l (해당 디렉토리에 이동 후 또는 경로 적어준다)  

drwxr-xr-x, 2 {유저네임} {유저네임} 으로 바뀐 것을 확인할 수 있다.



## vscode c언어 컴파일 빌드 한글 깨지는 경우
vscode로 c언어 컴파일 빌드할 때 한글 깨지는 경우  
```
덈뀞?섏꽭???멸퀎  
```
이런식으로 될 경우에는   

vscode 프로그램의 오른쪽 하단 중 UTF-8로 되어 있는 곳을   
select encoding 을 눌러서 Reopen with Encoding이 열리는데   
이 때 kor 을 검색해서  EUC-KR을 선택해준다  

euc-kr로 열리자마자 또 이상하게 깨지는 경우가 있는데 그 때는 다시 ctrl+z 키를 눌러주고   
다시 컴파일 빌드를 하면 한글 안 깨지고 잘 됨



## 우분투에서 한글 입력이 깨질때 
이상하게도 실제 코딩하는 곳? 즉 파일 코드를 바꿀때는 한글이 이상하게 입력이 되는데,  
다른 메뉴나 검색할 때는 잘 입력되는 현상  

결론은 무척;; 당황스럽게도 간단하지만.. 많이도 헤맸다;; 한~두시간;;  
결론은 폰트 패밀리 지정에서 'Droid Sans Fallback'를 제거!   

한글 입력 관련해서는 블로그등에서 다양하게 많은데 이거는 조금 찾기 어려웠다 ㅋㅋ

가장 간단한것은 우분투 셋팅에서 Region & Language 부분에서     
Language를 한국 으로 바꾸면 메뉴등이 한글로 바뀐다. 입력도 잘 됨. 그러면 해결!  

하지만!!   
영어로 메뉴등이 나오게 해야해서 그러다 보니, language 언어 부분은 그대로 영어로 해놓야해서;;

vscode 에서 입력이 (특정 단어) 계속 잘 안되는 현상  
예를 들어   
각을 입력하면 ㄱㅏㄱ 이렇게 된다던가..  

결론은  
vscode preference에서 font를 지정해주면 되는 것임   
preference를 열면 거의 바로 보이는데 font famliy가 보이는데    

'Droid Sans Mono', 'monospace', monospace, 'Droid Sans Fallback'
요렇게 되어 있는데   

'Droid Sans Fallback' 요놈만 지워주면 바로 적용된다.  



## dependencies 에러 관련 error: Failed dependencies: libXss.so.1()(64bit)
```
error: Failed dependencies:
	libXss.so.1()(64bit) is needed by code-1.50.1-1602601064.el7.x86_64
```
그러면 libXScrnSaver 설치해줘야 한다. 다행이도 친절하게 뭐가 필요한지 알려준다.  
구글링 해보면 libXScrnSaver필요하다고 함. 이번에는 yum명령어로 설치   

```
$sudo yum install libXScrnSaver
```
필요한 의존성을 해결했기때문에 (설치로) 다시 rpm 명령어로 vscode를 설치한다  
(다시 처음으로..)
```
$sudo rpm -ivh code-1.50.1-24.rpm
```

> 참고: rpm과는 다르게 yum/dnf명령어는 install을 요청하는 외부(인터넷?)   repository에서 자동으로 다운 후 설치 해줌  
이게 rpm 패키지랑은 다른 점 인 듯 (최신버전은 대개 repo에 없기 때문에 소스파일을 받아서 설치하는 방식으로 한다)  

그리고 이것도 엣날 자료..;; 2022 July 기준   
지금은 vscode에서 rpm으로 파일로 설치를 안하고   
(아마 지원은 할 듯??) 어쨋든 공식 홈피에서 확인