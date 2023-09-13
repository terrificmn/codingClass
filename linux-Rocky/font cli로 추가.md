# 폰트추가하기
> GUI 에서는 폰트파일을 더블 클릭하면 설치를 할 수 있다

기본 home디렉토리로 이동 시킴 (/home/계정$user/로 이동 후 fonts 디렉토리 만들어주기   
숨김디렉토리로 .fonts 로 만들면 됨 (font로 만들면 font인식을 못하는 것 같음, 주의!)  
```
$mkdir .fonts
```
숨기파일 확인
```
$ls -la 
```

폰트 다운받기, 압축이면 압축풀고 ttf 파일을   
$mv example_fontfile_name.ttf /home/$user/.fonts/   
(여기에서 폰트 이름이 길면 확장자가 안나올 수 있으므로 잘 확인할 것)   

그리고 명령어 실행  
```
$fc-cache -v
$fc-cache-64 -v
```

>fc-cache -v 만 해줘도 충분

succeeded 라고 나오면 완료!  

vscode에 적용시키려면 일단,  vscode를 종료했다가 다시 켜준다.    
file-preferences->settings 를 들어가서    
Text Editor의 Font를 보면 폰트를 지정할 수가 있는데..   
폰트 이름을 정확히 입력해줘야지 표시가 된다..   
그런데.. ttf의 파일명과는 또 폰트이름이 다른것 같다;;   

그래서 윈도우에서 fonts라고 검색하면 설치된 폰트들을 볼 수가 있는데..   
여기에서 설치했던 폰트 이름을 검색해보면 정확한 폰트명을 알 수가 있다..   

예를 들어서 ...   
BMJUA_otf.otf 로 설치한 폰트인데..파일명은 BMJUA_otf    
그래서 BMJUA_otf로 vscode 설정에서 font명을 입력해도 바뀌질 않는다.   
그래서 정확한 폰트명이 필요하다. (파일명과는 다름)    
위에서 fonts로 연 창에서 검색 창에 bm까지만 입력하면     
BM JUA_OTF 라는 폰트가 나오고 , 폰트의 info 버튼을 눌러보면 이름이 나온다.   
처음에 설치한 폰트명 파일명과는 다소 다르다. 스페이스 차이?   

> 참고로 DaddyTime 글자체는 'DaddyTimeMono Nerd Font Mono' ('싱글 쿼테이션 포함')   
실제 font 파일명이 아닌, 폰트를 더블 클릭했을 때 나오는 font 정보창에서 나오는 이름으로 해준다   
길다; 이렇게 해야 인식된다 

이제 이 이름을 가지고 vscode에 입력을 해주면 된다.  
끝!


**참고  
DESCRIPTION
       fc-cache scans the font directories on the system and builds font information cache files for applications  
       using  fontconfig for their font handling.

       If  directory  arguments  are  not  given,  fc-cache uses each directory in the current font configuration. 
       Each directory is scanned for font files readable by FreeType. 
       A cache is created which contains properties of each  font  and  the  associated filename.  
       This cache is used to speed up application startup when using the fontconfig library.

       Note that fc-cache must be executed once per architecture to generate font information customized for that architecture.

참고로 x-윈도우(?)에서 font 프로그램에서 검색해보면 잘 설치되었는지를 확인가능   
여기에 폰트 파일을 드래그하면 설치 되는지는 다음에 한번 해봐야겠음