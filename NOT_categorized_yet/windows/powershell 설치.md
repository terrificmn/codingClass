powershell 설치 (현재 7버전, 버전6 이상 추천)
https://github.com/PowerShell/PowerShell/releases?WT.mc_id=-blog-scottha
windows -64로 선택 후 다운받고 powershell 설치!

> tar, zip 버전은 소스파일(또는 리눅스용)이므로 windows에서 사용할 경우에는    
PowerShell-7.3.3-win-x86.msi 같은 파일로 받아준다  
preview 버전 보다는 그 바로 아래 하위 버전으로 다운 받음   


그 다음 필요한 모듈 설치 (posh-git and oh-my-posh)
아래처럼 입력하면 됨
	Install-Module posh-git -Scope CurrentUser
	Install-Module oh-my-posh -Scope CurrentUser


**설정 및 참고 깃허브 참고
https://github.com/JanDeDobbeleer/oh-my-posh?WT.mc_id=-blog-scottha


[ohmyposh 위젯 설치-및 사용법-Document](https://ohmyposh.dev/docs/installation/windows)

oh-my-posh init pwsh --config "C:/Users/jihyo/AppData/Local/Programs/oh-my-posh/themes/jandedobbeleer.omp.json"

 
Enable the prompt:

# Start the default settings
	Set-Prompt
# Alternatively set the desired theme:
	Set-Theme Agnoster


To enable the engine edit your PowerShell profile:

if (!(Test-Path -Path $PROFILE )) { New-Item -Type File -Path $PROFILE -Force }
그리고 다음 명령어를 치면 메모장이 열림
	notepad $PROFILE

Append the following lines to your PowerShell profile:
메모장에 아래 3줄 추가 (마지막줄 Set-Theme은 콘솔의 테마를 설정해줌, 테마는 많은 듯 Set-Theme Agnoster 또는 Paradox)

Import-Module posh-git
Import-Module oh-my-posh
Set-Theme Paradox

참고: 테마 설정 후 관련 색 보기 명령어
Show-ThemeColors


------------------------------
**참고 nerd폰트 다운 사이트
https://www.nerdfonts.com/
여기서 원하는 폰트 다운로드

***참고:
ttf(truetype)- 비트맵 (일반 문서작업)
otf(opentype)- 벡터 (깨질염려가 없는 고해상도 출력물에 사용)

-------------------------------

현재 사용하는 VSCODE EXtensions

Bracket Pair Colorizer
indent-rainbow
Prettier - Code formatter (자바스크립트, html, json ,타입스크립트,등 지원)
Auto Rename Tag
Better Comments
CSS Peek
Live Server
Material Icon Theme
Material Theme
Material Theme Icons
Community Material Theme

PHP Intelephense

